image prefmenu: 
    "gui/preferences/prefmenu.png"
    alpha 0
    pause 0.4
    alpha 1

image prefmenuhover: 
    "gui/preferences/prefmenu_hover.png"
    alpha 0
    pause 0.4
    alpha 1

image prefmenuanim: 
    "gui/preferences/prefmenu_anim.png"
    xalign 1.2
    easein 0.4 xalign 1.0
    alpha 0

image prefmenuanim2: 
    "gui/preferences/prefmenu_anim2.png"
    xalign 1.2
    alpha 0
    easein 0.4 xalign 1.0
    alpha 1

#menuoptions back

image menuback:
    "gui/mainmenu/menuoptions/menuoptionback.png"

image menuback_hover:
    "gui/mainmenu/menuoptions/menuoptionback_hover.png"
    


image default_mm:
    "gui/mainmenu/menubg.png"
    alpha 1
    #linear 0.75 alpha 0
    #alpha 1

#mm imagemamp

image im_mm_ground:
    "gui/mainmenu/imagemap/menubg_ground.png"
    alpha 0
    easein 0.8 alpha 0
    alpha 1

image im_mm_hover:
   "gui/mainmenu/imagemap/menubg_hover.png"
   alpha 0
   easein 0.8 alpha 0
   alpha 1


image prefmenuanimred: 
    "gui/preferences/prefmenured_anim.png"
    xalign 1.005
    alpha 0
    ease 0.4 alpha 0
    #easein 0.28 xalign 1.001 alpha 1
    easein 0.2 xalign 1.004 alpha 1


image menucardanim:
    "gui/mainmenu/menucard.png"
    yalign 0.5
    xalign -1
    easein 0.2 xalign 0.02
    easein 0.18 xalign 0
    alpha 1

image menuitem_new:
    "gui/mainmenu/menuitems/menuitem_new.png"
    xalign 1.2
    alpha 0
    easein 0.35 xalign 1.0 alpha 1

image menuitem_load:
    "gui/mainmenu/menuitems/menuitem_load.png"
    xalign 1.2
    alpha 0
    easein 0.45 xalign 1.0 alpha 1

image menuitem_preferences: 
    "gui/mainmenu/menuitems/menuitem_preferences.png"
    xalign 1.2
    alpha 0
    easein 0.55 xalign 1.0 alpha 1

image menuitem_extras:
    "gui/mainmenu/menuitems/menuitem_extras.png"
    xalign 1.2
    alpha 0
    easein 0.65 xalign 1.0 alpha 1

image menuitem_credits:
    "gui/mainmenu/menuitems/menuitem_credits.png"
    xalign 1.2
    alpha 0
    easein 0.75 xalign 1.0 alpha 1

image menuitem_quit:
    "gui/mainmenu/menuitems/menuitem_quit.png"
    xalign 1.2
    alpha 0
    easein 0.85 xalign 1.0 alpha 1

image menuitem_back:
    "gui/mainmenu/menuitems/menuitem_back.png"
    xalign 1.2
    alpha 0
    easein 0.45 xalign 1.0 alpha 1
    alpha 0

image menuitem_day9:
    "gui/mainmenu/menuitems/menuitem_day9.png"
    xalign 1.2
    alpha 0
    easein 0.25 xalign 1.0 alpha 1
    linear 0.20 alpha 1
    alpha 0

image menuitem_backers:
    "gui/mainmenu/menuitems/menuitem_backers.png"
    xalign 1.2
    alpha 0
    easein 0.35 xalign 1.0 alpha 1
    linear 0.10 alpha 1
    alpha 0

image menuitem_unknown:
    "gui/mainmenu/menuitems/menuitem_unknown.png"
    xalign 1.2
    alpha 0
    easein 0.35 xalign 1.0 alpha 1
    linear 0.10 alpha 1
    alpha 0


image menuoption_back:
    "gui/mainmenu/menuoptions/menuoptionback.png"
    alpha 0
    linear 0.45 alpha 0
    alpha 1

image scvnlogomm:
    xalign 0
    alpha 0
    "gui/mainmenu/scvnlogosmall.png"
    yalign .1
    easein 0.4 xalign 0.2 alpha 1

