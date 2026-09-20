# 设置走独立 persistent，不和解锁、存档槽混字段。

init python:
    from collections import namedtuple

    SettingsRecord = namedtuple(
        "SettingsRecord",
        ("afm_level", "font_size_level", "window_mode"),
    )

    _SETTINGS_DEFAULT = SettingsRecord("mid", "mid", "window")
    _AFM_LEVELS = ("slow", "mid", "fast")
    _FONT_SIZE_LEVELS = ("small", "mid", "large")
    _WINDOW_MODES = ("window", "fullscreen")
    _FONT_PATH = "fonts/MAPLEMONO-NF-CN-REGULAR.TTF"
    _AFM_TIME_BY_LEVEL = {
        "slow": 30,
        "mid": 15,
        "fast": 5,
    }
    _CPS_BY_LEVEL = {
        "slow": 25,
        "mid": 50,
        "fast": 80,
    }
    # 对白名 / 对白 / 按钮。中档对齐现有 say 窗口。
    _SIZE_BY_LEVEL = {
        "small": (24, 18, 16),
        "mid": (28, 22, 18),
        "large": (34, 28, 22),
    }

    class _SettingsStore(object):

        def load(self):
            data = persistent.sakura_settings
            if not isinstance(data, dict):
                return _SETTINGS_DEFAULT
            record = SettingsRecord(
                data.get("afm_level", _SETTINGS_DEFAULT.afm_level),
                data.get("font_size_level", _SETTINGS_DEFAULT.font_size_level),
                data.get("window_mode", _SETTINGS_DEFAULT.window_mode),
            )
            if not self._record_valid(record):
                return _SETTINGS_DEFAULT
            return record

        def save(self, record):
            if not self._record_valid(record):
                return False
            window_mode = record.window_mode
            if self.is_android():
                window_mode = self.load().window_mode
            persistent.sakura_settings = {
                "afm_level": record.afm_level,
                "font_size_level": record.font_size_level,
                "window_mode": window_mode,
            }
            renpy.save_persistent()
            self.apply_current()
            return True

        def sync_afm(self):
            level = self.load().afm_level
            preferences.afm_time = _AFM_TIME_BY_LEVEL.get(
                level,
                _AFM_TIME_BY_LEVEL["mid"],
            )
            preferences.text_cps = self.text_cps()

        def apply_current(self):
            rec = self.load()
            self.sync_afm()
            sizes = _SIZE_BY_LEVEL.get(rec.font_size_level, _SIZE_BY_LEVEL["mid"])
            renpy.store.sakura_font = _FONT_PATH
            renpy.store.dialogue_name_size = sizes[0]
            renpy.store.dialogue_text_size = sizes[1]
            renpy.store.ui_text_size = sizes[2]
            # 不在这里写 fullscreen：运行时以 preference 为准，避免改速度把 F 打回去。

        def apply_display(self):
            if self.is_android():
                preferences.fullscreen = True
                return
            rec = self.load()
            preferences.fullscreen = rec.window_mode == "fullscreen"

        def text_cps(self):
            level = self.load().afm_level
            return _CPS_BY_LEVEL.get(level, _CPS_BY_LEVEL["mid"])

        def is_android(self):
            return bool(getattr(renpy, "android", False))

        def _record_valid(self, record):
            if record.afm_level not in _AFM_LEVELS:
                return False
            if record.font_size_level not in _FONT_SIZE_LEVELS:
                return False
            if record.window_mode not in _WINDOW_MODES:
                return False
            return True

    SettingsStore = _SettingsStore()


default sakura_font = "fonts/MAPLEMONO-NF-CN-REGULAR.TTF"
default dialogue_name_size = 28
default dialogue_text_size = 22
default ui_text_size = 18


init 2 python:
    SettingsStore.apply_current()
    if SettingsStore.is_android():
        SettingsStore.apply_display()
