# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.
screen bars:
    frame:
        style "top_bar"
    frame:
        style "bottom_bar"
        
init python:
    config.thumbnail_width = 160
    config.thumbnail_height = 90

    style.enc_list = Style(style.default)
    style.enc_frame = Style(style.default)
    style.enc_entry = Style(style.default)
    style.enc_list_text = Style(style.text)
    style.nvl_window.xpadding = 270
    style.nvl_window.ypadding = 80
    style.nvl_window.background = "gui/nvl.png"
    
    style.enc_list.background = "gui/glossary.png"
    style.enc_entry.background = "gui/glossary2.png"
    style.enc_frame.background = None
    

    style.enc_list_text.hover_color = "#f12"
    style.enc_list_text.hover_background = "#333333"

    style.enc_list_text.selected_color = "#f12"

    #style.enc_list.hover = "#222222"

            
init -2 python: 
    style.top_bar.area = (0, 0, 1.0, 114) # sets xpos, ypos, width, height for item
    style.top_bar.background = "#000" # background colour is black
    
    style.bottom_bar.area = (0, 606, 1.0, 114) # sets xpos, ypos, width, height for item
    style.bottom_bar.background = "#000" # background colour is black




##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            #if who:
                #text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    #use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    #use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu
    #zorder -1
    #$ renpy.transition(dissolve)

    $ renpy.music.stop(channel='sound', fadeout=None)
    
    

    # The background of the main menu.
    window:
        style "mm_root"

    add "menuitem_new"
    add "menuitem_load"
    add "menuitem_preferences"
    add "menuitem_credits"
    add "menuitem_extras"
    add "menuitem_quit"
    add "logo2"
    add "logosc"
    add "logovn"

    #add "scvnlogomm"




    # The main menu buttons.
    #frame:
        #style_group "mm"
        #xalign .98
        #yalign .98RR
        #has vbox

        #textbutton _("Start Game") action Start()
        #textbutton _("Load Game") action ShowMenu("mm_load")
        #textbutton _("Extras") action ShowMenu("extras_menu")
        #textbutton _("Preferences") action ShowMenu("mm_preferences")
        #textbutton _("Help") action Help()
        #textbutton _("Quit") action Quit(confirm=False)
        
            # The various buttons.

    imagemap:
        ground "im_mm_ground"
        idle "im_mm_ground"
        hover "im_mm_hover"
        selected_idle "im_mm_hover"
        selected_hover "im_mm_hover"
        
        hotspot (1010,337,239,39) action Start()
        hotspot (1010,390,239,39) action ShowMenu("mm_load")
        hotspot (1010,441,239,39) action ShowMenu("mm_preferences")
        hotspot (1010,497,239,39) action ShowMenu("extras_menu")
        hotspot (1010, 550,239,39) action Start("endcredits")
        hotspot (1010, 653,239,39) action Quit()
init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"

##############################################################################
# EXTRAS
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen extras_menu():

    # This ensures that any other menu screen is replaced.
    tag menu
    #zorder -1
    add "default_mm"
    #add "menuitem_back"
    #if not persistent.beat_game:
        #add "menuitem_unknown"
    #if persistent.beat_game:
        #add "menuitem_backers"
    #add "menuitem_day9"
    add "e_logo2title"
    add "e_logosctitle"
    add "e_logovntitle"
    add "logosextra"



    # The background of the main menu.
    #window:
        #style "mm_root"

    #add "menuitem"
    #add "menuitem2"
    #add "menuitem3"
    #add "menuitem4"
    #add "logo2"
    #add "logovn"

    #add "scvnlogomm"



    # The main menu buttons.
    #frame:
        #style_group "mm"
        #xalign .98
        #yalign .98
        #has vbox

        #textbutton _("Day9") action Start("day9scene")
        #textbutton _("Dev/Backer Commentary") action Start("backerscene")
        #textbutton _("Main Menu") action ShowMenu("main_menu")
        #textbutton _("Quit Game") action Quit(confirm=False)
        
            # The various buttons.

    imagemap:
        if not persistent.beat_game:
            ground "extras_menu_unknown"
            idle "extras_menu_unknown"
            hover "extras_menu_hover_unknown"
        if persistent.beat_game:
            ground "extras_menu" 
            idle "extras_menu"
            hover "extras_menu_hover" 
        #selected_idle "im_mm_hover"
        #selected_hover "im_mm_hover"
        
        hotspot (1010,440, 246,42) action Start("day9scene") hovered ShowTransient("the_img", img="extras_day9") unhovered Hide("the_img")
        if persistent.beat_game:
            hotspot (1010,497,246,42) action Start("backerscene") hovered ShowTransient("the_img", img="extras_backer") unhovered Hide("the_img")
        if not persistent.beat_game:
            hotspot (1010,497,246,42) action None hovered ShowTransient("the_img", img="extras_backer_unknown") unhovered Hide("the_img")

        hotspot (1030, 597,246,47) action Return()
        
