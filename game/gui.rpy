# 设计基准 1280×720，白底黑字。只引用包内字体。

init python:
    gui.init(1280, 720)
    config.check_conflicting_properties = True

define gui.text_font = "fonts/MAPLEMONO-NF-CN-REGULAR.TTF"
define gui.name_text_font = "fonts/MAPLEMONO-NF-CN-REGULAR.TTF"
define gui.interface_text_font = "fonts/MAPLEMONO-NF-CN-REGULAR.TTF"

define gui.accent_color = "#000000"
define gui.idle_color = "#000000"
define gui.idle_small_color = "#404040"
define gui.hover_color = "#333333"
define gui.selected_color = "#000000"
define gui.insensitive_color = "#8888887f"
define gui.muted_color = "#666666"
define gui.hover_muted_color = "#444444"
define gui.text_color = "#000000"
define gui.interface_text_color = "#000000"

define gui.text_size = 22
define gui.name_text_size = 30
define gui.interface_text_size = 22
define gui.label_text_size = 24
define gui.notify_text_size = 16
define gui.title_text_size = 50

define gui.main_menu_background = Solid("#ffffff")
define gui.game_menu_background = Solid("#ffffff")

define gui.dialogue_text_xalign = 0.0
define gui.dialogue_text_line_spacing = 8
