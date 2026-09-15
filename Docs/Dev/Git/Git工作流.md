# Git 工作流

- 目的：规定分支、提交、忽略规则。本轮不在仓库根创建文件，只给模板。
- 读者：实现者、发布者。
- 关系：GitHub 展示见 [GitHub展示](GitHub展示.md)。验收挂钩见 [验收清单](../测试/验收清单.md)。小版本标签见 [Docs/Ver/README.md](../../Ver/README.md)。
- 版本：v1.1
- 日期：2026-09-15

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

不要把无关格式化与功能改动混在一次提交。不要提交存档、密钥、`.rpyc`。

## 3. `.gitignore` 模板

实现阶段放到仓库根：

```gitignore
# Ren'Py
*.rpyc
*.rpymc
*.rpa
cache/
saves/
game/saves/
game/cache/

# 构建
dist/
*.apk
*.aab
*.exe

# 本地
.vscode/
.idea/
*.log
__pycache__/
.python-version

# 系统
Thumbs.db
Desktop.ini
.DS_Store
```

说明：`.vscode/` 默认忽略。若团队决定提交推荐扩展文件，可改为只跟踪 `.vscode/extensions.json` 与 `settings.json`，仍忽略工作区其它本地文件。与 [开发环境](../调研/开发环境.md) 一致。

不要提交：玩家存档、密钥、过大二进制。本版本白图很小，可以进库。日后正式美术再考虑 Git LFS。

## 4. 不提交的内容

- `persistent` 与 slot 文件
- Ren'Py 自动生成的 `log.txt`、traceback
- Android 签名密钥
- 含账号的本地配置

## 5. 标签与发布

出包与小版本结束时在 `main` 打标签，与 [Docs/Ver](../../Ver/README.md) 对齐：`v0.1.0` … `v0.9.0`，完整双端为 `v1.0.0`。Release 资产命名见 GitHub 展示文。

## 6. 修订记录

| 版本 | 变更 |
|---|---|
| v1.0 | 主干 + 短分支；gitignore 模板本轮不落盘。 |
| v1.1 | 标签与 Docs/Ver 小版本对齐。 |
