# 启动后白底占位。尚无标题 screen。

# 位图须铺满设计分辨率；原图像素尺寸不够时 scene 不会自动拉伸。
image white = Transform("images/white.png", xysize=(1280, 720))

label splashscreen:
    return

label boot:
    window hide
    scene white
    if not catalog_logged:
        $ _log_catalog()
        $ catalog_logged = True
    # 占位：停在白屏。点击后仍回到本 label，避免空跑剧本。
    pause
    jump boot
