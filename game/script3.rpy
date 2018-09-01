###Act3
#stuff for the showmatch
init python:
    renpy.music.register_channel("Track1", "music", True)
    renpy.music.register_channel("Track2", "music", True)
    renpy.music.register_channel("Track3", "music", True)
    renpy.music.register_channel("Track4", "music", True)
    renpy.music.set_volume(1, 0, channel="Track1") 
    renpy.music.set_volume(0, 0, channel="Track2") 
    renpy.music.set_volume(0, 0, channel="Track3") 
    renpy.music.set_volume(0, 0, channel="Track4") 
    
label S34DayBeforeLan:
    ##bg park
    scene black with squares:
        align (0,0)
    pause 1
    scene bg parknight with squares:
        align (0, 0)
    $ renpy.music.set_volume(0.1, 0, channel="sound")
    play sound "sfx/nightcricket.ogg" fadein 2.0 loop
    window show dissolve
    "Given the mood coming out of the cafe, I’m surprised to find that none of us have all that much to say as we loiter around a park bench."
    show stunt phone at right:
        xpos 1.05
    show accel thinking3 at left:
        xpos -.1
    show reva concerned at left:
        xpos .2
    with dissolve
    "Stunt’s attention never strays from the game on his phone, while Reva and Accel simply stare off into space."
    hide stunt
    hide accel
    hide reva
    show jett considering at center
    with dissolve
    "Jett paces back and forth, though her gait lacks its usual purpose. Between all five of us, silence."
    hide jett with dissolve
    "Maybe not all that much needs to be said. We all know the stakes. Everyone’s done their part to prepare for tomorrow."

    "It’s natural for us to feel nervous. The key is to keep it from affecting our chance of winning."

    r "It is sad."
    show reva concerned at center with dissolve
    "I shift my gaze towards Reva, surprised to find her staring at the ground."

    m  "What is?"
    stop sound fadeout 2.0
    show reva neutral2 with dissolve
    play music "sfx/Searching For Game Master.ogg" fadein .7
    r "This may be the last evening we gather as a team."
    show accel concerned at left
    show reva at right
    with dissolve
    a "Ehh, c'mon Reva. Don’t say stuff like that. It won't do us any good."
    show reva concerned with dissolve
    r "But it is the truth."
    show reva neutral with dissolve
    r "Mach, please win tomorrow. I do not want to stop spending time with all of you."
    show reva glasses with dissolve
    r "I have been a happier person since I joined this team. I would strongly prefer to stay that way."
    hide reva
    hide accel
    show jett considering at center
    with dissolve
    "Guarded as she is, Reva intones a sadness that the rest of us are trying to deny. Even Jett ceases her march to observe the exchange."
    show accel thinking3 at left
    show reva neutral at right
    hide jett
    with dissolve
    m  "I feel the same way, Reva. I’ll win tomorrow, I promise."
    show reva frown with dissolve
    r "The penalty for lying is death."
    $ renpy.pause(1.0)
    show reva glasses with dissolve
    "Reva breathes out a sigh and collects herself."
    show reva smile with dissolve
    r "I believe that you will."
    show reva at left
    hide accel
    show stunt neutral at right
    with dissolve
    s  "Me too. Mach probably plays an important part of my story to become the greatest player of all time."
    show stunt neutral grin with dissolve
    s "The first chapter can’t end with a loss. It just wouldn’t make sense."
    hide stunt
    hide reva
    show accel neutral at left
    with dissolve
    #large accel
    "An arm slings itself around my shoulder. With a glance, I find that it belongs to Accel."

    a "Feeling alright?"

    m "Not as bad as before, but the pressure is still there."

    a "As your coach, I am obligated to encourage you to win. But what’s most important is what you want."
    show accel thinking2 with dissolve
    a "For what it’s worth, I’m with Reva. I’d be sad to see you leave Korea."

    m  "I’ve got more than enough motivation for tomorrow. Is that what we’re here for?"
    hide accel
    show jett considering at center
    with dissolve
    j  "It isn’t just for you."
    
    "For the first time first since she barged into my room, Jett addresses me directly. Her expression is devoid of the intensity that I’ve come to know her for."
    show jett neutral3 with dissolve
    j  "I wasn’t lying when I said that you had the potential to be great. True as that is, it doesn’t make you special."

    j  "Everyone has the capability to be a champion. It isn’t genetic or unique."
    show jett neutral with dissolve
    j  "I’m not denying the existence of talent. But it's not nearly as essential as people make it out to be. StarCraft—and everything else—is about way more than that."
    show jett neutral2 with dissolve
    j  "Most people are either unwilling or unable to work hard. Simply being able to overcome that barrier makes it possible to do things that other people sit around and daydream about."
    show jett neutral3 with dissolve
    j  "If you've done that, you can lose without regrets. Have you?"

    m  "Yeah. I have."
    show jett smile with dissolve
    j  "Good. Then all that's left is to trust it'll earn us the win."
    hide jett with dissolve
    "Silence follows Jett’s final remarks, leaving us with an air of gravitas. It’s only a quip from Stunt that saves the rest of us from our glum-faced staredown."
    stop music fadeout 1.0
    show stunt smug at center with dissolve
    s  "Deep."

    m  "Don’t be a prick, Stunt."
    play music "sfx/Deep Thought Intro.ogg"
    queue music "sfx/Deep Thought Loop.ogg"
    hide stunt
    show accel neutral at right
    show jett neutral at left
    with dissolve
    a "Alright. Let’s go over the game plan for tomorrow."

    a "How you play is up to you. But it's probably smart to stick to what you've been practicing."

    m "Yeah. I know better than to invent a build on the fly."
    show accel thinking2 with dissolve
    a "How about you open us up, Jett? Still against the build Reva prepared for game one?"
    show jett considering with dissolve
    j "I understand the idea, I just don’t think it’s a sure win. Bolt will probably assume Mach is looking to steal a win, so he’ll be on the lookout for something non-standard."
    show reva expected at right:
        xpos .97
    show stunt neutral at left:
        xpos .03
    hide accel
    hide jett
    with dissolve
    r "It was devised with that in mind. If executed as planned, it should secure a lead, if not a victory."
    show stunt yell with dissolve
    s "Don’t give Bolt any respect that he hasn’t earned. If you let him set the pace for the series, it'll be an uphill battle."
    hide stunt
    hide reva
    show accel neutral at right
    show jett considering at left
    with dissolve
    a "I agree with that, actually." 
    show jett unimpressed with dissolve
    j "Alright, fine. It's just not my style of play."
    show accel thinking with dissolve
    a" Moving on, how about mid-game?"

    m  "Um, I was planning on my usual style. Dropships to establish map control and slow down his third base. If I scout that he’s being too greedy, I go for the kill."
    show jett casual with dissolve
    j  "That’s solid. I wouldn’t change anything there."
    show stunt neutral grin at left:
        xpos .03
    show reva neutral at right:
        xpos .97
    hide accel
    hide jett
    with dissolve
    s  "Seconded. It’s annoying playing against those kind of terrans if I can't kill them early."
    show reva glasses with dissolve
    "Reva fidgets with her glasses, evidently disagreeing."

    r "Do not write off the possibility of mech."
    show reva at left
    hide stunt
    show jett angry at right
    with dissolve
    j  "He’s barely practiced mech! Why would you even suggest that?"
    show reva expected with dissolve
    r "It is the ideal unit composition when played at its apex."
    show jett unimpressed with dissolve
    j "Only if he can get there safely, which’ll be practically impossible against a protoss as lethal as Bolt."
    show reva neutral with dissolve
    "Reva concedes her suggestion with a shrug."
    show accel neutral at right
    hide reva
    show jett neutral at left
    with dissolve
    a "Last thing. Late game. If Bolt manages to get on three bases, don’t try to end the game in a direct fight unless you have tons of defenses prepared to slow down his march."
    show accel thinking2 with dissolve
    a "The fully-powered protoss army is stronger than a maxed out terran, so you have to look elsewhere to find an edge."
    show jett thinking with dissolve
    j  "The opposite is true in Brood War, so he's used to being the aggressor. If you see Bolt eager to engage with you, don’t automatically assume it's because he'll roll you."

    m  "That reminds me. Are there any other kind of mistakes that Brood War players make when they first switch to StarCraft 2? You and Accel should know better than anyone."
    show accel thinking3
    show jett neutral
    with dissolve
    a "Hm. It’s the little things, honestly. Knowledge that you take for granted that Bolt has to work for."
    show accel neutral with dissolve
    a "You can look at five marauders and know they’ll crush seven stalkers without actively thinking about it, for example. He probably can’t yet."
    show jett neutral3 with dissolve
    j  "That, and his strategies. Bolt hasn't been playing Star2 for as long as you, so he's probably only up to date on standard builds from the current meta."
    j "He’ll be relying on game sense and mechanics to carry him through that shortcoming. If you can get a read on him, he won't be able to fall back onto an older style."
    show jett smile with dissolve
    j  "And as strong a Brood War player as he is, Bolt isn’t immune to slip-ups, especially in a new game. If he expands too fast or spreads his army too thin, crush him."
    #add in info that jett knows specifically
    m  "Yeah. Got it."
    show accel thinking
    show jett neutral3
    with dissolve
    a "Then I guess we’ve done everything we can. Nothing to do but play."
    show accel neutral with dissolve
    a "You’ll want to run through some warm-ups and get a glimpse of the crowd early to keep your nerves down, so don’t be late."
    "When I answer with a nod, Accel smiles."
    show reva neutral at left:
        xpos -.1
    show stunt neutral at right:
        xpos 1.1
    show accel neutral behind jett at right:
        xpos .9
    show jett neutral at left:
        xpos .12
    with dissolve
    "A final glimpse at the four faces of my teammates underscores the need to win tomorrow. Nothing else needs to be said. Everyone has placed not only their trust, but also their futures in me."
    "Failure is not an option."
    window hide dissolve
    stop music fadeout 5.0
    scene black with slowfade:
        align (0,0)
    scene bg apartmentnight with midfade:
        align (0, 0)
    window show dissolve
    "I won’t be in this apartment for much longer."

    "But I'm going to leave it on my own terms."
    
    #dream here?
    stop music fadeout 2.0
    window hide dissolve
    jump S35ShowmatchWithBolt

