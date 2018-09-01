
##scenes
#intro_battle
#alloutattack1
#alloutattack2
#boltgame
#revabattle1
#studio_game1
#studio_game2
#studio_game3
#studio_game4
#studio_game5
#studio_game6
#reva_vs_stunt
#reva_ladder
#reva_ladder2
#archonbattle1
#archonbattle2
#showmatch1
#showmatch2
#showmatch3
#showmatch4
#showmatch5

#alloutattack1
#boltgame
#alloutattack2
#showmatch4




####intro
label alloutattack1:
    scene bg aoa1 opening with fade:
        align(0,0)
    play music "sfx/terran2.mp3"
    window show dissolve
    "Workers, minerals, vespene gas, and a command center. I start out every match with only these resources at my disposal. It's my job to turn them into something that can defeat my opponent."
    show bg aoa1 building with dissolve:
        align(0,0)
    $ persistent.en19_locked = False
    $ encyclopaedia.unlockEntry(en19, persistent.en19_locked)
    "Generally, that means I need to build structures capable of training units for my army. My {color=#FF5E5E}build order{/color} determines how my end of the matchup plays out."

    show bg black with dissolve:
        align(0,0)
    
    play sound "sfx/battle/helliomove.ogg" fadein 1.0
    show aoa1 scouting:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True
    $ persistent.en10_locked = False
    $ encyclopaedia.unlockEntry(en10, persistent.en10_locked)
    "This game, I've opted for a quick hellion attack. Not only will it offer me a chance to deal some damage to my opponent, but it will also allow me to {color=#FF5E5E}scout{/color}."
    scene bg aoa1 scoutedzerg with dissolve:
        align(0,0)

    "But it seems I don't have much to worry about. My opponent went for a greedy build order—focusing entirely on his economy instead of his army."
    hide bg aoa1
    show black behind aoa1:
        align (0,0)
    with dissolve
    play sound "sfx/battle/hellionsfire.ogg" fadein 1.0
    $ show_flamethrower_left()
    show aoa1 harass1: 
        yalign 0.4 alpha 0.0
        crop(0,0,500, 350)
        easein 0.6 alpha 1.0 crop(0,0,1280, 350) subpixel True

    "Unfortunately for him, the match isn't going to last long enough for that risk to pay off. My hellions make short work of his single queen and handful of zerglings."
    stop sound fadeout 1.0
    hide aoa1 harass1

    play sound "sfx/battle/hellionsfire.ogg" fadein 1.0

    show aoa1 harass2:
        yalign 0.4 alpha 0.0
        xalign 1
        crop(0,0, 180, 720)
        easein 0.6 alpha 1.0 xalign 0.4
        easein 0.6 crop(-400,0, 1280, 720) subpixel True

    "With his frontline out of the way, I'm free to rush into his mineral line and roast his workers, denying him the resources he needs to muster an army."
    hide aoa1 harass2

    #marine bullet
    #hellion flame
    stop sound fadeout 1.0
    play sound "sfx/battle/hellionsmarinesfire.ogg" fadein 1.0
    
    show white with Dissolve(0.1):
        align(0,0)
    scene bg aoa1 killbase with dissolve:
        align(0,0)
    hide white with Dissolve(0.2)
    $ persistent.en6_locked = False
    $ encyclopaedia.unlockEntry(en6, persistent.en6_locked)
    "Facing down a marine reinforcement, it's not long before my zerg opponent types out the two letters: {color=#FF5E5E}GG{/color}. Easy."
    stop music fadeout 1.0
    stop sound fadeout 1.0
    window hide dissolve

jump S7meetAccel

#all out attack 2
label alloutattack2:
    play music "sfx/terran3.mp3"
    scene bg aoa2 opening with dissolve:
        align(0,0)
    window show dissolve
    show playercards_accel:
        xalign 1.5
        yalign 0.5
        alpha 0
        easein 0.4 xalign 1.0 alpha 1
    "I haven't gone up against a player as strong as Accel in a while. There probably wasn't a single person at the VSL qualifier at his level."
    "That only makes a potential victory all the more tantalizing. It's a chance to prove to myself that I've got what it takes."
    "Even if I've decided on playing standard, I've still got a decision to make in how to execute my mid-game strategy."
    "This map is well-suited for a hellion attack. I'll have plenty of room to poke around his expansion since it lacks a choke point."
    "An attack by air might also be a strong option. The distance between our bases is relatively long by land, but it'll take a banshee less than five seconds to travel from mine to his."
    "I'm confident with both styles. It's just a matter of how I want to execute the attack."
    hide playercards_accel with easeoutright
    window hide dissolve
    menu:
        "Hit and run with hellions":
            jump alloutattack2hellions
        "Air assault with banshees":
            jump alloutattack2banshee

label alloutattack2hellions:

 
    scene bg black with dissolve:
        align(0,0)
    window show dissolve
    show aoa2 hellion build:
       xalign 0.9 alpha 0.0
       easein 0.5 alpha 1.0 xalign 0.4
    window show dissolve
    "I produce my hellions two at a time and send my first four across the map."
    play sound "sfx/battle/helliomove.ogg" fadein 1.0
    show aoa2 hellion moveout:
        yalign 0.0 alpha 0.0
        xalign 0.4
        easein 0.6  yalign 0.4 alpha 1.0 subpixel True
    "It takes a few extra seconds to clear out the space between our bases. Confident that I have enough breathing room, I prepare for my first attack."
    hide aoa2
    ##redo
    play sound "sfx/battle/hellionexplode.ogg" fadein 1.0
    $ show_flamethrower_right()
    show aoa2 hellion denied with dissolve:
        xpos 0.4 alpha 0.0
        crop(300,0, 250, 720)
        xalign 1.0
        easein .4 crop(0,0, 800, 720) xalign 0.8 alpha 1.0
    $ persistent.en12_locked = False
    $ encyclopaedia.unlockEntry(en12, persistent.en12_locked)
    "My hellions make a beeline for his natural expansion's worker line. With some decent {color=#FF5E5E}micro{/color} on my part, I manage to secure a few worker kills before ordering a retreat."

    hide aoa2
    play sound "sfx/battle/helliomove.ogg" fadein 1.0
    show aoa2 hellion escape:
        yalign 0.0 alpha 0.0
        xalign 0.4
        easein 0.4 yalign 0.4 alpha 1.0

  
    "A lesser player might have sacrificed four hellions for more economic damage. But I've practiced this style enough to know that I'll lose map control without them."
    stop sound fadeout 1.0
    jump alloutattack2end


label alloutattack2banshee:

    scene bg black with dissolve:
        align(0,0)

 

    show aoa2 banshee build:
        yalign 0.4
        xalign 1 alpha 0.0
        crop(300,0, 400, 720)
        easein 0.6 xalign 0.4 alpha 1.0
        easein 0.6 crop(-280,0, 1280, 720) subpixel True
    window show dissolve
    "I cut all extraneous unit production to get out a banshee as soon as possible. The earlier I'm able to hit, the less chance that Accel will have the right defenses."
    play sound "sfx/battle/bansheecloaked.ogg" fadein 1.0    
    show aoa2 banshee move:
        yalign 0.0
        xalign 0.6
        crop(0,0, 1280,350)
        easein 0.2 yalign 0.4
    
    show aoa2alt banshee marinedistraction:
        xalign -0.5
        easein 0.4 xalign -0.02 subpixel True

    "With my banshee en route, I clear out the path to his base with a handful of marines. Denying information to my opponent is important, even if I don't plan to attack from that blind spot."

    hide aoa2

    #asset
    show white with Dissolve(0.1):
        align(0,0)
    $ show_missile_both()

    pause .35

    $ show_tank_blast()
    play sound "sfx/battle/bansheesshooting.ogg" fadein 1.0

    scene bg aoa2 bansheeattack:
        align(0,0)
    hide white with Dissolve(0.2)

    "It seems to have been the right choice, as his marines are out of position when my banshee arrives at his base. I manage to secure a few worker kills before ordering a retreat."
    ##asset missiles
    stop sound fadeout 1.0
    play sound "sfx/battle/bansheeexplosion.ogg" fadein 1.0
    


    scene bg black with Dissolve(0.1):
        align(0,0)

    show aoa2 bansheeescape:
        yalign 0
        alpha 0
        xalign 0.5
        easein 0.4 yalign 0.3 alpha 1 subpixel True


    "Since I didn't lose my banshee, Accel has to spend minerals on air defense. Knowing that, I prepare to transition to a full-on ground army."
    stop sound fadeout 1.0
    jump alloutattack2end

label alloutattack2end:
    stop sound fadeout 1.0
    scene bg black with dissolve:
        align(0,0)

    play sound "sfx/battle/buildingplaced.ogg" fadein 1.0    
    show aoa2 takethird with dissolve:
        align(0,0)
    "This game is going insanely well. Though Accel took his expansion before I did, the damage he took puts us on even footing."
    
    hide aoa2
    show aoa2 moveout:
        yalign 0
        alpha 0
        easein 0.4 yalign 0.4 alpha 1 subpixel True
    "I follow up with an army of marines, marauders, and dropships: the bread and butter of most terran players."
    "Since I cleared the space between our bases, he's in the dark about the timing of this next attack. There's a solid chance that I could do enough damage here to end the game!"
    
    hide aoa2
    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    show aoa2 acceldrop:
        xalign 1.0
        alpha 0
        easein 0.4 xalign 0.4 alpha 1 subpixel True
    "But just as I arrive at the outskirts of Accel's expansion, one of his dropships uploads a handful of marines in my base. Tch, that's going to slow down my ability to reinforce."
    #marine shots
    stop sound fadeout 1.0
    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    show white with Dissolve(0.1):
        align(0,0)

    scene bg aoa2 accelattacks:
        align(0,0)

    hide white with Dissolve(0.2)
    $ persistent.en11_locked = False
    $ encyclopaedia.unlockEntry(en11, persistent.en11_locked)
    "Woah! Shit! With my focus on the {color=#FF5E5E}drop{/color} in my main, Accel rushed into the army I left outside of his base while I wasn't paying attention. He's got a concave formation on me!"
    "And just like that, my advantage evaporates. Though I manage to stay in the game for a bit longer, Accel wisely guards his lead by immediately taking a third base."
    stop sound fadeout 1.0

    $ show_tank_blast()
    play sound "sfx/battle/seigeattack.ogg" fadein 1.0
    show white with Dissolve(0.1):
        align(0,0)

    show bg aoa2 aoa2 lose with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)

    hide white with Dissolve(0.2)
    "Soon enough, his economic advantage is reflected in the size of his army. After my blunder, Accel's play was airtight. There really wasn't anything for me to do."
    "With a groan, I offer a gg and concede the match."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    window hide dissolve
    hide aoa2 with Dissolve(.2)


    stop sound fadeout 1.0
    #return
    window hide dissolve
