# Git 工作流

- 目的：规定分支、提交、仓库根忽略规则。`.gitignore` 已在仓库根。
- 读者：实现者、发布者。
- 关系：GitHub 展示见 [GitHub展示](GitHub展示.md)。验收挂钩见 [验收清单](../测试/验收清单.md)。小版本标签见 [Docs/Ver/README.md](../../Ver/README.md)。
- 版本：v1.2
- 日期：2026-09-20

## 1. 仓库

- 根目录：`Sakura/`
- 主干分支：`main`
- 功能分支：`feat/<子系统>`，例如 `feat/save-store`
- 修缺陷：`fix/<验收编号>`，例如 `fix/tc18-auto`

短生命周期。合并回 `main` 后删分支。

不强制 Pull Request。若使用 GitHub 协作：PR 描述必须列出触及的验收 TC 编号。

## 2. 提交说明

中文，一句话写清**为什么**，不要只列文件名。

```text
feat: 单槽写入只走 SaveStore，避免 UI 直接存档

fix: 回放 Return 不再写槽，防止鉴赏覆盖续玩
```

不要把无关格式化与功能改动混在一次提交。不要提交存档、密钥、`.rpyc`、安装包。

## 3. `.gitignore`

仓库根已有，维护时与下列内容对齐。**不要**忽略整个 `.vscode/`：`extensions.json` 与 `settings.json` 要进库。

```gitignore
# Ren'Py 编译与运行时
*.rpyc
*.rpymc
*.rpa
game/cache/
game/saves/
log.txt
traceback.txt

# 构建与签名（不要进库）
dist/
*.apk
*.aab
*.exe
*.keystore
android.keystore
bundle.keystore

# 本地与系统
.idea/
*.log
__pycache__/
Thumbs.db
Desktop.ini
.DS_Store
```

Ren'Py 语言扩展有时会把 `editor.tokenColorCustomizations` 写进 `.vscode/settings.json`。**不要提交**；脏了就 `git restore -- .vscode/settings.json`。

不要提交：玩家存档、密钥、过大二进制。本版本白图很小，可以进库。日后正式美术再考虑 Git LFS。`Docs/Res/` 里的展示截图可以进库（文档资源，体积可控）。

## 4. 不提交的内容

- `persistent` 与 slot 文件
- Ren'Py 自动生成的 `log.txt`、traceback
- Android 签名密钥
- 含账号的本地配置
- Launcher 产出的 zip / 自压的 `.7z` / `.apk`（Release 资产不进 git）
- `DEBUG_START` 停在某一节的元组

## 5. 标签与发布

出包与小版本结束时在 `main` 打标签，与 [Docs/Ver](../../Ver/README.md) 对齐：`v0.1.0` … `v0.9.0`，完整双端为 `v1.0.0`。Release 资产命名见 GitHub 展示文。

## 6. 修订记录

| 版本 | 变更 |
|---|---|
| v1.0 | 主干 + 短分支；gitignore 模板本轮不落盘。 |
| v1.1 | 标签与 Docs/Ver 小版本对齐。 |
| v1.2 | `.gitignore` 改为已落盘；跟踪 `.vscode`；补密钥与安装包忽略。 |
