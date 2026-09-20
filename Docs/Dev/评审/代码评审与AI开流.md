# 代码评审与 AI 开流

- 目的：让 AI 与人工评审按同一套禁止项和会话切分工作，稳定产出。
- 读者：实现者、代码评审、AI 会话。
- 关系：契约见接口设计；风格见 [编码规范](../实现/编码规范.md)。`.cursor/rules` **已落盘短指针**（`sakura.mdc`、不可逆补充），不要把整份设计贴进去。
- 版本：v1.3
- 日期：2026-09-20

## 1. 开流顺序

```text
设计评审通过
  → 一次会话只做一个子系统
    → 对照接口实现
      → 代码评审
        → 跑相关验收项 + renpy lint
```

禁止：未读设计就写 screen；一次会话同时改存档与三章剧本。

## 2. 会话切分（推荐顺序）

1. 工程骨架 + `engine_flags` + 白图字体
2. `NodeCatalog` + data 表
3. `SaveStore` + `UnlockStore` + `SettingsStore`
4. `PlaySession` + 引擎 AFM（`toggle_afm`）
5. 标题 / HUD / 设置 / Log
6. 选择肢三入口 + 中章 `scr_choice_hold`
7. 鉴赏
8. 按章脚本（ch1 → ch2 → ch3 → after → inner）
9. Win 包；再 Android 包

每个会话必读：

- [README](../README.md)
- 本文件
- 对应小版本 TODO：[Docs/Ver/README.md](../../Ver/README.md)
- [编码规范](../实现/编码规范.md)
- 该子系统接口文
- 相关游戏设计章节

## 3. 禁止项（评审直接拒）

- 扩大 scope：新设置项、新快捷键、新章、新 CG ID
- 改节点 ID、CG ID、`slot_id`、`line_id` 规则
- 把解锁写入存档槽
- 鉴赏写槽
- 恢复回滚 / Skip / Hide / 退出确认
- 自管 Auto（pending/active 或点击不退出）
- 用系统 Python 跑游戏
- 对 `.rpy` 开 Ruff 格式化
- 一次 PR/一次会话改无关的两层（例如顺手改 GitHub 文案）

## 4. 代码评审清单

| 项 | 问 |
|---|---|
| 契约 | 函数名、参数个数、返回与副作用是否与接口文一致 |
| 唯一入口 | 是否只有 SaveStore 写槽、UnlockStore 写解锁 |
| HUD/快捷键 | 是否调用同一函数 |
| 体量 | 文件 ≤500、目录 ≤15、参数 ≤5 |
| 多余功能 | diff 里是否出现未文档化行为 |
| 回放 | `replay` 是否所有写槽路径早退 |
| Auto | 是否只用引擎 AFM，有无自管状态机 |
| ID | 是否出现拼错的 node/cg |
| 资源 | 是否引用了非 `white` 的临时网图或系统字体 |

输出：通过 / 修改后重评。不通过不得宣称该子系统完成。

## 5. Cursor rules（已落盘）

`.cursor/rules` 只放短指针，例如：

```text
先读 Docs/Dev/README.md 与 Docs/Ver/README.md。
当前只做 Docs/Ver 里未勾完的最小版本。
一次只做一个可验收切片。
禁止实现需求分析里的「明确不做」。
不要改节点 ID。
不要用系统 Python 跑游戏。
```

禁止把整份设计文档贴进 rules。改规则时只改短指针，并与本文禁止项对齐。

## 6. 修订记录

| 版本 | 变更 |
|---|---|
| v1.0 | 会话切分、禁止项、评审清单；rules 留到实现阶段。 |
| v1.1 | 会话改为 PlaySession+引擎 AFM；禁止自管 Auto。 |
| v1.2 | 切分含中章 `scr_choice_hold`。 |
| v1.3 | `.cursor/rules` 改为已落盘短指针。 |
