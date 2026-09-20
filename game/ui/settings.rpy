# 选项三项 + 快捷键只读页。改完立刻走 SettingsStore.save（内部 apply）。

init python:
    def settings_set(field, value):
        rec = SettingsStore.load()
        if not SettingsStore.is_android():
            rec = rec._replace(
                window_mode="fullscreen" if preferences.fullscreen else "window",
            )
        if field == "afm_level":
            rec = rec._replace(afm_level=value)
        elif field == "font_size_level":
            rec = rec._replace(font_size_level=value)
        elif field == "window_mode":
            rec = rec._replace(window_mode=value)
        else:
            return
        SettingsStore.save(rec)
        if field == "window_mode":
            SettingsStore.apply_display()
        renpy.restart_interaction()


screen settings_pick(caption, is_on, pick_action):
    textbutton caption:
        action pick_action
        selected is_on
        text_bold is_on
        text_size ui_text_size
        text_color "#000000"
        text_hover_color "#333333"
        text_font sakura_font
        background None
        hover_background None
        padding (8, 4)


screen settings_row(row_caption, picks):
    vbox:
        spacing 4
        text row_caption:
            color "#000000"
            size ui_text_size
            font sakura_font
        hbox:
            spacing 16
            for cap, picked, act in picks:
                use settings_pick(cap, picked, act)


screen scr_settings():
    modal True
    zorder 50
    default page = "options"
    $ rec = SettingsStore.load()
    $ window_full = preferences.fullscreen

    add Solid("#FFFFFF")

    vbox:
        xalign 0.5
        yalign 0.12
        spacing 18
        xmaximum 720

        hbox:
            xalign 0.5
            spacing 24
            use settings_pick(COPY_SETTINGS_OPTIONS, page == "options", SetScreenVariable("page", "options"))
            use settings_pick(COPY_SETTINGS_HOTKEYS, page == "hotkeys", SetScreenVariable("page", "hotkeys"))

        if page == "options":
            use settings_row(
                COPY_SETTINGS_AFM,
                [
                    (COPY_SETTINGS_AFM_SLOW, rec.afm_level == "slow", Function(settings_set, "afm_level", "slow")),
                    (COPY_SETTINGS_AFM_MID, rec.afm_level == "mid", Function(settings_set, "afm_level", "mid")),
                    (COPY_SETTINGS_AFM_FAST, rec.afm_level == "fast", Function(settings_set, "afm_level", "fast")),
                ],
            )
            use settings_row(
                COPY_SETTINGS_SIZE,
                [
                    (COPY_SETTINGS_SIZE_SMALL, rec.font_size_level == "small", Function(settings_set, "font_size_level", "small")),
                    (COPY_SETTINGS_SIZE_MID, rec.font_size_level == "mid", Function(settings_set, "font_size_level", "mid")),
                    (COPY_SETTINGS_SIZE_LARGE, rec.font_size_level == "large", Function(settings_set, "font_size_level", "large")),
                ],
            )
            if not SettingsStore.is_android():
                use settings_row(
                    COPY_SETTINGS_WINDOW,
                    [
                        (COPY_SETTINGS_WINDOW_WIN, not window_full, Function(settings_set, "window_mode", "window")),
                        (COPY_SETTINGS_WINDOW_FULL, window_full, Function(settings_set, "window_mode", "fullscreen")),
                    ],
                )
        else:
            text COPY_HOTKEY_HELP:
                color "#000000"
                size ui_text_size
                font sakura_font
                xalign 0.5
                textalign 0.0

        textbutton COPY_SETTINGS_CLOSE:
            action Function(toggle_settings)
            text_size ui_text_size
            text_color "#000000"
            text_hover_color "#333333"
            text_font sakura_font
            background None
            hover_background None
            xalign 0.5
            padding (8, 8)

    key "K_ESCAPE" action Function(toggle_settings)
