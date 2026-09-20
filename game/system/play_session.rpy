# 播放会话。Auto 只切引擎 AFM，不自管 pending/active。

init python:
    from collections import namedtuple

    PlayContext = namedtuple(
        "PlayContext",
        (
            "play_mode",
            "chapter_id",
            "node_id",
            "line_id",
            "style",
            "route",
        ),
    )

    class _PlaySession(object):

        def __init__(self):
            self._context = None

        def current(self):
            return self._context

        def current_line_ref(self):
            ctx = self._context
            if ctx is None:
                return None
            return LineRef(
                ctx.chapter_id,
                ctx.node_id,
                ctx.line_id,
                ctx.style,
                ctx.route,
            )

        def start_new_game(self):
            first = NodeCatalog.first_line_id("ch1_start")
            ctx = PlayContext(
                "play",
                "ch1",
                "ch1_start",
                first,
                "omote",
                "main",
            )
            self._bind(ctx)
            SaveStore.write_line(SLOT_MAIN, self.current_line_ref())
            jump_to_line(first)

        def continue_game(self):
            rec = SaveStore.load_slot(SLOT_MAIN)
            if rec is None:
                return False
            # 0.9 再接续玩状态表；本版本从槽内 line_id 句首播。
            ctx = PlayContext(
                "play",
                rec.chapter_id,
                rec.node_id,
                rec.line_id,
                rec.style,
                rec.route,
            )
            self._bind(ctx)
            jump_to_line(rec.line_id)
            return True

        def enter_after(self):
            if not UnlockStore.is_after_unlocked():
                return False
            return self._enter_play_node("after_start")

        def enter_inner(self):
            if not UnlockStore.is_inner_unlocked():
                return False
            return self._enter_play_node("inner_start")

        def enter_replay(self, node_id):
            if not UnlockStore.is_node_unlocked(node_id):
                return False
            return self._enter_mode_node("replay", node_id)

        def advance_replay(self):
            ctx = self._context
            if ctx is None or ctx.play_mode != "replay":
                return False
            next_id = NodeCatalog.next_node_in_chapter(ctx.node_id)
            if next_id is None:
                self.commit_leave()
                return True
            return self._enter_mode_node("replay", next_id)

        def on_node_reached(self, node_id):
            node = NodeCatalog.get_node(node_id)
            if node is None:
                return
            first = NodeCatalog.first_line_id(node_id)
            route = NodeCatalog.route_of_chapter(node.chapter_id)
            ctx = self._context
            if ctx is None:
                ctx = PlayContext(
                    "play",
                    node.chapter_id,
                    node_id,
                    first,
                    self._style_for_node(node),
                    route,
                )
            else:
                line_id = ctx.line_id
                if not line_id.startswith(node_id + ":"):
                    line_id = first
                ctx = ctx._replace(
                    chapter_id=node.chapter_id,
                    node_id=node_id,
                    line_id=line_id,
                    route=route or ctx.route,
                )
            self._bind(ctx)
            if ctx.play_mode != "play":
                return
            UnlockStore.unlock_node(node_id)
            SaveStore.write_line(SLOT_MAIN, self.current_line_ref())

        def on_cg_shown(self, cg_id):
            ctx = self._context
            if ctx is None or ctx.play_mode != "play":
                return
            UnlockStore.unlock_cg(cg_id)

        def on_line_shown(self, line_id):
            ctx = self._context
            if ctx is None:
                return
            node_id = line_id.rsplit(":", 1)[0]
            node = NODE_BY_ID.get(node_id)
            if node is None:
                self._context = ctx._replace(line_id=line_id)
                return
            route = NodeCatalog.route_of_chapter(node.chapter_id)
            self._context = ctx._replace(
                line_id=line_id,
                node_id=node_id,
                chapter_id=node.chapter_id,
                route=route or ctx.route,
            )

        def run_choice_fake(self, left, right):
            picked = renpy.call_screen("scr_choice_fake", left, right)
            self._log_system_line(COPY_LOG_CHOICE_PREFIX + picked)

        def run_choice_display(self, left, right):
            renpy.call_screen("scr_choice_display", left, right)
            self._log_system_line(COPY_LOG_CHOICE_UNSELECTED)

        def run_choice_true(self):
            picked = renpy.call_screen("scr_choice_true")
            if picked == "continue":
                caption = COPY_CHOICE_TRUE_CONTINUE
            else:
                caption = COPY_CHOICE_TRUE_END
            self._log_system_line(COPY_LOG_CHOICE_PREFIX + caption)
            ctx = self._context
            if ctx is None or ctx.play_mode != "play":
                return
            UnlockStore.unlock_after()
            if picked == "continue":
                self._enter_play_node("after_start")
                return
            self._end_to_after_slot()

        def commit_leave(self):
            self.flush_leave()
            renpy.jump("boot")

        def flush_leave(self):
            ctx = self._context
            if ctx is not None and ctx.play_mode == "play":
                ref = self.current_line_ref()
                if ref is not None:
                    SaveStore.write_line(SLOT_MAIN, ref)
            self._clear()

        def apply_style(self, style):
            if style not in STYLES:
                style = "omote"
            ctx = self._context
            if ctx is not None:
                self._context = ctx._replace(style=style)
            if style == "ura":
                renpy.store.dialogue_window_bg = "#2A2A2A"
                renpy.store.dialogue_text_color = "#FFFFFF"
            else:
                renpy.store.dialogue_window_bg = "#FFFFFF"
                renpy.store.dialogue_text_color = "#000000"

        def sync_inner_dim(self):
            ctx = self._context
            if ctx is not None and ctx.chapter_id == "inner":
                renpy.show_screen("scr_inner_dim")
            elif renpy.get_screen("scr_inner_dim"):
                renpy.hide_screen("scr_inner_dim")

        def _enter_play_node(self, node_id):
            return self._enter_mode_node("play", node_id)

        def _enter_mode_node(self, play_mode, node_id):
            node = NodeCatalog.get_node(node_id)
            if node is None:
                return False
            first = NodeCatalog.first_line_id(node_id)
            route = NodeCatalog.route_of_chapter(node.chapter_id)
            ctx = PlayContext(
                play_mode,
                node.chapter_id,
                node_id,
                first,
                self._style_for_node(node),
                route,
            )
            self._bind(ctx)
            if play_mode == "play":
                SaveStore.write_line(SLOT_MAIN, self.current_line_ref())
            jump_to_line(first)
            return True

        def _bind(self, ctx):
            self._context = ctx
            preferences.text_cps = SettingsStore.text_cps()
            SettingsStore.sync_afm()
            self.apply_style(ctx.style)
            self.sync_inner_dim()

        def _clear(self):
            self._context = None
            self.apply_style("omote")
            self.sync_inner_dim()

        def _style_for_node(self, node):
            if node.chapter_id == "inner":
                return "ura"
            if node.node_id.startswith("ch3_ura"):
                return "ura"
            return "omote"

        def _log_system_line(self, what):
            narrator.add_history("adv", None, what)

        def _end_to_after_slot(self):
            first = NodeCatalog.first_line_id("after_start")
            node = NodeCatalog.get_node("after_start")
            if first is None or node is None:
                self.commit_leave()
                return
            route = NodeCatalog.route_of_chapter(node.chapter_id)
            ctx = PlayContext(
                "play",
                node.chapter_id,
                node.node_id,
                first,
                "omote",
                route,
            )
            self._bind(ctx)
            SaveStore.write_line(SLOT_MAIN, self.current_line_ref())
            self._clear()
            renpy.jump("boot")

    PlaySession = _PlaySession()

    def toggle_afm():
        preferences.afm_enable = not preferences.afm_enable


default dialogue_window_bg = "#FFFFFF"
default dialogue_text_color = "#000000"


init 3 python:
    # 关窗先写当前句；仍走 Quit(confirm=False)，避免 quit_action 里再 quit 递归。
    config.quit_callbacks.append(PlaySession.flush_leave)
