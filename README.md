# 四月，未命名的树

本地文字冒险（ADV）。目标平台 Windows 10+ 与 Android 5.0+，无网页版。

画面目前是白底黑字占位，无正式美术、音乐、语音。尚无玩家发行包。

## 开发

用 **Ren'Py 8 Launcher** 打开本仓库。不要用系统 Python 跑游戏。

Launcher 的工程目录应设成上一级 `Renpy_Projects`，让列表里出现 `Sakura`。不要把工程目录设成本仓库根，否则会找不到项目。

编辑器用 Cursor Profile **Py Dev**，工作区会把 `*.rpy` 当成 Ren'Py。语法高亮需要官方扩展 `renpy.language-renpy`，不要装已停更的 `LuqueDaniel.languague-renpy`。说明见 [开发环境](Docs/Dev/调研/开发环境.md)。

- 文档入口：[Docs/Dev/README.md](Docs/Dev/README.md)
- 当前小版本：[Docs/Ver/README.md](Docs/Ver/README.md)
- 剧本原文：`Docs/Res/剧本.txt`（不要改）

```text
Docs/     设计、接口、验收、小版本 TODO
game/     脚本、系统、数据、占位图、随包字体
```

出包仍走 Launcher 的 Windows / Android 构建。出包前跑 Lint，并勾 [验收清单](Docs/Dev/测试/验收清单.md)。
