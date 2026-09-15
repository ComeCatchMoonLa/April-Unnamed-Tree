# 全部场景 / CG 占位都指向铺满的白图，便于以后只换文件。

init python:
    _WHITE_FULL = Transform("images/white.png", xysize=(1280, 720))
    _PLACEHOLDER_IMAGE_IDS = (
        "bg_sakura_yard",
        "bg_hospital_403",
        "bg_room_night",
        "bg_hospital_to_yard",
        "bg_slope_to_hospital",
        "bg_yard_fullbloom",
        "bg_hospital_surgery",
        "bg_black",
        "bg_ninth_spring",
        "bg_apartment_morning",
        "bg_dining",
        "bg_bedroom_night",
        "bg_slope_sakura",
        "bg_kitchen",
        "bg_bedroom_inner",
        "bg_slope_inner",
        "cg_yayoi_backlight",
        "cg_sakura_blizzard",
        "cg_fullbloom_backlight",
        "cg_black_pink",
    )
    for _image_id in _PLACEHOLDER_IMAGE_IDS:
        renpy.image(_image_id, _WHITE_FULL)
