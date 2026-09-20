# 第 3 段换成四项设置。现在只占位，点击回标题。

screen scr_settings():
    modal True
    zorder 50

    button:
        xysize (1280, 720)
        background Solid("#FFFFFF")
        action Hide("scr_settings")
        text COPY_TITLE_SETTINGS:
            color "#000000"
            size 28
            font gui.interface_text_font
            xalign 0.5
            yalign 0.5

    key "K_ESCAPE" action Hide("scr_settings")
