# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
## other files
## characters.rpy
# The game starts here.

init:
    $ slowfade = Fade(2, 0, 2)
init:
    $ midfade = Fade(1, 0, 1)
    $_game_menu_screen = "navigation"

init:

    $ timer_range = 0
    $ timer_jump = 0

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

label splashscreen:
    scene black with dissolve:
        align (0,0)
    show image "bg/1111.png" at center:
        alpha 0.0 ypos .95
        easein .5 alpha 1.0 ypos 1.0 subpixel True
    pause 1.5
    show image "bg/1111.png" at center:
        alpha 1.0 ypos 1.0
        easeout .5 alpha 0.0 ypos 1.05 subpixel True
    $renpy.pause(1.0, hard=True)
    show image "bg/workoffiction.jpg" with Dissolve(0.5):
        yalign 0.5
    pause 5.0
    return

label start:              
    jump gamebegins
    
label gamebegins:
    window hide dissolve
    show bg city at center:
        ypos 1.0

    show logosctitle:
        xalign 0.2 alpha 1
        easein 0.2 xalign 0 alpha 0
    show logovntitle:
        xalign 0.2 alpha 1
        linear 0.2 alpha 1
        easein 0.2 xalign 0.4 alpha 0
    show logo2title:
        yalign 0.0 alpha 1
        xalign 0.2
        linear 0.4 alpha 1
        easein 0.2 yalign -0.5 alpha 0

    pause 1.0

    hide logosctitle
    hide logovntitle
    hide logo2title 
    if not persistent.day9:
        "SC2VN - это визуальная новелла о StarCraft в Южной Корее, и людях, которые играют в неё."

        "Эсли вам не знаком eSports или StarCraft,то вы можете посмотреть небольшой озвученный отрывок, который познакомит вас с StarCraft."

        "Или, вы можете посмотреть его позже в Дополнительно и начать сразу читать."
        window hide dissolve
        $persistent.day9 = True
        menu:
            "I want to learn more about StarCraft.":
                jump day9scene
            "I'll watch it later.":
                pass
                
    show malemach:
        crop(0,0,640,720)
        xpos -120
        alpha 0
        easein 0.3 xpos 0 alpha 1

    show femmach:
        crop(640,0,640,720)
        xpos 740
        alpha 0
        easein 0.3 xpos 640 alpha 1

    "In SC2VN, you select the gender of the main character, Mach."
    "The choice will mostly impact how he or she appears. The story differences are minor."
    "Now, select the main character."
    hide malemach
    hide femmach

    jump genderchoice


label genderchoice:
    hide malemach
    hide femmach

    show screen char_select()

    pause

    jump genderchoice


label genderchoiceloop:
    show malemach:
        crop(0,0,640,720)
        xpos -120
        alpha 0
        easein 0.3 xpos 0 alpha 1

    show femmach:
        crop(640,0,640,720)
        xpos 740
        alpha 0
        easein 0.3 xpos 640 alpha 1

    pause 0.2

    jump genderchoice

label femmachchoice:
    hide screen char_select
    show femmach:
        crop(640,0,640,720)
        xpos 640
        alpha 1
        easein 0.3 xpos 200 alpha 1
    "Begin the story as the female main character?"

    menu:
        "Yes, I want to play as the female main character.":
            hide femmach with dissolve
            jump fcityfade
        "No, I want to rethink my choice.":
            hide femmach with Dissolve(0.2)
            jump genderchoiceloop


label malemachchoice:
    hide screen char_select
    show malemach:
        crop(0,0,640,720)
        xpos 0
        alpha 1
        easein 0.3 xpos 400
    "Begin the story as the male main character?"
    menu:
        "Yes, I want to play as the male main character.":
            hide malemach with dissolve
            jump mcityfade
        "No, I want to rethink my choice.":
            hide malemach with Dissolve(0.2)
            jump genderchoiceloop

label mcityfade: 
    stop music fadeout 4.0
    show bg city at center:
        easeout 4.0 ypos 1.52 subpixel True
    $renpy.pause (1, hard=True)
    show black with Dissolve(2.0):
        align (0,0)
    jump S1studioQualifier

label fcityfade: 
    stop music fadeout 4.0
    show bg city at center:
        easeout 4.0 ypos 1.52 subpixel True
    $renpy.pause (1, hard=True)
    show black with Dissolve(2.0):
        align (0,0)
    jump FeMachOpening

label day9scene:
    hide screen main_menu
    #show screen show_enc_button  
    scene bg black with Dissolve(1.0):
        align (0,0)
    play music "sfx/Eighty A.ogg" fadein 1.0
    queue music "sfx/Eighty B.ogg"
    $ renpy.music.set_volume(.3, .5, channel="music") 
    scene bg stage:
        align (0, 0)
    show timmy sad at right:
        ypos .75 xpos .95
    with Dissolve(3.0)
    window show dissolve
    play sound "sfx/day1.ogg"
    timmy".... Hhhhhhhhhhhhhhhh."
    show day neutral at left:
        xpos -.2 ypos .75
        parallel:
            linear 1.0 xpos .05
        parallel:
            block:                
                linear .15 ypos .77
                linear .15 ypos .73
                repeat  

    $ renpy.pause(1)
    show day happy at left:
        xpos .05 ypos .757
    $ renpy.pause(.3)
    play sound "sfx/day2.ogg"
    day9 "Hey Timmy! Long time no see. How's it going?"
    play sound "sfx/day3.ogg"
    show timmy think
    timmy "Oh, hey Day9... Not too good."
    show day hmm
    play sound "sfx/day4.ogg"
    day9 "Aww, why so glum dude? What's up?"
    play sound "sfx/day5.ogg"
    timmy "Well, I wanna play this super neat new game, it's called SC2VN. But I don't know that much about StarCraft. I'm afraid a bunch of stuff is just going to go over my head."
    show day neutral
    play sound "sfx/day6.ogg"
    day9 "Aww, don't get down on yourself Timmy. How about I help you out on some background info? That way, you won't feel so lost."
    show timmy happy
    play sound "sfx/day7.ogg"
    timmy "Wow, really...? Thanks Day9, you're the best!"
    show day happy
    play sound "sfx/day8.ogg"
    day9 "No problem Timmy! So, what would you like to know?"
    show timmy neutral
    play sound "sfx/day9.ogg"
    timmy "Okay, well, what were the earliest days of StarCraft like in Korea?"
    show day eyebrow
    play sound "sfx/day10.ogg"
    show image "char/bonus/ChalkSuit.png" at center behind day, timmy
    day9 "Oh you mean the days when players dressed up in spacesuits and played in tiny studios with fog machines?"
    show timmy surprised
    play sound "sfx/day11.ogg"
    timmy "Aaaaww that sounds sooooo cooooool...!"
    show day hmm
    play sound "sfx/day12.ogg"
    day9 "Okay hold on, we're getting a little ahead of ourselves. Don't you need me to tell you what StarCraft actually is?"
    show timmy sad
    play sound "sfx/day13.ogg"
    timmy "Please Day9, I'm not that bad. What kind of person downloads visual novels about StarCraft without knowing that it’s a popular real time strategy game made by Blizzard?"
    show day neutral
    play sound "sfx/day14.ogg"
    day9 "Well Timmy, in the off-chance that this is a recording designed for complete newbies to eavesdrop upon, how about I go over a few basics?"
    play sound "sfx/day15.ogg"
    show timmy think
    timmy "Guhhh, fine....."
    show day instruct
    show timmy neutral
    play sound "sfx/day161.ogg"
    hide image "char/bonus/ChalkSuit.png"
    show image "char/bonus/toi.jpg" at center:
        ypos .43
    day9 "Like you said Timmy, StarCraft is a highly competitive game. Rather than the black and white of chess pieces, players choose between three different races, each with its own advantages and playstyles."
    play sound "sfx/day162.ogg"
    hide image "char/bonus/toi.jpg" at center
    show image "char/bonus/races.png" at center:
    show day animated
    day9 "The powerful, enigmatic protoss. The scrappy, efficient terran. Or the swarmy, insect-like zerg. For fifteen years StarCraft has been played professionally in South Korea."
    play sound "sfx/day17.ogg"
    show timmy surprised
    show day neutral
    timmy "Wow, really? You mean... people can play video games for a living?"
    play sound "sfx/day18.ogg"
    show day happy
    day9 "That’s right Timmy! Corporate sponsors fund teams for millions of dollars just like any other sport, and the players compete in televised tournaments for cash prizes in events known as StarLeagues. eSports is the real deal!"
    play sound "sfx/day19.ogg"
    show timmy neutral
    timmy "And people actually tune into the tournaments? They watch StarCraft on TV?"
    play sound "sfx/day20.ogg"
    show timmy surprised
    timmy "I can't believe it!"
    play sound "sfx/day21.ogg"
    show day instruct
    show timmy neutral
    hide image "char/bonus/races.png" at center
    show image "char/bonus/ChalkGirl.png" at center
    day9 "Believe it, Timmy! Those television broadcasts helped expose StarCraft to non-gamers, and fans began to follow eSports not only because they played the game themselves, but because they could get invested in the players, personalities, rivalries, the storylines!"
    play sound "sfx/day22.ogg"
    show timmy sad
    show day neutral
    hide image "char/bonus/esports.jpg" at center
    timmy "I guess that makes sense. So, eSports became popular in Korea in the early 2000s... But what was happening everywhere else in the world?"
    play sound "sfx/day23.ogg"
    show day eyebrow
    show timmy neutral
    day9 "Well StarCraft was certainly successful in the West, with a ton of great competitors existing from all over the world."
    play sound "sfx/day24.ogg"
    show day hmm
    day9 "But, StarCraft didn't really catch on as a televised eSport anywhere else."
    play sound "sfx/day25.ogg"
    show day neutral
    day9 "So as a result, the Korean players, with their professional training and their televised tournaments were head and shoulders above everyone else."
    play sound "sfx/day26.ogg"
    show timmy sad
    timmy "Well okay, the Koreans were better in Starcraft 1 {i}(Brood War){/i}. But wasn't everyone on an even playing field when StarCraft 2 came out?"
    play sound "sfx/day271.ogg"
    show day instruct
    show timmy neutral
    day9 "Well at first yeah, but you have to remember that Korea already had an infrastructure for televised eSports. They simply rolled that same regimented practice schedule over to StarCraft 2."
    play sound "sfx/day272.ogg"
    show day eyebrow
    day9 "And even though everyone started the same, quickly, Korea left the rest of the world in the dust."
    play sound "sfx/day28.ogg"
    show day hmm
    day9 "Only a handful of non-Korean players have been able to put up a challenge. Nothing really compares to the Korean team house."
    play sound "sfx/day29.ogg"
    show timmy surprised
    timmy "What's a team house?"
    play sound "sfx/day30.ogg"
    show day eyebrow
    day9 "C'mon Timmy, you can figure this one out."
    play sound "sfx/day31.ogg"
    show timmy think
    timmy "Uhhhhhnnmmmmm?????"
    play sound "sfx/day321.ogg"
    show day happy
    hide image "char/bonus/ChalkGirl.png"
    show image "char/bonus/ChalkHouse.png" at center
    day9 "A for effort Timmy! It's pretty much what it sounds like. A team house is both living quarters and a practice environment."
    play sound "sfx/day322.ogg"
    show day instruct
    show timmy neutral
    hide image "char/bonus/ChalkHouse.png" at center
    show image "char/bonus/ChalkCoach.png" at center
    day9 "Coaches and managers add structure to a daily schedule, they match you up against practice partners in a way that's more productive to you. And because everyone lives together..."
    play sound "sfx/day323.ogg"
    show image "char/bonus/ChalkHouse.png" at center
    hide image "char/bonus/ChalkCoach.png" at center
    show day animated
    day9 "... they're talking strategy all the time. It's pretty much unanimously agreed upon that Korea is the place to be to get better at StarCraft."
    play sound "sfx/day324.ogg"
    show day instruct
    hide image "char/bonus/ChalkHouse.png"
    show image "char/bonus/drewbie.jpg" at center:
        ypos .43
    day9 "As a result, western pros head abroad to train or bootcamp pretty regularly."
    play sound "sfx/day33.ogg"
    show timmy happy
    show day neutral
    hide image "char/bonus/drewbie.jpg" at center
    timmy "Wow. I feel so enlightened! All of this knowledge......!"
    play sound "sfx/day34.ogg"
    show day happy
    day9 "Thrilled to be of service Timmy. Anything else I can assist with?"
    play sound "sfx/day35.ogg"
    show timmy neutral
    timmy "Yeah I think covers everything Mr. Nine. Now I can read SC2VN without googling every five minutes! Thanks for helping me out. I super, duper appreciate it."
    play sound "sfx/day36.ogg"
    show day neutral
    day9 "Totally."
    play sound "sfx/day37.ogg"
    show timmy happy
    timmy "Anyways, I'll see you later! Thanks again!"
    play sound "sfx/day38.ogg"
    show day happy
    day9 "Good luck Timmy! And try not to get a bad ending!"
    window hide dissolve
    $persistent.day9 = True
    stop music fadeout 2.0
    stop sound
    show black with slowfade:
        align (0, 0)
