# 启动后白底占位。尚无标题 screen。

image white = "images/white.png"

label splashscreen:
    return

label boot:
    scene white
    # 占位：停在白屏。点击后仍回到本 label，避免空跑剧本。
    pause
    jump boot