screen the_img(img):
    add img pos (0, 0)

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    add "prefmenuanimred"
    add "prefmenuanim"
    add "prefmenuanim2"
    #zorder 1


    imagemap:
         ground "prefmenu"
         hover "prefmenuhover"
         idle "prefmenu"
         
         hotspot (1020, 21, 261, 44) action ShowMenu("encyclopaedia_list")
         hotspot (1020, 138, 261, 44) action Return()
         hotspot (1020, 205, 261, 44) action ShowMenu("save")
         hotspot (1020, 270, 261, 44) action ShowMenu("load")
         hotspot (1020, 330, 261, 44) action ShowMenu("preferences")
         hotspot (1020, 394, 261, 44) action MainMenu()
         hotspot (1020, 518, 261, 44) action Quit()

    #frame:
        #style_group "gm_nav"
        #xalign .98
        #yalign .98

        #has vbox

        #textbutton _("Return") action Return()
        #textbutton _("Save Game") action ShowMenu("save")
        #textbutton _("Load Game") action ShowMenu("load")
        #textbutton _("Main Menu") action MainMenu()
        #textbutton _("Help") action Help()
        #textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox



        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:

            style_group "file_picker_nav"

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 1
        $ rows = 10

        # Display a grid of file slots.
        grid columns rows:
            #null width 1280
            transpose True
            xfill False
            xsize 620
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    #use navigation
    #use file_picker
    add "save_bg"

    imagemap:
         ground "gui/preferences/prefmenu.png"
         hover "gui/preferences/prefmenu_hover.png"
         
         hotspot (1020, 138, 261, 44) action Return()
         hotspot (1020, 205, 261, 44) action ShowMenu("save")
         hotspot (1020, 270, 261, 44) action ShowMenu("load")
         hotspot (1020, 330, 261, 44) action ShowMenu("preferences")
         hotspot (1020, 394, 261, 44) action MainMenu()
         hotspot (1020, 518, 261, 44) action Quit()
         

    imagemap:
        ground "files"
        idle "files"
        hover "files_selected"
        selected_idle "files_selected"
        cache False
     
        hotspot (587,610,65,32) clicked FilePage(1) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (663,610,65,32) clicked FilePage(2) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (745,610,65,32) clicked FilePage(3) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (821,610,65,32) clicked FilePage(4) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (900,610,65,32) clicked FilePage(5) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"


        
        hotspot (74,148,418,110) clicked FileSave(1):
            use load_save_slot(number=1) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (74,263,418,110) clicked FileSave(2):
            use load_save_slot(number=2) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (74,375,418,110) clicked FileSave(3):
            use load_save_slot(number=3) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (74,490,418,110) clicked FileSave(4):
            use load_save_slot(number=4) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,148,418,110) clicked FileSave(5):
            use load_save_slot(number=5) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,263,418,110) clicked FileSave(6):
            use load_save_slot(number=6) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,375,418,110) clicked FileSave(7):
            use load_save_slot(number=7) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,490,418,110) clicked FileSave(8):
            use load_save_slot(number=8) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
            
        hotspot (192,606,150,39) clicked FilePage("auto")
        hotspot (343,608,152,38) clicked FilePage("quick")

        #hotspot (#,#,#,#) action Return() activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"


screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    #use navigation
    add "load_bg"

    imagemap:
         ground "gui/preferences/prefmenu.png"
         hover "gui/preferences/prefmenu_hover.png"
         
         hotspot (1020, 138, 261, 44) action Return()
         hotspot (1020, 205, 261, 44) action ShowMenu("save")
         hotspot (1020, 270, 261, 44) action ShowMenu("load")
         hotspot (1020, 330, 261, 44) action ShowMenu("preferences")
         hotspot (1020, 394, 261, 44) action MainMenu()
         hotspot (1020, 518, 261, 44) action Quit()

    imagemap:
        ground "files"
        idle "files"
        hover "files_selected"
        selected_idle "files_selected"
        cache False
     
        hotspot (587,610,65,32) clicked FilePage(1) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (663,610,65,32) clicked FilePage(2) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (745,610,65,32) clicked FilePage(3) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (821,610,65,32) clicked FilePage(4) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (900,610,65,32) clicked FilePage(5) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"


        
        hotspot (74,148,418,110) clicked FileLoad(1):
            use load_save_slot(number=1) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (74,263,418,110) clicked FileLoad(2):
            use load_save_slot(number=2) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (74,375,418,110) clicked FileLoad(3):
            use load_save_slot(number=3) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (74,490,418,110) clicked FileLoad(4):
            use load_save_slot(number=4) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,148,418,110) clicked FileLoad(5):
            use load_save_slot(number=5) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,263,418,110) clicked FileLoad(6):
            use load_save_slot(number=6) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,375,418,110) clicked FileLoad(7):
            use load_save_slot(number=7) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,490,418,110) clicked FileLoad(8):
            use load_save_slot(number=8) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"

        #hotspot (#,#,#,#) action Return() activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (192,606,150,39) clicked FilePage("auto")
        hotspot (343,608,152,38) clicked FilePage("quick")
screen mm_load():

    # This ensures that any other menu screen is replaced.
    tag menu

    #use navigation
    add "default_mm"
    add "load_bg"
    #add "menuitem_back"

    imagemap:
         ground "menuoption_back"
         hover "gui/mainmenu/menuoptions/menuoptionback_hover.png"
         

         hotspot (1030, 597,246,47) action Return()

    imagemap:
        ground "files"
        idle "files"
        hover "files_selected"
        selected_idle "files_selected"
        cache False
     
        hotspot (587,610,65,32) clicked FilePage(1) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (663,610,65,32) clicked FilePage(2) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (745,610,65,32) clicked FilePage(3) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (821,610,65,32) clicked FilePage(4) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (900,610,65,32) clicked FilePage(5) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"


        
        hotspot (74,148,418,110) clicked FileLoad(1):
            use load_save_slot(number=1) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (74,263,418,110) clicked FileLoad(2):
            use load_save_slot(number=2) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (74,375,418,110) clicked FileLoad(3):
            use load_save_slot(number=3) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (74,490,418,110) clicked FileLoad(4):
            use load_save_slot(number=4) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,148,418,110) clicked FileLoad(5):
            use load_save_slot(number=5) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,263,418,110) clicked FileLoad(6):
            use load_save_slot(number=6) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,375,418,110) clicked FileLoad(7):
            use load_save_slot(number=7) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"
        hotspot (564,490,418,110) clicked FileLoad(8):
            use load_save_slot(number=8) #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"

        #hotspot (#,#,#,#) action Return() activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"

        hotspot (192,606,150,39) clicked FilePage("auto")
        hotspot (343,608,152,38) clicked FilePage("quick")

screen load_save_slot:
    $ file_text = "% 2s. %s\n%s" % (
                        FileSlotName(number, 8),
                        FileTime(number, empty=_("Empty Slot")),
                        FileSaveName(number))

    add FileScreenshot(number) xpos 20 ypos 8
    text file_text xpos 200 ypos 20 size 18 color "#ffffff" outlines [(0, "#000000", 2, 1)] kerning 2 font "gui/calibri.ttf"
    
    key "save_delete" action FileDelete(number)
    
