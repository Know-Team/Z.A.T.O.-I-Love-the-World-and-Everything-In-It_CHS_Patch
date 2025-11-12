









init -2 python:
    gui.init(1280, 720)













define -2 gui.accent_color = '#ffffff'


define -2 gui.idle_color = '#888888'



define -2 gui.idle_small_color = '#aaaaaa'


define -2 gui.hover_color = '#DEC17E'



define -2 gui.selected_color = '#ffffff'


define -2 gui.insensitive_color = '#8888887f'



define -2 gui.muted_color = '#3d5166'
define -2 gui.hover_muted_color = '#5b7a99'


define -2 gui.text_color = '#ffffff'
define -2 gui.interface_text_color = '#ffffff'





define -2 gui.text_font = "cour.ttf"


define -2 gui.name_text_font = "cour.ttf"


define -2 gui.interface_text_font = "cour.ttf"

translate SimplifiedChinese style default:
    font "Plix-ExtraLight.otf"
translate SimplifiedChinese style label_text:
    font "Plix-ExtraLight.otf"
translate SimplifiedChinese style gui_text:
    font "Plix-ExtraLight.otf"
translate SimplifiedChinese style button_text:
    font "Plix-ExtraLight.otf"
translate SimplifiedChinese style say_dialogue:
    font "Plix-ExtraLight.otf"
translate SimplifiedChinese style history_text:
    font "Plix-ExtraLight.otf"
translate SimplifiedChinese style confirm_prompt_text:
    font "Plix-ExtraLight.otf"
translate SimplifiedChinese style choice_button_text:
    font "Plix-ExtraLight.otf"

translate SimplifiedChinese python:
    gui.name_text_font = "Plix-ExtraLight.otf"

define -2 gui.text_size = 22


define -2 gui.name_text_size = 30


define -2 gui.interface_text_size = 22


define -2 gui.label_text_size = 24


define -2 gui.notify_text_size = 16


define -2 gui.title_text_size = 50





define -2 gui.main_menu_background = "gui/main_menu.png"
define -2 gui.game_menu_background = "gui/game_menu.png"








define -2 gui.textbox_height = 185



define -2 gui.textbox_yalign = 1.0




define -2 gui.name_xpos = 200
define -2 gui.name_ypos = -60



define -2 gui.name_xalign = 0.0



define -2 gui.namebox_width = None
define -2 gui.namebox_height = None



define -2 gui.namebox_borders = Borders(20, 15, 20, 15)



define -2 gui.namebox_tile = False





define -2 gui.dialogue_xpos = 268
define -2 gui.dialogue_ypos = 35


define -2 gui.dialogue_width = 744



define -2 gui.dialogue_text_xalign = 0.0








define -2 gui.button_width = None
define -2 gui.button_height = None


define -2 gui.button_borders = Borders(4, 4, 4, 4)



define -2 gui.button_tile = False


define -2 gui.button_text_font = gui.interface_text_font


define -2 gui.button_text_size = gui.interface_text_size


define -2 gui.button_text_idle_color = gui.idle_color
define -2 gui.button_text_hover_color = gui.hover_color
define -2 gui.button_text_selected_color = gui.selected_color
define -2 gui.button_text_insensitive_color = gui.insensitive_color



define -2 gui.button_text_xalign = 0.0








define -2 gui.radio_button_borders = Borders(18, 4, 4, 4)

define -2 gui.check_button_borders = Borders(18, 4, 4, 4)

define -2 gui.confirm_button_text_xalign = 0.5

define -2 gui.page_button_borders = Borders(10, 4, 10, 4)

define -2 gui.quick_button_borders = Borders(10, 4, 10, 0)
define -2 gui.quick_button_text_size = 14
define -2 gui.quick_button_text_idle_color = gui.idle_small_color
define -2 gui.quick_button_text_selected_color = gui.accent_color












define -2 gui.choice_button_width = 790
define -2 gui.choice_button_height = None
define -2 gui.choice_button_tile = False
define -2 gui.choice_button_borders = Borders(100, 5, 100, 5)
define -2 gui.choice_button_text_font = gui.text_font
define -2 gui.choice_button_text_size = gui.text_size
define -2 gui.choice_button_text_xalign = 0.5
define -2 gui.choice_button_text_idle_color = "#cccccc"
define -2 gui.choice_button_text_hover_color = "#ffffff"
define -2 gui.choice_button_text_insensitive_color = "#444444"









