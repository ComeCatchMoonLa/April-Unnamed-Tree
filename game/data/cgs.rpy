# CG 表。四个 ID 与设计文档逐字一致。尾章表·二复用 cg_fullbloom_backlight，本表只登记首次出现章。

init -10 python:
    from collections import namedtuple

    CgDef = namedtuple("CgDef", ("cg_id", "name", "first_chapter_id"))

    CG_DEFS = (
        CgDef("cg_yayoi_backlight", "逆光的弥生，花与光尘", "ch1"),
        CgDef("cg_sakura_blizzard", "樱吹雪·二人", "ch1"),
        CgDef("cg_fullbloom_backlight", "满开·逆光", "ch2"),
        CgDef("cg_black_pink", "黑·一粒粉", "ch3"),
    )

    CG_BY_ID = {cg.cg_id: cg for cg in CG_DEFS}