label S35ShowmatchWithBolt:
    ##studiohallway
    ##studiobooth
    scene black with slowfade:
        align (0,0)
    scene bg hallway:
        align (0, 0)
    show black:
        align (0, 0)
    with midfade
    with fade
    window show dissolve
    play sound "sfx/vocal.ogg." fadein 2.0 loop
    k "How are you feeling, Mach?"
    m "Eh?"
    hide black
    show kim neutral at center
    with dissolve
    "I blink my eyes and rub them awake. An hour of warm-up at the studio has left me with only fifteen minutes before the match is set to begin."
    "The powder on my face feels weird. Standard procedure for all broadcasted matches, or so the makeup artist said."
    "Behind Mr. Kim, a small crowd filters into the stage area. The semi-finals for the Victory StarLeague begins right after the showmatch, so it’s unlikely that everyone is here just to watch me and Bolt play."

    "But judging by the number of people sporting the black and white colors of Shock T1, there are at least a few."

    m "Oh, Mr. Kim. Sorry. I’m well."
    show kim smug with dissolve
    k "Good. Best of luck in your match. Let’s hope that this is the beginning of a long and fruitful partnership."

    "I lower my head in a curt bow."

    m "I appreciate it."
    show kim neutral with dissolve
    "Mr. Kim matches my bow with a nod, and then slips around the corner and into the studio."
    hide kim with dissolve
    "I’m allowed only a minute of time to myself before the businessman's presence is replaced by Accel's."
    show accel neutral at center with dissolve
    a "Ready?"

    m "Yeah. I’m ready."

    "And I am. I stretch out my wrists and crack my knuckles to emphasize it."
    show accel thinking2 with dissolve
    a "Good. Let’s go."
    stop sound fadeout 2.0
    window hide dissolve
    scene black with squares:
        align (0,0)
    play music "sfx/alt.ogg" fadein 4.0
    pause 2
    scene bg studio with squares:
        align (0, 0)
    window show dissolve
    caster "But before we get into that, we have a special match before the VSTL begins, don’t we?"

    commentator "That’s right. Most of you have likely heard the news that Accel and Jett have left their teams to begin their own."

    analyst "Regardless of how the fans feel, one must admit that it was quite an ambitious decision."

    caster "Certainly! But today we have a match to decide whether those two will have their risk pay off!"

    commentator "A generous prize from Enoch Group has allowed us to host a showmatch between two wildly different players."

    analyst "A new sponsor! How exciting. On top of that, it’s refreshing to see that KPGA has finally begun to embrace StarCraft 2. How much do we know about the protoss Bolt?"

    caster "Ah, he’s a very strong player from Shock T1. But this is his first appearance in a StarCraft 2 match, isn’t that right?"

    commentator "We’ll have to see how his Brood War skills translate!"

    analyst "What about his opponent, Mach? Do we know much about him?"

    caster "There was very little information available about him online, so we must assume that he is an amateur. All the same, he must be quite skilled for Jett and Accel to call him their teammate."
    "It dawns on me that this match is probably being broadcasted online. Should I have told my parents or friends to tune in and watch?"
    play voice "sfx/zing.ogg"
    show white at center with Dissolve(.1)
    hide bg
    show image "bg/flashback.jpg" at center
    with Dissolve(.1)
    play voice "sfx/zing.ogg"
    show image "bg/flashback2.jpg" at center
    with Dissolve(.1)
    show white at center with Dissolve(.1)
    show bg studio at center
    hide white with Dissolve(.1)
    pause .5
    "… No. {w=.5}Enough." 
    "I’m tired of obsessing over acceptance from everyone from back home. This has nothing to do with them."

    commentator "Now, let’s get the comments from our players. Please welcome, Bolt and Mach!"
    stop music fadeout 3.0
    show rival smug at center with dissolve
    "A production assistant gestures me forward, and I step out onto the stage. Bolt approaches from the other side, standing just a few feet from me when we come to a stop."
    play music "sfx/Greased Lightning Intro.ogg"
    queue music "sfx/Greased Lightning Loop.ogg"
    show rival fierce with dissolve
    play voice "sfx/clapper.ogg" fadein 1.0
    "He gives a wave, and a few dozen people erupt into cheers. Among them are the screams of at least ten fangirls."

    "With a microphone in hand, he address the crowd with a charming disposition, completely opposite from every interaction I’ve shared with him."

    b "First, I would like to thank my fans for coming today. I've worked hard to prove that KPGA players will place first in StarCraft 2 championships in the near future."
    show rival smug with dissolve
    b "I’ve always performed well under pressure throughout my pro-gaming career, but today I don't think that I have much to worry about."
    play voice "sfx/laughing.ogg"
    "The comment draws a few laughs from the audience, KPGA fans and not. He continues."

    b "I am confident that I'll only drop one map today. My opponent's year of StarCraft 2 must have earned him at least one win against my single week."

    "That’s just an outright lie. But judging by crowd’s reaction, they’re buying it completely."
    show rival fierce with dissolve
    b "Foreigners could never compete in Brood War. I'm here to prove that the same is true in StarCraft 2."

    b "I promise to show you all good games. Please cheer for me!"
    play voice "sfx/clapper.ogg" fadein 1.0
    "He lifts a fist to another uproar of applause. What a fake piece of shit."
    hide rival with dissolve
    "But before I can spend anymore time lingering on how much I dislike Bolt, the VSL hostess takes the mic from him and offers it to me."

    hostess "Say a few words to your fans. I was told you can speak Korean, correct?"

    "Before I know it, the microphone is in my hand. I try my best not to look bewildered and turn my attention to the audience."

    m "Ehm. Hello. I’m Mach. I want to thank my team for helping me prepare for today's match, and the Enoch Group for sponsoring the showmatch." 
    m "I will do my best to win. Thank you."
    play voice "sfx/machclap.ogg"
    "My earnest approach earns me a polite response from the crowd, though not one that comes close to matching Bolt's."

    hostess "Please shake hands and go to your booths."
    window hide dissolve
    show la at lightning_bolt(1)
    show lb at lightning_bolt(2)
    show lc at lightning_bolt(3)
    show image "bg/cg4male.png" at center:
        xpos 1.5
        easein .2 xpos .5
    show image "bg/cg4bolt.png" at center:
        xpos -0.5
        easein .2 xpos .5
    pause .17
    play voice "sfx/thunder.ogg"
    show white with Dissolve(.05):
        align (0,0)
    hide white
    show bg cg4:
        align (0, 0)
    with Dissolve(.2)
    window show dissolve
    "Bolt is first to turn. His smile, no doubt designed and manufactured in an underground KPGA laboratory, belies the edge I see in his eyes."

    "He offers his hand, and I reach forward to take it for a single shake."
    b "I hope you practiced hard.{color=#110000}{vspace=30}{i}I am going to destroy you.{/i}"
    m "I did, don't worry.{vspace=30}{i}Not likely. I really, really want to see you lose."
    b "That's good. It would be a shame to disappoint the fans with an uneven series.{vspace=5}{color=#110000}{i}It doesn't matter what you want. You're trash, and after this you'll never forget it.{/i}"
    m "Agreed. Let's make sure to show exciting games.{vspace=30}{i}Easy to say. Let's see if you can actually do it.{/i}"
    "We separate without incident and I turn to take my place in the booth."
    
    window hide dissolve
    scene bg backstage:
        align (0, 0)
    show jett unimpressed at center:
        xpos .42
    with dissolve
    window show dissolve
    "Jett stands outside the door with my keyboard, mouse, and mousepad in hand."
    show jett neutral2 with dissolve
    j  "What the hell is this?"
    show image "char/bonus/key.png" at center:
        ypos .5 alpha 0.0 xpos .6
        easein .5 ypos .7 alpha 1.0 subpixel True
    "She drops a keycap into my hand."
    m "Um… I think that’s my Windows key?"
    show image "char/bonus/key.png" at center:
        ypos .7 alpha 1.0 xpos .6
        easeout .5 ypos .9 alpha 0.0 subpixel True
    show jett neutral3 with dissolve
    j  "It doesn’t belong on a pro-gamer’s keyboard. Fat-fingering that during a battle will tab you out and lose you the game."
    show jett considering with dissolve
    "She huffs and breaks eye contact. It’s obvious that she’s at least as stressed as I am."
    m "Jett. I’ve got this."
    show jett thinking2 with dissolve
    $ renpy.pause(1)
    show jett considering with dissolve
    j  "I know. Do your best, Mach. Fighting."

    "With a nod, she pushes open the booth door."
    stop music fadeout 5.0
    window hide dissolve
    scene bg booth with dissolve:
        align (0, 0)
    play voice "sfx/boothdoor.ogg"
    window show dissolve
    "Once inside, the ambient sound of the stage lights, cameras, and screens die down. All that I can hear is the subtle hum of the crowd and my own pulse." 
    play voice "sfx/Heartbeat.mp3"
    "It would be peaceful, if not for the adrenaline burning through my veins."
    "This is my first time inside of a booth. My heart is racing, and nothing I try to tell myself as I plug in my peripherals and configure my settings helps to calm it."
    "Playing in front of a crowd in the VSL has been a goal of mine for more than a year. Even with how hard I've been working, it feels like there should have been more build up to this moment."
    play voice "sfx/Heartbeat.mp3"
    "Yet, here I am. I reach out to touch the soundproofing material, if only to allow another of my senses to confirm that the moment is real."
    "Even as I try to keep my focus away from the crowd and on the game, I keep glancing past the computer monitor and towards my teammates seated in the front row."
    "They wave and cheer at me as the studio lights dim. I force myself to look back at the PC and focus entirely on the match at hand."

    "Everything I’ve done over the past week… No. The months I’ve been in Korea, and even the time before that. It’s all lead up to this moment."
    #BATTLE SCENE! Following scene follows from a victory.
