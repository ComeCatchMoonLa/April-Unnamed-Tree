# GitHub 展示

- 目的：同时服务开发者克隆与玩家下载。本轮只给模板，不创建仓库根 README、不建 Pages、不选定 License。
- 读者：初始化 GitHub 仓库的人。
- 关系：忽略规则见 [Git工作流](Git工作流.md)。文档入口仍是 [Docs/Dev/README.md](../README.md)。小版本见 [Docs/Ver/README.md](../../Ver/README.md)。
- 版本：v1.1
- 日期：2026-09-15

## 1. 仓库 About

初始化时填写：

- Description：`本地 ADV《四月，未命名的树》—— Ren'Py 8，Windows / Android`
- Topics 建议：`renpy` `visual-novel` `adv` `galgame` `chinese`
- 勾选 Releases；Wiki 不必开
- License：**待填**。未选定前不要在 GitHub 点 License 模板，也不要在根 README 写假协议名

## 2. 开发者向：根 README 模板

实现阶段拷到仓库根 `README.md`。可按当时真实目录微调，但必须包含文档入口。

````markdown
# 四月，未命名的树

本地文字冒险（ADV）。Windows 10+ 与 Android 5.0+。无网页版。

本版本无正式美术、音乐、语音；画面为白底黑字占位。

## 开发

- 引擎：Ren'Py 8 SDK（用 Launcher 打开本目录，不要用系统 Python 运行）
- 编辑器：Cursor Profile「Py Dev」+ 工作区设置，见 `Docs/Dev/调研/开发环境.md`
- 开发文档入口：[`Docs/Dev/README.md`](Docs/Dev/README.md)
- 小版本 TODO：[`Docs/Ver/README.md`](Docs/Ver/README.md)
- 剧本：`Docs/Res/剧本.txt`

目录（实现后）：

```text
Docs/     文档
game/     脚本、系统、UI、数据、占位图、字体
```

出包：在 Ren'Py Launcher 构建 Windows / Android。出包前跑 Lint，并勾 `Docs/Dev/测试/验收清单.md`。

## 玩家

从 Releases 下载对应包。说明见下方「玩家向」发布约定。
````

根 README 不要粘贴整份设计。

## 3. 玩家向：Release

资产命名：

| 平台 | 文件名 |
|---|---|
| Windows | `April-Unnamed-Tree-win-vX.Y.Z.zip` |
| Android | `April-Unnamed-Tree-android-vX.Y.Z.apk` |

Release 说明至少含：

- 版本与日期
- 需要 Win10+ / Android 5.0+
- 本版本无语音、无正式美术、无音乐
- 单存档、无回滚
- 文档不面向玩家；玩家不需要装 Ren'Py SDK

截图：允许白底标题与对话各一张，放 `Docs/Res/screenshots/`（该目录实现阶段再建）。不要用程序花瓣图冒充成品。

## 4. GitHub Pages

可选单页，路径建议 `docs/site/` 或仓库 Pages 根（注意与 `Docs/` 开发文档分开，避免混淆）。

单页结构：

1. 标题与一句话简介
2. 下载链接（指向最新 Release）
3. 平台说明
4. 声明：无语音、无正式美术、标记音效不播放
5. 不提供源码编译教程（那是根 README 的事）

本阶段不强制上线 Pages。未发布包时不要放空下载按钮。

## 5. 安全与展示边界

- 不要在 README 贴存档路径里的个人进度
- 不要公开 Android 签名密钥
- 仓库可以公开源码；`saves/` 不得进库

## 6. 修订记录

| 版本 | 变更 |
|---|---|
| v1.0 | 开发者 README 模板 + 玩家 Release/Pages 约定；License 待填。 |
| v1.1 | 根 README 模板增加 Docs/Ver 入口。 |