return
label backerscene:
    show black with Dissolve(2.0):
        align (0,0)
    play music "sfx/Blue Pineapple.ogg" fadein 2.0
    scene bg pcbang:
        align (0, 0)
show jon neutral at center
show cam thinking at left:
    xpos -.06
show damen neutral at right:
    xpos 1.09
with Dissolve(2.0)
window show dissolve
ca "Can you believe this? Relegated to a scene in the extras… I didn’t back the project for this!"
show damen calm with Dissolve(.2)
d "Calm down. We got a cameo in the main game, didn't we?"
show cam intense with Dissolve(.2)
ca "FOR LIKE LITERALLY TWO SECONDS. I wanted them to go deep into my life and backstory! What makes me tick? What’s my motivation?!"
show jon shrug with dissolve
jo "So this is going to be one of those extra scenes… Well let’s make the most of it. What’s the story excuse for us to be here anyway?"
show damen phone with Dissolve(.2)
d "We won a contest hosted by the VSL. It includes an all-expenses paid trip to the VSL Finals and a voucher for a free day at a hot spring just outside of Seoul."
show jon neutral with Dissolve(.2)
jo "Wait, give me that. That kind of pandering isn’t in the budget. Besides, this isn’t an otome game."
show damen calm with Dissolve(.2)
d "Five out of the seven characters are male, not including us or Mach. Are you sure about that?"
show jon shrug with Dissolve(.2)
jo "Well, it’s certainly not a BL game. And that’s a decent ratio for eSports!"
show cam thinking with Dissolve(.2)
ca "Reva isn’t brave enough to go outdoors unless it’s for StarCraft, which leaves us with Jett for OVA-style hijinks..."
window hide dissolve
stop music fadeout 2.0
scene white with Dissolve(2.0, hard=True):
    align(0,0)
play music "sfx/spring.ogg" fadein 1.0
$renpy.pause (1, hard=True)
show spring:
    align(0,0)
show jettoutline:
    align(0,0)
show steamsmall:
    align(0,0)
show steamsmall2:
    align(0,0)
show steamsmall3:
    align(0,0)
show steambig:
    align(0,0)
    linear 2 xpos -.5 subpixel True
show foreground:
    align(0,0)
with Dissolve(3.0, hard=True)
$renpy.pause (.5, hard=True)
play sound "sfx/scary.mp3"
$renpy.pause (.5, hard=True)
hide steamsmall
hide steamsmall2
with Dissolve(1.0)
stop music fadeout 2.0
hide steamsmall3
with Dissolve(1.4)
hide steambig
hide jettoutline
with Dissolve(.2)
$renpy.pause (1, hard=True)
scene white with Dissolve(.05):
    align (0,0)
play sound "sfx/spine.ogg"
scene black with dissolve:
    align (0,0)
pause .3
show white with Dissolve(.05):
    align (0,0)
play sound "sfx/spine.ogg"
hide white with Dissolve(.4)
show white with Dissolve(.05):
    align (0,0)
play sound "sfx/spine.ogg"
hide white with Dissolve(.4)
pause 1
play music "sfx/Blue Pineapple.ogg" fadein 2.0
scene bg pcbang:
        align (0, 0)
show jon neutral at center
show cam smile at left:
    xpos -.06
show damen calm at right:
    xpos 1.09
with dissolve
window show dissolve
ca "We would die for sure."
show damen phone with Dissolve(.2)
d "According to canon sources, she can throw a shot glass at 85 mph."
show jon shrug with Dissolve(.2)
jo "That’s before the hydralisk range buff, too. Dangerous. Very dangerous. Attempting a run-by would be a mistake."
show cam neutral with Dissolve(.2)
ca "Fine then, no hot springs. How are we going to spend our time then?"
show jon neutral with Dissolve(.2)
jo "There’s plenty of things we can do! We can go to Seoul Tower, on a hike, to a k-pop concert… What’s with that look?"
show damen calm with Dissolve(.2)
d "The budget. We can only go to places that are in the main story."
show cam intense with Dissolve(.2)
ca "Agh! Those cheapskates! Forget StarCraft, this is the actual ded gaem!"
show jon smile with Dissolve(.2)
jo "Would you rather them have cut your expressions and poses down to pay for us to sightsee?"
show cam thinking with Dissolve(.2)
ca "Hm. Good point. I value my emotions."
jo "Then c’mon. Let’s go find something to do."
show bg cafe:
    align (0,0)
show damen neutral 
with fade
d "The Golden Zonefire lounge. Do PC bangs typically have lounge areas?"
show jon neutral with Dissolve(.2)
jo "I don’t think so. But it would be too repetitive to show only the area with computers, don’t you think?"
show cam neutral with Dissolve(.2)
ca "Also, the keyboard sounds get annoying after so long. I think sacrificing realism was a good trade off."
show damen phone with Dissolve(.2)
d "It says here that the team was originally supposed to hang out at a coffee shop."
show cam intense with Dissolve(.2)
ca "Pft. Hipsters."
show jon shrug with Dissolve(.2)
jo "A PC bang lounge is more fitting for a bunch of pro-gamers. But they won’t get to spend much time here in the future since they’ll be slaves of Jett’s team house."
show cam thinking with Dissolve(.2)
ca "The sequel will be very exciting. It will feature 20,000 StarCraft scenes, a dishwashing minigame, and a single match in the VSL round of 32. Try to avoid the wrist surgery bad ending."
jo "Please don’t get people’s hopes up like that…"
show cam intense with Dissolve(.2)
ca "What, don’t tell me that there won’t be a sequel?! #BrokenPromises!"
show damen smile with Dissolve(.2)
d "It is probably too early to tell without knowing the reception. It also depends on whether or not the game goes on Steam."
show cam thinking with Dissolve(.2)
ca "Oh. That explains the picture of the Pudge."
show jon neutral with Dissolve(.2)
jo "Wait one moment. Do you see that object on the table there?"
hide jon
hide cam
hide damen
with Dissolve(.1)
show bg cafe:
    easein 1.0 zoom 4.0 ypos -2.1 xpos -.9 subpixel True
pause 1
ca "A reminder that cigarettes exist! No! Now the game is going to be rated T for terrible, terrible influences."
play voice "sfx/nope.ogg"
show image "char/bonus/censor.jpg":
    xpos .3 ypos .467
pause .8
jo "Well, it can’t be helped. There’s not much else to be said of this place, so let’s continue."
scene bg cafe:
    align(0,0)
show jon neutral at center
show cam neutral at left:
    xpos -.06
show damen phone at right:
    xpos 1.09
with dissolve
d "Before we go, there’s an anecdote here. Do you remember how Jett asked who Mach was by saying: ‘Name?’"
show damen smile with Dissolve(.2)
d "That exact thing happened to the writer at the open bracket of a major tournament. I have a special note that says: ‘Caliber is an S rank bully, please unfollow him on Twitter.’"
show jon smile with Dissolve(.2)
jo "Brutal."
show bg streetside:
    align (0, 0)
show jon neutral
with fade
jo "Hm. Where to next?"
show cam intense with Dissolve(.2)
ca "Wait, we can admire our surroundings a bit. Look at the Korean on the signs! Wow, amazing. I wonder who performed the incredible feat of coming up with the characters?"
show damen calm with Dissolve(.2)
d "There is a high likelihood that one these signs has an error."
show cam thinking with Dissolve(.2)
ca "Ha. Ha. Well, you know…"
show damen neutral with Dissolve(.2)
d "And while we're on the topic of inaccuracies, Korean players are most often referred to by their real names instead of their handles as is typical in the Western scene."
show cam neutral with Dissolve(.2)
ca "That one was intentional! Please, the team tried their best..."
show damen:
    linear .1 xpos .97
show jon shrug with Dissolve(.2)
jo "Hey, would that coffee shop you mentioned have been Cafe Latte? I could go for drink right now. A shame that we can’t go inside."
show damen smile with Dissolve(.2):
    xpos 1.09
d "Look up. It appears that *onster has its own building in Seoul. Perhaps you can try there?"
ca "Wow, the EG sponsorship really must have paid off! I wonder who runs the office?"
hide jon
hide damen
hide cam
with Dissolve(.2)
window hide dissolve
stop music fadeout 2.0
show bg streetside:
    easein 1.0 zoom 4.0 xpos -1.2
show bg boardroom with Dissolve(2.0):
    align (0, 0) zoom 2.5 ypos -.5
show image "char/datgeoff.png" at right:
    alpha 0.0 xpos 1.5 ypos 1.1
    easein 8.0 xpos 1.18 alpha 1.0
play music "sfx/judgement.ogg"
$ renpy.pause(7.0, hard=True)
show image "char/keikaku.png" at center with Dissolve(2.0):
    ypos .6 xpos .4
$ renpy.pause(2.0, hard=True)
stop music fadeout .5
$ renpy.pause(.5)
hide bg streetside2
play music "sfx/Blue Pineapple.ogg" fadein 2.0
show bg streetside:
    align (0,0)
hide image "char/datgeoff.png"
hide image "char/keikaku.png"
show jon smile at center
show cam neutral at left:
    xpos -.06
show damen calm at right:
    xpos 1.09
with Dissolve(1.0)
window show dissolve
jo "Who knows? Well, let’s go take a look at Stomping Grounds. We’ve been away from computers for too long as is."
d "Gaming addiction is a very serious problem in South Korea. Be careful with those jokes, unless you want to undergo shock therapy."
scene bg streetside2:
    align (0, 0)
show jon neutral at center
show cam neutral at left:
    xpos -.06
show damen calm at right:
    xpos 1.09
with fade
ca "Ooh, street food. Are you guys hungry?"
show damen:
    linear .1 xpos .88
show jon neutral:
    linear .1 xpos .4
jo "That looks like a Tornado Potato. An intense food with a name to match."
show damen smile with Dissolve(.2)
d "It would not surprise me to learn of a pro-gamer with that as his handle."
show cam smile with Dissolve(.2)
ca "If we’re going for realism, it would be more like TorNado_potAtO. Maybe one is the team name and the other is the handle."
show jon shrug with Dissolve(.2)
jo "There’s a pro-gamer who once had a tomato haircut. It was possibly the only hairstyle more gaudy than Stunt’s. Google it, I'm serious."
show cam intense with Dissolve(.2)
ca "We will need to get a confirmation on that from StarCraft's official hair authority before passing judgment."
show damen calm with Dissolve(.2)
d "... Clearly, this background has weak material for jokes. We should escape it as soon as possible."
show bg darkpcbang:
    align (0, 0)
show damen phone:
    xpos 1.09