init -2 python:
    
    config.thumbnail_width = 160
    config.thumbnail_height = 90


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu


    # Include the navigation.
    #use navigation
    add "configure_bg"


    imagemap:
         ground "gui/preferences/prefmenu.png"
         hover "gui/preferences/prefmenu_hover.png"
         
         hotspot (1020, 138, 261, 44) action Return()
         hotspot (1020, 205, 261, 44) action ShowMenu("save")
         hotspot (1020, 270, 261, 44) action ShowMenu("load")
         hotspot (1020, 330, 261, 44) action ShowMenu("preferences")
         hotspot (1020, 394, 261, 44) action MainMenu()
         hotspot (1020, 518, 261, 44) action Quit()
    imagemap:   
        ground "configure_idle"
        idle "configure_idle"
        hover "configure_selected"
        selected_idle "configure_selected" 
        selected_hover "configure_selected" 
        alpha False
        
        hotspot (366, 142, 181, 44) action Preference("display", "fullscreen")
        hotspot (554, 140, 186, 50) action Preference("display", "window")
        #hotspot (359, 365, 192, 45) action Preference("skip", "seen")
        #hotspot (548, 365, 183, 44) action Preference("skip", "all")
        #hotspot (359, 447, 183, 45) action Preference("after choices", "stop")
        #hotspot (546, 447, 186, 47) action Preference("after choices", "skip")
        
        bar pos (369, 390) value Preference("text speed") style "pref_slider"
        bar pos (369, 304) value Preference("sound volume") style "pref_slider"
        bar pos (369, 255) value Preference("music volume") style "pref_slider"
        #bar pos (369, 552) value Preference("auto-forward time") style "pref_slider"

   

init -2 python:
    style.pref_slider.left_bar = "gui/preferences/bar_full.png"
    style.pref_slider.right_bar = "gui/preferences/bar_empty.png"

    style.pref_slider.xmaximum = 360
    style.pref_slider.ymaximum = 10
    style.pref_slider.thumb = None
    #style.pref_slider.thumb_offset = 25
    #style.pref_slider.thumb_shadow = None

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen mm_preferences():

    tag menu


    # Include the navigation.
    #use navigation
    add "default_mm"
    add "configure_bg"
    #add "menuitem_back"

    imagemap:
         ground "menuoption_back"
         hover "gui/mainmenu/menuoptions/menuoptionback_hover.png"
         alpha False
         

         hotspot (1030, 597,246,47) action Return()

    imagemap:   
        ground "configure_idle"
        idle "configure_idle"
        hover "configure_selected"
        selected_idle "configure_selected" 
        selected_hover "configure_selected"
        alpha False
        
        
        hotspot (366, 142, 181, 44) action Preference("display", "fullscreen")
        hotspot (554, 140, 186, 50) action Preference("display", "window")
        #hotspot (359, 365, 192, 45) action Preference("skip", "seen")
        #hotspot (548, 365, 183, 44) action Preference("skip", "all")
        #hotspot (359, 447, 183, 45) action Preference("after choices", "stop")
        #hotspot (546, 447, 186, 47) action Preference("after choices", "skip")
        
        bar pos (369, 390) value Preference("text speed") style "pref_slider"
        bar pos (369, 304) value Preference("sound volume") style "pref_slider"
        bar pos (369, 255) value Preference("music volume") style "pref_slider"
        #bar pos (369, 552) value Preference("auto-forward time") style "pref_slider"





init -2 python:
    style.pref_slider.left_bar = "gui/preferences/bar_full.png"
    style.pref_slider.right_bar = "gui/preferences/bar_empty.png"

    style.pref_slider.xmaximum = 360
    style.pref_slider.ymaximum = 10
    style.pref_slider.thumb = None
    #style.pref_slider.thumb_offset = 25
    #style.pref_slider.thumb_shadow = None


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True
    add "gui/yesno/blankspace.png"
    window:
        style "gm_root"

    imagemap:
        ground "gui/yesno/yesno_ground.png"
        hover "gui/yesno/yesno_hover.png"
        
        hotspot (471,311,144,51) action yes_action
        hotspot (666, 314, 132, 55) action no_action
        
    #background    


    if message == layout.ARE_YOU_SURE:
        add "gui/yesno/sure.png"
 
    elif message == layout.DELETE_SAVE:
        add "gui/yesno/deletesavedtxt.png"
        
    elif message == layout.OVERWRITE_SAVE:
        add "gui/yesno/overwrite.png"
        
    elif message == layout.LOADING:
        add "gui/yesno/loadsavedtxt.png"
        
    elif message == layout.QUIT:
        add "gui/yesno/quittxt.png"
        
    elif message == layout.MAIN_MENU:
        add "gui/yesno/maintxt.png"
 



    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 0.93

        #textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        #textbutton _("Q.Save") action QuickSave()
        #textbutton _("Q.Load") action QuickLoad()
        #textbutton _("Skip") action Skip()
        #textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        #textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5
        ypos -135
        xpos -308

    style quick_button_text:
        is default
        size 18
        idle_color "#ffffff"
        hover_color "#000000"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


