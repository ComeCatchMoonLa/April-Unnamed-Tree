# 0.7 换成章节/CG 列表。现在只占位，点击回标题。

screen scr_gallery():
    modal True
    zorder 50

    button:
        xysize (1280, 720)
        background Solid("#FFFFFF")
        action Hide("scr_gallery")
        text COPY_TITLE_GALLERY:
            color "#000000"
            size dialogue_name_size
            font sakura_font
            xalign 0.5
            yalign 0.5

    key "K_ESCAPE" action Hide("scr_gallery")