jump S9meetJett
#jett_practice
label jett_practice:
    scene black with dissolve:
        align (0,0)
    show split:
        crop(0,0,0,0)
        easein 0.4 crop(0,0,1280,720)
    play sound "sfx/battle/zerglingroachesvsterran.ogg" fadein 1.0
    show split1anim behind split:
        xpos -.5
        easein .4 xpos -.015

    show split2anim behind split:
        xpos 1.0
        easein .4 xpos .31
    pause .5
    window show dissolve
    "Game after game is a beatdown. I can't crack her defenses when I attack, and I'm barely holding on when she goes on offense." 
    "She's just as unforgiving in pointing out my mistakes as she is in-game."
    
    stop sound fadeout 1.0
    scene bg jettpractice wall with dissolve:
        align(0,0)

    j "Your wall at the ramp to your natural is trash. How the hell do you get away with this? You're asking to get busted."
    m "It's not something I really think about that much. I just throw it up, you know?"
    j "Fix it or be punished."
    "That probably isn’t an idle threat. Jett is the type of player capable of ending the game instantly if she can capitalize on the right kind of mistake."
    "Her style has been characterized as both passive and reactive. She takes her time and watches her opponents, patient for the right moment to strike. She only takes a risk if it’s calculated in her favor."
    "Given her former success, the style has suited her well. Though I can’t help but wonder why she hasn’t lately been performing at her previous level. Maybe she’s lost her killer instinct?"

    scene bg black with Dissolve(.2):
        align(0,0)
    
    show jettpractice banelings at center:
        ypos .2 alpha 0.0
        easein .6 ypos .62 alpha 1.0 subpixel True
    pause .6


    hide jettpractice
    $ baneling_blast_particle.reset_positions()
    $ baneling_blast_particle_smoke.reset_positions()
    play sound "sfx/battle/bansheeexplosion.ogg" fadein 1.0
    $ show_baneling_blast()
    show bg jettpractice explosions with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)

   


    "Guess not. A reminder of the skill difference between us rushes up the ramp to my natural expansion and crushes my wall, as promised."
    
    stop sound fadeout 1.0
    play sound "sfx/battle/zerglingsurroundmarines.ogg" fadein 1.0
    scene bg jettpractice lings with dissolve:
        align(0,0)

    "In the aftermath of the destruction, she swarms my base and seizes an easy win. Jett revels in her victory with a predatory smile."
    j "Wrecked."
    stop sound fadeout 1.0
    window hide dissolve

jump S11zonefireRival
#bolt game
label boltgame:
    play music "sfx/terran2.mp3"
    scene bg boltgame opening with dissolve:
        align(0,0)
    window show dissolve
    show playercards_bolt:
        xalign 1.5
        yalign 0.5
        alpha 0
        easein 0.4 xalign 1.0 alpha 1

    "If the idea behind practicing against a good player is to improve, I should probably play standard."
    hide playercards_bolt with Dissolve(0.2)
    #image blackwhite = im.MatrixColor(
    #"ingame/terran/bolt/1opening.jpg",
    #im.matrix.desaturate())

    #scene blackwhite with dissolve:
        #align(0,0)

    show boltgame scout1:
        yalign 0.5 xpos 1.0
        easein .5 xpos .4 subpixel True

    "Still the temptation to all-in is always there. How sick would it be to grab a quick win on a KPGA player?"
    window hide dissolve
    menu:
        "Go for an early attack":
            jump boltgame_cheese
        "Play out a standard game":
            pass

    scene bg boltgame decision1 with dissolve:
        align(0,0)
    window show dissolve
    "It’s probably best that I follow Jett's advice. I opt for a standard macromanagement game, this guy’s build permitting."
    "I take my natural expansion and begin teching up.  The match progresses quietly with only a few brief skirmishes with his stalkers and my marines."
    play sound "sfx/battle/scan.ogg" fadein 1.0
    show white with Dissolve(0.1):
        align(0,0)
    show bg boltgame scan:
        align(0,0)
    hide white with Dissolve(0.2)
    "My scan show that he's not doing anything out of the ordinary. One of us has to make a move sooner or later."
    stop sound fadeout 1.0
    scene bg boltgame decision1 with dissolve:
        align(0,0)
    "I start constructing my starport and researching my bio upgrades. I’m surprised to find that they finish without any pressure coming from the protoss army."
    



    scene bg boltgame decision2 with dissolve:
        align(0,0)
    
    "This could be a good time to go for some drop play and try to snipe some of his critical tech buildings."
    "If I were to play an aggressive drop style, I need to be confident in my control and in the fact that I can outplay him."
    "On the other hand, this game has been exceptionally quiet. If I could get up another expansion, I’ll have a serious economic advantage going into the late game."
    window hide dissolve
    menu:
        "Risk an early third base":
            jump boltgame_fastthird
        "Get aggressive with dropships":
            jump boltgame_drop
    #return

label boltgame_cheese:
    play sound "sfx/battle/buildingplaced.ogg" fadein 1.0
    scene bg boltgame buildrax with dissolve: 
        align (0,0)
    window show dissolve
    $ persistent.en8_locked = False
    $ encyclopaedia.unlockEntry(en8, persistent.en8_locked)
    "Screw it, I'm not in the mood for {color=#FF5E5E}macro{/color}."
    
    scene bg boltgame raxbuilt with dissolve: 
        align (0,0)

    "I place two early barracks mid-map, just outside his scouting path. With luck, he won’t see my strategy until it’s coming at him."
    "My heart pounds as I watch my marine count grow. He still hasn’t scouted my all-in."
    "This is a huge advantage. I've got this."

    #asset - marines moving up?



    play sound "sfx/battle/singlemarine.ogg" fadein 1.0
    scene bg boltgame rushattack with dissolve:
        align(0,0)
    "I bring my marines to his base and charge up the ramp leading to his high ground. I leave an SCV on the low ground to construct a bunker just in case I have to fall back."
    
    stop sound fadeout 1.0
    scene bg black with Dissolve(0.1):
        align(0,0)
    play sound "sfx/battle/marinegroupshooting.ogg" fadein 1.0

    show boltgame marinesmoveup:
        xalign 1.0
        alpha 0
        easein 0.4 xalign 0.4 alpha 1 subpixel True
    "He retreats with his lone zealot and begins to chronoboost something out of his gateway, likely a stalker. He still hasn’t pulled his probes, so I start heading towards the mineral line."
    window hide dissolve
    play sound "sfx/fastslash.ogg"
    show blacksolid at right:
        xpos 2.0
        linear .1 xpos 1.0 subpixel True
    pause .3
    play sound "sfx/zealotslash.ogg"
    show swoosh1 at center behind blacksolid
    show blacksolid at right:
        linear .1 xpos 0.0 subpixel True
    show swoosh1 at center  with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8)
    hide boltgame

    play sound "sfx/battle/stalkerzealotprobesurroundmarines.ogg" fadein 1.0
    show boltgame stalkerzealot behind swoosh1 with Dissolve(0.1):
        xalign 1.0
        alpha 0
        easein 0.4 xalign 0.4 alpha 1 subpixel True
    pause .5

    hide swoosh1 with Dissolve(.1)
    window show dissolve

    "Shit! He preemptively pulled a handful of probes and hid them out of my vision! With my exit cut off, I won't be able to escape!"
    "Things look even worse when he gets his first stalker out. He might actually hold this!"
    "I do everything I can salvage the situation, but it's too late. The single marine I manage to get into my bunker is useless at this point. From the low ground, I can’t do any damage to his units."
    
    show boltgame lose:
        xalign 1.0
        alpha 0
        easein 0.4 xalign 0.4 alpha 1 subpixel True

    "My attack was completely routed. Even though he didn't scout out the rush, he defended without breaking a sweat."
    window hide dissolve
    stop music fadeout 2.0
    stop sound fadeout 2.0
jump boltlosecheese

label boltgame_fastthird:
    scene bg boltgame placethird with dissolve:
        align(0,0)
    window show dissolve
    "I cut marines long enough to save up for a quick third base. It finishes before my first dropship is even out."

    scene bg boltgame thirddone with dissolve: 
        align(0,0)

    "Just as my expansion finishes constructing, a red blip shows up on my minimap. Is it a void ray? I have missile turrets to defend, so I should be fine."

    #asset warpin
    play sound "sfx/battle/warpin.ogg" fadein 1.0
    scene bg boltgame zealotwarp with dissolve: 
        align(0,0)

    "Wait no...it's floating on the outskirts of my base.  A warp prism? He’ll be be able to warp his units into my base! My army is completely out of position!"

    #scene bg black:
        #align(0,0)
    play sound "sfx/battle/marinekillzealot.ogg" fadein 1.0
    show boltgame attackzealots with easeinright:
        xpos .2
        yalign 0.40

    "He starts warping in just outside of my static defenses. Zealots rush into my base and tear my mineral line to pieces before I can move units back to defend. This is bad."

    stop sound fadeout 1.0
    hide boltgame with easeoutright
    
    #asset stalker shooting
    scene bg black with Dissolve(0.2):
        align(0,0)
    play sound "sfx/battle/stalkersshootingcc.ogg" fadein 1.0
    $ show_stalker_lasers()
    scene bg boltgame stalkerskillthird with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8): 
        align(0,0)
    "Oh god, he's at my natural too?  He’s got such a big army! I can’t keep my defenses up with my economy crippled."

    stop sound fadeout 1.0
    show boltgame stalkersmarch at center:
        ypos .2 alpha 0.0
        easein .5 ypos .7 alpha 1.0 subpixel True
        
    show black behind boltgame with dissolve:
        align (0,0)
    pause .3
    play voice "sfx/battle/stalkersblink.ogg"
    show white with Dissolve(.1):
        align (0,0)
    hide boltgame
    hide black
    play sound "sfx/battle/stalkersshootingcc.ogg" fadein 1.0
    $ show_protoss_blast()
    show bg boltgame stalkerswin with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8): 
        align(0,0)
    hide white with Dissolve(.2)
    pause .3
    "I spread myself way too thin. Ugh. If only I had done a better job scouting."
    "With my production structures camped, my units die almost the second they finish training. That's checkmate."
    #return
    stop sound fadeout 1.0
    stop music fadeout 2.0
    window hide dissolve
