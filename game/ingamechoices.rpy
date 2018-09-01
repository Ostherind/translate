
        

screen stuntbattle_choice:
    imagemap:
        ground "ingamedemo/8stuntchoiceterran.png"
        hover "ingamedemo/8stuntchoiceterran_hover.png"

        hotspot (1, 68, 1278, 199) clicked Return("stuntright") activate_sound
        hotspot (1, 333, 1278, 191) clicked Return("stuntwrong") activate_sound

screen shattered_choice:
    imagemap:
        ground "battle/battleselect.jpg"
        hover "battle/battleselected.jpg"
        
        hotspot (527, 247, 145, 139) clicked Return("macro")
        hotspot (59, 130, 138, 127) clicked Return("attack")


screen rival_opening:
    imagemap:
        ground "ingame/rivalopeningchoice.jpg" 
        hover "ingame/rivalopeningchoiceselected.jpg"
        
        hotspot (838, 356, 373, 124) clicked Return("cheese") activate_sound
        hotspot (270, 177, 387, 134) clicked Return("standard") activate_sound
        
screen rival_mid:
    imagemap:
        ground "ingame/rivalmidchoice.jpg"
        hover "ingame/rivalmidchoiceselected.jpg"
        
        hotspot (744, 489, 375, 119) clicked Return("expand") activate_sound
        hotspot (224, 42, 375, 125) clicked Return("drop") activate_sound