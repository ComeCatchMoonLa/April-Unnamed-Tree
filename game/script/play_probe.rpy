# 0.4 最小调试入口。Shift+O 后 jump play_probe / play_probe_continue / play_probe_replay_check。

label play_probe:
    python:
        _afm_before = preferences.afm_enable
        toggle_afm()
        _afm_after = preferences.afm_enable
        toggle_afm()
        SettingsStore.sync_afm()
        _cps = SettingsStore.text_cps()
        _afm_time = preferences.afm_time
        _pref_cps = preferences.text_cps
    "AFM [_afm_before]->[_afm_after] 已复原 enable=[preferences.afm_enable] cps=[_cps]/[_pref_cps] afm_time=[_afm_time]"
    $ PlaySession.start_new_game()

label play_probe_continue:
    $ _ok = PlaySession.continue_game()
    "继续失败：无槽或损坏"
    jump boot

label play_probe_replay:
    python:
        UnlockStore.unlock_node("ch1_start")
        _before = SaveStore.load_slot(SLOT_MAIN)
        _probe_before = _before.line_id if _before is not None else "None"
        _ok = PlaySession.enter_replay("ch1_start")
    "replay 未解锁或失败；槽仍 [_probe_before]"
    jump boot

label play_probe_replay_check:
    python:
        _after = SaveStore.load_slot(SLOT_MAIN)
        _probe_after = _after.line_id if _after is not None else "None"
        _mode = None
        ctx = PlaySession.current()
        if ctx is not None:
            _mode = ctx.play_mode
    "replay 后槽 line_id=[_probe_after] 会话=[_mode]"
    jump boot