#####################
init python:
    renpy.music.register_channel("MTrack1", "music", True)
    renpy.music.register_channel("MTrack2", "music", True)
    renpy.music.register_channel("MTrack3", "music", True)
    renpy.music.register_channel("MTrack4", "music", True)
    renpy.music.set_volume(1, 0, channel="MTrack1") 
    renpy.music.set_volume(0, 0, channel="MTrack2") 
    renpy.music.set_volume(0, 0, channel="MTrack3") 
    renpy.music.set_volume(0, 0, channel="MTrack4") 


    
play MTrack1 "sfx/zhi.ogg"
queue MTrack1 "sfx/zh.ogg"
play MTrack2 "sfx/zhi.ogg"
queue MTrack2 "sfx/zh3.ogg"
play MTrack3 "sfx/zhi.ogg"
queue MTrack3 "sfx/zh4.ogg"
play MTrack4 "sfx/zhi.ogg"
queue MTrack4 "sfx/zh5.ogg"

$ renpy.music.set_volume(1, 0, channel="MTrack1") 
$ renpy.music.set_volume(0, 0, channel="MTrack2") 
$ renpy.music.set_volume(0, 0, channel="MTrack3") 
$ renpy.music.set_volume(0, 0, channel="MTrack4") 

label showmatch1:
    
    scene bg showmatch1 opening with dissolve:
        align(0,0)
    show playercards_bolt_final:
        xalign 1.5
        yalign 0.5
        alpha 0
        easein 0.4 xalign 1.0 alpha 1
    "The second the loading screen ends, I put the plan into action. I rush one of my starting SCVs across the map."
    scene bg black with dissolve:
        align(0,0)


    show showmatch1 scout:
        yalign 0.0
        alpha 0
        easein 0.4 yalign 0.4 alpha 1 subpixel True
    "But I'm not sending it to his base."
    "It comes to a stop on the outskirts of his fourth base location. It's only barely closer to his base than mine, honestly."
    "But it's close enough to buy me precious seconds."

    show showmatch1 proxyeverything:
        xalign 1.0
        alpha 0
        easein 0.4 xalign 0.4 alpha 1 subpixel True


    "Reva called this build 'Proxy Everything.'"


    "Depot. Gas. Rax. Reactor. Fac. Starport. I've drilled it to perfection and hit every timing within the second."
    "Bolt didn't even scout. He'll pay for that mistake."

    play sound "sfx/battle/medivacloada.ogg" fadein 1.0
    hide showmatch1
    show showmatch1 dropship:
        crop(0,0,1280,500)
        yalign 0 alpha 0.0
        easein 0.4 alpha 1.0 yalign 0.35 subpixel True


    "My dropship rushes straight into his base at a timing that normally wouldn't be possible. Every single one of those extra seconds is precious."

    stop sound fadeout 1.0
    show showmatch1 dropship with easeintop:
        crop(0,0,1280,500)
        yalign 0.4
        easein 0.4 crop(-20,0,0,500) alpha 0

    hide showmatch1

    #asset hellion flame
    $ show_flamethrower_right()
    show white with Dissolve(0.1):
        align(0,0)
    play sound "sfx/battle/hellionsfire.ogg" fadein 1.0
    show bg showmatch1 hellionharass1:
        align(0,0)
    hide white with Dissolve(0.2)
    window show dissolve
    "Perfect! I unload my hellions straight into his mineral line. He was completely unprepared!"

    stop sound fadeout 1.0
    show bg black with dissolve:
        align(0,0)
    play sound "sfx/battle/helliomove.ogg" fadein 1.0 
    show showmatch1 hellionchase:
        ypos 1 alpha 0
        xalign 0.4
        easein 0.4 ypos 0.0 alpha 1
    "He tries to escape with his workers, but I'm too quick in giving chase. I'm not letting you get away, Bolt."

    stop sound fadeout 1.0
    #hide showmatch1 with easeouttop
    show showmatch1 hellionchase:
        ypos 0.0 alpha 1
        xalign 0.4
        easein 0.4 ypos -0.5 alpha 0
    
    hide showmatch1

    $ show_flamethrower_left()
    play sound "sfx/battle/hellionsfire.ogg" fadein 1.0
    show showmatch1 hellionharass2:
        alpha 0 
        crop(0,0,200,720)
        yalign 0.5
        xalign 0
        easein 0.3 xalign 0.4 alpha 1
        easein 0.4 crop(-400,0,1280,720) 
    "My hellions weave past his slow-moving army and deal another blow to his economy. That one must have crippled him."

    stop sound fadeout 1.0
    #hide showmatch1 with easeoutright

    #asset terran army moving in
    #aset shooting
    hide showmatch1
    show showmatch1 terranarmy:
        xalign 0.4
        yalign 0 alpha 0.0
        easein 0.4 alpha 1.0 yalign 0.35 subpixel True
    "He remains in the game only as an act of defiance. With my victory assured, I march into his base with an overwhelming force and take a fight on his turf."


    hide showmatch1
    $ show_tank_blast()
    show white with Dissolve(0.1):
        align(0,0)
    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    show bg showmatch1 win with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)
    hide white with Dissolve(0.2)
    "Tch. He scrapes together a final defense and actually manages to dent my army, though it's not enough to swing the game back."
    $ show_protoss_blast()
    show white with Dissolve(0.1):
        align(0,0)    
    show bg showmatch1 finalvictory with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)
    hide white with Dissolve(0.2)
    "Not bad. But game one is mine."    
    #return
    window hide dissolve
    stop sound fadeout 1.0
    $ renpy.music.set_volume(.3, 1, channel="MTrack1") 
    scene bg booth at center with dissolve
    window show dissolve
    "A gentle knock at the door behind me catches my attention while the studio prepares for the next game. A moment later, the door slides open."
    play sound "sfx/slidingdoor.ogg"
    pause .5
    show reva expected at center with dissolve
    r "Just as planned. Well executed, Mach."
    m "Seriously, where did you of all people come up with a build like that?"
    show reva neutral with dissolve
    r "Just because I loathe cheese does not mean I will not admit that it is occasionally useful and appropriate."
    m "I guarantee we'll be seeing it on the ladder for the next month."
    show reva smile with dissolve
    r "With luck, they will call it the Mach Build."
    show reva glasses with dissolve
    r "Maintain your momentum. Fighting."
    hide reva with dissolve
    "She hurries out of the booth and back to her seat in the crowd when I nod. Just as before, the studio lights dim and the second match gets under way."
    window hide dissolve