show cam neutral
show jon neutral at center
with fade
d "Stomping Grounds. Also known as the PC bang that Stunt’s mom runs. He’s the hero of the cafe until he’s defeated and captured by Mach."
show cam intense with Dissolve(.2)
ca "Lucky for him that this isn’t a *ance game. Gahahaha!"
show jon shrug with Dissolve(.2)
jo "Hero to a bunch of middle schoolers, at least. How old is Stunt anyway?"
show damen neutral with Dissolve(.2)
d "Sixteen. But that makes him fifteen by our standards. Korean age is slightly different."
show cam thinking with Dissolve(.2)
ca "... Hm… Something seems off."
show jon neutral with Dissolve(.2)
jo "What is it?"
hide damen
hide jon
hide cam
show bg darkpcbang:
    linear .3 zoom 1.4 xpos -.36
pause .3
ca "Why are they advertising for the VSL? If it was just a little poster I would understand, but that thing on the right covers the entire wall."
scene bg darkpcbang at center:
    zoom 1.0
show damen phone at right:
    xpos 1.09
show cam neutral at left:
    xpos -.06
show jon neutral at center
with dissolve

d "Oh. It says here that this was originally the background for the qualifier area. You know, the opening shot where Mach whines about losing?"
show damen smile with Dissolve(.2)
d "But there was only one scene there, so they repurposed it to be a second PC bang."
show cam intense with Dissolve(.2)
ca "What?! That’s lazy!"
stuntmom "HEY! Don’t speak badly of my establishment!"
show cam thinking with Dissolve(.2)
ca "Ah! S-Sorry, Mrs. Stunt…"
show jon shrug with Dissolve(.2)
jo "Hm. Do you think that there's a Mr. Stunt?"
show damen calm with Dissolve(.2)
d "If there is, he has a troubled relationship with his family. Maybe he’s always overseas, or maybe he’s just a deadbeat."
show jon smile with Dissolve(.2)
jo "Oh, poor Stunt. No wonder why he’s such a twerp. No male role models."
show image "bg/bonus scene.jpg" at center:
    ypos .6 xpos .5
show damen smile with Dissolve(.2)
d "He could have had it a lot worse on the female Mach route if this were a certain type of doujin."
show cam smile with Dissolve(.2)
ca "... P-Please. This isn't one of those kind of games. Let's not go there."
hide image "bg/bonus scene.jpg"
show jon shrug with Dissolve(.2)
jo "Hm. I find this place is more aesthetically appealing than Golden Zonefire. Why couldn’t Stomping Grounds have been the main cafe?"
show damen neutral with Dissolve(.2)
d "Because then the game would be too dark. This story is about StarCraft, not Diablo."
show jon neutral with Dissolve(.2)
jo "You have a point…"
show damen phone with Dissolve(.2)
d "In reality, most PC bangs have low light like this. It helps ease eye strain and makes it easier to hide from your parents when you haven’t returned home for four days."
show cam thinking with Dissolve(.2)
ca "When you say it so matter-of-factly, I get the impression that you know from experience."
show damen neutral with Dissolve(.2)
d "Don’t haze me. We must save our efforts for the cast of the main story."
show cam intense with Dissolve(.2)
ca "You’re right! We can’t bother with infighting when our spotlight is so brief. This scenario is already 40 percent done!"
show jon shrug with Dissolve(.2)
jo "Good point. Who should we bully next?"
show cam thinking with Dissolve(.2)
ca "Mr. Yeon’s store is pretty close…" 
show cam neutral with Dissolve(.2)
ca "Wait, what’s with the look?"
show jon shrug with Dissolve(.2)
jo "We can’t antagonize an old man! We’ll show up on the news as an example of the negative influence that foreigners have in Korea."
show damen calm with Dissolve(.2)
d "Mr. Yeon lives a respectable, ascetic lifestyle. There’s no way that he has any regrets about working long past the age of retirement. He said so himself, so it must be true."
show cam thinking with Dissolve(.2)
ca "Ergh, now I feel bad. Please, to people that ship characters, leave Mr. Yeon alone. His life is hard enough already."
show damen smile with Dissolve(.2)
d "There’s another minor character we can bother. C'mon."
scene black with fade:
    align (0,0)
#elevator ding
jo "Hmm, what do you think it is that Enoch Group does?"
d "The main story implies that Mr. Kim’s explanation is vague because he assumes that Mach is an idiot. While he does actually think that, Mr. Kim was also not being completely forthright."
play sound "sfx/bell.mp3"
pause .5
s "Ehh, excuse me! You can’t just…!"
scene bg boardroom:
    align (0, 0)
show damen neutral at right:
    xpos 1.09
show cam neutral at left:
    xpos -.06
show jon neutral at center
with fade
ca "Damn! He’s not here. Well, it makes it easier to talk behind his back at least. So, what are the details on Mr. Skinny-Tie?"
show damen phone with Dissolve(.2)
d "Well, don’t you find it somewhat suspicious that he was trying to sponsor a team out of nowhere? And his wording at certain times too was particularly ominous."
show cam thinking with Dissolve(.2)
ca "Wait… Don’t tell me..."
show damen neutral with Dissolve(.2)
d "Yes, it’s true. Mr. Kim will pressure Jett to match fix."
show jon shrug with Dissolve(.2)
jo "That's a huge spoiler for the next game! You just ruined more sequel potential, you monster!"
show damen calm with Dissolve(.2)
d "The hints were there, I merely pointed them out. It’s just a theory of mine, anyway…"
show cam intense with Dissolve(.2)
ca "What a bastard! Mr. Kim is killing eSports! Do you think that he’s the one that *KP got involved with?"
show damen smile with Dissolve(.2)
d "The Kong is guilty until proven innocent, apparently."
show jon neutral with Dissolve(.2)
jo "Well, putting that aside. How do you think that Jett would react to the pressure?"
show cam thinking with Dissolve(.2)
ca "She’s too honorable give up her dignity for a few bucks. She’d get a job at Enoch to help support the team before throwing matches! I guarantee it."
show jon smile with Dissolve(.2)
jo "Hmm, businesswoman Jett. The concept is undeniably appealing."
show damen neutral with Dissolve(.2)
d "Holding a clipboard, asking in a patient yet firm voice where the TPS reports are..." 
show cam smile with Dissolve(.2)
ca "This is the ideal moment for more fanservice. Sadly, we must use our imaginations instead. A crushing moment of defeat for everyone involved."
show damen calm with Dissolve(.2)
d "We should escape this building before the Enoch secretary calls security on us."
show cam intense with Dissolve(.2)
ca "That’s probably a good idea. Let’s go and and see Mach’s apartment."
show jon shrug with Dissolve(.2)
jo "People might get the wrong idea about our intentions, though."
show cam smile with Dissolve(.2)
ca "Psh, it’s fine! There’s no jail background in this game, so we’re safe."
show bg apartmentday:
    align (0, 0)
show damen neutral at right:
    xpos 1.09
show cam neutral at left:
    xpos -.06
show jon neutral at center
with fade
jo "Isn’t it a little bit strange that both female and male Mach have the same kind of room?"
show cam thinking with Dissolve(.2)
ca "Come on. There’s plenty to complain about when it comes to cut corners, but that’s a bit of a stretch. It’s not like there’s underwear lying on the floor or something."
show damen smile with Dissolve(.2)
d "Do a better job of hiding the disappointment in your voice next time."
show jon shrug with Dissolve(.2)
jo "Who do you think that picture is of in the bookshelf there?"
hide jon
hide damen
hide cam
show bg apartmentday:
    linear .5 zoom 2.1 ypos -.4
pause .5
d "Hm. It says here that it was a photo of Mach’s parents at one point, but that was before the relationship with them was changed in the script. Now, it’s a picture of Zyzz."
jo "That seems less of a strangely fitting role model for a pro-gamer and more of something made up on the spot for the sake of a joke. "
jo "... I’ll try not to judge too harshly."
d "Additionally, that poster in the background was supposed to be a generic kpop-styled poster. The producer had in mind a girl’s group, but instead they got a solo artist."
ca "Ah, Mach. Such pedestrian tastes… I was hoping he’d appreciate a YG aesthetic."
show bg apartmentday at center:
    zoom 1.0
show damen neutral at right:
    xpos 1.09
show cam neutral at left:
    xpos -.06
show jon neutral at center
with dissolve
d "Hold on, let’s skip ahead a bit."
show bg apartmentnight with dissolve:
    align (0, 0)
show cam thinking with Dissolve(.2)
ca "How did you do that? And wait… The clock in the background didn’t change! It’s still 9:38."
show jon shrug with Dissolve(.2)
jo "Time must stand still in this room. It’s only the light from outside that changes."
show damen phone with Dissolve(.2)
d "This is the writer’s favorite background. A stark contrast from the PC bang which was the producer’s favorite."
show cam intense with Dissolve(.2)
ca " A dark and lonely room vs. a bright and social one, both as places to play StarCraft. The difference in personalities is clear."
show jon smile with Dissolve(.2)
jo "It’s pretty small here, but considering the location it’s not so bad. Better than Reva’s goshiwon, at least."
show cam thinking with Dissolve(.2)
ca "What’s the deal with Reva, anyway? She's like the child of Rei and IdrA."
show damen neutral with Dissolve(.2)
d "She grew up in a rural part of Korea with a computer as her only friend. She ranks as the poorest person on the team."
show jon neutral with Dissolve(.2)
jo "Oh, that’s sad. Perhaps we should avoid making jokes at her expense."
show damen smile with Dissolve(.2)
d "Reva is also the only person on the team who has a happy, stress free relationship with her parents. They support her pro-gamer goals fully, even though they don’t understand eSports."
show cam intense with Dissolve(.2)
ca "Gah! Ignorant bumpkins and their love of their only child… All pro-gamers should share the story of Doublelift."
show jon shrug with Dissolve(.2)
jo "I don’t understand her obsession with mech though."
show damen neutral with Dissolve(.2)
d "It’s a strategy that suits Reva’s personality quite well. She and Artosis should work together to defend the sanctity of tank lines and double armories."
show cam smile with Dissolve(.2)
ca "Oh, will she also switch to a card game for children in the sequel?"
show jon smile with Dissolve(.2)
jo "Cruel… So cruel..."
show bg streetnight:
    align (0, 0)
show jon neutral
show cam neutral
with fade
show damen smile with Dissolve(.2)
d "The entrance to Namdan Park is across the street on the left. Do you think that most people caught that on their own?"
show jon shrug with Dissolve(.2)
jo "Maybe. From the park you can see Mach’s apartment building as well. Too bad that the VSL studio is too far away to see from here."
show cam smile with Dissolve(.2)
ca "Wasn’t the actual GSL studio in on the top floor of a middle school at one point? Stunt should have a ton of fans show up to his matches!"
show bg studio:
    align (0, 0)
show jon neutral
show cam neutral
show damen neutral
with fade
jo "Back already. This area is probably the one closest to a real location, that being the GSL studio before they moved to Gangnam."
show cam thinking with Dissolve(.2)
ca "Mm. The booth designs give it away, even if the lighting and logo is slightly different."
show damen phone with Dissolve(.2)
d "This is where all of the regular season games are played throughout the VSL. Around fifty people can fit comfortably in here."
show jon shrug with Dissolve(.2)
jo "There are four booths not because of a 2v2 league, but so that players can adjust their settings and set-up while a game is ongoing. Keeps things rolling or whatever."
show cam intense with Dissolve(.2)
ca "Tch, but where are the casters! The crowd?! I’m all Ready to Roar!"
show jon smile with Dissolve(.2)
jo "Ready or Not!"
show damen smile with Dissolve(.2)
d "Ready to Giv-- {w=.5}{nw}"
show damen calm
extend "Hm, no. I will maintain my composure."
show cam neutral with Dissolve(.2)
ca "If the devs were brave, they’d have put the song in the game instead of some random alt. Cowards."
show jon shrug with Dissolve(.2)
jo "Please, the nostalgia pandering is already close to maximum."
show damen neutral with Dissolve(.2)
d "At this rate, our scene will be far too opaque for the weebs who have been conned into reading this far and don’t know anything about StarCraft."
show jon smile with Dissolve(.2)
jo "Those fans have our appreciation for sticking it out this long! Maybe we should do something to reward their patience?"
show cam intense with Dissolve(.2)
ca "What! They already got a scene with Day9! What a waste, if they don’t know StarCraft they wouldn’t even know who he is! Such a squandered opportunity. The devs should have conned him into saying some absolutely EPIC memes."
#enig-fucking-assholes named protoss, fuck those dudes man
stop music
show day bonus at right:
    xpos 1.2 ypos .8
    easein .5 xpos 1.0 subpixel True
