# 节点表。ID 与设计文档逐字一致，禁止改名。

init -10 python:
    from collections import namedtuple

    NodeDef = namedtuple("NodeDef", ("node_id", "chapter_id", "name", "trigger"))

    NODE_DEFS = (
        NodeDef("ch1_start", "ch1", "樱树下", "首章开头 / 【场景：旧校舍后·樱树】"),
        NodeDef("ch1_cg_backlight", "ch1", "逆光的弥生", "【CG：逆光的弥生，花与光尘】"),
        NodeDef("ch1_choice", "ch1", "首章选择肢", "第一组 ▶【选择肢】出现前"),
        NodeDef("ch1_cg_blizzard", "ch1", "樱吹雪", "【CG：樱吹雪·二人】"),
        NodeDef("ch2_start", "ch2", "缺席的树", "中章开头 / 【场景：旧校舍后·樱树】"),
        NodeDef("ch2_hospital", "ch2", "医院 403", "【场景：市立医院·403室】"),
        NodeDef("ch2_room", "ch2", "反驳练习", "【场景：自己房间·深夜】"),
        NodeDef("ch2_choice", "ch2", "中章选择肢", "第二组 ▶【选择肢】出现前"),
        NodeDef("ch2_fullbloom", "ch2", "满开", "【CG：满开·逆光】（中章）"),
        NodeDef("ch3_ledger", "ch3", "账簿", "尾章开头 / 【开场·无画面】"),
        NodeDef("ch3_omote1", "ch3", "表·一", "▎表·一"),
        NodeDef("ch3_ura1", "ch3", "里·一", "▎里·一"),
        NodeDef("ch3_omote2", "ch3", "表·二", "▎表·二"),
        NodeDef("ch3_ura2", "ch3", "里·二", "▎里·二"),
        NodeDef("ch3_omote3", "ch3", "表·三", "▎表·三"),
        NodeDef("ch3_black", "ch3", "表·四 黑", "▎表·四 / 【画面：黑】"),
        NodeDef("ch3_ura3", "ch3", "里·三", "▎里·三"),
        NodeDef("ch3_omote5", "ch3", "表·五", "▎表·五"),
        NodeDef("ch3_staff", "ch3", "制作名单与真选项", "【STAFF ROLL】"),
        NodeDef("after_start", "after", "公寓早晨", "【场景：公寓·周日早晨】"),
        NodeDef("after_read", "after", "餐桌朗读", "【场景：餐桌·朗读】"),
        NodeDef("after_night", "after", "卧室", "【场景：卧室·夜】"),
        NodeDef("after_tree", "after", "坡道", "【场景：坡道·樱树】"),
        NodeDef("inner_start", "inner", "厨房", "▎里·一 / 【场景：厨房】"),
        NodeDef("inner_mail", "inner", "四封信", "▎里·二"),
        NodeDef("inner_note", "inner", "失败的实验记录", "▎里·三"),
        NodeDef("inner_night", "inner", "黑着写", "▎里·四"),
        NodeDef("inner_slope", "inner", "坡道", "▎里·五"),
        NodeDef("inner_end", "inner", "本日有事", "▎里·尾声"),
    )

    NODE_BY_ID = {node.node_id: node for node in NODE_DEFS}
    CHAPTER_IDS = ("ch1", "ch2", "ch3", "after", "inner")
    ROUTE_BY_CHAPTER = {
        "ch1": "main",
        "ch2": "main",
        "ch3": "main",
        "after": "after",
        "inner": "inner",
    }