jump showmatch2
label showmatch2:

    init:
        $ timer_range = 0
        $ timer_jump = 0
    $ renpy.music.set_volume(1, 1, channel="MTrack1") 
    scene bg showmatch2 opening with dissolve:
        align (0,0)

    
    window show dissolve
    "Phew. Okay, keep it cool. The momentum is in my favor now. I should make use of this breathing room."
    "I need to find out how Bolt's going to be playing for the rest of the set. He went for a standard expansion last game, but I wasn't able to see his army as intended."
    "This map is good for two-base play. I should definitely go for drops, but I still need to decide on an opening."
    ##update sound
    window hide dissolve

    $ time = 1.0
    $ timer_range = 1.0
    $ timer_jump = 'showmatch2boltrush'
    show screen countdown
    menu:
        "Grab a quick expansion.":
            jump showmatch2boltrush
        "Lean on him with some early pressure.":
            jump showmatch2boltrush
        "Feint an aggressive strategy.":
            jump showmatch2boltrush

label showmatch2boltrush:
    scene bg black with Dissolve(0.1):
        align(0,0)
    play sound "sfx/battle/nexuswarpin.ogg" fadein 1.0
    show showmatch2 proxygate:
        alpha 0
        yalign 0
        xalign 0.4
        easein 0.4 yalign 0.30 alpha 1 subpixel True
    window show dissolve
    "Woah, wait a second! Bolt is proxy-gating me!"
    stop sound fadeout 1.0
    #hide showmatch2  with dissolve
    play sound "sfx/battle/buildingplaced.ogg" fadein 1.0
    show showmatch2 bunkerup:
        alpha 0
        xalign 1.0
        easein 0.4 xalign 0.4 alpha 1 subpixel True

    "God dammit, I didn't even consider the possibilty! I veer my gameplan in a defensive direction, but Bolt's attack is already overwhelming my mineral line."
    

    show showmatch2alt mineralline:
        xalign -0.5
        easein 0.4 xalign -0.05 subpixel True

    "Even with all the practice I had against Stunt's rushes, there's nothing I can do when caught so offguard. For every step forward I take with SCV and marine micro, Bolt seizes five with damage to my economy."


    #hide showmatch2 with dissolve

    #asset cannon attack

    play sound "sfx/fastslash.ogg"
    show blacksolid at right:
        xpos 2.0
        linear .1 xpos 1.0 subpixel True
    pause .3
    play sound "sfx/zealotslash.ogg"
    show swoosh1 at center behind blacksolid
    hide showmatch2alt
    hide showmatch2 
    show blacksolid at right:
        linear .1 xpos 0.0 subpixel True
    show swoosh1 at center  with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8)
    play sound "sfx/battle/zealotslashingbuildings.ogg"
    show bg showmatch2 lose at center
    hide swoosh1 with Dissolve(0.1)

    


    "I can't stay in the game any longer and tap out a gg. Urgh! Just like that, he evened up the series!"
    window hide dissolve
    stop sound fadeout 1.0

    $ renpy.music.set_volume(.3, 1, channel="MTrack1") 
    scene bg booth at center with dissolve
    show black at center behind bg
    window show dissolve
    "I barely have time to take my headphones off before I feel a pair of hands clamp down on my shoulders."
    play sound "sfx/Footstep.mp3"
    show bg booth at vpunch
    s "Keep it up!{w=.5}{nw}" 
    play sound "sfx/Footstep.mp3"
    show bg booth at vpunch
    extend " Stay in the zone!{w=.5}{nw}"
    play sound "sfx/Footstep.mp3"
    show bg booth at vpunch
    extend " You got this!{w=.5}"
    m "Ow. Ow! Okay, enough."
    show stunt neutral grin at center with dissolve
    s "He got really lucky. Scouted your base first, and you only barely missed the probe as it came up your ramp."
    show stunt smug with dissolve
    s "C'mon, you've been practicing with the future protoss bonjwa and his macro-battery. The next game is yours for the taking."
    m "Yeah. There's no way I'm letting another proxy get by me."
    show stunt fist with Dissolve(.2)
    s "That's what I'm talking about! FIGHTING!"
    hide stunt with dissolve
    window hide dissolve
    stop MTrack1 fadeout 1.0
    $ renpy.music.set_volume(.5, 1, channel="MTrack2") 
label showmatch3:
    scene bg showmatch3 opening with dissolve:
        align(0,0)
    window show dissolve
    "Alright. Keep it together. There's no way I'll let another proxy get by me."
    "My scout reveals little information, save that he's going for a one-base tech build. There are several things I need to be prepared for, so I should make sure the front of my base is reinforced."
    scene bg showmatch3 expo with dissolve:
        align(0,0)
    "As long as I keep my army on the ramp, I should be able to respond to any flying units. With each second that ticks by, I pull more and more away with the game."

    scene bg black:
        align(0,0)

    show showmatch3 tech:
        yalign 0 alpha 0.0
        easein 0.4 alpha 1.0 yalign 0.20 subpixel True
    "Just as long as I don't tech too aggressively and focus on maintaining a sizable army, I should be fine."

    #hide showmatch3 with easeoutbottom
    scene bg black:
        align(0,0)
    play sound "sfx/battle/singlemarauderfire.ogg" fadein 1.0
    show showmatch3 stalker:
        ypos 1.0 alpha 0.0
        xalign 0.4
        easein 0.4 alpha 1.0 ypos 0.0 subpixel True
    "Huh, did he transition into something more standard? He takes some damage on a scouting stalker before hastily pulling it away."

    hide showmatch3

    scene bg showmatch3 expo2 with dissolve:
        align(0,0)
    "Was that it? I should probably double check whether or not he's got an expansion down. It might be a good call to throw down a missile turret in my main as well, just as a precaution."

    #asset stalkers moving in w/ blink
    play voice "sfx/battle/stalkersblink.ogg"
    #show white with Dissolve(0.1):
        #align(0,0)
    $ show_protoss_blast()

    show white with Dissolve(0.1):
        align(0,0)
    show showmatch3 blink behind white:
        align(0,0)
    hide white with Dissolve(0.2)
    play sound "sfx/battle/stalkersshootingcc.ogg" fadein 1.0
    "Blink stalkers! Shit, he had vision on my high ground?! Must have been an observer... Argh! Why didn't I see it?!"

    #asset cleanup
    #show white with Dissolve(0.1):
        #align(0,0)
    $ show_stalker_lasers()
    show showmatch3 lose with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)
    #hide white with Dissolve(0.2)
    "He's able to pick off several units just as they finish building at my barracks, the numbers advantage heavily on his side."
    "I empty my bunkers and rush them up my ramp, but he turns my own choke point against me and handily defeats my entire army with some ridiculously precise micro."
    "I have nothing left to do but gg and accept the fact that I'm now down a game."
    window hide dissolve
    stop sound fadeout 1.0
    $ renpy.music.set_volume(.3, 1, channel="MTrack2") 
    scene bg booth at center with dissolve
    window show dissolve
    a "Knock knock."
    play sound "sfx/slidingdoor.ogg"
    pause .2
    show accel neutral at center with dissolve
    a "Yo. How are you feeling?"
    m "Do you want the polite answer or the honest answer?"
    show accel thinking2 with dissolve
    a "You're playing well, but Bolt's been able to sniff out where you're weakest. You need to confront him head-on."
    m "A macro game with a KPGA pro? Is that smart?"
    show accel laughing with dissolve
    a "Hey, no one ever said that StarCraft was an easy game."
    show accel neutral with dissolve
    a "We practice long hours for the moments like this. Show the crowd how hard you've been working."
    m "... Alright. I won't go down without a fight."
    show accel thinking with dissolve
    a "Good. Fighting."
    hide accel with dissolve
    window hide dissolve
    stop sound fadeout 1.0
    #return 
