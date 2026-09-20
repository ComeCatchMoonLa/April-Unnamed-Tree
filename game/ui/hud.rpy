# 游玩/回放五键 overlay。标题无会话时不画按钮。
# F1/S 必须走 underlay keymap：对白层上的 screen key 吃不到，且 show_screen 后要 restart 才立刻出界面。

init python:
    def toggle_settings():
        if renpy.get_screen("scr_settings"):
            renpy.hide_screen("scr_settings")
        else:
            renpy.show_screen("scr_settings")
        renpy.restart_interaction()

    def toggle_log():
        if PlaySession.current() is None:
            return
        if renpy.get_screen("scr_log"):
            renpy.hide_screen("scr_log")
        else:
            renpy.show_screen("scr_log")
        renpy.restart_interaction()

    def hud_save():
        ctx = PlaySession.current()
        if ctx is None or ctx.play_mode != "play":
            return
        ref = PlaySession.current_line_ref()
        if ref is None:
            return
        if SaveStore.write_line(SLOT_MAIN, ref):
            renpy.notify(COPY_HUD_SAVED)
            renpy.restart_interaction()


init 2 python:
    config.keymap["sakura_settings"] = ["K_F1"]
    config.keymap["sakura_save"] = ["noshift_K_s"]
    config.underlay.append(
        renpy.Keymap(
            sakura_settings=toggle_settings,
            sakura_save=hud_save,
        )
    )
    if "scr_hud" not in config.overlay_screens:
        config.overlay_screens.append("scr_hud")
    renpy.clear_keymap_cache()


screen hud_entry(caption, btn_action, enabled=True, selected_on=False):
    textbutton caption:
        action btn_action
        sensitive enabled
        selected selected_on
        text_bold selected_on
        text_size ui_text_size
        text_color "#000000"
        text_hover_color "#333333"
        text_insensitive_color "#888888"
        text_font sakura_font
        background None
        hover_background None
        padding (6, 4)


screen scr_hud():
    zorder 10
    $ ctx = PlaySession.current()
    $ overlay_open = (
        renpy.get_screen("scr_settings")
        or renpy.get_screen("scr_log")
        or renpy.get_screen("scr_gallery")
        or renpy.get_screen("scr_gallery_cg")
        or renpy.get_screen("scr_staff_menu")
        or renpy.get_screen("scr_choice_fake")
        or renpy.get_screen("scr_choice_display")
        or renpy.get_screen("scr_choice_true")
    )

    if ctx is not None:
        if not overlay_open:
            key "K_ESCAPE" action Function(PlaySession.commit_leave)
            key "game_menu" action Function(PlaySession.commit_leave)
            key "a" action Function(toggle_afm)
            key "l" action Function(toggle_log)

        hbox:
            xalign 1.0
            yalign 0.0
            xoffset -16
            yoffset 12
            spacing 12

            use hud_entry(COPY_HUD_RETURN, Function(PlaySession.commit_leave))
            use hud_entry(COPY_HUD_AUTO, Function(toggle_afm), True, preferences.afm_enable)
            use hud_entry(COPY_HUD_SETTING, Function(toggle_settings))
            use hud_entry(COPY_HUD_LOG, Function(toggle_log))
            use hud_entry(COPY_HUD_SAVE, Function(hud_save), ctx.play_mode == "play")
