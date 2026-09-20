# 里线全屏 60% 黑。不挡下层对话点击。
# zorder 高于 Log/设置（50），打开它们时仍保持暗，避免闪亮。
# add 只接受 displayable + transform 属性，且不能有子语句（见 screens.html Add）。
# Solid 会铺满分配到的区域；modal False 才把点击留给下层。

screen scr_inner_dim():
    zorder 55
    modal False
    add Solid("#000000") alpha 0.60
