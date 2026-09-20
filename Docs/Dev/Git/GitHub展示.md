# GitHub 展示

- 目的：约定仓库 About、根 README、Releases 怎么给开发者与玩家看。不改玩法。
- 读者：发版、改仓库简介的人。
- 关系：忽略规则见 [Git工作流](Git工作流.md)。文档入口仍是 [Docs/Dev/README.md](../README.md)。小版本见 [Docs/Ver/README.md](../../Ver/README.md)。
- 版本：v1.5
- 日期：2026-09-21
- 仓库：https://github.com/ComeCatchMoonLa/April-Unnamed-Tree

GitHub 仓库名是发行名 `April-Unnamed-Tree`。本机文件夹仍是 `Sakura`（Launcher 列表用这个名字），不要为了跟 GitHub 改本地目录。

根 `README.md`、标签 `v1.0.0`、Releases 双端包、About 简介与 Topics **已经落盘/已发布**。License 仍待填。不要建 Pages。

## 1. 仓库 About

已填，以后保持一致（不要改成假协议名）：

- Description：`本地 ADV《四月，未命名的树》—— Ren'Py 8，Windows / Android`
- Topics：`renpy` `visual-novel` `adv` `galgame` `chinese`
- Releases：开；Wiki：关
- License：**待填**。未选定前不要在 GitHub 点 License 模板，也不要在根 README 写假协议名

## 2. 根 README

正文以仓库根 [`README.md`](../../../README.md) 为准，不要在本文再贴一份会过期的拷贝。

约定仍有效：

- 必须有文档入口：`Docs/Dev/README.md`、`Docs/Ver/README.md`
- 必须嵌入 `Docs/Res/标题主界面.png` 与 `Docs/Res/对白.png`
- 写明引擎用 Launcher、不要系统 Python、工程目录是上一级 `Renpy_Projects`
- 不要把整份设计粘进 README
- 玩家只指向 Releases，不在 README 教编译

## 3. 玩家向：Release

当前最新：https://github.com/ComeCatchMoonLa/April-Unnamed-Tree/releases/tag/v1.0.0

以后每个小版本标签同样挂两文件（**不进 git**）：

| 平台 | 文件名 |
|---|---|
| Windows | `April-Unnamed-Tree-win-vX.Y.Z.7z`（Launcher 默认 zip，Release 改压 7z） |
| Android | `April-Unnamed-Tree-android-vX.Y.Z.apk`（Universal APK；不上 AAB） |

Release 说明至少含：

- 版本与日期
- 需要 Win10+ / Android 5.0+
- 本版本无语音、无正式美术、无音乐
- 单存档、无回滚
- 文档不面向玩家；玩家不需要装 Ren'Py SDK

仓库内截图：`Docs/Res/标题主界面.png`、`Docs/Res/对白.png`。根 `README.md` 与 `Docs/Ver/README.md` 必须嵌入这两张。不要设置/Log/鉴赏，不要程序花瓣图。这两张是文档资源，不要挪进 `game/images/`。

## 4. GitHub Pages

可选。路径建议 `docs/site/` 或仓库 Pages 根（与 `Docs/` 开发文档分开）。

若做单页：标题与一句话、指向最新 Release 的下载、平台说明、声明无语音/无正式美术/标记音效不播放。不要写源码编译教程（那是根 README 的事）。不要放空下载按钮。

**现在不上 Pages。**

## 5. 安全与展示边界

- 不要在 README 贴存档路径里的个人进度（可以写「档在用户目录、不在安装包」）
- 不要公开 Android 签名密钥，不要把 `.keystore` 当 Release 资产
- 仓库可以公开源码；`saves/`、构建产物、`dists` 不得进库

## 6. Contributors 侧栏

GitHub 仓库页 **Contributors: No contributors** 不是没人提交。当前 `main` 作者是：

```text
ComeCatchMoonLa <comecatchmoonla@example.com>
```

`example.com` 无法验证，GitHub 不能把提交算到账号上，侧栏就是空的。`.mailmap` 改不了这个侧栏。

不要为了填侧栏去改已经 push 的作者（等于重写 `main` 再 force push）。

以后新提交要出现在 Contributors：在 [GitHub Emails](https://github.com/settings/emails) 看已验证邮箱，本机自己改 `user.email` 与之相同。Agent **不改** git config。旧提交仍不会出现。

## 7. 修订记录

| 版本 | 变更 |
|---|---|
| v1.0 | 开发者 README 模板 + 玩家 Release/Pages 约定；License 待填。 |
| v1.1 | 根 README 模板增加 Docs/Ver 入口。 |
| v1.2 | Win Release 改为 `.7z`；Android 用 Universal APK；截图定为标题+对白。 |
| v1.3 | 改为已发布状态：指向真 README / v1.0.0 Release；不再当初始化模板。 |
| v1.4 | README/Ver 必须嵌展示截图；记下 Contributors 为空是 example.com 邮箱。 |
| v1.5 | 仓库改名为 `April-Unnamed-Tree`；本机目录仍叫 `Sakura`。 |
