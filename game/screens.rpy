# 最小 screen：覆盖官方模板里的 Skip/Hide/存档柜入口。不实现标题与 HUD。

screen say(who, what):
    window:
        id "window"
        background Solid(dialogue_window_bg)
        xfill True
        yalign 1.0
        ysize 180
        padding (40, 20, 40, 20)

        if who is not None:
            text who id "who" color dialogue_text_color size 28 font gui.text_font
            text what id "what" color dialogue_text_color size 22 ypos 40 font gui.text_font
        else:
            text what id "what" color dialogue_text_color size 22 font gui.text_font

screen choice(items):
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 12
        for i in items:
            textbutton i.caption action i.action text_color "#000000"

screen input(prompt):
    vbox:
        xalign 0.5
        yalign 0.5
        text prompt color "#000000"
        input id "input"

screen nvl(dialogue, items=None):
    window:
        background Solid("#ffffff")
        xfill True
        yfill True
        vbox:
            spacing 10
            for d in dialogue:
                text d.what color "#000000"

screen nvl_dialogue(dialogue):
    for d in dialogue:
        text d.what color "#000000"

screen notify(message):
    text message color "#000000" xpos 20 ypos 20

# 立刻进 start，避免停在默认主菜单/存档柜。
screen main_menu():
    tag menu
    timer 0.01 action Start()

# 关闭默认快捷条（Skip / Hide / Save / Auto 按钮）。
screen quick_menu():
    pass

screen skip_indicator():
    pass

# 无退出确认；若仍被调用则直接执行。
screen confirm(message, yes_action, no_action):
    timer 0.01 action yes_action
