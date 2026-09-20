# 章节/CG 分页。CG 全屏不是文本 replay，不进 PlaySession。

init python:
    def gallery_start_replay(node_id):
        if not UnlockStore.is_node_unlocked(node_id):
            return
        renpy.hide_screen("scr_gallery_cg")
        renpy.hide_screen("scr_gallery")
        PlaySession.enter_replay(node_id)

    def gallery_open_cg(cg_id):
        if not UnlockStore.is_cg_unlocked(cg_id):
            return
        renpy.show_screen("scr_gallery_cg", cg_id)


screen gallery_tab(caption, is_on, pick_action):
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


screen gallery_node_row(node):
    $ unlocked = UnlockStore.is_node_unlocked(node.node_id)
    $ caption = node.name if unlocked else COPY_GALLERY_LOCKED
    textbutton caption:
        action Function(gallery_start_replay, node.node_id)
        sensitive unlocked
        text_size ui_text_size
        text_color "#000000"
        text_hover_color "#333333"
        text_insensitive_color "#888888"
        text_font sakura_font
        background None
        hover_background None
        xalign 0.5
        padding (8, 4)


screen gallery_cg_row(cg):
    $ unlocked = UnlockStore.is_cg_unlocked(cg.cg_id)
    $ caption = cg.name if unlocked else COPY_GALLERY_LOCKED
    textbutton caption:
        action Function(gallery_open_cg, cg.cg_id)
        sensitive unlocked
        text_size ui_text_size
        text_color "#000000"
        text_hover_color "#333333"
        text_insensitive_color "#888888"
        text_font sakura_font
        background None
        hover_background None
        xalign 0.5
        padding (8, 4)


screen scr_gallery():
    modal True
    zorder 50
    default page = "chapters"
    default chapter_id = "ch1"

    add Solid("#FFFFFF")

    vbox:
        xalign 0.5
        yalign 0.08
        spacing 16
        xmaximum 900

        hbox:
            xalign 0.5
            spacing 24
            use gallery_tab(COPY_GALLERY_CHAPTER, page == "chapters", SetScreenVariable("page", "chapters"))
            use gallery_tab(COPY_GALLERY_CG, page == "cgs", SetScreenVariable("page", "cgs"))

        if page == "chapters":
            hbox:
                xalign 0.5
                spacing 16
                for tab_id, tab_name in COPY_GALLERY_CHAPTER_TABS:
                    use gallery_tab(tab_name, chapter_id == tab_id, SetScreenVariable("chapter_id", tab_id))

            vbox:
                xalign 0.5
                spacing 4
                for node in NodeCatalog.nodes_in_chapter(chapter_id):
                    use gallery_node_row(node)
        else:
            vbox:
                xalign 0.5
                spacing 8
                for cg in NodeCatalog.all_cgs():
                    use gallery_cg_row(cg)

        textbutton COPY_SETTINGS_CLOSE:
            action [Hide("scr_gallery_cg"), Hide("scr_gallery")]
            text_size ui_text_size
            text_color "#000000"
            text_hover_color "#333333"
            text_font sakura_font
            background None
            hover_background None
            xalign 0.5
            padding (8, 8)

    key "K_ESCAPE" action [Hide("scr_gallery_cg"), Hide("scr_gallery")]


screen scr_gallery_cg(cg_id):
    modal True
    zorder 60
    $ cg = NodeCatalog.get_cg(cg_id)
    $ caption = cg.name if cg is not None else ""

    if cg is not None:
        add cg.cg_id
    else:
        add Solid("#FFFFFF")

    button:
        xysize (1280, 720)
        background None
        action Hide("scr_gallery_cg")
        text caption:
            color "#000000"
            size dialogue_name_size
            font sakura_font
            xalign 0.5
            yalign 0.9

    key "K_ESCAPE" action Hide("scr_gallery_cg")
