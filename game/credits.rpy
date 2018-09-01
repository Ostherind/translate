
###staff
image staff cg = "credits/staff/cg.png"
image staff day9 = "credits/staff/day9.png"
image staff glynnis = "credits/staff/glynnis.png"
image staff music = "credits/staff/music.png"
image staff sendobg = "credits/staff/sendobg.png"
image staff sendoparticles = "credits/staff/sendoparticles.png"
image staff stephanie = "credits/staff/stephanie.png"
image staff temp0 = "credits/staff/temp0.png"
image staff timtj = "credits/staff/timtj.png"
image staff ui = "credits/staff/ui.png"
image staff blizzard = "credits/staff/blizzard.png"
image staff madewithrenpy = "credits/staff/renpy.png"
image staff solthrys = "credits/staff/solthrys.png"

#extra
image extras_unlocked = "credits/extras_msg.png"

##story

image storybacker justin ="credits/story/kickstarterproducers.png"

##designers
image backerchar jon="credits/designer/designer_jonengle.png"
image backerchartitle="credits/designer/designer_title.png"
image backerchar damen="credits/designer/damenknight.png"
image backerchar cameron="credits/designer/designer_cameronolsen.png"

##producers
image producer brandan= "credits/100/brandan corthell.png"
image producer adam= "credits/100/producer_adam.png" ##
image producer conrad= "credits/100/producer_conrad.png"
image producer crazykenny= "credits/100/producer_crazykenny.png"
image producer jessa= "credits/100/producer_jessafriend.png"
image producer kainny= "credits/100/producer_kainnyy.png" ##
image producer makerspace= "credits/100/producer_makerspace.png" ##
image producer mit = "credits/100/producer_mit.png" ##
image producer password= "credits/100/producer_password.png"
image producer pena= "credits/100/producer_pena.png"
image producer thomasrogge= "credits/100/producer_thomasrogge.png"
image producertitle= "credits/100/producer_title.png"


#contributors
image specialthanks = "credits/specialthanks.png"
image kscontributors = "credits/contributors.png"
image kssupercontributors = "credits/kickstartersupercontributors.png"
image prettycoolguys ="credits/prettycooguys.png"

image mask = "gui/grad_mask.png"

##to do thanks for playing

image thankyou = "credits/thankyou.png"

label endcredits:

   
    scene bg apartmentday at center with dissolve
    stop music fadeout 1.0

    play music "sfx/Temp0 Alive.ogg" fadein 1.0

    show mask at center with dissolve
    #staffff
    show staff timtj at center with dissolve
    $renpy.pause(2.0, hard=True)
    hide staff with dissolve

    show staff stephanie at center with dissolve
    
    $renpy.pause(2.0,hard=True)

    hide staff with dissolve
    show staff glynnis at center with dissolve
    $renpy.pause(2.0,hard=True)
    hide staff with dissolve
    show staff sendobg at center with dissolve
    $renpy.pause(2.0,hard=True)
    hide staff with dissolve
    show staff sendoparticles at center with dissolve
    $renpy.pause(2.0,hard=True)
    hide staff with dissolve

    show staff cg at center with dissolve
    $renpy.pause(2.0,hard=True)
    hide staff with dissolve

    show staff ui at center with dissolve
    $renpy.pause(2.0,hard=True)
    hide staff with dissolve

    show staff solthrys at center with dissolve
    $renpy.pause(2.0, hard=True)
    hide staff with dissolve

    show staff day9 at center with dissolve
    $renpy.pause(2.0,hard=True)
    hide staff with dissolve

    show staff music at center with dissolve
    $renpy.pause(2.0,hard=True)
    hide staff with dissolve

    show staff temp0 at center with dissolve
    $renpy.pause(2.0,hard=True)
    hide staff with dissolve

    show staff madewithrenpy at center with dissolve
    $renpy.pause(2.0, hard=True)
    hide staff with dissolve

    show staff blizzard at center with dissolve
    $renpy.pause(2.0,hard=True)
    hide staff with dissolve

    scene bg darkpcbang at center with dissolve
    
    show mask at center with dissolve

    $renpy.pause(2.0,hard=True)

    show storybacker justin at center with dissolve

    $renpy.pause(2.0,hard=True)
    hide storybacker with dissolve

    show backerchartitle at center with dissolve

    show backerchar jon at center with dissolve
    
    show jon neutral at right with easeinright
    $renpy.pause(2.0,hard=True)

    hide backerchar
    hide jon with dissolve
    show backerchar damen at center with dissolve
    show damen neutral at right with easeinright
    $renpy.pause(2.0,hard=True)

    hide backerchar
    hide damen with dissolve
    show backerchar cameron at center with dissolve
    show cam neutral at right with easeinright 
    $renpy.pause(2.0,hard=True)
    
    hide cam with dissolve
    scene bg studio at center with dissolve
    show mask at center with dissolve

    $renpy.pause(2.0,hard=True)

    show producertitle at center with dissolve

    show producer mit at center with dissolve

    $renpy.pause(2.0,hard=True)

    hide producer with dissolve
    show producer makerspace at center with dissolve

    $renpy.pause(2.0,hard=True)

    hide producer with dissolve
    show producer kainny at center with dissolve

    $renpy.pause(2.0,hard=True)

    hide producer with dissolve
    show producer adam at center with dissolve

    $renpy.pause(2.0,hard=True)

    hide producer with dissolve
    show producer brandan at center with dissolve

    $renpy.pause(2.0,hard=True)

    hide producer with dissolve
    show producer conrad at center with dissolve

    $renpy.pause(2.0,hard=True)
    hide producer with dissolve
    show producer crazykenny at center with dissolve

    $renpy.pause(2.0,hard=True)

    hide producer with dissolve
    show producer jessa at center with dissolve

    $renpy.pause(2.0,hard=True)

    hide producer with dissolve
    show producer password at center with dissolve

    $renpy.pause(2.0,hard=True)
    hide producer with dissolve
    show producer pena at center with dissolve

    $renpy.pause(2.0,hard=True)
    hide producer with dissolve
    show producer thomasrogge at center with dissolve

    $renpy.pause(2.0,hard=True)

    scene bg backstage at center with dissolve
    show mask at center with dissolve

    show prettycoolguys at center with dissolve

    $renpy.pause(6.0,hard=True)

    hide prettycoolguys with dissolve

    $renpy.pause(2.0, hard=True)

    show kssupercontributors:
        yalign -0.5
        linear 25 yalign 1.5
    $renpy.pause(25, hard=True)

    hide kssupercontributors 

    show kscontributors: 
        yalign  -0.4
        linear 43 yalign 1.5
    $renpy.pause(43,hard=True)

    show specialthanks:  
        yalign -0.8
        linear 22 yalign 3.0
    $renpy.pause(22,hard=True)

    hide specialthanks

    show thankyou at center with dissolve

    $renpy.pause(2.0,hard=True)
    stop music fadeout 1.0
    hide thankyou with dissolve

    $renpy.pause(1.0,hard=True)

    if persistent.extras_msg == True:
        $ persistent.extras_msg = False
        scene bg black at center with Dissolve(0.2)
        show extras_unlocked at center with dissolve
        $renpy.pause(2.0, hard = True)
        hide extras_unlocked with dissolve

    return