pause .5
play voice "sfx/assholes.ogg"
$ renpy.pause(5)
show cam thinking with Dissolve(.2)
ca "Woah, speak of the devil. Really laying your cards out on the table there, aren’t you Mr. Nine?"
play sound "sfx/flight.ogg"
pause .4
show image "char/cat.png" at left:
    ypos .8 xpos -.2
    linear .3 xpos 1.2 subpixel True
pause .2
show day:
    linear .05 xpos 1.2 subpixel True
play voice "sfx/claws.ogg"
queue sound "sfx/fight scene.ogg"
queue voice "sfx/rip.ogg"
$ renpy.pause(11)
#attacked by cat, death SFX, oh god sheriff get your claws out of me
show cam thinking with Dissolve(.2)
ca "... And now we know what race his cat plays."
play music "sfx/Blue Pineapple.ogg"
show jon shrug with Dissolve(.2)
jo "Uh. Where were we again?"
show damen smile with Dissolve(.2)
d "Helping out the newbies. Let’s start with the term dishwasher. That sounds like a nonsense insult to an outsider, doesn’t it?"
show jon smile with Dissolve(.2)
jo "I’ve got this one! It’s simple. There are chores to be done in the team house which generally fall to the B-teamers. Calling someone a dishwasher is the same thing as calling them a benchwarmer."
show cam intense with Dissolve(.2)
ca "What? They should just hire a housekeeper."
show jon shrug with Dissolve(.2)
jo "With what money?! {w=.5}{nw}"
show jon neutral
extend "Sorry, I channeled Jett there for a moment. Her VSL Champion status gives her a powerful aura in the studio."
show damen phone with Dissolve(.2)
d "It says here that there was originally supposed to be an attendant character to accompany Mr. Kim. She would ostensibly fulfill the role of housekeeper, but would actually be there to keep an eye on the team and report their actions back to Enoch."
show cam thinking with Dissolve(.2)
ca "That’s too bad. This game is a visual novel after all. It’s in desperate need of more women for lonely virgins to fawn over."
show damen smile with Dissolve(.2)
d "No projecting."
show cam intense with Dissolve(.2)
ca "What! I’m just saying what everyone is already thinking. I mean, look at Bolt. That guy looks like he was constructed in a fujoshi’s workshop. I'd bet that Reva has lewds of him on her computer."
show jon shrug with Dissolve(.2)
jo "About as sure of a bet that Stunt ran home and looked up the photoshoot that Jett talked about at the bar."
show damen calm with Dissolve(.2)
d "You know, Bolt's history with Jett was briefly addressed in the main game, but there’s a lot that Mach never learns about."
show jon smile with Dissolve(.2)
jo "They seem like they're cut from the same cloth. I’ll bet they had a rivalry in their middle school eSports club at the least."
show damen phone with Dissolve(.2)
d "Strange. The information on their relationship prior to the beginning of the game is all redacted."
show damen neutral with Dissolve(.2)
d "Well, it says here that Jett asked a longtime friend of hers on Shock for some replays who then ratted on her to Bolt. That’s why he brought the thumb drive for Mach."
show cam thinking with Dissolve(.2)
ca "Damn, betrayed. Well, wait, she was technically the one that initiated the a betrayal so-- whatever. Mach won, so it didn’t matter."
show jon neutral with Dissolve(.2)
jo "You could originally choose whether or not to give the replays back. Hell, I’d have hung onto it just for the free flash drive. Bolt’s kind of a weird guy."
show damen calm with Dissolve(.2)
d "Well, he’s frustrated by the fact that Brood War is losing popularity, and he pushes that frustration onto StarCraft 2 and the people playing it."
show cam intense with Dissolve(.2)
ca "How childish! What kind of miserable person would let their frustrations on the declining popularity of a video game affect those around them?"
stop music
play sound "sfx/Wind 3.mp3"
pause 4
play music "sfx/Blue Pineapple.ogg"
show jon shrug with Dissolve(.2)
jo "But he plays StarCraft 2 in secret at the beginning of the game, right? Why is that?"
show damen neutral with Dissolve(.2)
d "Probably because he was already thinking about jumping ship to SC2 and didn't want his team to know. Either that, or he found the game fun."
#... fu
show jon neutral with Dissolve(.2)
jo "Wait. Bolt is starting to sound vaguely apologetic. He was a huge jerk to Mach! We’re supposed to hate him."
show damen calm with Dissolve(.2)
d "He’s really just another guy trying to make it in eSports. You’ve already seen how tough it is for Jett’s team. Imagine that, plus the fear that all the money in your game's scene will be gone soon."
show jon shrug with Dissolve(.2)
jo "Hm. And I bet it seemed pretty unfair that a bunch of foreign investment went to StarCraft 2 rather than the game that built up eSports as we know it."
show cam thinking with Dissolve(.2)
ca "Wow, I never thought about it like that. KeSP-- I MEAN, KPGA guys have it rough."
show jon smile with Dissolve(.2)
jo "Should we expect a Vegeta style conversion at some point to unite against match fixing, then?"
show damen neutral with Dissolve(.2)
d "We’ve said too much as is. Let’s go see the team house before our time runs out."
show bg house:
    align (0, 0)
show jon neutral
show cam neutral
show damen neutral
with fade
d "People that see this apartment as humble are sadly mistaken. Team houses are not nearly this nice most of the time."
show cam smile with Dissolve(.2)
ca "The tradeoff is in size. If the team recruits anymore players, people might mistake this place for a gold farming den."
show jon smile with Dissolve(.2)
jo "I’ll bet that the fridge is stocked with Mach’s energy drinks. It’s very diligent of him to support the companies that sponsor eSports so selflessly."
show cam thinking with Dissolve(.2)
ca "What’s the layout for the team house anyway?"
show damen phone with Dissolve(.2)
d "It says here that there’s two bedrooms. One for guys and one for girls."
show jon shrug with Dissolve(.2)
jo "Huh. I would have expected Jett to demand a room to herself. And it’s too bad that someone as laidback as Accel has to share a space with Stunt."
show cam intense with Dissolve(.2)
ca "Maybe it’ll do the kid some good. Accel’s an old hand at this stuff."
show jon neutral with Dissolve(.2)
jo "It’s unfortunate that Accel is locked into that contract with Crash. He’d probably be the team’s best player."
show damen smile with Dissolve(.2)
d "Don’t get ahead of yourself. I have the power rankings right here."
show cam smile with Dissolve(.2)
ca "Oh! Dish it out. Who’s the best?"
show damen phone with Dissolve(.2)
d "The skill ranking is as follows: Jett > Accel > Reva > Mach > Stunt. However, Stunt has a high amount of potential to move up if he improves his mindset."
show jon shrug with Dissolve(.2)
jo "Damn. So if Bolt is Vegeta, then that means Jett is Goku?"
show damen neutral with Dissolve(.2)
d "Accel is Piccolo, Stunt is Gohan. Reva is an android. And, Mach… I’m sorry, but you’re Yamcha."
show jon smile with Dissolve(.2)
jo "... Brutal. Couldn’t even give him Krillin."
show cam thinking with Dissolve(.2)
ca "We’re giving Tasteless a run for his money when it comes to references here."
show jon neutral with Dissolve(.2)
jo "Alright. How are we going to wrap this up, boys? Anything you want to say to the fans out there?"
show damen phone with Dissolve(.2)
d "I have a direct message here from the devs, actually. It says: 'Thanks to our fans who waited patiently on release. We hoped that we showed you a good visual novel. Please support us in the future, fighting!'"
show cam smile with Dissolve(.2)
ca "I guess Mach really was just a self-insert for a Koreaboo all along."
d "Oh, and then at the bottom: ‘And a special thank you to all of our backers! The project would not have been possible without you.’"
show jon smile with Dissolve(.2)
jo "That’s us! We did it, guys! We saved eSports!"
stop music
show damen calm
show cam neutral
with Dissolve(.2)
pause 2
show cam thinking with Dissolve(.2)
ca "... Well, we saved SC2VN, at least."
play music "sfx/Blue Pineapple.ogg"
show jon neutral with Dissolve(.2)
jo "That about does it for us then. It was a pleasure providing a poorly disguised developer commentary alongside you two."
show damen smile with Dissolve(.2)
d "Likewise."
show cam intense with Dissolve(.2)
ca "Take care! Let’s meet again. Before StarCraft 3 comes out, please."
#end with some chibi animation
stop music fadeout 5.0
window hide dissolve
scene black with slowfade:
    align (0,0)
return

label S1studioQualifier:

    $ renpy.music.set_volume(0.5, .5, channel="sound")
    $ renpy.music.set_volume(0, 0, channel="Track2") 
    play Track1 "sfx/muffledapm.ogg" fadein 5.0 loop
    play Track2 "sfx/apmsound.ogg" fadein 5.0 loop
    
    $bar_choice_reva = False
    $bar_choice_accel = False
    $bar_choice_stunt = False
    $bar_choice_Jett = False

    $pc_reva = False
    $pc_protoss = False
    
    #INTRO SIGN UP, STAIRS
    scene black with slowfade:
        align (0,0)
    show bg cg11 at center with Dissolve(1):
        zoom 1.2 xpos .35
        linear 15 xpos .45 subpixel True
    window show dissolve
    show screen show_enc_button #DELETE THIS AFTER TESTING
    "There’s a certain feeling that every StarCraft player gets before they lose."
    "Most try to ignore it at first, as if the inevitable is just another challenge to fight through."
    "Like their past mistakes don’t count if they just try a little bit harder."    
    show bg cg11 at left with Dissolve(1):
        zoom 1.2 ypos 1.5
        linear 15 ypos 1.4 subpixel True
    "It's a natural thing. To believe otherwise contradicts the hours we spend practicing."
    "Still, every player must eventually come to terms with a defeat."
    "That they have to queue up for another game, or maybe that they flew across the world for nothing."
    show bg cg11 at right with Dissolve(1):
        zoom 1.2 ypos 1.0
        linear 15 ypos 1.1 subpixel True
    "I haven't met many players that can take a loss in stride."
    "It’s painful. It's permanent. It's proof that your best isn't always enough."
    $ renpy.music.set_volume(0, 1, channel="Track1") 
    $ renpy.music.set_volume(1, 1, channel="Track2")
    show bg cg12 with Dissolve(1):
        align (0,0) zoom 1.0
    "Long after my elimination, I remain at the PC with a blank look in my eye."
    "Clicks shoot from my finger as I leap from page to page. A tournament update mentions my defeat in passing, but no one acknowledges it."
    "When my frustration fades, I’m left only with guilt."
    show bg cg13 with Dissolve(1):
        align (0,0)
    "I should have practiced harder."
    stop Track2 fadeout 2.0
    window hide dissolve
    scene bg hallway2 with Dissolve(2):
        align (0,0)
    window show dissolve
    "I consider sticking around to watch the final few games, but the knot in my stomach persuades me to avoid anymore stress."
    "People are nice enough to a foreigner with the heart to attempt a StarLeague qualifier." 
    "But without a win, I’m just one more in a long line of losers."
    #stair sfx
    stop Track1 fadeout 2.0
    stop Track2 fadeout 2.0
    window hide dissolve

    jump S2interlude
    
label S2interlude:
    scene black with slowfade:
        align (0, 0)
    $ renpy.pause(.1, hard=True)
    show image "char/bonus/op1.png" at center with wiperight
    $ renpy.pause(1.5, hard=True)
    show image "char/bonus/op2.png" at center with wiperight
    $ renpy.pause(1.5, hard=True)
    show image "char/bonus/op3.png" at center with wiperight
    $ renpy.pause(5, hard=True)
    window hide dissolve
    jump S3apartmentGame

