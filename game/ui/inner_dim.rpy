# 里线全屏 60% 黑。不挡下层对话点击。

screen scr_inner_dim():
    zorder -2
    modal False
    add Transform(Solid("#000000"), alpha=0.60, xysize=(1280, 720)):
        focusmask False