#DANGEROUS~~
init -1 python:
 #Function that creates the buttons for each entry.
 #It makes one button, based on the value "x", associated to the given encyclopaedia "enc".
 #Used in a "for loop" on a screen to generate the correct buttons for every entry 
    def generateEntryButton(x,enc):  
        ui.hbox()
        if enc.showLockedButtons:
            if enc.all_entries[x][1].locked == False: #If the entry is unlocked, make the button to go to it. If it's locked, make an inactive "???" button
                #ui.textbutton(enc.all_entries[x][1].name, style=style.enc_list_text, clicked= [ enc.ChangeStatus(x), enc.SetEntry(x), Show("encyclopaedia_entry")] )
                ui.textbutton(enc.all_entries[x][1].name,  clicked= [ enc.ChangeStatus(x), enc.SetEntry(x), Show("encyclopaedia_entry")] )
                if enc.all_entries[x][1].status == None or enc.all_entries[x][1].status == False:
                    ui.textbutton ("New!")
          
            else: #If locked entries should be shown in the list, the "???" button should go to the entry. If not, it's an inactive button
                if enc.showLockedEntry:
                    #ui.textbutton("???", style=style.enc_list_text, clicked=[ enc.ChangeStatus(x), enc.SetEntry(x), Show("encyclopaedia_entry")])
                    ui.textbutton(enc.all_entries[x][1].name, clicked= [ enc.ChangeStatus(x), enc.SetEntry(x), Show("encyclopaedia_entry")] )
                else:
                    ui.textbutton("???")
    
        if enc.showLockedButtons == False: #Only showing unlocked entries in this case, no need for the "???" button
            ui.textbutton(enc.unlocked_entries[x][1].name, clicked= [ enc.ChangeStatus(x), enc.SetEntry(x), Show("encyclopaedia_entry")] )
            if enc.unlocked_entries[x][1].status == None or enc.unlocked_entries[x][1].status == False:  
                ui.textbutton ("New!")
        ui.close()
##############################################################################
# Encyclopaedia List
#
# Screen that's used to display the list of entries 
screen encyclopaedia_list:
    tag menu
 
    window:
        style "enc_list"

        vbox:
            spacing 10
  
            frame:
                #style_group "mm_root"
                #style "enc_list"
                style "enc_frame"
                xfill True
                xmargin 10
                xmaximum 400
                top_margin 10
                xpos 100
                ypos 10
                text "Glossary" size 36
    
            #frame:
                #style_group "mm_root"
                #xfill True
                #xmargin 10
    
    
                #hbox:
                    #xfill True
                    #text encyclopaedia.getPercentageUnlocked() + " Complete" #Percentage display

            frame:
                #style_group "mm_root"  
                xmargin 10
                yfill True
                xmaximum 400
                xpos 100
                bottom_margin 10
                ypos 30
                style "enc_frame"

   
                viewport:
                    #scrollbars "vertical"
                    #mousewheel True
                    #draggable True
     
                    vbox: 
                        #text encyclopaedia.sortingMode xalign 0.5 #Flavour text to display the current sorting mode.
     
                        python:
                            #If sorting by subject, display the subject heading and add an entry under it if it's the same subject
                            if encyclopaedia.sortingMode == "Subject":
                                for x in range(len(encyclopaedia.subjects) ):
                                    ui.text(encyclopaedia.subjects[x])
                                    for y in range(encyclopaedia.entry_list_size):  
                                        if encyclopaedia.getEntry(y).subject == encyclopaedia.subjects[x]:
                                            generateEntryButton(y,encyclopaedia)   
       
                            #If sorting by number, add the number next to the entry
                            #elif encyclopaedia.sortingMode == "Number":    
                                #for x in range(encyclopaedia.entry_list_size):
                                   # ui.hbox()
                                    #ui.textbutton (str(encyclopaedia.getEntry(x).number))
                                   # generateEntryButton(x,encyclopaedia)   
                                   # ui.close()
      
                            #If sorting Alphabetically or Reverse-Alphabetically, don't add anything before the entry
                            else:
                                for x in range(encyclopaedia.entry_list_size):
                                    generateEntryButton(x,encyclopaedia) 
    
    frame:
        xalign .98
        yalign .98
        vbox:
            spacing 10
            #textbutton "Sort A to Z" action encyclopaedia.Sort(sorting_mode="A to Z")
            #textbutton "Sort by Subject" action encyclopaedia.Sort(sorting_mode="Subject")
   
            #textbutton "Show/Hide Locked Buttons" action encyclopaedia.ToggleShowLockedButtons()
            #textbutton "Show/Hide Locked Entry" action encyclopaedia.ToggleShowLockedEntry()
   
            #Sort and SaveStatus are unnecessary if you're not using persistent data
            #textbutton "Return"  action [encyclopaedia.Sort(sorting_mode="Number"), encyclopaedia.SaveStatus(persistent.new_dict, "new_0"), Return()] #Sorting mode has to be number to save properly. "new_0" needs to be the prefix for the persistent dictionary.
