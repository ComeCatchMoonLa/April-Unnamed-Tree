# 三种选择肢各一个 screen。中章留屏是不能点的字，不是第四类选择肢。

screen choice_entry(caption, btn_action, locked=False):
    textbutton caption:
        action (NullAction() if locked else btn_action)
        text_size ui_text_size
        text_color "#000000"
        text_hover_color ("#000000" if locked else "#333333")
        text_font sakura_font
        background None
        hover_background None
        xalign 0.5
        text_align 0.5
        padding (8, 10)


screen scr_choice_fake(left, right):
    modal True
    zorder 30

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 16
        xmaximum 720
        use choice_entry(left, Return(left))
        use choice_entry(right, Return(right))


screen scr_choice_display(left, right):
    modal True
    zorder 30

    button:
        xysize (1280, 720)
        background None
        action Return()

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 16
        xmaximum 720
        use choice_entry(left, None, True)
        use choice_entry(right, None, True)


screen scr_choice_true():
    modal True
    zorder 30

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 16
        xmaximum 720
        use choice_entry(COPY_CHOICE_TRUE_CONTINUE, Return("continue"))
        use choice_entry(COPY_CHOICE_TRUE_END, Return("end"))


screen scr_choice_hold(left, right):
    # 低于 overlay 上的 HUD；对白在画面下沿，两行居中不挡。
    zorder 5
    modal False

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 16
        xmaximum 720
        text left:
            size ui_text_size
            color "#000000"
            font sakura_font
            text_align 0.5
            xalign 0.5
        text right:
            size ui_text_size
            color "#000000"
            font sakura_font
            text_align 0.5
            xalign 0.5