label showmatch4:

    scene bg showmatch4 opening with dissolve: 
        align(0,0)
    stop MTrack2 fadeout 1.0
    $ renpy.music.set_volume(.5, 1, channel="MTrack3") 
    window show dissolve
    "There's no way I'm giving up now. I've already proven to myself that I can beat this guy."
    "Forget the score. Focus on the game."
    
    scene bg showmatch4 expo with dissolve: 
        align(0,0)

    "This map is huge, but I opt for a conservative timing on my expansion. Bolt's shown a serious proclivity towards aggressive play."


    scene bg black with dissolve:
        align(0,0)

    show showmatch4 medivac:
        yalign 0 alpha 0.0
        easein 0.4 alpha 1.0 yalign 0.35 subpixel True

    "My scout reveals that we're on equal footing. Alright, time to drop the hammer."


    show showmatch4:
        easein 0.4 alpha 0.0 xpos -0.1

    $renpy.pause(0.4)

    hide showmatch4
    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    show showmatch4 dropexpo:
        alpha 0
        xpos 1.1
        crop (350, 0, 500, 720)
        easein 0.4 alpha 1.0 xpos 0.2
        easein 0.4 crop(0,0,800,720)

        

    "My first drop manages to catch him with his army out of position. Perfect."

    stop sound fadeout 1.0
    show showmatch4alt movingtothird with easeinleft:
        xalign -0.1

    "He has to be rushing back to defend against this drop. With that knowledge, I rush a second, smaller force into his third base."

    
    hide showmatch4alt

    hide showmatch4
    play sound "sfx/battle/protossdeathballvsterran.ogg" fadein 1.0
    
    #LAUNCH-TODO
    #reference from top - alpha in subtle
    show showmatch4 attackonthird:
        alpha 0
        yalign 0.5
        xalign 0.5
        easein 0.4 yalign 0.0 alpha 1


    "Tch, he held firm! The second prong of my attack slams right into an overwhelming force. It's too late for me to pull away."

    
    show showmatch4alt deniedharass with easeinright:
        xalign 1.1

    "Agh, that wasn't his entire army?! The damage I managed to inflict wasn't nearly worth the cost of those two forces..."

    stop sound fadeout 1.0
    hide showmatch4alt
    hide showmatch4
    
    show showmatch4 reinforce:
        alpha 0
        ypos 0.2
        xalign 0.5
        easein 0.4 ypos 0.0 alpha 1



    "I'm fine. I'm fine. I'm fine." 
    "I still have a decent army, I just need to contest the center of the map. I can't let him take another base."
    hide showmatch4
    play sound "sfx/battle/protossballstormcollo.ogg" fadein 1.0
    
    show white at flash(.05)
    show white at flash(.18) as white2
    show la at lightning_bolt(1)
    show lb at lightning_bolt(2)
    show lc at lightning_bolt(3)
    #hide white with Dissolve(0.1)

    show bg showmatch4 midfight:
        align(0,0)

    "ARGH! But he's already beat me to the punch! We clash briefly before I order a retreat, frantically reinforcing my wounded army."
    
    show showmatch4alt takethird with easeinright:
        xalign 1.1

    "I can't fall behind. Take more bases, keep my production going!"

    hide showmatch4alt with easeoutright
    stop sound fadeout 1.0
    "C'mon! I've got to deal some damage. If I just sit here and let him power up, he's going to roll me!"

    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    hide white
    show white with Dissolve(0.1):
        align(0,0)


   
    show showmatch4 midfight2:
        align(0,0)
    "Boom! Stalkers! This kind of pick-off is just what I needed!"

    hide white with Dissolve(0.1)

    stop sound fadeout 1.0
    scene bg black with dissolve:
        align(0,0)
    play sound "sfx/battle/medivacloada.ogg" fadein 1.0
    show showmatch4 midescape:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True

    "Shit, he's preparing an assault on my main! Pull back, pull back! I can defend this!"

    stop sound fadeout 1.0
    show showmatch4 midescape:
        yalign 0.35
        easein 0.4 xpos -0.4 alpha 0
    $renpy.pause(0.4)
    hide showmatch4
    show showmatch4 basedefence:
        xalign 1.0 alpha 0
        crop(0,0,450,720)
        easein 0.4 xalign 0.7 alpha 1
    $renpy.pause(0.4)
    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    show showmatch4 basedefence:
        xalign 0.7
        crop(0,0,450,720)
        easein 0.4 crop(0,0,1000,720)

    "Just before his forces arrive, I get in position at the top of my ramp. It's looking even for a while, until..."

    stop sound fadeout 1.0
    show white with Dissolve(0.1):
        align(0,0)


    play sound "sfx/battle/colossusdie.ogg" fadein 1.0
    $ show_protoss_blast()
    show showmatch4 basedefence2

    hide white with Dissolve(0.1)

    "Boom! HAH! This is the type of error a Brood War player makes! The burden to attack was mine, not his."

    stop sound fadeout 1.0
    scene bg black with dissolve:
        align(0,0)

    show showmatch4 medivacdrop:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True


    "This game's tempo is back in my favor, even if I'm still at an economic disadvantage. I need to hit while he's still rebuilding."

    show showmatch4 medivacdrop:
        yalign 0.35 alpha 1.0
        easein 0.2 alpha 0.0 xpos -0.5 subpixel True

    $renpy.pause(0.2)

    hide showmatch4

    show showmatch4 attackfourth:
        xalign 1.1
        crop(350,0,400,720)
        easein 0.4 xalign 0.8 subpixel True
    $renpy.pause(0.4)


    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    show showmatch4 attackfourth:
        xalign 0.8
        easein 0.4 crop(-200,0,1200,720)

    "Gotcha! The mineral line I failed to take down with my previous drop now lies in tatters."

    
    #hide showmatch4
    $ show_tank_blast()
    show white with Dissolve(0.1):
        align(0,0)
    show showmatch4 attackthird:
        xalign 0.4
    hide white with Dissolve(0.2)
    "And this time, my two-pronged attack catches a weak flank defending his third base! I'm pulling him apart!"

    stop sound fadeout 1.0
    play sound "sfx/battle/nexusexploding.ogg" fadein 1.0
    show showmatch4alt fourthexplodes with easeinright:
        xalign 1.1

    "I'm inflicting crushing economic damage. All I need to do is win one more fight."

    
    stop sound fadeout 1.0
    #hide showmatch4alt with easeoutright

    #hide showmatch4 with easeoutright
    
    scene bg showmatch4 econ with dissolve:
        align(0,0)

    "I'm spending my minerals and gas the second I mine it. My production has been on point all game long."

    show showmatch4 fourthsaturated with easeinright:
        xalign 1.1

    "There's absolutely no way this would have been possible without drilling for so many hours."
    hide showmatch4
    scene bg black with dissolve:
        align(0,0)

    show showmatch4 moveout:
        alpha 0
        ypos 0.2
        xalign 0.5
        easein 0.4 ypos 0.0 alpha 1


    "One more fight. Just one more fight! I march across the map and then charge up the ramp at his natural expansion."

    #hide showmatch4 with easeoutright
    $show_tank_blast()
    show white with Dissolve(0.1):
        align(0,0)
    hide showmatch4

    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    hide white with Dissolve(0.1)
    show bg showmatch4 end1  with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8):
        align(0,0)


    "I maneuver out of the way out his psi storms and pound the powerful, expensive units at the back of his army. With them all out of the way, I'm able to power through the rest of his force."



    

    show white with Dissolve(0.1):
        align(0,0)



    scene bg showmatch4 end2:
        align(0,0)

    "Yes! He types out a GG when I punch my way into his main base. The series is even!"
    window hide dissolve
    stop sound fadeout 1.0
    hide white with Dissolve(0.1)
    scene bg booth at center with dissolve
    $ renpy.music.set_volume(.3, 1, channel="MTrack3") 
    window show dissolve
    "My hands shake. The veins in my neck throb. My palms are covered with sweat."
    "My throat is dry. My eyes hurt. And I can't stop bouncing my leg."
    play sound "sfx/slidingdoor.ogg"
    pause .5
    j "Will you calm down? Sheesh."
    show jett neutral3 at center with dissolve
    m "I don't think that's going to be possible."
    show jett unimpressed with dissolve
    j "Tch. Typical amateur jitters. Don't try to ignore that adrenaline you're feeling—use it to your advantage."
    show jett neutral with dissolve
    pause 1.0
    show jett neutral3 with dissolve
    j "What else do you want me to say? You already know what to do."
    m "I don't know. Honestly, I didn't give any thought to how I'd feel if I made it this far. I kinda feel like throwing up, actually."
    show jett smile with dissolve
    j "In that case, just imagine how sick you'll be when you win this thing."
    m "In more ways than one."
    show jett neutral2 with dissolve
    j "Alright, enough chit-chat. Get serious, Mach."
    pause 1.0
    show jett smile with dissolve
    j "Fighting."
    hide jett with dissolve
    window hide dissolve
    stop MTrack3 fadeout 1.0
    $ renpy.music.set_volume(.5, 1, channel="MTrack4") 