jump boltlosegreed
label boltgame_drop:

    scene bg black with dissolve:
        align(0,0)
    show boltgame medivac at center:
        ypos .2 alpha 0.0
        easein .5 ypos .7 alpha 1.0 subpixel True
    pause .5
    window show dissolve
    "Dropship play is a defining characteristic of a top terran player. If I win with this, it's a good indication that I can stand toe-to-toe with the best players in Korea."
    "It's time to put my practice to work. I gather enough units for an attack at my starport as the first dropship finishes."

    play sound "sfx/battle/medivacloada.ogg" fadein 1.0
    show boltgame medivac at center:
        ypos .7 crop(0,0,1280, 400)
        easein 0.4 ypos .6 crop(0,0,1280, 200)
        easein 0.4 crop(-1280,0,1280, 200)
    pause .7
    
    stop sound fadeout 1.0
    show boltgame medivacmove:
        crop(0, 0, 0, 400) alpha 0.0 yalign 0.4
        easein 0.4 xpos .5  alpha 1.0 crop(0, 0, 1280, 400)

    "It's imperative he doesn't see me move out, so I make sure the watch towers are clear and avoid places where protoss players commonly leave their observers."
    
    

    show boltgame medivacmove:
        crop(0, 0, 1280, 400) xpos .5
        yalign 0.4
        easein 0.4 alpha 0.0 crop(-1280, 0, 1280, 400)

    hide boltgame

    play sound "sfx/battle/medivacloudout.ogg" fadein 1.0   
    show boltgame medivacdrop with easeintop:
        yalign 0.3
        crop(0, 0, 1280, 250)
    "When my dropships are in the clear, I fly straight into his base.  He's unprepared for the attack, and I unload all my units rush to snipe some important tech buildings."
    stop sound fadeout 1.0  
    show boltgame medivacdrop:
        yalign 0.3
        crop(0, 0, 1280, 250)
        easein 0.4 crop(0,-50,1280,720)

    window hide dissolve

    hide boltgame
    #show white with Dissolve(.1):
        #align (0,0)
    play sound "sfx/battle/mmstalkerzealot.ogg" #fadein 1.0
    $ show_stalker_lasers()
    show bg boltgame dropattack behind white with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8): 
        align(0,0)
    #hide white with Dissolve(.1)
    window show dissolve
    "With the damage to his infrastructure done, my units retreat for the safety of my dropship. That set him back a ton."
    stop sound fadeout 1.0
    scene bg black: 
        align(0,0)
    play sound "sfx/battle/medivacloada.ogg" fadein 1.0
    show boltgame dropescape with easeinright:
        crop(0, 0, 350, 720)
        xalign 0.5
    
    stop sound fadeout 1.0
    show boltgame dropescape:
        xalign 0.5
        easein 0.4 crop(0, 0, 800, 720)
    "The game is going incredibly well, so I decide to pull back on my aggression and build up an army for a final push."

    scene bg black with Dissolve(0.1):
       align(0,0) 

    show boltgame mmmoveout:
        yalign 0.0
        alpha 0
        easein 0.4 yalign 0.3 alpha 1 subpixel True
    "He's been too busy defending to get a decent standing army, and when I roll in with my amassed units..."
    
    #particleadd - marines firing

    hide boltgame mmmoveout with Dissolve(0.1)
    show white with Dissolve(0.1):
        align(0,0)

    play sound "sfx/battle/mmstalkerzealot.ogg"

    show bg boltgame attackbobbing:
        align(0,0)
    hide white with Dissolve(0.2)
    "... he kites back, bobbing and weaving away from my forces while delivering potshots."
    
    stop sound fadeout 1.0
    scene bg black with Dissolve(0.1):
       align(0,0) 

    show boltgame chasedown:
        yalign 0.0
        alpha 0
        easein 0.4 yalign 0.25 alpha 1 subpixel True
    "I give chase, the taste of victory tantalizingly close. I manage to corner his army, leaving him with nowhere to run."
    "But just as I move in to deliver to final blow…"

    scene bg black:
        align(0,0)

    play sound "sfx/battle/stalkzealotstorm.ogg" fadein 1.0
    play voice "sfx/battle/protossstorm.ogg" fadein 1.0
    show bg boltgame stormed:
        align(0,0)
    
    show white at flash(.05)
    show white at flash(.18) as white2
    show la at lightning_bolt(1)
    show lb at lightning_bolt(2)
    show lc at lightning_bolt(3)


    pause(0.6)




    "He flanks me with a half dozen templar, showering my army in high-damage storms! I pull back frantically, but my army is left in tatters!"
    hide white
    stop sound fadeout 1.0
    stop voice fadeout 1.0
#
    window hide dissolve
    play sound "sfx/battle/archonsfightmm.ogg" fadein 1.0
    play voice "sfx/battle/mmstalkerzealot.ogg" fadein 1.0
    show blacksolid at right:
        xpos 2.0
        linear .1 xpos 1.0 subpixel True
    pause .1
    show swoosh2 at center behind blacksolid
    show blacksolid at right:
        linear .1 xpos 0.0 subpixel True
    show swoosh2 at center  with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8)
    hide boltgame

    play sound "sfx/battle/stalkerzealotprobesurroundmarines.ogg" fadein 1.0
    show bg boltgame archonattack:
        align(0,0)
    pause .5

    hide swoosh2 with Dissolve(.1)
    window show dissolve

    "I try my hardest to gather enough units to mount a second offensive, but he continues to crush my attacks with only a handful of well-upgraded and well-microed zealots, stalkers and archons."
    "How the hell did this happen? My lead is gone!"
    stop sound fadeout 1.0
    stop voice fadeout 1.0
    scene bg black with Dissolve(0.1):
        align(0,0)

    show boltgame mmmoveoutscv: 
        yalign 0.0
        alpha 0
        easein 0.4 yalign 0.4 alpha 1 subpixel True

    "Frustrated, I box all of my workers and charge towards his base for a final attack. With my SCVs on the frontlines, I should have enough power to take a direct engagement."


   #particleadd - marines firing
    show white with Dissolve(0.1):
        align(0,0)
    
    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    scene bg boltgame contest4th:
        align(0,0)

    hide white with Dissolve(0.2)         
    
    "I roll through his fourth base uncontested! Yes! He’s giving up ground because he knows he can’t face me!"
    
    stop sound fadeout 1.0
    scene bg black with Dissolve(0.1):
        align(0,0)

    show boltgame moveupnatural: 
        yalign 0.0
        alpha 0
        easein 0.4 yalign 0.27 alpha 1 subpixel True

    "Emboldened, I drive up ramp leading to his natural to end the game…"
    
    
    #show white with Dissolve(0.1):
        #align(0,0)

    hide boltgame

    #PARTICLEISSUE

    scene bg black with Dissolve(0.1):
        align(0,0)
    #sfx add archon mmm battle
    play sound "sfx/battle/archonsfightmm.ogg" fadein 1.0
    play voice "sfx/battle/mmstalkerzealot.ogg" fadein 1.0
    show white at flash(.05)
    show white at flash(.18) as white2
    show la at lightning_bolt(1)
    show lb at lightning_bolt(2)
    show lc at lightning_bolt(3)
    show bg boltgame droplose with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)
    pause 0.2
    $ show_stalker_lasers()
    $ show_protoss_blast()
    #hide white with Dissolve(0.2)   

    "... And find myself face to face with an ambush. My frontline evaporates before I can issue the command to retreat, and he crushes what remains of my army a few moments later."
    "I can’t believe it. I lost."
    "I stare blankly at the screen for almost ten seconds before I finally type gg and quit out of the match."
    window hide dissolve
    stop voice fadeout 1.0
    stop music fadeout 2.0
    stop sound fadeout 2.0
jump boltlosedrops
label stuntgame:
    play music "sfx/terran3.mp3"
    scene bg stuntgame opening with dissolve: 
        align(0,0)
    window show dissolve
    show playercards_stunt:
        xalign 1.5
        yalign 0.5
        alpha 0
        easein 0.4 xalign 1.0 alpha 1
    
    "Cannons, two-gate, four-gate, blink, proxy robo, proxy stargate. There are a dozen different ways that Stunt could end this game early."

    "As a precaution, I scout around the interior of my base to ensure that I'm not being cannon rushed."
    
    hide playercards_stunt with Dissolve(0.2)

    play sound "sfx/battle/cannonfiring.ogg" fadein 1.0

    show stuntgame cannon:
         xpos -0.5
         yalign 0.4
         easein 0.4 xalign -0.02 subpixel True

    "And, as I discover, I am. Just outside my vision range and dangerously close to my worker line, a cannon finishes building." 
    
    stop sound fadeout 1.0
    play sound "sfx/battle/scvdie.ogg" fadein 1.0
    show stuntgame scvdie:
         xpos -0.5
         yalign 0.4
         easein 0.4 xalign -0.02 subpixel True
    
    "Some losses in a defense are inevitable, but if I handle this well it should put me ahead of Stunt."


    "It's gutsy of him to risk a best of one on a strategy like this. Practically all I have to do is scout it to score a victory."
    hide stuntgame with dissolve
    stop sound fadeout 1.0
    #hide stuntgame cannon with easeoutleft


    scene bg black with dissolve:
        align(0,0)
    play sound "sfx/battle/marinegroupshooting.ogg" fadein 1.0
    show stuntgame killcannon:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True
    "By microing my injured SCVs away from cannon shots, I'm able to end the rush at a low cost. In truth, that seemed like an exceptionally weak attack. Was Accel hyping this kid up for nothing?"
    stop sound fadeout 1.0
    #### update sound - just explosion
    play sound "sfx/battle/marineskillpylons.ogg" fadein 1.0
    $ show_protoss_blast()
    show stuntgame cannonexplode with Dissolve(0.15):
        yalign 0.35
        xalign 0.4

    "I end up only losing three of my workers by the time his single cannon is dead. Now, where's that probe..."

    stop sound fadeout 1.0
    play sound "sfx/battle/probemarineexplode.ogg" fadein 1.0
    show stuntgamealt killprobe:
       yalign 0.4
       xalign 1.5
       easein 0.4 xalign 1.01 subpixel True

    "There it is. With his probe down, there's no way he'll be able to drop down anymore cannons."

    stop sound fadeout 1.0
    #hide stuntgamealt with dissolve
    #hide stuntgame with dissolve

    scene bg stuntgame decision with dissolve:
        align(0,0)

    "Still, he's probably planning his next move. I have to decide what comes next."

    "If he's transitioning into something standard, this would be the perfect time to counter-attack." 
     
    "His tech has to be lacking, so there's no way he'll have strong enough units to defend a marine attack."

    "And while it seems incredibly unlikely, there's always a chance that he might have another attack ready."
     
    "If I want to err on the side of caution, I could stay in my base and simply tech up. But that might give him enough time to get back into the game."

    "I should make this call based on what I know about his playstyle."
    window hide dissolve
    menu:
        "Counter-attack with marines":
            jump stuntgame_counter
        "Stay on the defensive":
            jump stuntgame_stay


