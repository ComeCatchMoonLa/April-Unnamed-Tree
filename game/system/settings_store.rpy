# 设置走独立 persistent，不和解锁、存档槽混字段。

init python:
    from collections import namedtuple

    SettingsRecord = namedtuple(
        "SettingsRecord",
        ("afm_level", "font_size_level", "font_id", "window_mode"),
    )

    _SETTINGS_DEFAULT = SettingsRecord("mid", "mid", "sans", "window")
    _AFM_LEVELS = ("slow", "mid", "fast")
    _FONT_SIZE_LEVELS = ("small", "mid", "large")
    _FONT_IDS = ("sans", "serif")
    _WINDOW_MODES = ("window", "fullscreen")
    # 文档未给三档秒数；15 与 options 中档一致，慢/快按此对称。
    _AFM_TIME_BY_LEVEL = {
        "slow": 30,
        "mid": 15,
        "fast": 5,
    }

    class _SettingsStore(object):

        def load(self):
            data = persistent.sakura_settings
            if not isinstance(data, dict):
                return _SETTINGS_DEFAULT
            record = SettingsRecord(
                data.get("afm_level", _SETTINGS_DEFAULT.afm_level),
                data.get("font_size_level", _SETTINGS_DEFAULT.font_size_level),
                data.get("font_id", _SETTINGS_DEFAULT.font_id),
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
                "font_id": record.font_id,
                "window_mode": window_mode,
            }
            renpy.save_persistent()
            return True

        def sync_afm(self):
            level = self.load().afm_level
            preferences.afm_time = _AFM_TIME_BY_LEVEL.get(
                level,
                _AFM_TIME_BY_LEVEL["mid"],
            )

        def text_cps(self):
            return 50

        def is_android(self):
            return bool(getattr(renpy, "android", False))

        def _record_valid(self, record):
            if record.afm_level not in _AFM_LEVELS:
                return False
            if record.font_size_level not in _FONT_SIZE_LEVELS:
                return False
            if record.font_id not in _FONT_IDS:
                return False
            if record.window_mode not in _WINDOW_MODES:
                return False
            return True

    SettingsStore = _SettingsStore()


init 2 python:
    SettingsStore.sync_afm()