label S3apartmentGame:
    scene black with midfade:
        align(0,0)
    play music "sfx/terran2.mp3" fadein 10.0

    scene black:
        align (0,0)
    window show dissolve
    scene bg showmatch5 opening with dissolve:
        align(0,0)

    "Every game of StarCraft begins the same."


    scene bg black with Dissolve(0.1):
        align(0,0)


    show intro mine:
        alpha 0 
        yalign 0.0
        easein 0.4 yalign 0.3 alpha 1 subpixel True

    "Gather resources."




    show intro build:
        alpha 0 
        yalign 0.6
        easein 0.4 yalign 0.3 alpha 1 subpixel True
    "Train a worker. "

    show intro construct:
        alpha 0 
        yalign 0.0
        easein 0.4 yalign 0.3 alpha 1 subpixel True
    "Construct a building."

    show intro raisearmy:
        alpha 0 
        yalign 0.3 xpos .1
        easein 0.4 xpos 0.0 alpha 1 subpixel True

    "Rally an army."

    show intro defend:
        alpha 0 
        yalign 0.0
        easein 0.4 yalign 0.3 alpha 1 subpixel True

    "Defend a base."
    show intro contest:
        alpha 0 
        yalign 0.3 xpos -.1
        easein 0.4 xpos 0.0 alpha 1 subpixel True
    "Contest the map."

    scene bg showmatch4 econ with dissolve:
        align(0,0)

    
    "Turn something small into something more."

    play sound "sfx/battle/protossdeathballvsterran.ogg"
    show white with Dissolve(0.1):
        align(0,0)
    scene bg introbattle protoss:
        align(0,0)
    hide white with Dissolve(0.2)

    "This game is punishing. It’s stressful. It’s draining. It builds you up and tears you down."

    stop sound fadeout 1.0


    play sound "sfx/battle/terranvszerg.ogg"
    show white with Dissolve(0.1):
    show bg introbattle zerg with dissolve:
        align(0,0)
    hide white with Dissolve(0.2)

    "It’s not for everyone. It might not even be for me."

    "How many more chances am I going to get? Was that my last?"
    stop sound fadeout 1.0
    play sound "sfx/battle/unsiegedattacking.ogg"
    show white with Dissolve(0.1):   
    show bg introbattle terran with dissolve:
        align(0,0)
    hide white with Dissolve(0.2)
    "Oh. The feeling is back."

    "Hah… Why am I still trying? Why can’t I quit?"
    #return
    
    ##AUDIO: slam first
    stop music fadeout .2
    stop sound
    play voice "sfx/deskslam.mp3"
    scene white with Dissolve(.1):
        align(0,0)
    scene bg apartmentnight with Dissolve(.1):
        align(0,0)
    $ renpy.music.set_volume(0.3, .5, channel="sound")
    
    "My fist rattles the desk and sends a plastic bottle onto the floor. With my chin in hand, I throw myself into the match replay."
    play music "sfx/Brooding.ogg." fadein 2.0
    $ persistent.en1_locked = False
    $ encyclopaedia.unlockEntry(en1, persistent.en1_locked)
    show image "char/bonus/tip.png" at top:
        alpha 0.0 ypos -.05
        linear .5 alpha 1.0 ypos 0.0
    "I force down a measured breath. Losing a throwaway {color=#FF5E5E}ladder{/color} game shouldn't bother a player of my rank."
    show image "char/bonus/tip.png" at top:
        linear .5 alpha 0.0 ypos -.05
    "Scout denial and my poor control of the final fight gave my opponent the edge. In retrospect, my mistakes seem obvious." 
     
    "I toy with the conclusion that he was hacking before realizing that I’m just making excuses. No, I should have been able to win that one."
    "Despite the Grandmaster badge next to my handle, I find myself too anxious to queue up for another game."
    "The loss at the Victory StarLeague qualifier earlier today isn't helping my mindset. I comb my tiny room with a look, restless and unmotivated."
    
    "Sitting alone in a dark room for extended periods of time is incredibly depressing, a fact I learned only when it became a significant part of my life." 
    
    "Only one thing is certain. I’ve got to get out of here."
    window hide dissolve
    play sound "sfx/doorclose.mp3"
    scene bg streetnight with dissolve:
        align(0, 0)
    pause .6
    play sound "sfx/StepDown.ogg"
    $ renpy.pause(1)
    window show dissolve
    "After double-checking that my apartment's door is locked, I hustle down the stairs and onto the sidewalk. Light grows with each step towards the shining skyline."
    
    window hide dissolve
    
    scene bg citybig at left with Dissolve(1):
        linear 40 xpos -.5 subpixel True
        
    window show dissolve

    "Catchy pop beats and posters of flawless models dominate street after street. Foot traffic is thick and impatient. Seoul Tower stands tall from a distant hilltop."
    "But even the lingering excitement of life in a faraway place can't dredge me out of my hopelessness."
    "Sometimes, especially on days like this, I regret pursuing eSports. It's a thought I've had more times than I'd care to admit since coming to South Korea."
    "Even saying that, I know that I can't keep myself from competing. It's in my nature. And truth be told, this damn game is the only thing I'm good at."
    #black
    "What is StarCraft? Some respond to that with an explanation on its game mechanics or its storyline."
    "There are other popular answers too. That it requires the dexterity of a pianist alongside the strategic thinking of a chess player."
    "Maybe that's what StarCraft is to most people. But to the hundreds who carve out a living on it, StarCraft isn't such a simple thing."
    "It's the embodiment of competition, a perfect playing field. No need for athletic genes, rabid parents, tutting tutors, or expensive summer camps."
    "You pick up the game on your own. You learn. You improve. You work. If you're good enough, you can become a god."
    "And if you fail, you stay a nobody."
    window hide dissolve
    stop sound fadeout 4.0
    show black with Dissolve(1):
        align(0,0)
    window show dissolve
    "I'm not building towards a long-term career. {w=.5}I'm friendless in a foreign country. {w=.5}I'm respected by no one." 
    "And if I don’t qualify for the VSL next month, I’ll be back home at square one." 
    "I'll be nothing."
    "... But hey, at least I play video games all day."
    stop music fadeout 3.5
    stop sound fadeout 3.5
    window hide dissolve
    scene white with Dissolve(3.0):
        align(0, 0)
    play sound "sfx/Airport.ogg" fadein 3.0 loop
    scene image "bg/cg2bg.jpg":
        align (0,0)
    show image "bg/cg2mom.png" at center:
        zoom 1.0 xpos .5 ypos 1.0
    show image "bg/cg2dad.png" at center:
        zoom 1.0 xpos .5 ypos 1.0
    show image "bg/cg2mach1.png" at center
    with Dissolve(2.0)
    window show dissolve
    mom "Are you completely sure you haven’t forgotten anything?"
    mom "Do you have enough money for the cab when you land?"
    mom "Are you sure that the apartment got your money?"
    mom "Is your cell phone charged? You brought an extra charger, right?"
    m "Mom. I’m fine. Please, nothing bad is going to happen."
    dad "Remember. There won’t be anyone to do your laundry, cook your meals, or wake you up when you oversleep."
    dad "Budget well and you'll have two months. I won't hear anything about a loan for the flight home."
    "It takes effort to keep a frown from my face. I’m certain that my parents came to see me off only so that they could say they did."
    "I’ve already sunk the entirety of my savings into this. Now isn’t the time for second thoughts."
    "My dad gestures towards the security line and taps his watch twice."
    dad "Go on. The sooner this is over with the better."
    mom "Oh, come back in one piece, hun."
    "Nothing comes when I think of how to respond, so I only nod. Without another word, my parents walk away."
    window hide dissolve
    hide image "bg/cg2mom.png"
    hide image "bg/cg2dad.png"
    with Dissolve(1.0)
    pause .5
    show image "bg/cg2mach2.png" at center
    hide image "bg/cg2mach1.png"
    with Dissolve(1.5)
    $ renpy.pause(2.0, hard=True)
    stop sound fadeout 2.0
    scene white with Dissolve(2.0):
        align(0, 0)
    window show dissolve
    dad "He has to make his own mistakes."
    window hide dissolve
    pause 1
    play sound "sfx/street3.ogg" fadein 2.0 loop
    scene bg streetsidenight with Dissolve(1):
        align (0, 0) 
    window show dissolve
    play music "sfx/Blue Pineapple.ogg" fadein 2.0
    "I tighten my fist, pace quickening. Even though I want to prove everyone who's doubted me wrong, I’m tired of losing for no one’s sake but my own."

    "With the sun long set, overhead signs wash the streets in color. I’ve wandered so far that a walk back to my apartment would take almost a half hour."
    $ persistent.en2_locked = False
    $ encyclopaedia.unlockEntry(en2, persistent.en2_locked)
    "My renewed drive to practice my craft drives my search for a place to play. It’s not long before I see the words I’m looking for: {color=#FF5E5E}PC bang{/color}."

    "The amount of foot traffic suggests it's a pretty popular internet cafe. A sign on the front window reads Golden Zonefire."

    "Though I've only visited them a few times, PC bangs are one of the things that interested me most about Korea when I first got into StarCraft."

    "Duking it out for champion status of a neighborhood cafe is old school cool. Like the type of Western where a sheriff defends his turf against upstarts and outlaws."
    "It's an ideal that's a little bit dated these days. Most StarCraft 2 competition takes place either online or in broadcast studios."
    $ persistent.en3_locked = False
    $ encyclopaedia.unlockEntry(en3, persistent.en3_locked)
    "I'll admit, I’ve daydreamed of being born a decade earlier and playing the original eSport, {color=#FF5E5E}Brood War{/color}, during its rise alongside the PC bang." 
    "A better time. Or so they say online."
    window hide dissolve
    #steps
    stop sound fadeout 2.0
    jump S5goldenZonefire
    
label S5goldenZonefire:
    
    scene bg pcbang with Dissolve(1):
        align(0, 0)

    window show dissolve
    $ renpy.music.set_volume(1.0, 0, channel="sound")
    play sound "sfx/apmsound.ogg" fadein 1.0 loop

    "I trundle up the stairs and pass through the doorway, immediately struck by the size of the place. There has to be at least eighty computers."

    "The crowd is too large for an ordinary evening. There are more people than there are PCs, even."
    "I indulge my curiousity on the first person I see: A dark-haired guy observing a match of SC2 from behind someone’s shoulder."
    m "Excuse me. Is there an event going on?"
    show rival casual at center with dissolve:
        xpos .545
    "The guy turns and looks at me like I’m speaking something other than Korean. After a brief silence, he responds." 
    unknown "{w=.5}Are you new or something? {w=.5}How have you not heard of All-Out Attack?" 
    m "Yeah, I am new. Just asking."
    show rival bored at center with dissolve
    "He hums and glances away for a moment. Though he doesn’t apologize, he does fill me in."
    show rival smug at center with dissolve
    unknown "Golden Zonefire hosts a StarCraft 2 tournament called All-Out Attack once a month. It's one of the few places you'll find a decent player outside of an online cup or a StarLeague."
    show rival bored with dissolve
    unknown "Used to be a Brood War tournament, actually."
    m "I see. Thanks man. Who are you here to cheer for?"
    show rival annoyed with dissolve
    "He only stares in response. The guy walks away with a shake of his head, mumbling something about foreigners."
    hide rival with dissolve
    "The back of his shirt sports the Korean Pro-Gamer Association logo. Oh, he must be a Brood War fan."
    "None of the StarCraft teams under KPGA’s regulations compete in anything except the original game, Brood War. Understandably, they don't want to fracture a scene they've worked hard to build up."
    "And that’s lucky for those of us trying to keep from drowning in a game that’s already deep with talent. KPGA players train for unbelievable hours." 
    "Well, I came here to practice, and now I’m presented with an excellent chance to do so if what that guy said is true."
    "A few stares follow me as I walk forward to put my name on the sign-up list. I must look like a tourist in over my head."
    "I’m definitely not the first foreigner to go abroad for eSports, but most come to South Korea only once they have results or fame."
    "After paying for an hour's worth of PC time at the front desk, I settle for a station that has a mouse and keyboard similar to my setup back home."
    "A few minutes later, I join my opponent’s game lobby just in time for the start of the first round."
    "His name isn't familiar, so I check his profile to see he’s ranked midway through master league. Not bad for a casual player."
    "He seems eager enough by the rate he's spamming 'gogo' in the pre-game chat. The game gets underway once I confirm that I'm ready."
    stop music fadeout 2.0
    stop sound fadeout 2.0
    window hide dissolve

