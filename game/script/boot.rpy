# 启动后进标题。白图须铺满设计分辨率。

image white = Transform("images/white.png", xysize=(1280, 720))

label splashscreen:
    $ debug_apply_boot()
    return

label boot:
    window hide
    scene white
    if not catalog_logged:
        $ _log_catalog()
        $ catalog_logged = True
    jump title_loop

label title_loop:
    window hide
    scene white
    # 探针或占位句末 jump boot 时可能还挂着会话/暗层。
    $ PlaySession._clear()
    if gallery_reopen:
        $ gallery_reopen = False
        show screen scr_gallery
    call screen scr_title
    jump title_loop
