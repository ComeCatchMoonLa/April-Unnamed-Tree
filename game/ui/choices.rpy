# 三种选择肢各一个 screen。按钮一列居中；选择本身不是 line_id。

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