define -2 gui.slot_button_width = 276
define -2 gui.slot_button_height = 206
define -2 gui.slot_button_borders = Borders(10, 10, 10, 10)
define -2 gui.slot_button_text_size = 14
define -2 gui.slot_button_text_xalign = 0.5
define -2 gui.slot_button_text_idle_color = gui.idle_small_color
define -2 gui.slot_button_text_selected_idle_color = gui.selected_color
define -2 gui.slot_button_text_selected_hover_color = gui.hover_color


define -2 config.thumbnail_width = 256
define -2 config.thumbnail_height = 144


define -2 gui.file_slot_cols = 3
define -2 gui.file_slot_rows = 2









define -2 gui.navigation_xpos = 40


define -2 gui.skip_ypos = 10


define -2 gui.notify_ypos = 45


define -2 gui.choice_spacing = 22


define -2 gui.navigation_spacing = 4


define -2 gui.pref_spacing = 10


define -2 gui.pref_button_spacing = 0


define -2 gui.page_spacing = 0


define -2 gui.slot_spacing = 10


define -2 gui.main_menu_text_xalign = 1.0








define -2 gui.frame_borders = Borders(4, 4, 4, 4)


define -2 gui.confirm_frame_borders = Borders(40, 40, 40, 40)


define -2 gui.skip_frame_borders = Borders(16, 5, 50, 5)


define -2 gui.notify_frame_borders = Borders(16, 5, 40, 5)


define -2 gui.frame_tile = False











define -2 gui.bar_size = 25
define -2 gui.scrollbar_size = 12
define -2 gui.slider_size = 25


define -2 gui.bar_tile = False
define -2 gui.scrollbar_tile = False
define -2 gui.slider_tile = False


define -2 gui.bar_borders = Borders(4, 4, 4, 4)
define -2 gui.scrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.slider_borders = Borders(4, 4, 4, 4)


define -2 gui.vbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vslider_borders = Borders(4, 4, 4, 4)



define -2 gui.unscrollable = "hide"







define -2 config.history_length = 100



define -2 gui.history_height = None



define -2 gui.history_name_xpos = 155
define -2 gui.history_name_ypos = 50
define -2 gui.history_name_width = 155
define -2 gui.history_name_xalign = 1.0


define -2 gui.history_text_xpos = 170
define -2 gui.history_text_ypos = 50
define -2 gui.history_text_width = 740
define -2 gui.history_text_xalign = 0.0







define -2 gui.nvl_borders = Borders(0, 0, 0, 0)



define -2 gui.nvl_list_length = 6



define -2 gui.nvl_height = None



define -2 gui.nvl_spacing = 5



define -2 gui.nvl_name_xpos = 0
define -2 gui.nvl_name_ypos = 0
define -2 gui.nvl_name_width = 150
define -2 gui.nvl_name_xalign = 1.0


define -2 gui.nvl_text_xpos = 250
define -2 gui.nvl_text_ypos = 100
define -2 gui.nvl_text_width = 800
define -2 gui.nvl_text_xalign = 0.0



define -2 gui.nvl_thought_xpos = 550
define -2 gui.nvl_thought_ypos = 0
define -2 gui.nvl_thought_width = 550
define -2 gui.nvl_thought_xalign = 0.0


define -2 gui.nvl_button_xpos = 450
define -2 gui.nvl_button_xalign = 0.0







define -2 gui.language = "unicode"






init -2 python:



    @gui.variant
    def touch():
        
        gui.quick_button_borders = Borders(40, 14, 40, 0)



    @gui.variant
    def small():
        
        
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34
        
        
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.dialogue_xpos = 90
        gui.dialogue_width = 1100
        
        
        gui.slider_size = 36
        
        gui.choice_button_width = 1240
        gui.choice_button_text_size = 30
        
        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10
        
        gui.history_height = 190
        gui.history_text_width = 690
        
        gui.quick_button_text_size = 20
        
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        
        
        gui.nvl_height = 170
        
        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325
        
        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5
        
        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20
        
        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