label stuntgame_counter:
    scene bg black with dissolve:
        align(0,0)

    show stuntgame marines:
        xalign 0.4
        ypos 1.0 alpha 0
        easein 0.4 ypos 0.0 alpha 1 subpixel True
    window show dissolve
    "I don't want to give Stunt enough time to get back on his feet. Without applying some kind of pressure, he could easily take a blind risk and put us on even footing."
    "His cross-map position is guaranteed due to the map's version--"
    
    window hide
    play sound "sfx/fastslash.ogg"
    show blacksolid at right:
        xpos 2.0
        linear .1 xpos 1.0 subpixel True
    pause .3
    play sound "sfx/zealotslash.ogg"
    show swoosh1 yellow at center behind blacksolid
    show blacksolid at right:
        linear .1 xpos 0.0 subpixel True
    show swoosh1 yellow at center  with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8)
    show stuntgame zealots with easeintop:
        xalign 0.5
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.30 subpixel True

    hide swoosh1 yellow with Dissolve(.1)
    window show dissolve

    hide swoosh1 with Dissolve(0.1)
    "Woah, shit! Zealots?! How?!"
    
    stop sound fadeout 1.0
    #hide stuntgame with easeoutleft


    play sound "sfx/battle/cannonfiring.ogg" fadein 1.0

    show stuntgame marinesdie:
        yalign 0.4 alpha 0.0
        xalign 1.01
        easein 0.2 alpha 1.0 xalign 0.5 subpixel True
    $ show_stalker_lasers_right()

    "--- And again! I took my eyes off of my main army long enough that it ran into cannons positioned at the top of Stunt's choke point!"
    "I try desperately to pull my units back in time to defend, but the damage is done."
    stop sound fadeout 1.0
    #hide stuntgame with easeoutright
    scene bg stuntgame lose at center with Dissolve(.3)

    "With my economy completely eviscerated and his base well-fortified, I have no way to stay in the game."
    window hide dissolve
    stop sound fadeout 1.0
    stop music fadeout 1.0
jump stuntlose


label stuntgame_stay:
    scene bg black with dissolve:
        align(0,0)


    show stuntgame stayputbuild:
        yalign 0.0
        alpha 0
        easein 0.4 yalign 0.4 

    window show dissolve
    $ persistent.en15_locked = False
    $ encyclopaedia.unlockEntry(en15, persistent.en15_locked)
    "Even though I'm giving up a chance to win the game immediately, the safe thing to do is {color=#FF5E5E}tech{/color} up to dropships."
    

    show stuntgame scouted:
        yalign 0.4 alpha 0.0
        xalign 1
        crop(0,0, 180, 720)
        easein 0.6 alpha 1.0 xalign 0.4
        easein 0.6 crop(-400,0, 1280, 720) subpixel True


    "... But it looks like I won't need to. My precautionary scout uncovers an ambush waiting in a dark corner of my base."
    #hide stuntgame with easeoutright
    hide stuntgame with Dissolve(0.05)
    play sound "sfx/battle/marinekillzealot.ogg" fadein 1.0
    show stuntgame defend:
        yalign 0.4 alpha 0.0
        xalign 0
        easein 0.6 alpha 1.0 xalign 0.4 subpixel True


    "With more than enough units and space to micro my marines, I dispatch his zealots with barely any losses."


    stop sound fadeout 1.0
    #hide stuntgame with easeoutright
    ##PARTICLEISSUE
    play sound "sfx/battle/marineskillpylons.ogg" fadein 1.0
    $ show_protoss_blast()
    show stuntgame win:
      ypos 1.0 alpha 0 
      xalign 0.4
      easein 0.4 ypos 0.4 alpha 1 subpixel True

    "A cannon rush feint into a proxy gate? Absolutely ridiculous."
    "With his rush routed, Stunt quits out of the game without a gg."

    "I won. With surprising ease, too."
    stop sound fadeout 1.0
    stop music fadeout 1.0
jump stuntwin
label revabattle1:
    play music "sfx/terran2.mp3"
    scene bg battlereva opening with dissolve:
        align(0,0)
    show playercards_reva:
        xalign 1.5
        yalign 0.5
        alpha 0
        easein 0.4 xalign 1.0 alpha 1
    
    window show dissolve
    "Alright. Time to show Reva and everyone else that's watching what I'm made of."

    
    show bg black with dissolve:
        align(0,0)

    show battlereva scout:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True

    "I'm watching my scout cross the map when a thought occurs to me. If this guy supposedly hates rushes, I should be able to score a pretty easy win against him with one."
    $ persistent.en18_locked = False
    $ encyclopaedia.unlockEntry(en18, persistent.en18_locked)
    "There's a specific {color=#FF5E5E}proxy{/color} build that works really well on this map, especially against the type of player that Accel described Reva as. I might risk angering the person I'm trying to recruit, though."
    "Still, the game is being broadcast online. If I win, there's a chance that I could earn enough cred to find another player anyway."
    "Do I really want to go against Accel's advice? It's only one game, after all."
    window hide dissolve
    menu:
        "Prepare for a drawn out match":
            jump revabattlemacro
        "Snag a quick win":
            pass

    scene bg battlereva firstgas with dissolve:
        align(0,0)
    
    window show dissolve
    "Why should I have to play out some hour long snore-fest just because Reva doesn't like being cheesed? It's a part of the game, whether he likes it or not."

    scene bg black with dissolve:
        align(0,0)

    show battlereva scout2:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True
    "I divert my scouting SCV's path to the bottom corner of my opponent's natural expansion. With luck, he won't see this until it's too late."
    hide battlereva scout2  at center with dissolve
    play sound "sfx/battle/buildingplaced.ogg" fadein 1.0
    scene bg battlereva proxyrax with dissolve:
        align(0,0)
    "Proxy marauder is an incredibly strong build against anyone who expands early, but I could even do damage on the off-chance that he doesn't wall off entirely."
    scene bg battlereva completedrax with dissolve:
        align(0,0)
    "With my early gas and mineral production all devoted to this attack, I find myself in a promising position when my first marauder surges from the barracks."    
    scene bg black:
        align(0,0)
    play sound "sfx/battle/buildingplaced.ogg" fadein 1.0
    show battlereva marauderarrive:
        xalign 1 alpha 0 
        crop(0, 0, 300, 900)
        easein 0.4 xalign 0.5 alpha 1

    "Hah, command center first. He built an expansion before producing even a single unit. Punished."
    "I throw down a bunker at the bottom of my opponent's ramp,{nw}"
    
    show battlereva marauderarrive:
        xalign 0.5
        crop(0, 0, 300, 900)
        easein 0.8 crop(-0, 0, 600, 900)

    extend " and he immediately follows suit. But he has absolutely no chance to defend without an army to his name."
    hide battlereva marauderarrive
    
    show screen missile_particles_right
    play sound "sfx/battle/singlemarauderfire.ogg" fadein 1.0
    show white with Dissolve(0.1):
        align(0,0)
    show battlereva marauderwin at center
    hide white with Dissolve(0.2)
    $ show_tank_blast()
    "I waltz my marauder up the ramp just in time to watch his first marine scramble from a barracks and rush towards his bunker. But before he can get there, my marauder picks him off."

    stop sound fadeout 1.0
    hide battlereva marauderarrive
    stop music
    stop sound
    "... And just like that, the game ends. Reva quit out of the match without a single word."

jump revalose
    #return