jump alloutattack1

label S7meetAccel:

    scene bg pcbang with Dissolve(1.0):
        align(0,0)
    play music "sfx/Blue Pineapple.ogg" fadein 1.0
    play sound "sfx/apmsound.ogg" fadein 1.0 loop
    window show dissolve


    
    "As soon as the victory screen displays, anxiety floods out of my body."
    "StarCraft is tense. It isn't an exaggeration to say that there's never a moment to relax until a match is over."
    "Bristling with confidence, I get up to check my next opponent..."
    #surprise/dejection
    "... {w=.5}and... {w=.5}it’s...{w=.5}{nw}"
    play voice "sfx/Heartbeat.mp3"
    extend " {w=.05}A{w=.05}c{w=.05}c{w=.05}e{w=.05}l{w=.05}.{w=.05}.{w=.05}.{w=.05}."
    "I draw my lips in a line and let my shoulders slouch. Welp, that's the end of this tournament run."
    "Accel is one of South Korea’s strongest terran players. He’s well known for his old school cred, balanced playstyle, and friendly banter."
    "He lost in the round of eight of last season’s VSL. A respectable finish, if not a high-paying one."
    "From what I remember, Accel was a damn good Brood War player. But he was out of his prime when the sequel hit last year, so it makes sense that he switched."

    "While I’m considering what sort of rush I should do to steal a win, I feel a tap on my shoulder and turn."
     
    show accel neutral at center with dissolve

    a "Huh. So you {i}are{/i} a foreigner."
    
    "... And find none other than the man himself standing there."

    "This is a bit surreal, considering I've followed Accel's play for about as long as I've been into StarCraft. Luckily, his nonchalant manner disarms my surprise."

    m "Yeah. I think we play next round. I'm Mach, a terran."
    show accel concerned with Dissolve(.25)
    show accel neutral with Dissolve(.25)
    "He misses a beat before regaining his smile, likely surprised that I understood and then answered him."
    a "Yeah, I saw you won your game. Not bad."
    show accel thinking with dissolve
    a "It’s not common to see foreigners at All-Out Attack. Are you on a team?"
    m "I’m not. Trying to find one though. I'm sure you know how that goes."
    show accel thinking2 with dissolve
    "I grin stupidly, which Accel doesn’t seem to mind. He pauses to scratch his cheek before responding."
    show accel neutral with dissolve
    a "Well, good luck. Don't expect another easy match."
    m "You too. {w=.5}Uh. {w=.2}I mean, thanks." #keep this for female mach
    show accel laughing with dissolve
    "Goddamn it. At least he laughed."
    hide accel with dissolve
    "My stress from before is mostly gone. If I lose, big deal. I’m expected to lose. If I win, I beat Accel!"
    $ persistent.en5_locked = False
    $ encyclopaedia.unlockEntry(en5, persistent.en5_locked)
    $ persistent.en14_locked = False
    $ encyclopaedia.unlockEntry(en14, persistent.en14_locked)
    "I’m still chewing over which {color=#FF5E5E}cheese{/color} I should perform before finally deciding just to play {color=#FF5E5E}standard{/color}. I shouldn't squander the rare chance to practice against a top player."
    "He and I banter back and forth in the pre-game lobby for a bit before the game gets underway."
    #write some banter?
    

    stop music fadeout 1.0
    stop sound fadeout 2.0
    window hide dissolve
jump alloutattack2

label S9meetJett:

    play music "sfx/Blue Pineapple.ogg" fadein 1.0
    play sound "sfx/apmsound.ogg." fadein 2.0 loop
    scene bg pcbang with dissolve:
        align(0,0)
    window show dissolve
    "I didn’t exactly throw my lead, but I did get seriously outplayed."
    "Fantasizing about how a victory would have felt doesn't help me keep my mind off the loss. Knowing that I did my best only helps so much."
    "But not a moment later, Accel turns the corner with a smile and raised eyebrows."
    
    show accel neutral at center with dissolve

    a "Good game man, you’re actually not bad. I assumed you were here for fun or something."

    m "Oh, uh, thanks. I am here for fun though. You play really well."
    show accel thinking2 at center with dissolve
    a "I’m surprised, most foreigners don’t hit timings like that. Good vision control too. And your scouting was top notch."
    a "You’re really not on a team? Are you at least staying at a team house? Oh, are you studying abroad?"

    m "Nothing like that. I’m staying by myself in an apartment by the VSL studios."
    show accel thinking at center with dissolve
    a "{w=.5}So you came to Korea alone and on your own dime{w=.2}.{w=.2}.{w=.2}.{w=.5} And you’re not just visiting?"

    m "Err{w=.3}.{w=.3}.{w=.3}. {w=1}Yes?" 
    show accel confident at center with dissolve
    "I do my best not to seem awkward about my answer, but any reason to worry disappears when Accel smiles."
    a "It takes some serious guts to move out here like that. I can't think of a single person who's made it out here on their own." 
    show accel neutral at center with dissolve
    "A few nearby competitors watch our conversation. It’s probably not often that Accel gives his attention to a random nobody he crushes early in a bracket."
    a "I've got some time before my next game. Let me introduce you to a friend of mine." 
    m "Oh. Sure."

    hide accel neutral with dissolve
    "With a nod, Accel leads me from the PC area to the back of the cafe." 
    "We pass a number of known players on the way there, most lounging around no differently than the cafe's other patrons."
    "Maybe they aren't that different. I guess even professionals like to kick back with the tangle of cords and rush of caffeine every now and then."
    "Games shouldn’t be all business all the time. Although, I’d bet that KPGA executives disagree."
    stop sound fadeout 5.0
    window hide dissolve
    scene bg cafe with Dissolve(1):
        align(0,0)
    window show dissolve

    "Accel comes to a stop away from the constant tapping of keyboards. He then plops himself into a seat against a wall and invites me to join him with a wave of his hand."
    "As I take my seat, I look up to find someone I recognize at his side."
    show jett neutral at left:
    show accel neutral at right:
    with dissolve
    "Jett. A zerg and former VSL champion." 
    "She won StarCraft 2's very first Grand Final back in the beta. A year ago, she might have been the game’s most famous player."
    "Her flippant and inflammatory antics have made her a somewhat controversial figure. She rarely ggs and isn't afraid to talk trash on stage."
    #fines
    "And there she is, just sitting there. It's all I can do not to stare."
    "A smile plays on her lips when she glances past me to Accel."
    show jett smile with dissolve
    j "Accel, seriously. Stop promising my autograph as a reward for beating you."
    show accel confident with dissolve
    a "Hilarious. He can understand you, by the way. Who are you up against next round?"
    show jett neutral2 with dissolve
    j "Some zerg dishwasher on LhT Slash. Ugh, I hate ZvZ."
    "Jett rolls her eyes back to me. After a brief appraisal, she lifts her chin and speaks a single word."
    show jett neutral3 with dissolve
    j "{w=.5}Name?"
    m "What? {w=.5}Oh. I'm Mach, a terran. {w=.2}I'm on... {w=.5}Uh, well. I'm teamless."
    show jett unimpressed with dissolve
    "Jett shifts her gaze back to Accel as if to ask, ‘Why did you bring this noob back here?’"
    "But before she can actually say anything, Accel comes to my defense with an easy smile."
    show accel neutral with dissolve
    a "Hey, cool it with the judgment until you've seen him play."
    show accel thinking2 with dissolve
    a "Plus, you ever hear of a foreigner that came out here alone, just for StarCraft? My man right here did. You have to admit that's brave."
    "If that endorsement wasn’t convincing enough, he offers one of his classic grins for good measure. The response seems to satisfy her. For now." 
    show jett neutral with dissolve
    "While I try to keep from showing anything to contradict Accel's assessment, Jett aims her attention back at me."
    show jett neutral3 with dissolve
    j "Didn't see your name on the list of people who made it past the VSL qualifier. How'd you place?"
    m "I lost my second to last match. The qualifier before that, I dropped out on the final game of the last series."
    show jett neutral2 with dissolve
    j "Two attempts without making it, huh? Hard to tell much from that. Mainly depends on the bracket you had."
    show jett neutral with dissolve
    j "How do you live out here with no team? Do you stream or something?"
    m "I used to stream, but I don't get enough viewers to make any money. My following is pretty small."
    "Small is an understatement. Nonexistent is closer to the truth."
    show jett unimpressed with dissolve
    j "So your parents pay for everything?"
    m "No. I’m here on my summer job earnings and a little bit extra from my grandparents."
    show jett casual with dissolve
    j "Hm. How lucky. I never got any handouts."
    show accel confident with dissolve
    "This isn’t going very well. Still, Accel looks as collected as ever, watching with a smile as the interrogation continues."
    show jett neutral with dissolve
    j "Did you play Brood War?"
    m "Not really. I mean, I had a copy as a kid, but I wasn’t good. Had to cheat to even finish the campaign."
    show accel neutral with dissolve
    a "Oh, then you were only a little bit worse than Jett."
    show jett unimpressed 
    show accel laughing
    with dissolve
    "Jett scowls silently at the jab. It's true that the two years she spent playing Brood War were mostly unremarkable."
    show jett neutral 
    show accel neutral
    with dissolve
    j "Then this is your first try at professional gaming?"
    show jett neutral2 with dissolve
    "When I nod, she gives me a hard look."
    j "Why are you out here?"
    m "... Eh? What do you mean?"
    show jett unimpressed with dissolve
    j "I'm sure you're aware of your chances. It's been more than five years since a foreign pro-gamer accomplished anything noteworthy in Korea."
    "I know what she's getting at, but it's not like I have a particularly great or unique answer. I scratch behind my head and look away."
    m "I mean, why else? I want to become better at StarCraft. Everyone knows that Korea is the place to do that."
    show jett considering with dissolve
    j "And why is that?"
    m "Well. {w=.5}Because the best players are out here, also I've studied the language for a while now so I have a—{w=.5}{nw}"
    play sound "sfx/interupt.ogg"
    show white with Dissolve(.1):
        align (0,0)
    show jett angry
    hide white with Dissolve(.2)
    j "No! I'm asking why you want to become better."
    m "Oh! {w=.5}Er..."
    show jett unimpressed with dissolve
    "It feels like she's forcibly extracting the truth from me. All the same, I can't leave her expression unanswered."
    "I do my best to avoid showing the embarassment I feel in my honest response."
    m "... Because I want to be a champion. Or, at the least, show I can compete at that level. Everyone who plays this game wants that, don't they?"
    show jett neutral with dissolve
    j "Tch. You're right about one thing. Every idiot that makes it to grandmaster and takes a map off of a good player thinks they’re pro-gamer material."
    show jett casual
    with dissolve
    j "A champion, huh? Sheesh." 
    show jett neutral with dissolve
    "She clicks her tongue and sighs, but doesn't seem displeased. Well, at least any moreso than usual."
    "I wouldn't have much ground to stand on if I disagreed with her. Jett is one of the few who has accomplished what the rest of us dream about."
    show accel thinking2 with dissolve
    a "Don’t be so harsh. His style is solid and he stood toe to toe with me for a while. With enough time, he could compete."
    show accel neutral with dissolve
    a "What do you think? Why don’t you practice with him a bit?"
    show jett thinking with dissolve
    j "I could. Little harm in giving him a chance."
    "Uh, wait.{w=.5} Back up. {w=.5}What just happened? {w=.2}Did he say practice, {w=.3}and did she say yes?"
    show accel laughing 
    show jett neutral
    with dissolve
    "Accel answers her with a pleased expression. Jett takes a moment to stretch out before again crossing her arms across her chest."
    show jett neutral3 with dissolve
    j "Stop staring and say something, Mach."
    "The sound of my name wakes me from my stunned silence. I jolt upright and offer a flurry of nods."
    play sound "sfx/Footstep.mp3"
    show bg cafe with vpunch
    $ renpy.pause(.2)
    m "Sorry! I say yes. I definitely say yes."
    show jett casual 
    show accel concerned
    with dissolve
    "Jett and Accel watch me in silence until I lower myself back into my seat."
    show accel neutral
    show jett neutral
    with dissolve
    a "It takes some determination to come out here alone. Let's see if it translates to wins, eh?"
    "With a thumbs up, it’s settled. I have somehow found myself with one of the best practice partners in the world." 
    "I really hope this isn’t just for the novelty of playing with some random foreigner."
    show jett neutral3 with dissolve
    j "Accel, it's about time to get back to All-Out Attack. Wouldn't want you getting DQed if we'll be matching in the semis."
    show accel thinking2 with dissolve
    a "Can you be certain that I didn't lose to Mach already? What if this was my way of saving face?"
    show jett pleased with dissolve
    j "Funny. Have you lost to a foreigner even once?"
    show accel neutral with dissolve
    $ persistent.en9_locked = False
    $ encyclopaedia.unlockEntry(en9, persistent.en9_locked)
    a "Hey, you never know who's playing on a {color=#FF5E5E}barcode{/color} account." 
    show accel thinking with dissolve
    a "You sure you don't want to pot split? Final offer."
    show jett smile with dissolve
    j "Collude? With you? Not a chance."
    show accel neutral
    with dissolve
    a "What about you, Mach? Gonna stick around?"
    show jett neutral
    with dissolve
    "A PC bang with the bustle of a tournament isn’t a great training environment. The bracket will probably take a few hours to work through too."
    m "No, I’m gonna head home. Got a lot of practicing to do tonight."
    show accel thinking with dissolve
    a "Leaving already? Well, hey. It was good to meet you man."
    show jett casual with dissolve
    j "Be at Golden Zonefire tomorrow morning and we’ll find out if you’re overhyped."
    m "Will do."
    "I rise and offer them each a nod in thanks before heading back towards the PC area." 
    "The last thing I see is a vague smile from Jett as she leans over and whispers something to Accel."
    window hide dissolve
    show jett pleased with Dissolve(.5):
        xpos .2
    scene bg pcbang:
        align(0, 0)
    with Dissolve(1)
    window show dissolve
    "I squeeze my way through the growing crowd and manage to make it through the doorway leading outside."
    "When I hit the street, I’m met with a cool breeze and a rush of voices, sound, and light."
    window hide dissolve
    scene bg streetsidenight with Dissolve(1):
        align(0, 0)
    window show dissolve
    play sound "sfx/street3.ogg" fadein 1.0 loop
    "This is it. A shot. One final shot to make it happen."
    "One last chance to live the life I want."
    "I quicken my pace, eager for the comfort of a dark room and bright monitor."
    window hide dissolve
    stop sound fadeout 4.0
    show sky6 at center:
        ypos 2.0
    show sky5 at center:
        ypos 1.1
    show sky4 at center:
        ypos .9
    show sky3 at center:
        ypos .8
    show sky2 at center:
        ypos .7
    show sky1 at center:
        ypos 1.0
    with Dissolve(1.0)
    show sky5 at center:
        easein 5 ypos 1.8 subpixel True
    show sky4 at center:
        easein 5 ypos 1.8 subpixel True
    show sky3 at center:
        easein 5 ypos 1.8 subpixel True
    show sky2 at center:
        easein 5 ypos 1.8 subpixel True
    show sky1 at center:
        easein 5 ypos 2.1 subpixel True
    $ renpy.pause(5.0, hard=True)
    window show dissolve
    "This is the day that everything changes."
    window hide dissolve
    show sky6 at center:
        easein 5 ypos 2.6 subpixel True
    show sky5 at center:
        easein 5 ypos 2.82 subpixel True
    show sky4 at center:
        easein 5 ypos 2.8 subpixel True
    show sky3 at center:
        easein 5 ypos 2.75 subpixel True
    show sky2 at center:
        easein 5 ypos 2.7 subpixel True
    show sky1 at center:
        easein 5 ypos 3.0 subpixel True
    $ renpy.pause(5.0, hard=True)
    show logosctitle:
        xalign 0.0
        alpha 0
        easein 0.2 xalign 0.5 alpha 1
    show logovntitle:
         yalign 0.5
         alpha 0
         xalign 0.5
         linear 0.2 alpha 0
         easein 0.2 yalign 0.0 alpha 1
    show logo2title:
        xalign 0.5
        alpha 0
        yalign -0.5
        linear 0.4 alpha 0
        easein 0.2 yalign 0.0 alpha 1
    show titlecred:
        alpha 0
        yalign 0.20
        linear 0.6
        easein 0.2 yalign .45 alpha 1

    pause 5.0

    show titlecred:
        alpha 1
        yalign 0.45
        easein 0.2 yalign .60 alpha 0

    pause 1.0

    hide titlecred

    #"SC2VN! by teej and tim"
    stop music fadeout 5.0
    #Intro/splash screen?
    
    