image scvnlogoout:
    xalign 0.2
    alpha 1.0
    yalign 0.1
    "gui/mainmenu/scvnlogosmall.png"
    easein 0.4 xalign -0.5 alpha 0



##reverse


#logotitle
image logosc:
    "gui/logo/logosc.png"
    xalign 0.0
    alpha 0
    easein 0.2 xalign 0.2 alpha 1

image logovn:
    "gui/logo/logovn.png"
    yalign 0.5
    alpha 0
    xalign 0.2
    linear 0.2 alpha 0
    easein 0.2 yalign 0.0 alpha 1

image logo2:
    "gui/logo/logo2.png"
    #crop(0,0,300,267)
    #yalign 0.4
    xalign 0.2
    alpha 0
    yalign -0.5
    linear 0.4 alpha 0
    easein 0.2 yalign 0.0 alpha 1

image logosctitle:
    "gui/logo/logosc.png"

image logovntitle:
    "gui/logo/logovn.png"

image logo2title:
    "gui/logo/logo2.png"



image e_logosctitle:
    "gui/logo/logosc.png"
    xalign 0.2

image e_logovntitle:
    "gui/logo/logovn.png"
    xalign 0.2

image e_logo2title:
    "gui/logo/logo2.png"
    xalign 0.2

image logosextra:
    "gui/logo/extras.png"
    alpha 0
    xalign 0
    easein 0.2 xalign 0.2 alpha 1
#options menu

image optionsmenu_anim:
    "gui/preferences/configure.png"
    alpha 1
    crop(0,0,50,90)
    yalign 0.5
    easein 0.1 crop(0,0,1280,90)  alpha 1
    easein 0.2 crop(0,0,1280,720) alpha 1 subpixel True


image configure_bg:
    "gui/preferences/configure_bg.png"

image configure_idle:
    "gui/preferences/configure.png"

image configure_selected:
    "gui/preferences/configure_selected.png"


image save_bg:
    "gui/saveload/savebg.png"

image load_bg:
    "gui/saveload/loadbg.png"

image files:
    "gui/saveload/files.png"

image files_selected:
    "gui/saveload/files_selected.png"

##extras menu

image extras_menu:
    "gui/mainmenu/extras/extras_menu.png"
    alpha 0
    linear 0.45 alpha 0
    alpha 1

image extras_menu_hover:
    "gui/mainmenu/extras/extras_menu_hover.png"


image extras_menu_unknown:
    "gui/mainmenu/extras/extras_menu_unknown.png"
    alpha 0
    linear 0.45 alpha 0
    alpha 1

image extras_menu_hover_unknown:
    "gui/mainmenu/extras/extras_menu_unknown_hover.png"

image extras_day9:
    "gui/mainmenu/extras/day9extras.png"
    alpha 0
    xalign 0.05
    easein 0.2 alpha 1 xalign 0.0

image extras_backer:
    "gui/mainmenu/extras/backerextras.png"
    alpha 0
    xalign 0.05
    easein 0.2 alpha 1 xalign 0.0

image extras_backer_unknown:
    "gui/mainmenu/extras/backersextras_unknown.png"
    alpha 0
    xalign 0.05
    easein 0.2 alpha 1 xalign 0.0



####char files_selected

image malemach:
    "gui/charselect/malemach.png"
    alpha 1
    #xalign 0.0
image malemach_hover:
    "gui/charselect/malemach_hover.png"
    alpha 1
image femmach:
    "gui/charselect/femmach.png"
    alpha 1


image femmach_hover:
    "gui/charselect/femmach_hover.png"
    alpha 1

screen char_select():
    add "femmach"
    add "malemach"
    #zorder 2
    imagemap:
        ground "malemach"
        hover "malemach_hover"
        
        hotspot (1,94, 553,720) action Jump("malemachchoice") #hovered ShowTransient("char_img", img="malemach_hover") unhovered Hide("char_img")

    imagemap:
        ground "femmach"
        hover  "femmach_hover"
  
        hotspot (812,94,461,720) action Jump("femmachchoice") #hovered ShowTransient("char_img", img="femmach_hover") unhovered Hide("char_img")


screen char_img(img):
    zorder 0
    add img


transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown():
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    #bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

image titlecred:
    "bg/titlecred.png"