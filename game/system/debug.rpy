# 开发用。只在 splash 写槽/解锁；不要提交非 None/"new" 的 DEBUG_START。
# None 不动档；"new" 清空；("after", "after_read") 落到该节点首句。
define DEBUG_START = None
define DEBUG_UNLOCK_GALLERY = False

init python:
    _DEBUG_NODE_CG = {
        "ch1_cg_backlight": "cg_yayoi_backlight",
        "ch1_cg_blizzard": "cg_sakura_blizzard",
        "ch2_fullbloom": "cg_fullbloom_backlight",
        "ch3_ura3": "cg_black_pink",
    }

    def _debug_log(msg):
        # 本工程未开 config.log，renpy.log 不会进 log.txt；与目录转储一样用 print。
        print(msg)

    def debug_apply_boot():
        start = DEBUG_START
        if start == "new":
            SaveStore.clear_slot(SLOT_MAIN)
            UnlockStore.clear_all()
        elif isinstance(start, (tuple, list)) and len(start) == 2:
            _debug_seed_start(start[0], start[1])
        elif start is not None:
            _debug_log("DEBUG_START: ignored %r" % (start,))
        if DEBUG_UNLOCK_GALLERY:
            data = UnlockStore._load_raw()
            data["nodes"] = [node.node_id for node in NODE_DEFS]
            data["cgs"] = [cg.cg_id for cg in CG_DEFS]
            UnlockStore._save_raw(data)

    def _debug_seed_start(chapter_id, node_id):
        node = NodeCatalog.get_node(node_id)
        if node is None or node.chapter_id != chapter_id:
            _debug_log("DEBUG_START: bad pair %r %r" % (chapter_id, node_id))
            return
        nodes = []
        cgs = []
        for item in NODE_DEFS:
            nodes.append(item.node_id)
            cg_id = _DEBUG_NODE_CG.get(item.node_id)
            if cg_id is not None and cg_id not in cgs:
                cgs.append(cg_id)
            if item.node_id == node_id:
                break
        UnlockStore._save_raw({
            "after_unlocked": chapter_id in ("after", "inner"),
            "inner_unlocked": chapter_id == "inner",
            "nodes": nodes,
            "cgs": cgs,
        })
        first = NodeCatalog.first_line_id(node_id)
        route = NodeCatalog.route_of_chapter(chapter_id)
        SaveStore.write_line(
            SLOT_MAIN,
            LineRef(
                chapter_id,
                node_id,
                first,
                PlaySession._style_for_node(node),
                route,
            ),
        )