label S10zonefireJett:
    scene black with slowfade:
        align (0,0)
    play sound "sfx/street1.ogg" fadein 5.0 loop
    scene bg streetside with slowfade:
        align(0,0)
    window show dissolve
    #new casual track
    "True to her word, Jett sent me a reminder to get over to Golden Zonefire for some morning practice."     
    "I enjoy playing online and all, but matching against someone only a few feet away is way more productive."
    "Talking over games in person makes it easier to get feedback and improve. And that's what I need more than anything else."
    "The sting from my failure at the VSL qualifier will take time to fade. I don't want to experience that pain ever again."    
    stop sound fadeout 2.0
    window hide dissolve 

    scene bg pcbang with Dissolve(1):
        align(0,0)
    play sound "sfx/apmsound.ogg" fadein 1.0 loop
    play music "sfx/Full Server Intro.ogg"
    queue music "sfx/Full Server Loop.ogg"
    window show dissolve
    "I catch sight of Jett in a middle row, her attention locked on a ladder game. Without disturbing her, I take a seat at her side and watch the match unfold."
    "Furious taps and clicks rattle her keyboard. Her focus never drops from the game, much less her monitor. She's ahead, though not by much."
    "It's not long until she extends her lead in the late game and, a few minutes later, heaves a sigh of relief when her opponent ragequits out."
    "There's no need for me to consult my Korean skills to understand his final message: zerg imba."
    show jett smile at center with dissolve
    j "You actually showed. Color me surprised."
    m "How could I not? The better question is how you have the free time to practice with some amateur."
    j "I'm the charitable sort, obviously." 
    show jett neutral with dissolve
    j "Anyway, you're here, so let's stop wasting time. You've paid for your PC, yeah?"
    "I nod and log myself in at the station next to hers. A minute later, the two of us are grinding out practice matches."
    hide jett with dissolve
    window hide dissolve
jump jett_practice


label S11zonefireRival:

    scene bg pcbang with dissolve:
        align (0,0)

    window show dissolve

    "Before we get into the next game, I catch sight of a familiar face coming into the cafe."

    show rival smug at left with dissolve
    show rival:
        easein 1 alpha 0.0 xpos .2 subpixel True
    pause 1

    "Huh. Isn't that the same guy from last night?"

    m "Hey Jett. Do you know who that is?"
    show jett casual at center with dissolve
    "I thumb in the stranger’s direction as he passes by us, his attention occupied by a cell phone screen. Jett trails a look after him, wrinkles her nose, and shrugs."
    show jett neutral2 with dissolve
    j "He’s a KPGA player. Protoss. What about him? C’mon, get into the game already."
    m "Seriously? He was at All-Out Attack yesterday. What's he doing outside of his team house two days in a row?"
    show jett neutral with dissolve
    j "They’re only figuratively chained to their desks. Not all of them are shut-ins. Stop wasting time, let’s go."
    hide jett with dissolve
    "I double take away from Jett to find the player in question seated a few rows in front of us."
    "... And he's got the StarCraft 2 client open. Why would a KPGA player spend his practice time on anything but Brood War? Hm."
    m "Should I ask him for a game? I think I’m going to ask him for a game."
    show jett angst at center with dissolve
    j "What? No. Hold on, wait. You can't just—"
    hide jett with dissolve
    "But before she can stop me, I rise and shuffle my way past the rows of computers. Jett shoots me a withering glare over the top of her station before ducking back down."
    "Even though I’ve barely interacted with the guy, I can’t help but feel a little anxious as I edge closer to his PC."
    
    "Sure, he was a bit rude when we spoke. But the chance to challenge a KPGA pro is too good to pass up, especially if I'm trying to step up my game."
 
    "He’s about to jump into a match when I clear my throat right behind him. He subtly alt-tabs and then turns to regard me through half-lidded eyes."
    hide rival
    show rival casual at center with dissolve:
        xpos .545
    
    unknown "What?"
    
    m "Excuse me. Would you mind a practice game?"
    show rival smug at center with dissolve
    unknown "Uh. {w=.5}No. {w=.5}I’m just here to..."
    show rival bored with dissolve
    "He pauses. Recognition flits across his face."
    
    unknown "You're the guy from All-Out Attack yesterday, aren't you?"     
    "I nod sheepishly. His only reaction is to stare on."

    "For a moment, he looks ready to dismiss me and get to laddering. But at the last second, he nods." 
    show rival smug with dissolve
    unknown "Alright. One game."
    hide rival with dissolve
    "With a final nod, I return to my station. A moment later, he and I share a game lobby and are just about ready to begin."

    "He's playing on a barcode account. Typical. How have I still not managed to catch this guy’s name?"
    play voice "sfx/taptap.ogg"
    "A sharp tap against my headphones announces Jett’s return and displeasure."
    show jett unimpressed at center with dissolve
    j "You're obnoxious. If you lose and embarass me by association, I'm going to pretend I don't know you."
    hide jett with dissolve
    stop music fadeout 2.0
    "Anything else Jett has to say is drowned out along with the sounds of Golden Zonefire when I pull the earpad back on."
    stop sound fadeout 1.0
    window hide dissolve
