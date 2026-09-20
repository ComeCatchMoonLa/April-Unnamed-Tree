# 启动后进标题。白图须铺满设计分辨率。

image white = Transform("images/white.png", xysize=(1280, 720))

label splashscreen:
    python:
        if DEBUG_RESET_ON_BOOT:
            SaveStore.clear_slot(SLOT_MAIN)
            UnlockStore.clear_all()
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
    call screen scr_title
    jump title_loop
