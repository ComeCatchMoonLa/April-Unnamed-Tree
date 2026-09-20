# 第 3 段换成只读回顾。现在只占位，点击关闭。

screen scr_log():
    modal True
    zorder 50

    button:
        xysize (1280, 720)
        background Solid("#FFFFFF")
        action Hide("scr_log")
        text COPY_HUD_LOG:
            color "#000000"
            size 28
            font gui.interface_text_font
            xalign 0.5
            yalign 0.5

    key "K_ESCAPE" action Hide("scr_log")
    key "noshift_K_l" action Hide("scr_log")
