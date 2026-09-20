# 关闭默认回滚 / Skip / Hide / 退出确认 / 存档柜；打开引擎 AFM。
# toggle_afm 在 play_session；关窗写槽走 quit_callbacks。

default _confirm_quit = False
default preferences.afm_enable = True

define config.rollback_enabled = False
define config.hard_rollback_limit = 0
define config.allow_skipping = False
define config.fast_skipping = False
define config.has_autosave = False
define config.autosave_slots = 0
define config.quicksave_slots = 0
define config.autosave_on_quit = False
define config.autosave_on_choice = False
define config.autosave_on_input = False
define config.default_afm_enable = True
define config.quit_action = Quit(confirm=False)

init 1 python:
    # 在官方 keymap 之后清空，避免滚轮/右键/快捷键再打开默认功能。
    config.keymap["rollback"] = []
    config.keymap["rollforward"] = []
    config.keymap["hide_windows"] = []
    config.keymap["skip"] = []
    config.keymap["stop_skipping"] = []
    config.keymap["toggle_skip"] = []
    config.keymap["fast_skip"] = []
    config.keymap["save"] = []
    config.keymap["load"] = []
    config.keymap["quicksave"] = []
    config.keymap["quickload"] = []
    config.keymap["game_menu"] = []
    config.keymap["self_voicing"] = []
    config.keymap["clipboard_voicing"] = []
    # F1/S 改走 hud 里的 sakura_*，这里先摘掉默认帮助和截图。
    # 保留 toggle_fullscreen（F），不要清空。
    config.keymap["screenshot"] = []
    config.keymap["help"] = []
    config.help = None

    if "pad_rollback" in config.pad_bindings:
        config.pad_bindings["pad_rollback"] = []
    if "pad_hide_windows" in config.pad_bindings:
        config.pad_bindings["pad_hide_windows"] = []
    if "pad_toggle_skip" in config.pad_bindings:
        config.pad_bindings["pad_toggle_skip"] = []