jump boltgame
label boltlosecheese:
    scene bg pcbang with dissolve:
        align(0, 0)
    play sound "sfx/apmsound.ogg." fadein 2.0 loop
    window show dissolve
    "I don’t have long to sulk in defeat before the KPGA player makes his way over to me with a smirk. As promised, Jett is nowhere to be seen."
    show rival smug at center with dissolve
    unknown "That was ugly."
    "Tch. The worst part is that I don't even disagree with him."

    m "Yeah. Well. Nice micro, I guess."

    unknown "You guess? Well, maybe you're right. Didn't take all that much effort to defend against such a pitiful rush."
    stop sound fadeout 1.0
    play music "sfx/Greased Lightning Intro.ogg"
    queue music "sfx/Greased Lightning Loop.ogg"
    show rival fierce with dissolve
    "His grin darkens to one without humor. Is this guy serious?"
    m "What the hell is your problem?"
    show rival smug with dissolve
    unknown "You demand a game and whine when you get a little push-back? Look who's talking!"
    show rival fierce with dissolve
    unknown "Everyone knows your type: the foreigner out to make a name for himself. You fly out here on a whim and waste six weeks 'training.' You aren’t the first and unfortunately won’t be the last."
    unknown "Your plane ticket doesn't buy you the right to call yourself a pro-gamer. Save your money and your time and go back home."
    "I feel the heat rise in my face, half in anger and half in embarrassment. I’ve never dealt well with confrontation."
    "But before I can say anything else, Jett steps out from around the corner and cuts between the two of us."
    show jett casual at left 
    show rival at right:
        xpos .95
    with dissolve
    j "Still great at making friends, huh Bolt?"
    show rival bored with dissolve
    "He glances between the two of us, surprised. After a moment's pause, the so-called Bolt seizes back his smirk and meets Jett with a step forward."
    show rival smug with dissolve
    b "Been awhile, hasn't it? What's a supposed StarLeague champion doing with trash like this?"
    show jett neutral with dissolve
    "Bolt looks past her and tilts his head towards me. I take a step towards him, but an open palm from Jett stops me from going any further."
    show rival fierce with dissolve
    b "Maybe I shouldn't be surprised. Jumping ship to a scene bloated with foreign money has its upsides, but it won't be long before you forget the dignity of a pro-gamer."
    show jett smile with dissolve
    j "{i}The dignity of a pro-gamer,{/i} huh? You make it sound so distinguished."
    show rival bored with dissolve
    b "You've changed for the worse and you don't even realize it. How sad."
    show jett neutral3
    show rival fierce
    with dissolve
    b "Shouldn't be much longer until the KPGA finally accepts that there's no future in Brood War. You're smart enough to know what happens then. But hey, the scene could always use more casters."
    show jett smile with dissolve
    j"Whatever you say. For the record, what excuse did you give your coach for another day off? VIP's a little more lax than Shock T1, but I might want to borrow it someday."
    show rival annoyed with dissolve
    "At that, Bolt scowls. Jett doesn't waste the opening and strikes again."
    show jett pleased with dissolve
    j "Don't worry dongsaeng, your secret's safe with me. Run along now, I'm sure you've got coins to flip or something."
    "The standoff lasts a moment longer before Bolt lets out a lazy shrug, instantly killing off the intensity in his expression."
    show jett smile 
    show rival bored
    with dissolve
    b "I’ve got better things to do than offer advice to a mouthy chobo. Do what you want, kid."
    hide rival with dissolve
    "He thumbs his nose at me and returns to his station without another word." 
    "As soon as Bolt's out of sight, Jett takes my arm in a vice and practically drags me away."
    hide jett with dissolve
    #closeup
    show jett angst at center with dissolve
    j "What the hell was that?! He didn't even scout you! Is this how they play on the NA servers?"
    "Even after a heated confrontation, her concern is with the match before anything else. I almost laugh."
    m "It was stupid of me. I thought I could just grab a quick win..."
    show jett neutral2 with dissolve
    j "Play what you practice, for god's sake. If you're going to two rax in a tournament match, you better be damn sure you've done it a hundred times on ladder."
    "Her pointed critique defuses the tension from moments prior, even if it doesn't exactly make me feel any better."
    "When she's done going through my long list of mistakes, Jett flicks a hand back towards the PCs."
    stop music fadeout 3.0
    show jett unimpressed with dissolve
    j "Come on. Queue up a game against me."
    window hide dissolve
    stop sound fadeout 2.0
    scene black with midfade:
        align (0,0)
    jump S12CafeSceneTeamOrigins
    

label boltlosegreed:
    scene bg pcbang with dissolve:
        align(0, 0)
    play sound "sfx/apmsound.ogg." fadein 2.0 loop
    window show dissolve

    "I don’t have long to sulk in defeat before the KPGA player makes his way over to me with a smirk. As promised, Jett is nowhere to be seen."
    show rival smug at center with dissolve
    unknown "That was greedy."
    "Though it’s difficult to be graceful in defeat, I try my best anyway."
    m "Yeah, well. It's not something I've practiced a whole lot, and I didn't really produce as efficiently as I could have."

    unknown "Wouldn't have mattered. Bad mechanics should be the least of your worries."
    stop sound fadeout 1.0
    play music "sfx/Greased Lightning Intro.ogg"
    queue music "sfx/Greased Lightning Loop.ogg"
    show rival fierce with dissolve
    "His grin darkens to one without humor. Is this guy serious?"
    m "What the hell is your problem?"
    show rival smug with dissolve
    unknown "You demand a game and whine when you get a little push-back? Look who's talking!"
    show rival fierce with dissolve
    unknown "Everyone knows your type: the foreigner out to make a name for himself. You fly out here on a whim and waste six weeks 'training.' You aren’t the first and unfortunately won’t be the last."
    unknown "Your plane ticket doesn't buy you the right to call yourself a pro-gamer. Save your money and your time and go back home."
    "I feel the heat rise in my face, half in anger and half in embarrassment. I’ve never dealt well with confrontation."
    "But before I can say anything else, Jett steps out from around the corner and cuts between the two of us."
    show jett casual at left 
    show rival at right:
        xpos .95
    with dissolve
    j "Still great at making friends, huh Bolt?"
    show rival bored with dissolve
    "He glances between the two of us, surprised. After a moment's pause, the so-called Bolt seizes back his smirk and meets Jett with a step forward."
    show rival smug with dissolve
    b "Been awhile, hasn't it? What's a supposed StarLeague champion doing with trash like this?"
    show jett neutral with dissolve
    "Bolt looks past her and tilts his head towards me. I take a step towards him, but an open palm from Jett stops me from going any further."
    show rival fierce with dissolve
    b "Maybe I shouldn't be surprised. Jumping ship to a scene bloated with foreign money has its upsides, but it won't be long before you forget the dignity of a pro-gamer."
    show jett smile with dissolve
    j "{i}The dignity of a pro-gamer,{/i} huh? You make it sound so distinguished."
    show rival bored with dissolve
    b "You've changed for the worse and you don't even realize it. How sad."
    show jett neutral3
    show rival fierce
    with dissolve
    b "Shouldn't be much longer until the KPGA finally accepts that there's no future in Brood War. You're smart enough to know what happens then. But hey, the scene could always use more casters."
    show jett smile with dissolve
    j"Whatever you say. For the record, what excuse did you give your coach for another day off? VIP's a little more lax than Shock T1, but I might want to borrow it someday."
    show rival annoyed with dissolve
    "At that, Bolt scowls. Jett doesn't waste the opening and strikes again."
    show jett pleased with dissolve
    j "Don't worry dongsaeng, your secret's safe with me. Run along now, I'm sure you've got coins to flip or something."
    "The standoff lasts a moment longer before Bolt lets out a lazy shrug, instantly killing off the intensity in his expression."
    show jett smile 
    show rival bored
    with dissolve
    b "I’ve got better things to do than offer advice to a mouthy chobo. Do what you want, kid."
    hide rival with dissolve
    "He thumbs his nose at me and returns to his station without another word." 
    "As soon as Bolt's out of sight, Jett takes my arm in a vice and practically drags me away."
    hide jett with dissolve
    #closeup
    show jett angst at center with dissolve
    j "What the hell was that?! Did you close your eyes, expand, and hope for the best?"
    "Even after a heated confrontation, her concern is with the match before anything else. I almost laugh."
    m "I don't know. I was trying to be kinda tricky and put my third base where he wouldn't have normally scouted."
    show jett neutral2 with dissolve
    j "It's blatantly obvious that you're expanding if you haven't shown an army that late in the game. All he had to do was look around the map and collect a free win."
    "Her pointed critique defuses the tension from moments prior, even if it doesn't exactly make me feel any better."
    "When she's done going through my long list of mistakes, Jett flicks a hand back towards the PCs."
    stop music fadeout 3.0
    show jett unimpressed with dissolve
    j "Come on. Queue up a game against me."
    window hide dissolve
    stop sound fadeout 2.0
    scene black with midfade:
        align (0,0)
    jump S12CafeSceneTeamOrigins
    

label boltlosedrops:
    scene bg pcbang with dissolve:
        align(0, 0)
    play sound "sfx/apmsound.ogg." fadein 2.0 loop
    window show dissolve

    "I don’t have long to sulk in defeat before the KPGA player makes his way over to me with a smirk. As promised, Jett is nowhere to be seen."
    show rival smug at center with dissolve
    unknown "Hey. You actually know how to play. Wasn't expecting that I'd have to try."

    "It’s a compliment, regardless of how condescendingly he said it. Though it’s difficult to be graceful in defeat, I try my best anyway."

    m "I played my game the best I could. Kept vision on you, dropped when I could..."

    unknown "But it wasn’t enough. Sucks, man. It’s one thing to lose carelessly, but it’s another when everything goes as planned and you fail anyway."
    stop sound fadeout 1.0
    play music "sfx/Greased Lightning Intro.ogg"
    queue music "sfx/Greased Lightning Loop.ogg"
    show rival fierce with dissolve
    "His grin darkens to one without humor. Is this guy serious?"
    m "What the hell is your problem?"
    show rival smug with dissolve
    unknown "You demand a game and whine when you get a little push-back? Look who's talking!"
    show rival fierce with dissolve
    unknown "Everyone knows your type: the foreigner out to make a name for himself. You fly out here on a whim and waste six weeks 'training.' You aren’t the first and unfortunately won’t be the last."
    unknown "Your plane ticket doesn't buy you the right to call yourself a pro-gamer. Save your money and your time and go back home."
    "I feel the heat rise in my face, half in anger and half in embarrassment. I’ve never dealt well with confrontation."
    "But before I can say anything else, Jett steps out from around the corner and cuts between the two of us."
    show jett casual at left 
    show rival at right:
        xpos .95
    with dissolve
    j "Still great at making friends, huh Bolt?"
    show rival bored with dissolve
    "He glances between the two of us, surprised. After a moment's pause, the so-called Bolt seizes back his smirk and meets Jett with a step forward."
    show rival smug with dissolve
    b "Been awhile, hasn't it? What's a supposed StarLeague champion doing with trash like this?"
    show jett neutral with dissolve
    "Bolt looks past her and tilts his head towards me. I take a step towards him, but an open palm from Jett stops me from going any further."
    show rival fierce with dissolve
    b "Maybe I shouldn't be surprised. Jumping ship to a scene bloated with foreign money has its upsides, but it won't be long before you forget the dignity of a pro-gamer."
    show jett smile with dissolve
    j "{i}The dignity of a pro-gamer,{/i} huh? You make it sound so distinguished."
    show rival bored with dissolve
    b "You've changed for the worse and you don't even realize it. How sad."
    show jett neutral3
    show rival fierce
    with dissolve
    b "Shouldn't be much longer until the KPGA finally accepts that there's no future in Brood War. You're smart enough to know what happens then. But hey, the scene could always use more casters."
    show jett smile with dissolve
    j"Whatever you say. For the record, what excuse did you give your coach for another day off? VIP's a little more lax than Shock T1, but I might want to borrow it someday."
    show rival annoyed with dissolve
    "At that, Bolt scowls. Jett doesn't waste the opening and strikes again."
    show jett pleased with dissolve
    j "Don't worry dongsaeng, your secret's safe with me. Run along now, I'm sure you've got coins to flip or something."
    "The standoff lasts a moment longer before Bolt lets out a lazy shrug, instantly killing off the intensity in his expression."
    show jett smile 
    show rival bored
    with dissolve
    b "I’ve got better things to do than offer advice to a mouthy chobo. Do what you want, kid."
    hide rival with dissolve
    "He thumbs his nose at me and returns to his station without another word." 
    "As soon as Bolt's out of sight, Jett takes my arm in a vice and practically drags me away."
    hide jett with dissolve
    #closeup
    show jett angst at center with dissolve
    j "You had the game won! What the hell was that? An SCV pull at fifteen minutes? Is this what they teach you on the NA servers?"
    "Even after a heated confrontation, her concern is with the match before anything else. I almost laugh."
    m "My drops crippled him. I thought it would be enough to end the game."
    show jett neutral2 with dissolve
    j "So build units for two minutes and THEN go roll him. Don't be so damn impatient. Your upgrades were late too."
    "Her pointed critique defuses the tension from moments prior, even if it doesn't exactly make me feel any better."
    "When she's done going through my long list of mistakes, Jett flicks a hand back towards the PCs."
    stop music fadeout 3.0
    show jett unimpressed with dissolve
    j "Come on. Queue up a game against me."
    window hide dissolve
    stop sound fadeout 2.0
    scene black with midfade:
        align (0,0)
    jump S12CafeSceneTeamOrigins
    
    
    

