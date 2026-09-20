# 制作名单。整页是一个 button，点击任意处回标题（button 只允许一个子节点）。

screen scr_staff_menu():
    modal True
    zorder 50

    button:
        xysize (1280, 720)
        background Solid("#FFFFFF")
        action Hide("scr_staff_menu")
        vbox:
            xalign 0.5
            yalign 0.45
            spacing 12
            for line in COPY_STAFF_LINES:
                text line:
                    color "#000000"
                    size ui_text_size
                    font sakura_font
                    xalign 0.5

    key "K_ESCAPE" action Hide("scr_staff_menu")
