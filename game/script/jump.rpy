# 按 line_id 跳转。找不到则清会话回 boot（进标题）。

init python:
    def jump_to_line(line_id):
        if not LINE_ID_RE.match(line_id or ""):
            _jump_missing(line_id)
            return
        node_id, seq = line_id.rsplit(":", 1)
        if seq == "0001" and renpy.has_label(node_id):
            renpy.jump(node_id)
            return
        extra = "%s_%s" % (node_id, seq)
        if renpy.has_label(extra):
            renpy.jump(extra)
            return
        _jump_missing(line_id)

    def _jump_missing(line_id):
        renpy.log("jump_to_line: no label for %r" % (line_id,))
        PlaySession._clear()
        renpy.jump("boot")


label ch1_start:
    $ PlaySession.on_node_reached("ch1_start")
    $ PlaySession.on_line_shown("ch1_start:0001")
    "占位：ch1_start:0001"
    jump ch1_start_0002

label ch1_start_0002:
    $ PlaySession.on_line_shown("ch1_start:0002")
    "占位：ch1_start:0002"
    jump ch1_choice

label ch1_choice:
    $ PlaySession.on_node_reached("ch1_choice")
    $ PlaySession.on_line_shown("ch1_choice:0001")
    "占位：首章选择肢前"
    $ PlaySession.run_choice_fake(COPY_CHOICE_CH1_LEFT, COPY_CHOICE_CH1_RIGHT)
    jump ch1_choice_0002

label ch1_choice_0002:
    $ PlaySession.on_line_shown("ch1_choice:0002")
    "占位：首章选择肢后"
    jump ch2_choice

label ch2_choice:
    $ PlaySession.on_node_reached("ch2_choice")
    $ PlaySession.on_line_shown("ch2_choice:0001")
    "占位：中章选择肢前"
    $ PlaySession.run_choice_display(COPY_CHOICE_CH2_LEFT, COPY_CHOICE_CH2_RIGHT)
    jump ch2_choice_0002

label ch2_choice_0002:
    $ PlaySession.on_line_shown("ch2_choice:0002")
    "占位：中章选择肢后"
    jump ch3_staff

label ch3_staff:
    $ PlaySession.on_node_reached("ch3_staff")
    $ PlaySession.on_line_shown("ch3_staff:0001")
    "占位：制作名单"
    $ PlaySession.run_choice_true()
    $ PlaySession.commit_leave()

label ch2_start:
    $ PlaySession.on_node_reached("ch2_start")
    $ PlaySession.on_line_shown("ch2_start:0001")
    "占位：ch2_start:0001"
    $ PlaySession.commit_leave()

label ch3_ledger:
    $ PlaySession.on_node_reached("ch3_ledger")
    $ PlaySession.on_line_shown("ch3_ledger:0001")
    "占位：ch3_ledger:0001"
    $ PlaySession.commit_leave()

label after_start:
    $ PlaySession.on_node_reached("after_start")
    $ PlaySession.on_line_shown("after_start:0001")
    "占位：after_start:0001"
    $ PlaySession.commit_leave()

label inner_start:
    $ PlaySession.on_node_reached("inner_start")
    $ PlaySession.on_line_shown("inner_start:0001")
    "占位：inner_start:0001"
    $ PlaySession.commit_leave()
