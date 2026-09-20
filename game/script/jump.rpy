# 按 line_id 跳转。找不到则清会话回 boot（进标题）。

init python:
    _NODE_IMAGE = {
        "ch1_start": "bg_sakura_yard",
        "ch1_cg_backlight": "cg_yayoi_backlight",
        "ch1_choice": "cg_yayoi_backlight",
        "ch1_cg_blizzard": "cg_sakura_blizzard",
    }

    def script_say(line_id, who, what):
        PlaySession.on_line_shown(line_id)
        renpy.say(who, what)

    def script_restore_visuals(node_id):
        image_id = _NODE_IMAGE.get(node_id)
        if image_id is None:
            return
        renpy.scene()
        renpy.show(image_id)

    def jump_to_line(line_id):
        if not LINE_ID_RE.match(line_id or ""):
            _jump_missing(line_id)
            return
        node_id, seq = line_id.rsplit(":", 1)
        extra = "%s_%s" % (node_id, seq)
        if seq == "0001" and renpy.has_label(node_id):
            script_restore_visuals(node_id)
            renpy.jump(node_id)
            return
        if renpy.has_label(extra):
            script_restore_visuals(node_id)
            renpy.jump(extra)
            return
        ctx = PlaySession.current()
        # 尚无全文的节点：回放用占位句走到章末。
        if ctx is not None and ctx.play_mode == "replay" and seq == "0001":
            renpy.jump("replay_stub")
            return
        _jump_missing(line_id)

    def _jump_missing(line_id):
        renpy.log("jump_to_line: no label for %r" % (line_id,))
        PlaySession._clear()
        renpy.jump("boot")


label ch2_choice:
    $ PlaySession.on_node_reached("ch2_choice")
    $ PlaySession.on_line_shown("ch2_choice:0001")
    "占位：中章选择肢前"
    $ PlaySession.run_choice_display(COPY_CHOICE_CH2_LEFT, COPY_CHOICE_CH2_RIGHT)
    jump ch2_choice_0002

label ch2_choice_0002:
    $ PlaySession.on_line_shown("ch2_choice:0002")
    "占位：中章选择肢后"
    $ PlaySession.advance_replay()
    jump ch3_staff

label ch3_staff:
    $ PlaySession.on_node_reached("ch3_staff")
    $ PlaySession.on_line_shown("ch3_staff:0001")
    "占位：制作名单"
    $ PlaySession.run_choice_true()
    $ PlaySession.advance_replay()
    $ PlaySession.commit_leave()

label ch2_start:
    $ PlaySession.on_node_reached("ch2_start")
    $ PlaySession.on_line_shown("ch2_start:0001")
    "占位：ch2_start:0001"
    $ PlaySession.advance_replay()
    $ PlaySession.commit_leave()

label ch3_ledger:
    $ PlaySession.on_node_reached("ch3_ledger")
    $ PlaySession.on_line_shown("ch3_ledger:0001")
    "占位：ch3_ledger:0001"
    $ PlaySession.advance_replay()
    $ PlaySession.commit_leave()

label after_start:
    $ PlaySession.on_node_reached("after_start")
    $ PlaySession.on_line_shown("after_start:0001")
    "占位：after_start:0001"
    $ PlaySession.advance_replay()
    $ PlaySession.commit_leave()

label inner_start:
    $ PlaySession.on_node_reached("inner_start")
    $ PlaySession.on_line_shown("inner_start:0001")
    "占位：inner_start:0001"
    $ PlaySession.advance_replay()
    $ PlaySession.commit_leave()

label replay_stub:
    $ _stub_ctx = PlaySession.current()
    if _stub_ctx is None:
        jump boot
    $ _stub_node = _stub_ctx.node_id
    $ PlaySession.on_node_reached(_stub_node)
    $ PlaySession.on_line_shown("%s:0001" % _stub_node)
    "占位：[_stub_node]:0001"
    $ PlaySession.advance_replay()
    jump boot