label revabattlemacro:

    scene bg battlereva macroexpo with dissolve:
        align(0,0)
    window show dissolve
    "Ergh. It's not like I hate playing standard or anything, I just don't like that I'm playing straight into this guy's strong point. Whatever."
    play sound "sfx/battle/buildingplaced.ogg" fadein 1.0
    scene bg battlereva macrofactory with dissolve:
        align(0,0)

    "As expected, the game begins with a long calm. Reva shows absolutely no sign of early aggression, instead focusing entirely on building a strong economy."
    "I use the breathing room to invest heavily into structures for tank production."

    scene black with Dissolve(0.1):
        align(0,0)
    show bg battlereva barracksscout at center:
        yalign 0.0
        alpha 0
        easein 0.4 yalign 1.0 alpha 1

    "My scout reveals that Reva's doing the same thing. Just as Accel said, looks like it's going to be a long, drawn out tank vs. tank positioning war."

    scene bg black:
        align(0,0)

    show battlereva scouttank at center:
        ypos 0.5
        alpha 0
        easein 0.4 ypos 1.0 alpha 1

    "Reva and I split the map in half, one side littered with his bases, defensive structures and tanks, and one side with mine."

    scene bg battlereva macharmy with dissolve:
        align(0,0)
    "I'm not particularly comfortable with this style of play. I prefer an agile army accompanied by dropships, but it's next to impossible to break a meching terran if they have a strong economy."
    "Well, I need to start thinking about my next move. Even though my center map position--{nw}"
    hide battlereva scoutexpo
    window hide
    play sound "sfx/battle/seigeattack.ogg" fadein 1.0
    
    $ show_tank_blast()


    show bg battlereva tanksattack with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)
    
    pause .5
    window show dissolve
    "Woah! Shit, I'm under attack!"
    stop sound fadeout 1.0
    play sound "sfx/battle/seigeattack.ogg" fadein 1.0
    window hide dissolve
    scene bg black with dissolve:
        align(0,0)
    stop sound fadeout 1.0
    show battlereva revatanks at center with dissolve
    window show dissolve
    "Reva's inching his tank line towards the center of the map. He managed to find a weak position in my formation-- one of my tanks was a bit too far away from the rest, and it got picked off."
    ##redo scan seaquence
    window hide dissolve
    stop sound fadeout 1.0
    hide battlereva revatanks
    play sound "sfx/battle/nuclearlaunchdetected.ogg" fadein 1.0
    
    scene bg black with dissolve:
        align(0,0)
 
    $ renpy.pause(1.3, hard=True)
    window show dissolve
    "A nuke?! In a serious game?!"


    stop sound fadeout 1.0

    play sound "sfx/battle/scan.ogg" fadein 1.0
    show white with Dissolve(0.1):
        align(0,0)
    show battlereva scan1 at center with Dissolve(0.2)
    hide white with Dissolve(0.2)
    "Not here..."
    
    hide white 
    hide battlereva scan1
    play sound "sfx/battle/scan.ogg" fadein 1.0
    show white with Dissolve(0.1) :
        align(0,0)
    show battlereva scan2 at center with Dissolve(0.2)

    hide white with Dissolve(0.2)
    #hide white2 with Dissolve(0.2)
    "Not here either! Where's the nuke?! Shit, I need to catch it before I lose my army!"
    hide white
    hide battlereva
    play sound "sfx/battle/scan.ogg" fadein 1.0
    show white with Dissolve(0.1):
        align(0,0)
    show battlereva foundghost at center with Dissolve(0.2):
       xalign 0.4
       yalign 0.4
    hide white with Dissolve(0.2)
    "Boom! There's the ghost."
    #COMEBACK
    stop sound fadeout 1.0


    #particles tank blast
    hide battlereva foundghost
 
    play sound "sfx/battle/seigekillghost.ogg" fadein 1.0
    $ show_tank_blast()
    hide white

    show bg battlereva killghost with  Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)

    pause .5

    "Phew. I managed to catch it before the nuke went off. Alright, with that threat out of the way, I can get back to addressing the tank line{nw}"
    window hide
    stop sound fadeout 1.0

    play voice "sfx/battle/nukeland.ogg" fadein 1.0

    show white at center with Dissolve(1)

     #nuke explode sfx
    show bg battlereva nuked with dissolve:
        align(0,0)

    hide white with Dissolve(2)

    pause 1.4
    window show dissolve
    "Oh."
    window hide dissolve
    scene bg black with dissolve:
        align(0,0)

    stop music fadeout 2.0

    pause 0.5

jump revawin
    #return 

label studio_game1:
    play music "sfx/terran3.mp3"

    show bg studio at center

    caster "Spawning in at the 7 o’clock position for Team Crash is the blue protoss player, JangL!"
    commentator "His opponent from Team KaiNE at the 2 o’clock base is Shing!"
    #or just show this with the graphic
    "Protoss vs. Protoss, close positions. This match won’t last long."
    show jett neutral at right with dissolve:
        xpos .9
    j "Mirror matchups are so stupid. PvP most of all."
    show stunt fist at right with dissolve:
        xpos 1.15
    s "You don’t know the intricacies. It can sometimes be really intense!"
    show jett unimpressed with dissolve
    j "Literally every strategy is a coinflip. PvP should be considered gambling and made illegal."
    hide jett
    hide stunt
    with dissolve
    "PvP usually ends with both players on one base. The decision to expand is often too great of a risk, especially with the players as close as they are."
    "Moreso than in any other matchup, mind games are essential to securing an advantage."
    "Reach too far with aggression against a balanced strategy, you lose. Go middle of the road against a tech build, you lose. Tech up against an attack, you lose."
    play voice "sfx/clapper.ogg" fadein 1.0
    scene white with Dissolve(0.1):
        align(0,0)
    show black:
        align (0,0)
    show fourgate:
       xalign 0.4
    hide white with Dissolve(0.05)

    analyst "Yaaaaah! JangL and Shing both have opted for a four warpgate strategy!" 
    caster "Prepare to watch these two clash! It will all come down to their control!"
    "... Or, that. That can happen too."
    "Even with Jett’s grumbling, Stunt looks like he’s enjoying himself. After all, this is the type of game he loves."
    "Reva’s paying attention, though likely only to note the inefficiencies of Crash and KaiNE."
   
    show spottedattack at center:
        yalign 0
        crop(0, 0, 1280, 0)
        easein 0.18 yalign 0.5
        easein 0.8 crop(-0, 0, 1280, 900)
    hide fourgate
    with dissolve
        #show kaine player hiding in his own base
    "Both of the protoss players complete the buildings necessary for their attacks simultaneously, but it’s the Team Crash player who’s out of the map first."
    "A proxy pylon near the KaiNE player’s base will allow for quick front line reinforcements. Things would be going perfect for Crash, if not for one small problem…"

    show hiddenunits at center:
        yalign .3
        crop(0, 0, 0, 900)
        easein 0.18 yalign 0.3
        easein 0.8 crop(-0, 0, 1280, 900)
    hide spottedattack
    with dissolve
    "The attack was spotted. Rather than answer with his own attack, the KaiNE player is holding his units back at home… And he’s hiding half of them in a small corner of his base."


    

    show movingupramp at center:
        yalign 0
        crop(600, 0, 600, 900)
    hide hiddenunits
    with dissolve
    "I realize what’s happening just as the Crash player makes his move. Without the proper intel on his opponent, he feints a motion at his opponent’s ramp in the hopes of learning what he’s up against."

    show movingupramp at center:
        yalign 0
        crop(600, 0, 600, 900)
        easein 0.18 crop(0, 0, 1280, 900)

    "But the KaiNE player doesn’t even budge. No forcefield. No panicked chronoboost. Nothing. No defense at all."
    "After a moment’s hesitation, the Crash player charges up the ramp fully, confident that he’s caught his opponent in a moment of weakness."
    "For a moment, it looks like it was the right move. He heads forward to disable the KaiNE infrastructure…"

    hide movingupramp at center

    play sound "sfx/battle/forecfeild.ogg" fadein 1.0
    show white at center with Dissolve(0.1)
    
    
    show forcefield at center behind white
    hide white with Dissolve(.2)
    pause .3
    window show dissolve
    "And has his exit cut off. The KaiNE player reveals his hidden units and surges into Crash force."
    "Even though the battle begins with the two at an even unit count, the forcefield preventing the Crash player’s retreat also keeps his reinforcements from joining with his main army."
    hide forcefield at center with Dissolve(0.1)
    window hide dissolve
    $ show_stalker_lasers()
    play sound "sfx/battle/stalkersshootingcc.ogg"
    show forcefieldinbattle at center with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8)
    
    stop sound fadeout 1.0
    hide forcefield
    with dissolve
    window show dissolve
    "Despite some excellent unit control, the dwindling Crash army is devoured by the ambush. JangL taps out a gg, and the first game goes to KaiNE."

    scene threegateways at center with dissolve
    caster "An exceptional trap set by Shing! The key was the position of his three extra gateways!"
    analyst "He allowed the Crash player to catch sight of a single gateway, which led him to believe that there was hidden tech at the back of his base! Excellent tactical thinking."
    commentator "Indeed! It would have be too risky to find out with certainty what was coming next. He had to act. He should have cleared the path to his opponent’s base before showing his units!"
    window hide dissolve
    scene black with dissolve:
        align (0,0)
    scene bg studio:
        align (0,0)

    show stunt smug at right:
        xpos 1.15
    show jett neutral at right:
        xpos .9
    with dissolve
    window show dissolve
    s "Beautiful. Absolutely beautiful."
    show jett unimpressed with dissolve
    j "That could not have been more stupid. This is what happens in a matchup where scouting past the three minute mark is impossible."
    show reva glasses at left:
        xpos -.05
    show stunt neutral
    with dissolve
    r "KaiNE is fortunate that JangL hesitated. Had he disabled the forward gateway in time, Crash would have been victorious."
    "I aim my attention back at the Crash bench to see who they’re sending out next. Accel turns back and whispers to one of his teammates, and he starts heading for the booth."
    show jett smile with dissolve
    j "Finally, some ZvP. Better hope that Shing’s all-ins aren’t as pitiful as yours, Stunt."
    show stunt surprised with dissolve
    "Two minutes later, the Crash zerg stands cross map with the KaiNE player." 
    #return
    window hide dissolve
