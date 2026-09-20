# 主进度一键三态；里解锁后插在正下方。Esc 必须吞掉，主界面不能退出游戏。

screen title_entry(caption, btn_action, emphasized=False):
    textbutton caption:
        action btn_action
        text_size (ui_text_size + 8 if emphasized else ui_text_size)
        text_color "#000000"
        text_hover_color "#333333"
        text_font sakura_font
        background None
        hover_background None
        xalign 0.5
        padding (8, 4)


screen scr_title():
    $ has_save = SaveStore.has_slot(SLOT_MAIN)
    $ after_on = UnlockStore.is_after_unlocked()
    $ inner_on = UnlockStore.is_inner_unlocked()

    key "K_ESCAPE" action NullAction()
    key "game_menu" action NullAction()

    vbox:
        xalign 0.5
        yalign 0.42
        spacing 8

        text config.name:
            color "#000000"
            size gui.title_text_size
            font sakura_font
            xalign 0.5
            textalign 0.5

        null height 24

        if after_on:
            use title_entry(COPY_TITLE_AFTER, Function(PlaySession.enter_after), True)
        elif has_save:
            use title_entry(COPY_TITLE_CONTINUE, Function(PlaySession.continue_game), True)
        else:
            use title_entry(COPY_TITLE_NEW, Function(PlaySession.start_new_game), True)

        if inner_on:
            use title_entry(COPY_TITLE_INNER, Function(PlaySession.enter_inner))

        use title_entry(COPY_TITLE_GALLERY, Show("scr_gallery"))
        use title_entry(COPY_TITLE_STAFF, Show("scr_staff_menu"))
        use title_entry(COPY_TITLE_SETTINGS, Show("scr_settings"))
        use title_entry(COPY_TITLE_QUIT, Quit(confirm=False))
