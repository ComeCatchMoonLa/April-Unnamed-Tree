# 只读已显示对白与选择系统行。不可点行跳转。
# _history 是开关（bool）；真正的条目在 _history_list。

screen scr_log():
    modal True
    zorder 50
    predict False

    add Solid("#FFFFFF")

    vbox:
        xalign 0.5
        yalign 0.08
        spacing 16
        xsize 960

        text COPY_HUD_LOG:
            color "#000000"
            size dialogue_name_size
            font sakura_font
            xalign 0.5

        viewport:
            xysize (960, 480)
            mousewheel True
            draggable True
            yinitial 1.0

            vbox:
                spacing 12
                xsize 920
                for h in _history_list:
                    vbox:
                        spacing 2
                        if h.who:
                            text h.who:
                                color "#000000"
                                size ui_text_size
                                font sakura_font
                        text h.what:
                            color "#000000"
                            size dialogue_text_size
                            font sakura_font

        textbutton COPY_SETTINGS_CLOSE:
            action Function(toggle_log)
            text_size ui_text_size
            text_color "#000000"
            text_hover_color "#333333"
            text_font sakura_font
            background None
            hover_background None
            xalign 0.5
            padding (8, 4)

    key "K_ESCAPE" action Function(toggle_log)
    key "l" action Function(toggle_log)
