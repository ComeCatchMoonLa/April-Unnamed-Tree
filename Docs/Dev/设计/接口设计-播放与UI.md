# 接口设计：播放与 UI

- 目的：给出播放会话、Auto、选择肢、screen 与 label 契约。
- 读者：system、UI、脚本、评审、AI 会话。
- 关系：数据层见 [接口设计-数据与存档](接口设计-数据与存档.md)；行为见 [游戏设计-存档与播放](游戏设计-存档与播放.md) 与 [游戏设计-界面与操作](游戏设计-界面与操作.md)。
- 版本：v1.6
- 日期：2026-09-20

参数不得超过 5 个。会话状态放在 `PlayContext`，不要把上下文拆成一长串实参。

## 1. PlayContext

```text
PlayContext
  play_mode: string          # play | replay
  chapter_id: string
  node_id: string
  line_id: string
  style: string              # omote | ura
  route: string
```

同时只有一个活动上下文。离开游玩或回放时清会话，但 `play` 离开前先 `commit_leave`。回放离开回鉴赏，不经标题点「鉴赏」。

## 2. PlaySession

| 函数 | 参数 | 返回 | 副作用 |
|---|---|---|---|
| `start_new_game` | 无 | `None` | `play`；把槽写成 `ch1_start` 首句；跳转该句 |
| `continue_game` | 无 | `bool` | 无槽 False；有槽从 `line_id` 句首跳（标题仅在未解锁后日谈时调用） |
| `enter_after` | 无 | `bool` | 未解锁 False；槽在 after 则续该句，否则进 `after_start` |
| `enter_inner` | 无 | `bool` | 未解锁 False；槽在 inner 则续该句，否则进 `inner_start` |
| `enter_replay` | `node_id` | `bool` | 未解锁 False；`replay`；不写槽 |
| `on_node_reached` | `node_id` | `None` | play：unlock 节点 + 写槽；replay：忽略写槽 |
| `on_cg_shown` | `cg_id` | `None` | play：unlock CG；replay：忽略 |
| `on_line_shown` | `line_id` | `None` | 更新上下文当前句；不写槽 |
| `commit_leave` | 无 | `None` | play 写当前句后回标题；replay 不写，回鉴赏 |
| `apply_style` | `style` | `None` | 改对话框样式 |
| `sync_inner_dim` | 无 | `None` | `chapter_id==inner` 则开暗层，否则关 |
| `current` | 无 | `PlayContext \| None` | 无 |
| `current_line_ref` | 无 | `LineRef \| None` | 供 SaveStore |

`continue_game`：无槽或槽损坏返回 False。标题只在有槽且尚未 `after_unlocked` 时调用。真选项之后的 after/inner 续玩见存档与播放文 §3.4，走 `enter_after` / `enter_inner`。

`start_new_game`：把槽写成 `ch1_start` 首句。玩家标题仅在无槽时调用；有槽不得出现「新的游戏」。调试探针仍可调用（会覆盖槽）。

真选项「结束」：`unlock_after`；`write_line` 为 after 首句；回标题。不要进入 after 播放。

真选项「继续」：`unlock_after`；进入 `after_start` 播放。

后日谈章末：`unlock_inner`。

## 3. Auto（引擎 AFM）

不实现 `AutoController`。HUD 与快捷键共用下面一个入口：

| 函数 | 参数 | 返回 | 副作用 |
|---|---|---|---|
| `toggle_afm` | 无 | `None` | 立刻翻转 `preferences.afm_enable` |

- 句间等待、点击是否退出 Auto、模态暂停：全部跟引擎默认。
- 禁止自写 pending/active，禁止在点击路径里保留 Auto。
- `SettingsStore.sync_afm` 按 `afm_level` 写 `preferences.afm_time` 与 `preferences.text_cps`。
- screen 里也可用引擎 `Preference("auto-forward enable")`，但必须与 `toggle_afm` / `A` 改同一 preference。

## 4. 选择肢入口

三种独立函数，对应三个 screen。不要合并成带 type 字符串的万能函数（若必须共用内部 helper，对外仍三入口）。

| 函数 | 参数 | 行为 |
|---|---|---|
| `run_choice_fake` | `left: string`, `right: string` | 两可点按钮；点任一继续；Log「选择：文案」；无分支变量 |
| `run_choice_display` | `left: string`, `right: string` | 不可点；空白/对话框点击关闭；Log「选项（未选择）」 |
| `run_choice_true` | 无 | 固定「继续」「结束」；见 PlaySession 规则 |