label studio_game2:
    play sound "sfx/battle/nexuswarpin.ogg" fadein 1.0
    scene bg studio2 thirdbase with dissolve:
        align(0,0)
    window show dissolve

    "The match opens off slowly, but a sudden greedy opening from the KaiNE protoss elicits a call for attention from the commentators."
    play sound "sfx/clapper.ogg" fadein 1.0
    caster "Yaaah! How bold! The map does not lend itself to a nexus first, yet he has planted one down without pause!"
    analyst "And it seems that it will be going unpunished! With one victory already, it seems that KaiNE decided now was an appropriate time to take a risk!"
    stop sound fadeout 1.0
    scene bg studio2 econ with dissolve:
        align(0,0)

    commentator "This spells bad news for Crash. With the protoss economy established so quickly, zerg will struggle to survive his powerful mid-game attack!"
    play sound "sfx/battle/warpin.ogg" fadein 1.0    
    show studio2 warpin:
        xalign 1.5
        easein 0.4 xalign 1.0

    "The commentator’s warning shows itself to be a well-informed one. The Crash player realizes his disadvantaged position too late. From inside the booth, he looks visibly shaken."
    stop sound fadeout 1.0
    #hide studio2 with easeoutright

    scene bg black with dissolve:
        align(0,0)

    show studio2 stalkers:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True

    "Shing marches across the map at the eight minute mark with an absurd number of blink stalkers, not bothering to clear the watch towers on the way over. His unscouted forward pylon allows him to power forward unchecked."
    ##asset stalker shoot
    show studio2 stalkers:
        yalign 0.35 alpha 1
        easein 0.4 xpos 1.01 alpha 0 subpixel True
    play sound "sfx/battle/stalkerskillingroaches.ogg" fadein 1.0
    $ show_stalker_lasers()
    show bg studio2 murderroaches with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)
    "The Crash zerg’s clumsy defense is painful to watch. The game was decided by the two minute mark, even if it took the protoss another seven to play it out."
    window hide dissolve
    stop sound fadeout 1.0
    scene black with dissolve:
        align (0,0)
    scene bg studio:
        align (0,0)
    show stunt neutral at right:
        xpos 1.15
    show jett neutral at right:
        xpos .9
    show reva neutral at left:
        xpos -.1
    with dissolve
    window show dissolve
    j "That was embarassing."
    show stunt smug 
    with dissolve
    s "Not my prefered all-in style, but I’ll admit it has its merits."
    show reva surprised
    show jett unimpressed
    with dissolve
    "A sudden realization that three out of four of us are on camera puts our conversation on pause. The VSL loves to show foreigners and girls in the breaks between games on stream for whatever reason."
    show reva sweat with dissolve
    "Reva shields her face and glances away while I wave and watch myself on screen with an undeniably awkward expression."
    "The cameraman makes the mistake of panning past us to focus solely on Jett."
    play voice "sfx/evil.mp3"
    scene black:
        align (0,0)
    show image "char/death.jpg" at center:
        ypos .5
    with Dissolve(.1)
    pause 1.0
    "Not a second later, the scene switches back to the casters."
    scene bg studio:
        align (0,0)
    show stunt neutral at right:
        xpos 1.15
    show jett unimpressed at right:
        xpos .9
    show reva neutral at left:
        xpos -.1
    with dissolve
    j "What kind of idiot doesn’t drone scout? He went pool first! It was an easy slow ling rally for the win."
    show reva glasses with dissolve
    r "The map lends itself to a typical zerg playstyle. He mistakenly believed that if he could defend an early rush from protoss, he would have an advantage going into the mid-game."
    show stunt smug with dissolve
    s "Mmm. I can already taste the extra large bibimbap. I’ll take cash, Jett."
    show jett neutral with dissolve
    j "Quiet. 0-2 isn’t impossible to come back from."
    window hide dissolve
label studio_game3:
    scene black with dissolve:
        align (0,0)
    show studio3 probe:
         ypos 1.0
         xalign 0.4 alpha 0
         easein 0.4 alpha 1 ypos 0.0 subpixel True
    window show dissolve
    "But Jett’s confidence falters a minute into the third game. The KaiNE protoss immediately sends a probe cross-map, intent on deciding the game with an early rush."

    show studio3 probe:
        ypos 0.0
        xalign 0.4 alpha 1
        easein 0.4 alpha 0 ypos -0.5

    hide studio3 probe
    show studio3alt hatchery with dissolve:
        xalign 0.4
        yalign 0.4
    j "SCOUT AROUND YOUR NATURAL, MORON. IT TAKES TWO SECONDS."
    
    play sound "sfx/battle/nexuswarpin.ogg" fadein 1.0
    show studio3 proxygates:
        alpha 0
        yalign 0.20
        xalign -0.5
        easein 0.4 xalign -0.1 alpha 1 subpixel True

    "And, as if he somehow heard the order through his booth’s soundproof foam, the Crash zerg catches sight of the proxy gateways just as they finish constructing."
    hide studio3 with easeoutleft
    caster "A moment later and the game would have been decided! How will the zerg react?!"
    stop sound fadeout 1.0
    scene bg black with dissolve:
        align(0,0)

    play sound "sfx/battle/spinecrawleruproot.ogg" fadein 1.0
    show studio3 spinelift:
        alpha 0
        yalign 0
        crop(600,0,600,720)
        easein 0.4 xalign 0.8 alpha 1 subpixel True
    "He responds by throwing down static defense in his main. A good option, since a pair of stationary spinecrawlers are too strong to contest with just a few zealots."
    scene black at center with Dissolve(0.1)
    show studio3 attackhatchery at center:
        alpha 0 ypos 0.55
        linear 0.3 alpha 1.0 ypos 0.65

    "The hatchery finishes despite the protoss’ efforts to force a cancel. It looks like Crash is going to stabilize here. Or would, if not for..."
    j "No! What are you doing!?! STOP!"
    
    show studio3 spinelift:
        xalign 0.8
        yalign 0
        crop(600,0,600,720)
        easein 0.4  crop(-200,0,1280,720)        
    "Jett takes two fistfuls of her own hair when the zerg uproots a spinecrawler and begins moving it down the ramp."
    "The protoss reaction is instant. The KaiNE player rushes in to take a fight with the remaining static defense."
    #asset - zealot slash
    play sound "sfx/fastslash.ogg"
    show blacksolid at right:
        xpos 0.0
        linear .1 xpos 1.0 subpixel True
    pause 0.3
    show swoosh2 at center behind blacksolid
    show blacksolid at left:
        linear .1 xpos 1280 subpixel True
    play sound "sfx/zealotslash.ogg"
    show swoosh2 at center  with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8)
    play sound "sfx/battle/zealotskillingzerglings.ogg" fadein 1.0
    scene bg studio3 win with dissolve:
        align(0,0)
    hide swoosh2 with Dissolve(0.1)
    "Even with a handful of zerglings and a queen aiding, the spinecrawler falls with only a single casualty for the protoss."
    analyst "An unmistakable blunder! He aimed to defend his natural expansion with the second spinecrawler, but failed to wait until he had enough zerglings!"
    caster "Such impatience is going to cost Crash the game and perhaps the series!"
    "With the free pick-off, it’s not long until the KaiNE player snowballs his lead into a victory." 
    stop sound fadeout 1.0
    window hide dissolve
    scene black with dissolve:
        align (0,0)
    scene bg studio:
        align (0,0)
    show stunt neutral grin at right:
        xpos 1.15
    show jett neutral3 at right:
        xpos .9
    show reva neutral at left:
        xpos -.1
    with dissolve
    window show dissolve
    "One of his teammates charges into the booth and claps his back a dozen times, both of them smiling through some banter."
    "It’s a stark difference from the Crash bench. All save Accel look ready to accept defeat."
    "With a calm look back at his coach and a nod, he rises to replace his fallen teammate."
    analyst "It seems that Crash will send Accel as their final player. Will he be able to prevent the all-kill from Shing?"
    commentator "We must take into account KaiNE’s morale. The momentum in the series certainly favors a fourth and final victory."
    play sound "sfx/interupt.ogg"
    show jett angry 
    show stunt surprised
    with Dissolve(.2)
    j "ACCEL. DO NOT LOSE."
    show jett thinking with Dissolve(.2)
    "A few of the people seated in front of Jett wince at the volume of her jeer, turn around, stare, and then realize that they were about to shush a VSL Champion."
    show jett thinking2 
    show reva smile
    show stunt neutral grin
    with Dissolve(.5)
    "By the time she's finished signing a phone case from one of them, Accel is in the booth and ready to go."
    m "Think he can bring it back, Reva?"
    show reva glasses with dissolve
    r "No single player on KaiNE can match Accel."
    "I find myself in agreement with that. But Reva’s specific wording and lack of a conclusion leaves me wondering."
    hide reva
    hide stunt
    hide jett
    with dissolve
    commentator "What could be the final match of the day begins now! Accel against Shing, who will emerge victorious?"
    "Accel looks at home in the booth. He shows the four of us a smile and a thumbs up just before the game loads in."
    window hide dissolve
label studio_game4:
   
    scene bg black with dissolve:
        align(0,0)
    #asset marine firing
    show studio4 approachramp:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True
    window show dissolve
    "Despite the dire position his team is in, Accel wastes no time fighting back for control of the series." 
    play sound "sfx/battle/marinekillzealot.ogg" fadein 1.0
    show white at center with Dissolve(0.1)
    show studio4 deflect
    hide white with Dissolve(0.2)

    "He deflects the KaiNE player’s pressure with a well positioned marine force at the top of his ramp, killing off a zealot and scaring away a stalker."
    stop sound fadeout 1.0
    show studio4 leaveramp with dissolve
    caster "A vital maneuver! The protoss now lacks the information on whether or not Accel is expanding!"
    analyst "How will he cover his options? Accel’s cloaked banshee is nearly complete!"
    play sound "sfx/battle/nexuswarpin.ogg" fadein 1.0
    scene bg studio4 expo with dissolve:
        align(0,0)
    "The KaiNE player hesitates, and second later, throws down an expansion. Jett heaves a sigh of relief, confident that the game is decided."
    j "Classic protoss move. {i}Don’t Think, Guess.{/i}"
    stop sound fadeout 1.0
    
    show studio4 starport with easeinleft:
        xalign -0.05
        yalign 0.4
    show studio4alt bansheebuild with easeinright:
        xalign 1.05
        yalign 0.1
    "It’s true that if Accel had been expanding, the KaiNE player would have earned a slight edge."
    hide studio4alt with easeoutright
    
    #banshee shooting
    play sound "sfx/battle/bansheemove.ogg"
    show studio4alt2 banshee with easeinright:
        xalign 1.1
        yalign 0.3
    "Instead he’s is forced to watch helplessly as Accel’s banshee flies straight into his base and blasts his worker line to pieces."
    show studio4alt2:
       easeout 1.0 xpos 2.0
    show studio4:
        easeout 1.0 xpos -0.5

    #asset - banshee missiles

    #show white with Dissolve(0.1):
        #align(0,0)
    show bg studio4 bansheewin at center with dissolve
    play sound "sfx/battle/bansheesshooting.ogg" fadein 1.0
    $ show_missile_both()
    pause .5
    $ show_tank_blast()
    show bg studio4 bansheewin with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)
    #hide white with Dissolve(0.05)

    
    "With a highly delayed and evidently begrudged gg from KaiNE, Accel puts Crash on the board."
    j "Hah. Salty that he didn’t get his all-kill."
    window hide dissolve
    stop sound fadeout 1.0
    #return