label showmatch5:
    scene bg showmatch5 opening with dissolve:
        align(0,0)
    show black at center behind bg
    window show dissolve
    "Stay calm. Just one more."
    "Cross off that checklist. Depots. Rax. Expand."

    scene black at center with dissolve
    show showmatch5 scoutexpo:
        alpha 0
        yalign 0
        easein 0.4 yalign 0.35 alpha 1
    play sound "sfx/battle/singlestalkershoot.ogg"
    "A stalker denies my scout at the front of his natural expansion. Tch, that's frustrating."

    show bg showmatch5 standard with dissolve:
        align(0,0)
    "Without knowing the timing on his second base, it's unsure of how much damage I need to do. When my dropships come out, I need to find a good angle to attack him from. Let's see..."

    #asset scan

    show white with Dissolve(0.1):
        align(0,0)
    hide bg 
    play sound "sfx/battle/scan.ogg" fadein 1.0
    show showmatch5 scan with Dissolve(0.1):
        align(0,0)
    hide white with Dissolve(0.2)
    "... Woah. What? Six gates and a robo this early? How is that possible? That literally isn't possible."


    stop sound fadeout 1.0
    scene bg black with dissolve:
        align(0,0)
    show showmatch5 scout:
        crop(0,0,250,720)
        xalign 1.0 alpha 0
        easein 0.4 xalign 0.4 alpha 1

    $renpy.pause(0.4)

    show showmatch5 scout:
        crop(0,0,250,720)
        xalign 0.4
        easein 0.4 crop(-100,0,900,720)
        
    "But I'm forced to witness the reality of the situation march across the map. His army is ridiculously huge."
    "This is insane. He faked an expansion and intentionally delayed his one-base attack to catch me offguard."
    "I... simply do not have enough units to defend against his army. I won't for another minute, either."
    "By then, the game will be over."
    window hide dissolve
    $ renpy.music.set_volume(0, 1, channel="MTrack4") 
    hide showmatch5

    show showmatch5 allinmovingin:
        alpha 0
        ypos -100
        xalign 0.5
        easein 0.4 ypos 0 alpha 1
    pause 0.8

    #LAUNCH-TODO
    #fade music to low
    #fade away the image to medivacs
    #kick it back it when it zooms back
    $ show_stalker_lasers
    show white with Dissolve(0.1):
        align(0,0)
    play sound "sfx/battle/immortalarmyattack.ogg" fadein 1.0
    show showmatch5 attack1:
        align(0,0)
    hide white with Dissolve(0.2)
    pause 2.0
    stop sound fadeout 1.0

    #music load
    show showmatch5 attack1bw with Dissolve(1.0)
    window show dissolve
    "I'm going to lose."
    $ renpy.music.set_volume(.5, 1, channel="MTrack4") 
    stop sound fadeout 1.0
    hide showmatch5
    
    play sound "sfx/battle/medivacloada.ogg" fadein 1.0
    show showmatch5 medivac at center with Dissolve(.2)
        
    "No! I don't need to take a direct engagement to win against Bolt!"
    "It's time for a base trade."

        
    show showmatch5 medivac:
        easein 0.4 xalign 0.0 alpha 0 subpixel True 

    $renpy.pause(0.3)

    hide showmatch5 with easeoutright
    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    show showmatch5 baserace1:
        yalign .70 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True
    "With my entire army loaded in four dropships, I sprint across the map and unload into his base."
    "Bolt has two options. One: Pull back his army and suffer serious damage in the meantime or, two, rush into my base and do the same as I'm doing to him."
    stop sound fadeout 1.0
    #hide showmatch5 with easeoutright
    ##update sound
    play sound "sfx/battle/immortalattackrocks.ogg" fadein 1.0
    show showmatch5 baserace2:
        xalign 1.0
        yalign 0.4
        crop(0,0,250,720) alpha 0
        easein 0.4 xalign 0.4 alpha 1 
        easein 0.4 crop(0,0,600,720)



    "He opts for number two. Alright. I've been in these kind of situations before. This kind of game is far less about macro, micro, or anything like that. It's all about staying calm and making the right decisions."

    stop sound fadeout 1.0
    #hide showmatch5 with easeoutright

    hide showmatch5
    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    show showmatch5 tossrace:
        crop(0,0,250,720)
        alpha 0
        xalign 0.0
        yalign 0.4
        easein 0.4 xalign 0.4 alpha 1 subpixel True
        easein 0.4 crop(-200,0,1200,720)
    

           
        
    "I'm okay. His army is big, but mine is fast. I just need to focus on hunting his buildings down."

    #hide showmatch5 with easeoutright
    #update sound - sentry stalkers shooting
    stop sound fadeout 1.0
    hide showmatch5
    play sound "sfx/battle/singlestalkershoot.ogg" fadein 1.0
    show showmatch5 fly:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True
        

    "We trade building for building, the remnants of my main base unable to get away from his massive force."

    #hide showmatch5 with easeoutright

    play sound "sfx/battle/MMMprotossbase.ogg" fadein 1.0
    show showmatch5 killpylon with easeinright:
        crop(150,0,250,720)
        easein 0.4 xalign 0.4 subpixel True
        easein 0.4 crop(-200,0,1000,720)

    #LAUNCH-TODO effect

        
    "Found another pylon! If I keep this up, I can put him in an unwinnable situation."
    window hide dissolve
    $ show_protoss_blast()
    play sound "sfx/battle/marineskillpylons.ogg" fadein 1.0

    show showmatch5 pylonexplode with dissolve:
        crop(-200,0,1000,720)
        xalign 0.4
    pause 0.5
    #hide showmatch5 with easeoutright
    hide showmatch5
    show showmatch5 factoryscout:
        xalign 1.0
        crop(0,0,300,720)
        alpha 0
        easein 0.4 xalign 0.5 alpha 1 subpixel True
        easein 0.4 crop(0,0,800,720)
    window show dissolve
    "All he has left is a single pylon, the one he used to reinforce his attack." 


    #hide showmatch5 with easeoutright
    hide showmatch5
    show showmatch5 hidedepot:
        xalign 1.0
        alpha 0
        easein 0.4 alpha 1 xalign 0.5 subpixel True

        
    "Just before my final building bursts in the flames, I throw down a supply depot in a corner of the map guarded by terrain and distance."
    "If he wants to win, he'll have to abandon his final pylon. It's looking like this game might end up as a draw."
    "I'm about to ask if he wants the tie when I notice something in the corner of my eye."
    #hide showmatch5 with easeoutright
    #update sound
    hide showmatch5
    play sound "sfx/battle/immortalattackrocks.ogg" fadein 1.0
    show showmatch5 rocks:
        yalign 0.0 alpha 0
        easein 0.4 yalign 0.4 alpha 1 subpixel True
        
    ".... WOAH. He just pulled a significant part of his army away from his pylon! He's destroying the rock barrier!" 

        
    stop sound fadeout 1.0
    #hide showmatch5 with easeoutright
    
    show showmatch5 movemidmap:
        yalign 0.0 alpha 0
        easein 0.4 yalign 0.4 alpha 1 subpixel True
    "Shit! SHIT! I'm not in position to defend my final building! Not like this, god!"
    "I have to beat him to it. Go. GO!"
    stop MTrack4 fadeout 5.0
    #hide showmatch5 with easeoutright

    window hide dissolve
    show showmatch5 movemidmap:
        easein 0.2 yalign 0.8 alpha 0
    show showmatch5final1 protossmovein:
        crop(150,0,50,0)
        xalign 0.5 alpha 1
        easein 0.2 crop(150,0,50,720)
        easein 0.2 crop(0,0,400,720) subpixel True
        #easein 0.4 crop(0,0,1280,400) subpixel True
    pause 1.0

    show showmatch5final1 protossmovein:
        crop(0,0,400,720) 
        xalign 0.5
        easein 0.1 crop(150,0,50,720)
        easein 0.1 crop(150,0,50,0)
    pause 0.05
    play sound "sfx/battle/stim.ogg"
    show showmatch5final2 final terranmovein:
        yalign 0.5
        crop(0,50,0,50)
        easein 0.2 crop(0,50,1280,50)
        easein 0.2 crop(0,0,1280,400) subpixel True
    pause 1.0
    play sound "sfx/battle/buzzbuzz.ogg"
    show showmatch5final2 final terranmovein:
        yalign 0.5
        crop(0,0,1280,400)
        easein 0.1 crop(0,50,1280,50) subpixel True
        easein 0.1 crop(0,50,0,50) subpixel True
 
    pause .05
    show showmatch5final3 final protossattack:
        crop(150,0,50,0)
        xalign 0.2 alpha 1
        easein 0.2 crop(150,0,50,720)
        easein 0.2 crop(0,0,400,720) subpixel True
    pause 1.0
    show showmatch5final3 final protossattack:
        crop(0,0,400,720)
        xalign 0.2 alpha 1
        easein 0.1 crop(150,0,50,720)
        easein 0.1 crop(150,0,50,0) subpixel True
    pause .05
    play voice "sfx/battle/MMMprotossbase.ogg"
    show showmatch5final4 final terranattack:
        yalign 0.3
        crop(0,50,0,50)
        easein 0.2 crop(0,50,1280,50)
        easein 0.2 crop(0,0,1280,400) subpixel True
    pause 1.0
    stop voice fadeout 1.0
    stop sound fadeout 1.0
    scene black at center with Dissolve(1.0)
    pause 1.0
    #hide showmatch5 with easeoutright

    


    hide showmatch5final1
    hide showmatch5final2
    hide showmatch5final3
    hide showmatch5final4
    show white with Dissolve(0.1):
        align(0,0)
    play sound "sfx/battle/nexusexploding.ogg" fadein 1.0
    $ show_protoss_blast()
    show bg showmatch5 finalexplosion:
        align(0,0)
    hide white with Dissolve(0.2)
    
    pause 2.0
    window hide dissolve
    $ renpy.pause(2.0, hard=True)
    scene black at center with Dissolve(2.0)
    pause 1.0
    stop sound fadeout 1.0
    scene bg booth with dissolve:
        align (0, 0)
    window show dissolve
    
    ############################
    
    "All is slow and silent. My heart thunders against my ribcage. I can feel the blood roaring through my veins."
    play music "sfx/Victory Intro.ogg"
    queue music "sfx/Victory Loop.ogg"
    "A second later, I rip my headphones off and scream in triumph. "

    "This high... I’ve never felt anything like it. All the effort and hardship I’ve poured into the twenty years of my life. This one moment is worth it all."
    play voice "sfx/Slam.ogg"
    show jett pleased at center with Dissolve(.2):
        xpos .35
    "With a thump, Jett bursts through the booth's door and pounds my back with claps between her own cheers."
    show accel neutral behind jett at center with Dissolve(.2):
        xpos .6
    show stunt neutral grin behind jett at left with Dissolve(.2):
        xpos -.1
    show reva smile behind jett at right with Dissolve(.2):
        xpos 1.1
    
    "She’s soon joined by the rest of my team who follow suit, sharing in my victory."

    "{w=1}No, not my victory. Our victory."
    window hide dissolve
    scene bg studio with dissolve:
        align (0, 0)
    window show dissolve
    "With some prodding from Accel, we collect ourselves and step out onto the stage to show our gratitude to the crowd with waves and smiles."

    "But before the VSL hostess can cross the stage for a post-game interview, Bolt emerges from his booth with a macabre expression splattered across his face."
    play music "sfx/Rusted Lightning Intro.ogg"
    queue music "sfx/Rusted Lightning Loop.ogg"
    show rival evil at center with Dissolve(.2)
    "He wrenches the microphone from the hostess' hand and points at me from the other side of the stage."

    b "Savor that win, you piece of shit. It’s the last you’ll ever have against me."

    "The crowd reacts with a mixture of astonishment and encouragement, the latter coming mainly from the fans dressed in Shock T1’s black and white."

    "Emboldened by my failure to respond, he continues."
    show rival annoyed with dissolve
    b "The current StarCraft 2 pro-gamers pool disgraces eSports. I pledge to my fans that I will expose these frauds for what they are."
    show rival bored with Dissolve(.2)
    pause .2
    b "I hereby announce my retirement from Brood War."
    show rival annoyed with dissolve
    b "I am immediately going full-time with StarCraft 2 with the intent to take the VSL Championship on behalf of those that deserve the honor of calling themselves professional gamers."
    play voice "sfx/mic.ogg"
    show white with Dissolve(.05):
        align(0,0)
    show rival bored
    hide white with Dissolve(.2)
    "With that, Bolt slams the microphone against the ground, causing its plastic shell to fracture and a loud screech to emit from the speakers."
    hide rival with Dissolve(.3)
    stop music fadeout 4.0
    play sound "sfx/vocal.ogg." fadein 2.0 loop
    "He stalks off stage and through the players’ exit without another word, trailed by the stares of his fans."
    "Woah. There’s no way that was a part of the KPGA’s plan."
    show stunt neutral grin at center with dissolve
    s "That guy really likes to break electronics, huh? I wonder how many keyboards he’s been through."
    show stunt at right
    show jett casual at left
    with dissolve
    "I share a baffled look with Jett before the VSL hostess picks up what remains of the microphone and steps to my side. My teammates take it as a cue to vacate the stage."
    hide stunt
    hide jett
    with dissolve
    "The post-game interview is short and formal, with half of the crowd completely unresponsive to my attempt to show good sportsmanship."

    "Either they’re on Bolt's side, or they're impatient to see the VSTL get started."
    play voice "sfx/machclap.ogg"
    "Still, a handful of people cheer me off the stage as the studio begins to set up for team league. "

    "Among them is a familiar wisp of grey hair. But when I search for the face to whom it belongs, I don't see who I'm looking for."
    window hide dissolve
    scene bg backstage with dissolve:
        align (0, 0)
    window show dissolve
    show damen neutral at center
    show image "char/jon.png" at left
    show image "char/cam.png" at right
    with dissolve
    "To my utter surprise, a trio of foreigners approach backstage with autograph requests. I oblige them nervously, unfamiliar with how to properly sign the mousepads they hand me."
    show image "char/jon2.png" at left
    show damen smile
    show image "char/cam2.png" at right
    hide image "char/jon.png"
    hide image "char/cam.png"
    with dissolve
    jo "Thanks man!"
    d "Yeah, thanks!"
    ca "You rock!"
    hide image "char/jon2.png"
    hide damen
    hide image "char/cam2.png"
    with dissolve
    "I scratch behind my head when they head off, surprised and humbled."
    stop sound fadeout 1.0
    play music "sfx/Victory Loop.ogg" fadein 4.0
    j  "Not a bad start, Mach."
    show jett smile at center with dissolve
    "I turn to find Jett watching me from across the room. She pushes off the wall and ambles toward me."
    show jett thinking2 with dissolve
    j  "And. Uh. For the record, I’m sorry that I hit you."

    m "It might have been what I needed. There’s no hard feelings."
    show jett considering with dissolve
    j  "It wasn't right. There was probably a better option."

    m "It’s in the past. Seriously."
    show jett smile with dissolve
    "She smiles genuinely, far wider than I've ever seen from her before."

    j  "You’ll make a good teammate."
    play voice "sfx/clap.ogg"
    show jett neutral2 with Dissolve(.2)
    pause .3
    "A sudden clap purges the expression from her face. Just like that, it’s back to the intense Jett that I’m much better acquainted with."

    j  "Alright, enough backpatting. Back to the team, we’ve got places to be."
    show jett neutral3 with dissolve
    "Without bothering to answer my curious look, she rolls her wrist in a beckoning motion and leads me out into the hallway of the VSL studio."
    hide jett with dissolve
    window hide dissolve
    scene bg hallway with Dissolve(1.0):
        align (0,0)
    window show dissolve
    play sound "sfx/vocal.ogg." fadein 2.0 loop
    "It’s crowded, with even more people pouring into the studio in anticipation of the semi-final team league match."

    "But off away from the foot traffic, we find Mr. Kim with Accel, Stunt and Reva."
    show kim neutral at center with dissolve
    "He turns to regard Jett and then me with a smile, restrained in comparison to my teammates."
    show kim confident with dissolve
    k "And the victor arrives. Congratulations, Mach."

    "I lower my head in a bow without taking my eyes off of him."

    m "Thank you."
    show kim neutral with dissolve
    k "I’ll send word for my assistant to publish a press release. The sponsorship should be no surprise given how quickly this type of information spreads, but it should be a nice PR boost for Enoch Red."
    hide kim
    show stunt neutral grin at right:
        xpos .97
    show reva smile at left:
        xpos .03
    with dissolve
    s "{w=.5}... Alright, I’ll admit. That’s a pretty good name."
    hide stunt
    hide reva
    show kim neutral at center 
    with dissolve
    k "Mm. I’ll leave the rest to Jett. I expect great things from you five."
    hide kim with dissolve
    show reva neutral at center
    show stunt neutral at right:
        xpos 1.05
    show jett considering at left:
        xpos -.05
    with dissolve
    "When Mr. Kim turns to leave, Reva, Stunt and I probe Jett with looks."

    m "The rest?"
    show jett casual with dissolve
    j "It’ll be easier for me to show than to explain. C’mon, it’s not far."
    hide reva
    hide stunt
    hide jett
    with dissolve
    pause .1
    show reva neutral at right
    with dissolve
    "I fall in line behind Stunt and Accel after Jett takes off, stepping in time with Reva at my side. She leans towards me with an offered smile."
    show reva glasses with dissolve
    r "Congratulations. You avoided the death penalty."

    m "Yeah. Now instead of dying an instant death, I die a slow one at the hands of a Korean practice regimen."

    r "Oh. In that case, it is not too late."
    show reva smile with dissolve
    "She gently chops the back of my neck. I feign decapitation and then straighten back up to meet her smile."
    window hide dissolve
    jump S36Finale