文案常量（首章/中章）放 data 或脚本字面量均可，但不得在 UI 里改字。

## 5. Label 入口

脚本 label 必须存在且稳定：

| label | 含义 |
|---|---|
| `splash_or_boot` | 可选；最终落到标题 |
| `title_loop` | 标题；不在游玩会话中 |
| `ch1_start` | 与节点 `ch1_start` 对齐，下同 |
| `ch2_start` | 中章 |
| `ch3_ledger` | 尾章开头 |
| `after_start` | 后日谈 |
| `inner_start` | 里后日谈 |

其它节点可用 label 或节点内跳转，但 `PlaySession` 跳转必须以 `line_id` 能定位为准。推荐每个节点一个 label，名称等于 `node_id`。

从任意 `line_id` 开始播放：由脚本提供 `jump_to_line(line_id)`（参数 1 个）。找不到则回标题并视为读档失败。

## 6. Screen 契约

| screen | 何时 | 必须提供的行为 |
|---|---|---|
| `scr_title` | 标题 | 主进度一键三态；里解锁后紧插其下；Esc 不退出 |
| `scr_hud` | 游玩/回放 overlay | 五键；replay 时 Save 禁用 |
| `scr_settings` | 模态 | 选项三项 + 快捷键只读页；F1 关闭自己 |
| `scr_log` | 模态 | 只读；不可跳转 |
| `scr_gallery` | 鉴赏 | 章节/CG 分页 |
| `scr_gallery_cg` | CG 全屏 | 白图+名称；点击回列表 |
| `scr_staff_menu` | 主界面制作名单 | 固定文案；点击回标题 |
| `scr_choice_fake` | 首章 | 见上 |
| `scr_choice_display` | 中章 | 见上 |
| `scr_choice_true` | 尾章 | 见上 |
| `scr_inner_dim` | inner 时 | 全屏 60% 黑；不挡点击到下层对话 |

HUD 与快捷键必须调用同一 PlaySession 函数（Return/Save）以及同一 `toggle_afm`，禁止各写一套。

设置中 Android 隐藏窗口/全行。无字体列表。Windows 保留引擎 `F` 切全屏。

## 7. 样式与亮度

| 函数 | 参数 | 行为 |
|---|---|---|
| `apply_style` | `style` | omote 白底黑字；ura 深灰底白字 |
| `sync_inner_dim` | 无 | 见 PlaySession |

色值默认：omote `#FFFFFF`/`#000000`；ura `#2A2A2A`/`#FFFFFF`；暗层 `#000000` alpha 0.60。

## 8. 输入

| 输入 | 绑定 |
|---|---|
| `A` | `toggle_afm`（仅游戏场景） |
| `L` | 打开/关 Log（仅游戏场景） |
| `S` | play 则 `SaveStore.write_line`；replay 忽略 |
| `F1` | 开关设置 |
| `Esc` | 游戏场景 = Return（play 回标题，replay 回鉴赏）；标题忽略；设置打开时关设置 |
| `F` | 切换窗口/全屏（仅 Windows；与设置窗口项同一 preference） |
| Android 返回 | 同当前场景的 Return / 关设置 |

## 9. 完成定义（本接口）

实现本接口算完成，当且仅当：

- 无槽「新的游戏」/ 有槽「继续」/ 解锁后「后日谈」+ 可选「里」/ 鉴赏回放 / 真选项两条路径可按契约走通
- replay 下 Save、节点到达、Return、退出都不写槽；Return 与章末回鉴赏
- Auto 为引擎默认 AFM（`toggle_afm` + preference）
- 所有 screen 名称与上表一致（允许加前缀但评审文档须同步；本版本就用上表名）

## 10. 修订记录

| 版本 | 变更 |
|---|---|
| v1.0 | 给出 PlaySession、Auto、选择肢、screen/label 契约。 |
| v1.1 | 删除 AutoController；改为 `toggle_afm` 与引擎 AFM。 |
| v1.2 | 标题显隐；`start_new_game` 不再作为有槽玩家入口。 |
| v1.3 | 主进度三态；`enter_after` / `enter_inner` 按槽续玩。 |
| v1.4 | 设置三项；速度带动 CPS；快捷键页两列；保留 `F`。 |
| v1.5 | 快捷键页不要求表格对齐。 |
| v1.6 | `commit_leave`：replay 回鉴赏；play 仍回标题。 |