label studio_game5:
    scene bg studio with dissolve:
        align(0,0)


    show stunt neutral at right:
        xpos 1.15
    show jett neutral at right:
        xpos .9
    with dissolve
    window show dissolve
    m "Why did the protoss leave so early? He could have at least gone for a base trade or something."
    show stunt yell with dissolve
    s "Are you kidding? Terrans have had base trades figured out for almost a year now! God, I wish my gateways could fly."
    show jett unimpressed with dissolve
    m "I guess. But there's no reason to throw in the towel so early. Even if he was going to lose, he could at least try to wear Accel out for the games to come. Accel could easily bring this back."
    hide jett
    hide stunt
    with dissolve
    "But even with his team’s first loss, the KaiNE coach looks confident. He gestures for one of his youngest players, speaks to him for almost an entire minute, and then sends him to the booth."
    play sound "sfx/clapper.ogg" fadein 1.0
    caster "Ahhhh! The KaiNE coach sends an amateur terran to face Accel? He must have confidence in either his young talent or remaining two players!"
    commentator "We must assume he wants to give the young terran some experience. Certainly, there is no other reason to send him against as strong a contender as Accel!"
    stop sound fadeout 1.0

    "Reva watches the KaiNE coach impassively, never allowing her attention to leave him until the fifth game loads in."
    window hide dissolve
    #crops wrong
    scene bg black with dissolve:
        align(0,0)
    play sound "sfx/battle/buildingplaced.ogg" fadein 1.0
    show studio5 ccfirst with easeinleft:
        crop(0,0,350,720)
        alpha 0
        xalign 0.0
        yalign 0.4
        easein 0.4 xalign 0.4 alpha 1

    stop sound fadeout 1.0
    show studio5 ccfirst:
        crop(0,0,350,720)
        xalign 0.4
        yalign 0.4
        easein 0.4 crop(0,0,700,720)
    window show dissolve
    caster "Yaaaaaah! KaiNE opens with command center first!"
    commentator "It seems that the KaiNE team has a strong preference to set the pace of the game and force their opponents to react! How will Accel respond?"
    j "Accel is going to scout it and throw down his own CC. What else? He’ll outmacro this kid anyway."
    "Reva answers Jett with a nod, though not in a way that makes her seem particularly pleased." 
    #hide studio5 with easeoutright
    stop sound fadeout 1.0
    play sound "sfx/battle/buildingplaced.ogg" fadein 1.0
    hide studio5
    show studio5 ccresponse:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True

    "As predicted, Accel’s thorough scout discovers the KaiNE command center early enough to stay in an economy focused game."
 
    #asset marines firing
    stop sound fadeout 1.0
    play sound "sfx/battle/medivacexplode.ogg" fadein 1.0
    $ show_tank_blast()
    show white at center with Dissolve(0.1)
    hide studio5
    show bg studio5 killmedivac behind white:
        align(0,0)
    hide white with Dissolve(0.2)

    "Even with the amateur terran’s slight advantage, Accel claws his way back onto even footing and then claims a lead when he catches a drop on route to his base."
    window hide

    #asset explosion
    stop sound fadeout 1.0
    play sound "sfx/battle/seigeattack.ogg" fadein 1.0
    $ show_tank_blast()
    scene bg studio5 siege with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)
    window show dissolve
    "The Crash fans roar a cheer when Accel charges his opponent’s tank line in a way reminiscent of old Brood War mech battles. Old habits die hard."
    stop sound fadeout 1.0
    play sound "sfx/battle/scan.ogg" fadein 1.0
    show white with Dissolve(0.1):
        align(0,0)
    scene bg studio5 scan with dissolve:
        align(0,0)
    hide white with Dissolve(0.1)

    "Even with the game all but decided, the KaiNE terran remains until Accel moves forward to destroy his base. Just before offering his gg, the KaiNE amateur scans to reveal all of the Accel’s structures."
    r "As I thought."
    stop sound fadeout 1.0
    window hide dissolve
    scene black at center with dissolve
    scene bg studio:
        align (0,0)
    show reva glasses at left
    with dissolve
    window show dissolve
    "I wince as Jett belts out a ear-shattering cheer and then turn to Reva."
    m "What do you mean?"
    show reva expected with dissolve
    r "KaiNE will send their terran ace."
    show stunt smug at right:
        xpos 1.6 alpha 0.0
        easein .5 xpos 1.15 alpha 1.0
    show jett neutral at right:
        xpos 1.25 alpha 0.0
        easein .5 xpos .9 alpha 1.0
    show reva at left:
        easein .5 xpos -.1
    s "Not such a hard guess, really."
    play voice "sfx/clapper.ogg" fadein 1.0
    show jett thinking2 with dissolve
    "But even the previously confident Jett watches KaiNE's bench now. Sure enough, their team’s ace pulls himself to his feet, peels off his team jacket, and tosses it to a squealing fangirl."
    #screams
    "... Did she just sniff it? I’m going to pretend I didn’t see that."
    "The Crash coach paces back and forth with his hands behind his back. His bench looks far more invested in the series than they did two games ago."
    analyst "What a treat! The highest level of terran versus terran is about to unfold before us!"
    caster "I am excited to see how Accel measures up! His TvT has always been his strongest matchup."
    window hide dissolve
    scene black with dissolve:
        align (0,0)
    window show dissolve
    "Jett and Reva watch restlessly as the game loads up. Even Stunt has stopped cheering against Crash."
    r "KaiNE will go command center first. If Accel does not two rax, he will be at a disadvantage."
    s "Are you from the future or something? What’s with these super specific predictions?"
    j "Shut up. Watch."

label studio_game6:

    scene bg studio6 cc with dissolve:
        align(0,0)

    "Accel opens with standard play and repeats the scout of his opponent’s CC first at a timing near identical to last game."
    window hide dissolve
    scene bg black with dissolve:
        align(0,0)
    
    #show studio6 bunker:
       # yalign 0 alpha 0.0
        #easein 0.2 alpha 1.0 yalign 0.35 subpixel True
    play sound "sfx/battle/buildingplaced.ogg" fadein 1.0
    #pause 1.0

    hide studio6
    show studio6 scvbunker:
        xalign 0.4
        ypos -0.5 alpha 0.0
        easein 0.2 alpha 1.0 ypos .0 subpixel True
    with dissolve
    window show dissolve
    "Feigned bunker aggression provokes brief panic in the KaiNE ace, forcing him to pull a handful of SCVs to contest what could be a direct counter to his build."
    r "A good move. But it will not be enough."
    show studio6 scvbunker:
        xalign 0.4
        ypos 0.35 alpha 1
        easein 0.2 alpha 0 ypos 1.0
    play sound "sfx/battle/cancel.ogg" fadein 1.0
    hide studio6
    #$ show_tank_blast()
    show white at center with Dissolve(0.1)
    show bg studio6 cancel: #with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)
    hide white with Dissolve(0.2)
    "When the fake rush ends, the KaiNE player throws his head back, heaves a sigh of relief, and smiles. He begins teching aggressively, a dangerous option without scouting Accel."
    s "Can you please explain what is going on? Why do you know what’s happening before it happens?"
    scene black at center with dissolve
    j "The KaiNE ace used the amateur to bait out Accel’s response to CC first. This isn’t something that would be possible if they weren’t ahead by so many games."
    m "They sent their best player to face Accel with full knowledge of his reaction. But Accel can adapt on the fly, right?"
    j "Easier said than done."
    "Sure enough, Accel’s answer is the exact same as it was to the amateur before. Improvising is a rare skill for StarCraft players, even for someone as skilled and well-rounded as Accel." 
    r "The KaiNE player will build two starports behind his natural to avoid Accel’s typical scan patterns. He will then clear out Accel’s map vision with hellions and then camp Accel’s production with banshees and vikings."
    j "This isn’t over. Accel will scout the gas timings and might realize that something is off."
    scene bg studio6 starports with dissolve:
        align(0,0)

    "But the strategy proves to be too specific for Accel to cover without scouting directly. The missile turret in his worker line won’t protect his production structures."
    play sound "sfx/battle/scan.ogg" fadein 1.0
    show studio6 scan:
        xalign 1.5 alpha 0.0
        easein 0.4 xalign 1.1 alpha 1.0
    "Accel's scan misses the mark by mere pixels. There's no chance he'll be prepared in time."

    scene bg black with dissolve:
        align(0,0)

   #sound update
    play sound "sfx/battle/bansheecloaked.ogg" fadein 1.0
    show studio6 banshees:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True
    "With the center of the map clear, the KaiNE terran flies straight for Accel’s base."
    analyst "Unbelievable! We rarely see such a unit composition, but it is the perfect answer in this scenario!"
    show studio6 banshees:
        yalign 0.35 alpha 1.0
        easein 0.4 xpos -0.1 alpha 0.0 subpixel True



    stop sound fadeout 1.0
    hide studio6
    #asset banshee missiles


    play sound "sfx/battle/bansheesshooting.ogg" fadein 1.0
    scene white at center with Dissolve(0.1)
    show black behind white at center
    $ show_missile_both()
    show bg studio6 attack:
        align(0,0)

    show bg studio6 attack with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)
    $ show_tank_blast()
    hide white with Dissolve(0.2)
    "The vikings keeps Accel’s inferior air force at bay, while the banshees pound Accel’s structures and tanks without answer."
    "An attempt to establish a missile turret defense costs Accel a ton of workers. When he eventually stabilizes, his army is less than half the size of the KaiNE ace’s."

    stop sound fadeout 1.0
    scene bg black with dissolve:
        align(0,0)
    play sound "sfx/battle/unsiegedattacking.ogg" fadein 1.0
    

    show studio6 losearmy:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True

    "The game is over. Yet Accel remains until the bitter end, trading as cost-efficiently with his inferior force as he can." 


    stop sound fadeout 1.0
    #hide studio6 with easeoutright
    play sound "sfx/battle/bansheesshooting.ogg" fadein 1.0
    show studio6 bansheearmy at left:
        xpos -0.05 alpha 0.0
        easein 0.3 xpos 0.05 alpha 1.0


    "It’s only once the KaiNE ace dances his units back and forth that Accel finally taps out."

    stop sound fadeout 1.0
   #assets more battles
    $ show_tank_blast()
    play sound "sfx/battle/unsiegedattacking.ogg" fadein 1.0
    scene bg studio6 lose with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)

    "A cheer from the ace’s fans announces the conclusion of the series. 4-2, KaiNE."
    window hide dissolve
    stop sound fadeout 1.0
    stop music fadeout 2.0