label S36Finale:
    stop music fadeout 3.0
    stop sound fadeout 3.0
    scene black with squares:
        align(0,0)
    pause 3
    play music "sfx/Full Server Intro.ogg"
    queue music "sfx/Full Server Loop.ogg"
    window show dissolve
    j  "... This one."
    play voice "sfx/fumble.ogg"
    "She tests the key against the lock only to find that it doesn’t fit."

    j  "No, wait. This one."
    play voice "sfx/fumble2.ogg"
    "We retrace our steps back down the apartment building’s hallway to a door we passed earlier. She tries the key and, again, it doesn't fit."
    a "Are we on the wrong floor?"
    j "No! Will you just... Wait. Oh, it's the one across the hall."
    window hide dissolve
    play sound "sfx/doorclose.mp3"
    pause .3
    scene bg house with dissolve:
        align (0, 0)
    window show dissolve
    "This time, the key slides into the lock and then turns, revealing a mostly unfurnished room."

    "It’s small, and it’s not in a great part of town. But I can’t deny the pride welling up inside of me as I step inside, shoulder to shoulder with my teammates."

    "We spread out instinctively, looking over the plain floors and countertops as if we were inspecting a mansion."
    show stunt neutral at left 
    show jett neutral at right
    with dissolve
    s "How'd you get this so quickly?"
    show jett casual with dissolve
    j  "It was a good deal, but they wanted the deposit more than a week ago. Someone else was trying to snatch it out from under us."
    m "You put money down on our team house without knowing whether or not I’d win against Bolt?"
    show jett thinking2 with dissolve
    "Jett dodges the question by glancing away, leaving Accel to swoop in and fill the silence."
    hide jett
    hide stunt
    show reva neutral at left
    show accel confident at right
    with dissolve
    a "Nice having a team that believes in you, eh? That’s not all, by the way."
    show accel neutral with dissolve
    "He gestures towards a lonely cardboard box off in the corner of the room."
    show accel thinking2 with dissolve
    a "Stunt, I think you should have the honor."
    hide jett
    hide accel
    hide reva
    show stunt phone at center
    with dissolve
    "Somehow, Stunt has found the time during this monumental occasion to pull out his phone." 

    "But, as instructed, he makes his way to the corner of the room and peels back the box’s lid." 
    hide stunt with dissolve
    "What follows is a sound of unbridled joy."
    play voice "sfx/explode.ogg"
    s "{size=+15}{fast}HEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLLL YEEEEEEEEEEEEEAAAAAAAAAAAAAH!"
    play voice "sfx/rummage.ogg"
    "He rummages around in the box’s contents before pulling free a red and white jacket."

    "One by one, Stunt practically rips them free and tosses them towards the four of us."
    show image "char/bonus/jacket.png" at center:
        ypos .6 alpha 0.0 xpos .5
        easein .5 ypos .8 alpha 1.0 subpixel True
    play voice "sfx/catch.ogg"
    "I catch mine and, on closer inspection, find the Enoch Red logo on the back."
    show image "char/bonus/jacket.png" at center:
        ypos .8 alpha 1.0 xpos .5
        easeout .5 ypos 1.0 alpha 0.0 subpixel True
    pause .5
    show jett considering at center with dissolve
    "Jett’s expression is too neutral to be authentic. I think it’s simply that she has a hard time admitting that she had faith all along."

    "Knowing that makes me happy, so I have no reason to press her on it."
    play voice "sfx/lurch.ogg"
    show stunt neutral grin at right:
        alpha 0.0 xpos 1.4
        easein .3 alpha 1.0 xpos 1.1 subpixel True
    pause .5
    s "YO! IT’S TIME TO CELEBRATE!"
    play voice "sfx/interupt.ogg"
    show jett angry with Dissolve(.2)
    j  "You got your chance to celebrate a week ago! Now is time to practice."
    "Oh how easily Jett breaks herself out of her quiet trance when the chance to play empress arrives."
    show stunt fist with dissolve
    s "Pft, how? There’s like two PCs here! C’mon, last time before we’re VSL champs. I swear."
    hide stunt
    hide jett
    show reva neutral at left
    show accel neutral at right
    with dissolve
    a "I'm with the kid."
    show reva expected with dissolve
    r "I concur."
    hide reva
    hide accel
    show jett considering at center
    with dissolve
    m "C’mon, Jett. One last time."
    stop music fadeout 3.0
    show jett unimpressed with dissolve
    j  "Accel, you’re supposed to be on my side. And the rest of you are too willful. I’ll break you of it eventually."
    show jett considering with dissolve
    pause 1
    show jett neutral with dissolve
    j  "One. {w=.5}Last. {w=.5}Time."
    play sound "sfx/run.ogg"
    show stunt neutral grin at right:
        alpha 1.0 xpos 1.5
        easein 1 alpha 1.0 xpos -.1 subpixel True
    pause .4
    show jett neutral3 with Dissolve(.2)
    pause .3
    play music "sfx/Blue Pineapple.ogg" fadein 4.0
    "Stunt takes the opportunity to throw on his team jacket and sprint into the hallway, the rest of us quick to follow suit." 
    window hide dissolve
    scene black with squares:
        align (0,0)
    pause 1
    show image "bg/cg5mamach.jpg" at center
    with slowfade
    window show dissolve
    "It's cold. The coldest it’s been since I came to Seoul."

    "But I don’t feel it. I’m warmed by my newfound confidence. By the camaraderie I’ve forged with my teammates."

    "This is everything I have ever wanted. A team, friends, and a goal to work towards."

    "When I take a step back, it seems silly. It’s nothing I could explain to a random person on the street."

    "I beat someone at a video game, I’ve earned a free bunk bed in a tiny apartment, and I’m obligated to work for more than ten hours a day."

    "But I can say with certainty—with the knowledge that I’ve given it my all:"

    "We’re all going to make it."
    if not persistent.beat_game:
        $ persistent.extras_msg = True
    $ persistent.beat_game = True
    window hide dissolve
    stop music fadeout 5.0
    scene black with slowfade:
        align (0,0)
    pause 2.0
    jump endcredits 
    return

##gameend
