# 游戏身份与窗口。不在此写玩法。

define config.name = _("四月，未命名的树")
define gui.show_name = True
define config.version = "0.1.0"
define build.name = "AprilUnnamedTree"
define config.save_directory = "AprilUnnamedTree"

# 本版本静音；不要因缺音频文件报错。
define config.has_sound = False
define config.has_music = False
define config.has_voice = False

# 无转场。
define config.enter_transition = None
define config.exit_transition = None
define config.intra_transition = None
define config.after_load_transition = None
define config.end_game_transition = None
define config.window_show_transition = None
define config.window_hide_transition = None

define config.window = "show"

# 打字速度固定；句间 AFM 默认见 engine_flags。
default preferences.text_cps = 50
default preferences.afm_time = 15

define gui.about = _("")