jump CrashLose


label reva_vs_stunt:

    scene bg revastunt intro with dissolve:
        align(0,0)

    "."
    show white with Dissolve(.1):
        align (0,0)
    play sound "sfx/battle/marinegroupshooting.ogg" fadein 1.0
    scene bg revastunt zealotrush:
        align(0,0)
    hide white with Dissolve(0.2)
    "."
    
    show revastunt proberush with easeintop:
        xalign 0.4
        yalign -0.1

    "."
    stop sound fadeout 1.0
    hide revastunt with dissolve
    #assets zealot slash probe poke
    play sound "sfx/battle/zealprobesattacking.ogg" fadein 1.0
    show white with Dissolve(.1):
        align (0,0)
    scene bg revastunt surround:
        align(0,0)
    hide white with Dissolve(0.2)

    "."
    
    stop sound fadeout 1.0
    #return

label reva_ladder:

    scene bg revaladder opening with dissolve:
        align(0,0)
    play music "sfx/terran1.mp3"
    window show dissolve
    r "Your APM is low."
    "I wince and respond with a flurry of unneccesary keystrokes. I’ve never cracked 300 APM, even when I’m focused on doing so."
    scene bg revaladder building with dissolve:
        align(0,0)

    "A minute or two passes without comment, though it’s hard to tell whether or not that means she thinks I’m playing well."

    r "Your engineering bays are late."
    play sound "sfx/battle/buildingplaced.ogg" fadein 1.0
    "Are they? {w=.5}They are. {w=.5}Dammit."
    scene bg revaladder engi with dissolve:
        align(0,0)

    
    "I whip my mouse hard, box a pair of SCVs, and slam down the two delayed structures."


    #asset scan 
    show white with Dissolve(.1):
        align (0,0)
    play sound "sfx/battle/scan.ogg" fadein 1.0
    show bg revaladder scouted:
        align(0,0)
    hide white with Dissolve(0.2)
   
    "I check his army composition with a scan and decide I'm ready to challenge him."

    #asset ingame moving out to attack
    scene bg black:
        align(0,0)

    

   
    stop sound fadeout 1.0
    show revaladder approach:
        ypos 1.0
        xalign 0.4
        alpha 0
        easein 0.4 ypos 0.02 alpha 1 subpixel True
    "Delayed upgrades or no, I managed to keep a close enough eye on my opponent’s tech that I have a massive swell of vikings by the time his colossus come into play."
    

    show revaladder approach:
        ypos 0.02
        xalign 0.4
        alpha 1
        easein 0.4 ypos -0.1 alpha 0 subpixel True




    show white with Dissolve(.1):
        align (0,0)
    play sound "sfx/battle/protossdeathballvsterran.ogg" fadein 1.0
    show bg revaladder attack:
        align(0,0)
    hide white with Dissolve(0.2)

    "His army gets caught in an awkward position when he tries to establish his third base, allowing me to power forward into his base. It’s a win I’d normally celebrate with a self-assured smile."
    window hide dissolve
    stop sound fadeout 1.0

jump revaroom2

label reva_ladder2:

    scene bg revaladder2 opening with dissolve:
        align(0,0)

    "I had thought that Reva’s low-key attitude might have made her a little bit lenient with my mistakes. But she’s not all that different from Jett, minus how she delivers her criticism."

    "My next match is on the largest map in the current ladder pool. I’ll have a pretty easy time defending my expansions with the way that the map’s choke points are constructed."
    play sound "sfx/battle/buildingplaced.ogg" fadein 1.0
    scene bg revaladder2 sneakthird with dissolve:
        align(0,0)

    "Rather than poke and prod with marines or go for early aggression, I throw down a quick third base in a far-flung corner of the map shortly I begin my natural expansion."
    show reva glasses at left:
        xpos -.5
        easein 5 xpos -.15 subpixel True
    "Pulling off this kind of tactic is incredibly rewarding. If it goes unscouted, I'm practically guaranteed to win."
    show reva at left:
        linear .5 xpos -.15 subpixel True
    r "Why are you doing that? Practice something useful."
    "I shift my gaze aside to find Reva uncomfortably close to both me and the monitor."
    m "What if I decide to hide an expansion against Bolt?"
    show reva neutral with dissolve
    r "Are you going to risk the team on a coinflip? Cancel it and aim for a long game."
    play sound "sfx/battle/cancel.ogg" fadein 1.0
    show bg revaladder2 cancelthird with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)
    "Reva offer the advice too firm to be called a suggestion, and I find myself moving the mouse to do as instructed. This gaffe is going to set me back a fair bit."
    hide reva with dissolve
    scene bg revaladder2 expo with dissolve:
        align(0,0)

    "I gear up for a drawn out match by focusing on my upgrades and base defense. It’s not long before my protoss opponent and I have split the map in half and are jockeying for position."
    r "Build more defenses. You can afford a dozen planetary fortresses."

    m "Is that really necessary?"

    r "Mach, your opponent is protoss. Protoss players will stop at nothing to cheat an honest terran out of an earned win."

    "Funny. I typically image balance whiners as loud and obnoxious in real life. I wonder if she quit playing random out of guilt."

    scene bg revaladder2 planetary with dissolve:
        align(0,0)
    "Still, I oblige her and cram as many static defense structures as I can into a vital choke point."
    scene bg revaladder2 idlearmy with dissolve:
        align(0,0)

    r "There is an observer over your army."
    scene bg black with dissolve:
        align(0,0)
    
    show white with Dissolve(0.1):
        align(0,0)
    play voice "sfx/battle/scan.ogg" fadein 1.0
    play sound "sfx/battle/probemarineexplode.ogg" fadein 1.0
    show revaladder2 snipeobs at center
    hide white with Dissolve(0.1)
    "I squint to find that she’s right. Damn, how did I not catch that earlier? With a scan, I pick off the protoss scout and reposition my units."
    stop sound fadeout 1.0
    #hide revaladder2 with easeoutright
    hide revaladder2
    show revaladder2 approaching:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True

    "It takes a few minutes to adjust my army composition to one that better suits the extreme late game, but I’m soon ready to clash with my opponent."

    "At this point, StarCraft becomes less about strategy and more about patience. It's important to know when to stalk and when to pounce."

    "I sense an opening at last and rush into my opponent’s weak flank. Out of the corner of my eye I can see Reva tensing up, invested as much as I am in the outcome of the battle."

    hide revaladder2
    play sound "sfx/battle/protossballstormcollo.ogg" fadein 1.0
    show white at flash(.05)
    show white at flash(.18) as white2
    show la at lightning_bolt(1)
    show lb at lightning_bolt(2)
    show lc at lightning_bolt(3)
    show bg revaladder2 stormed with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)



    "But try as I might, my snipes don’t connect with the high templar scattered amongst the protoss army." 
    "He drowns my units in psi storm and steamrolls down the center of the map, destroying my constructed defenses along the way."

    window hide
    stop sound fadeout 1.0
    ##update sound

    play sound "sfx/fastslash.ogg"
    show blacksolid at right:
        xpos 0.0
        linear .1 xpos 1.0 subpixel True
    pause .3

    show swoosh2 at center behind blacksolid
    show blacksolid at left:
        linear .1 xpos 1280 subpixel True
    show swoosh2 at center  with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8)
    play sound "sfx/battle/archonsfightmm.ogg"
    show bg revaladder2 losebase behind swoosh2:
        align(0,0)
    hide swoosh2 with Dissolve(0.2)
#######################################################

    window show dissolve
    "I struggle pointlessly to mount a counteroffensive, but the damage is done. I’m forced to tap out a gg and quit the match with a huff."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    window hide dissolve
jump revaroom3
    #return 

label archonbattle1:

    scene bg black with dissolve:
        align(0,0)
    show archon stalker1:
        yalign 0.4 alpha 0.0
        xalign 1
        crop(0,0, 180, 720)
        easein 0.6 alpha 1.0 xalign 0.4
        easein 0.6 crop(-250,0, 1280, 720) subpixel True


    play sound "sfx/battle/singlestalkershoot.ogg" fadein 1.0
    #show archon stalker1:
        #crop(0,0,250,720)
        #xalign 0.4
        #easein 0.4 crop(0,0,800,720)

    #issue #enc_issue #fix this
    #$ persistent.en21_locked = False
    #$ encyclopaedia.unlockEntry(en21, persistent.en21_locked)

    "I soon find that her confidence is well placed. Even with Reva's economy-focused build order, Stunt's stalker harass makes my life difficult."
    stop sound fadeout 1.0
    show archon stalker2 with dissolve:
        crop(-250,0, 1280, 720)
        xalign 0.4


    "He dances the single unit back and forth at the entrance to my natural, all of his focus devoted to its control."

    "It's a painfully effective frustration that succeeds in slowing down my attempts at establishing economy and tech."

    "My multitasking and micro are brought to their limits, and we haven’t even hit the five minute mark. This is insane."
    "And very, very good practice."
    "I don’t have the chance to spare a glance over my shoulder at Accel or Jett, but I’d make a pretty sure bet that they’re just as intent on the game as Stunt, Reva, and I are."
    #hide archon with easeoutright
    
    #play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    play sound "sfx/battle/stalkersshootingcc.ogg" fadein 1.0
    
    ##LAUNCH-TODO tonight
    show archon timing:
        xalign 0.4
        crop(0,250, 1280, 500)
        yalign 0 alpha 0.0
        easein 0.4 alpha 1.0 yalign 0.35 subpixel True
        easein 0.4 crop(0,0,1280, 600)
    $ show_stalker_lasers_top()
    "The match drags on up until the Stunt and Reva archon rolls over my paltry force with a well-timed and perfectly controlled two-base push. It wasn't even close."
    #update sound - mmm vs stalkers

    #return
    stop sound fadeout 2.0
    window hide dissolve
jump postarchon1