screen encyclopaedia_entry:
    tag menu
    use encyclopaedia_list
 
    window:
        style "enc_entry"  

        xfill True
        yfill True
        vbox:
            spacing 10
  
            frame:
                style_group "enc_text"
                xfill True
                xmargin 10
                top_margin 10
                xmaximum 200
                xpos 460
                background None
                $page_indicator = "%s" % (encyclopaedia.getEntryData()[1].getName()) # Flavour text to indicate which page we're current on
                text page_indicator size 36
  
            frame:
                id "entry_nav"
                #style_group "mm_root"
                style_group "enc_text"
                xfill True
                xmaximum 400
                xmargin 10
                xpos 460
                background None
                hbox:
                    xfill True
                    textbutton "Previous Entry" xalign .02 action encyclopaedia.PreviousEntry() #Relative to the sorting mode
                    textbutton "Next Entry" xalign .98 action encyclopaedia.NextEntry() #Relative to the sorting mode  
       
            hbox:
                $ddd = config.screen_width
                $dd = config.screen_width/2
                $pp = config.screen_height/2
                if encyclopaedia.getEntryData()[1].hasImage: #If the entry or sub-entry has an image, add it to the screen   
                    frame:
                        xmargin 10
                        yfill True
                        xfill True

                        xmaximum dd
                        ymaximum pp  

                        $current_image = encyclopaedia.getEntryData()[1].getImage()
                        add current_image crop (0,10,dd-30,pp-10)
   
                window:
                    id "entry_window"
                    style "default"
                    xmargin 10
                    xfill True
                    yfill True
                    xalign 0.5
                    xmaximum 440
                    xpos 700
                    ymaximum pp
                    background None
                    viewport:
                        #scrollbars "vertical"
                        #mousewheel True  
                        #draggable True
                        xfill True
                        yfill True  
                        vbox:
                            spacing 15
                            for item in encyclopaedia.entry_text: #entry_text is a list of paragraphs from what whatever the current entry is
                                text item

            #frame:
                #style_group "mm_root"  
                #xfill True
                #yfill False
                #xmargin 10
   
                #hbox:
                    #xfill True  
  
                    #if encyclopaedia.getEntryData()[1].hasSubEntry: #If there's a sub-entry, add Prev/Next Page buttons     
                        #textbutton "Previous Page" xalign .02 action encyclopaedia.PreviousPage()

                        #text "Page %d / %d" % (encyclopaedia.sub_current_position, encyclopaedia.getEntryData()[1].pages) #Flavour text to indicate which sub-page is being viewed

                        #textbutton "Next Page" xalign .98 action encyclopaedia.NextPage()  
 
                    #else:
                        #text("")
 
        frame:
            xfill True
            xmargin 10
            xmaximum 200
            xpos 610
            ypos 20
            style "enc_text"
            background None
            hbox:
                xfill True
                #textbutton "Close Entry" id "close_entry_button" xalign 0.02 clicked [encyclopaedia.ResetSubPage(), Show("encyclopaedia_list")]
                #text "Sorting Mode: %s" % (encyclopaedia.sortingMode,) #Flavour text that displays the current sorting mode


##############################################################################
# Encyclopaedia Button
#
# Contains a button to open the encyclopaedia at any time during the game
screen show_enc_button:
    spacing 10
    #textbutton "Open Encyclopaedia" xalign .98 yalign .02 action ShowMenu("encyclopaedia_list")
 

