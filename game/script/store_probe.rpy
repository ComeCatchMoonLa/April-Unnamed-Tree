# 0.3 最小调试入口。不挂默认启动。Shift+O 后 jump store_probe / store_probe_reload。

label store_probe:
    python:
        _probe_line = LineRef("ch1", "ch1_start", "ch1_start:0001", "omote", "main")
        _probe_write = SaveStore.write_line(SLOT_MAIN, _probe_line)
        _probe_replay = SaveRecord(
            SLOT_MAIN,
            "1970-01-01T00:00:00Z",
            "ch1",
            "ch1_start",
            "ch1_start:0001",
            "omote",
            "main",
            "replay",
            {"x": 1},
        )
        _probe_reject = SaveStore.write_record(_probe_replay)
        _probe_rec = SaveStore.load_slot(SLOT_MAIN)
        _probe_line_id = _probe_rec.line_id if _probe_rec is not None else "None"
        _probe_reserved_ok = _probe_rec is not None and _probe_rec.reserved == {}
        UnlockStore.unlock_node("ch1_start")
        UnlockStore.unlock_node("ch1_start")
        UnlockStore.unlock_cg("cg_yayoi_backlight")
        UnlockStore.unlock_after()
        UnlockStore.unlock_node("no_such_node")
        _probe_node = UnlockStore.is_node_unlocked("ch1_start")
        _probe_after = UnlockStore.is_after_unlocked()
        _probe_unknown = UnlockStore.is_node_unlocked("no_such_node")
        _probe_settings = SettingsRecord("fast", "large", "serif", "fullscreen")
        _probe_saved = SettingsStore.save(_probe_settings)
        SettingsStore.sync_afm()
        _probe_loaded = SettingsStore.load()
        _probe_cps = SettingsStore.text_cps()
        _probe_afm = _probe_loaded.afm_level
        _probe_size = _probe_loaded.font_size_level
        _probe_font = _probe_loaded.font_id
        _probe_afm_time = preferences.afm_time
    "存档：写入 [_probe_write] 拒绝回放 [_probe_reject] line_id=[_probe_line_id] reserved空=[_probe_reserved_ok]"
    "解锁：节点 [_probe_node] after [_probe_after] 未知 [_probe_unknown]"
    "设置：保存 [_probe_saved] afm=[_probe_afm] 字号=[_probe_size] 字体=[_probe_font] cps=[_probe_cps] afm_time=[_probe_afm_time]"
    jump boot

label store_probe_reload:
    python:
        _probe_rec = SaveStore.load_slot(SLOT_MAIN)
        _probe_line_id = _probe_rec.line_id if _probe_rec is not None else "None"
        _probe_node = UnlockStore.is_node_unlocked("ch1_start")
        _probe_after = UnlockStore.is_after_unlocked()
        _probe_loaded = SettingsStore.load()
        _probe_afm = _probe_loaded.afm_level
    "重启读档：line_id=[_probe_line_id] 节点 [_probe_node] after [_probe_after] afm=[_probe_afm]"
    jump boot

label store_probe_damage:
    python:
        _probe_backup = persistent.sakura_save_slots
        persistent.sakura_save_slots = {SLOT_MAIN: {"schema_version": 999}}
        _probe_bad = SaveStore.load_slot(SLOT_MAIN) is None
        persistent.sakura_save_slots = _probe_backup
        renpy.save_persistent()
    "损坏槽为 None：[_probe_bad]"
    jump boot
