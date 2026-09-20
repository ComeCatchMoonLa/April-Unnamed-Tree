# 按 line_id 跳转。找不到则清会话回 boot（进标题）。

init python:
    _NODE_IMAGE = {
        "ch1_start": "bg_sakura_yard",
        "ch1_cg_backlight": "cg_yayoi_backlight",
        "ch1_choice": "cg_yayoi_backlight",
        "ch1_cg_blizzard": "cg_sakura_blizzard",
        "ch2_start": "bg_sakura_yard",
        "ch2_hospital": "bg_hospital_403",
        "ch2_room": "bg_room_night",
        "ch2_choice": "bg_room_night",
        "ch2_fullbloom": "cg_fullbloom_backlight",
        "ch3_ledger": "white",
        "ch3_omote1": "bg_slope_to_hospital",
        "ch3_ura1": "white",
        "ch3_omote2": "cg_fullbloom_backlight",
        "ch3_ura2": "white",
        "ch3_omote3": "bg_hospital_surgery",
        "ch3_black": "bg_black",
        "ch3_ura3": "bg_sakura_yard",
        "ch3_omote5": "bg_ninth_spring",
        "ch3_staff": "white",
        "after_start": "bg_apartment_morning",
        "after_read": "bg_dining",
        "after_night": "bg_bedroom_night",
        "after_tree": "bg_slope_sakura",
        "inner_start": "bg_kitchen",
        "inner_mail": "bg_dining",
        "inner_note": "bg_dining",
        "inner_night": "bg_bedroom_inner",
        "inner_slope": "bg_slope_inner",
        "inner_end": "bg_kitchen",
    }

    def script_say(line_id, who, what):
        PlaySession.on_line_shown(line_id)
        renpy.say(who, what)

    def script_restore_visuals(node_id):
        image_id = _NODE_IMAGE.get(node_id)
        if image_id is None:
            return
        renpy.scene()
        renpy.show(image_id)

    def jump_to_line(line_id):
        if not LINE_ID_RE.match(line_id or ""):
            _jump_missing(line_id)
            return
        node_id, seq = line_id.rsplit(":", 1)
        extra = "%s_%s" % (node_id, seq)
        if seq == "0001" and renpy.has_label(node_id):
            script_restore_visuals(node_id)
            renpy.jump(node_id)
            return
        if renpy.has_label(extra):
            script_restore_visuals(node_id)
            renpy.jump(extra)
            return
        ctx = PlaySession.current()
        # 未写的节点回放才走占位句。
        if ctx is not None and ctx.play_mode == "replay" and seq == "0001":
            renpy.jump("replay_stub")
            return
        _jump_missing(line_id)

    def _jump_missing(line_id):
        renpy.log("jump_to_line: no label for %r" % (line_id,))
        PlaySession._clear()
        renpy.jump("boot")


label replay_stub:
    $ _stub_ctx = PlaySession.current()
    if _stub_ctx is None:
        jump boot
    $ _stub_node = _stub_ctx.node_id
    $ PlaySession.on_node_reached(_stub_node)
    $ PlaySession.on_line_shown("%s:0001" % _stub_node)
    "占位：[_stub_node]:0001"
    $ PlaySession.advance_replay()
    jump boot
