#FEMALE MACH SCRIPT
label FeMachOpening:

    $ fbar_choice_reva = False
    $ fbar_choice_accel = False
    $ fbar_choice_stunt = False
    $ fbar_choice_jett = False

    $ fpc_reva = False
    $ fpc_protoss = False

    $ renpy.music.set_volume(0.5, .5, channel="sound")
    $ renpy.music.set_volume(0, 0, channel="Track2") 
    play Track1 "sfx/muffledapm.ogg" fadein 5.0 loop
    play Track2 "sfx/apmsound.ogg" fadein 5.0 loop
    
    #INTRO SIGN UP, STAIRS
    scene black with slowfade:
        align (0,0)
    show image "bg/cg1b1.jpg" at center with Dissolve(1):
        zoom 1.2 xpos .35
        linear 15 xpos .45 subpixel True
    window show dissolve
    show screen show_enc_button #DELETE THIS AFTER TESTING
    "There’s a certain feeling that every StarCraft player gets before they lose."
    "Most try to ignore it at first, as if the inevitable is just another challenge to fight through."
    "Like their past mistakes don’t count if they just try a little bit harder."    
    show image "bg/cg1b1.jpg" at left with Dissolve(1):
        zoom 1.2 ypos 1.5
        linear 15 ypos 1.4 subpixel True
    "It's a natural thing. To believe otherwise contradicts the hours we spend practicing."
    "Still, every player must eventually come to terms with a defeat."
    "That they have to queue up for another game, or maybe that they flew across the world for nothing."
    show image "bg/cg1b1.jpg" at right with Dissolve(1):
        zoom 1.2 ypos 1.0
        linear 15 ypos 1.1 subpixel True
    "I haven't met many players that can take a loss in stride."
    "It’s painful. It's permanent. It's proof that your best isn't always enough."
    $ renpy.music.set_volume(0, 1, channel="Track1") 
    $ renpy.music.set_volume(1, 1, channel="Track2")
    show image "bg/cg1b2.jpg" with Dissolve(1):
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

label FS3apartmentGame:
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
    show image "bg/cg2_1b.png" at center
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
    show image "bg/cg2_2b.png" at center
    hide image "bg/cg2_1b.png"
    with Dissolve(1.5)
    $ renpy.pause(2.0, hard=True)
    stop sound fadeout 2.0
    scene white with Dissolve(2.0):
        align(0, 0)
    window show dissolve
    mom "She has to make her own mistakes."
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
    
label fS5goldenZonefire:
    
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
    m "I see. Thank you. Are you here cheering for someone?"
    show rival annoyed with dissolve
    "He only stares in response. The guy walks away with a shake of his head, mumbling something about foreigners."
    hide rival with dissolve
    "The back of his shirt sports the Korean Pro-Gamer Association logo. Maybe he's a Brood War fan or something."
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
jump falloutattack1
label fS7meetAccel:

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

    m "Um. I think we play next round. I'm Mach, a terran."
    show accel concerned with Dissolve(.25)
    show accel neutral with Dissolve(.25)
    "He misses a beat before regaining his smile, likely surprised that I understood and then answered him."
    a "Yeah, I saw you won your game. Not bad."
    show accel thinking with dissolve
    a "Foreigners are an uncommon sight at All-Out Attack. Are you a pro-gamer? What team are you on?"
    m "I don't know if you could call me a pro-gamer at this point, and I don't have a team. Trying to find one, though."
    show accel thinking2 with dissolve
    "I do my best not to look too hopeful, though Accel's blank expression is hard to read either way. He pauses to scratch his cheek before responding."
    show accel neutral with dissolve
    a "Well, good luck. Don't expect another easy match."
    m "You too. {w=.5}Uh. {w=.2}I mean, thanks." #keep this for female mach
    show accel laughing with dissolve
    "Oh god, kill me. At least he laughed."
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
jump falloutattack2
label fS9meetJett:

    play music "sfx/Blue Pineapple.ogg" fadein 1.0
    play sound "sfx/apmsound.ogg." fadein 2.0 loop
    scene bg pcbang with dissolve:
        align(0,0)
    window show dissolve
    "I didn’t exactly throw my lead, but I did get seriously outplayed."
    "Fantasizing about how a victory would have felt doesn't help me keep my mind off the loss. Knowing that I did my best only helps so much."
    "But not a moment later, Accel turns the corner with a smile and raised eyebrows."
    
    show accel neutral at center with dissolve

    a "Hey, good game. You’re actually not bad. I assumed you were here for fun or something."

    m "Oh, um, thanks. I am here for fun though. You play really well."
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
    a "Hilarious. She can understand you, by the way. Who are you up against next round?"
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
    a "Hey, cool it with the judgment until you've seen her play."
    show accel thinking2 with dissolve
    a "Plus, you ever hear of a foreigner that came out here alone, just for StarCraft? My girl right here did. You have to admit that's brave."
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
    m "I used to stream, but uh. Well. I don't anymore."
    "Jett raises her eyebrow, waiting for me to elaborate until I look away. Without missing a beat, she moves onto the next question."
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
    a "Don’t be so harsh. Her style is solid and she stood toe to toe with me for a while. With enough time, she could compete."
    show accel neutral with dissolve
    a "What do you think? Why don’t you practice with her a bit?"
    show jett thinking with dissolve
    j "I could. Little harm in giving her a chance."
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
    a "Leaving already? Well, hey. It was good to meet you."
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
    stop music fadeout 5.0
    #Intro/splash screen?
    
    
label fS10zonefireJett:
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
jump fjett_practice

label fS11zonefireRival:

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
    
    unknown "You're the chick from All-Out Attack yesterday, aren't you?"
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
jump fboltgame
label fboltlosecheese:
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
    unknown "Everyone knows your type: the foreigner out to make a name for herself. You fly out here on a whim and waste six weeks 'training.' You aren’t the first and unfortunately won’t be the last."
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
    b "I’ve got better things to do than offer advice to a mouthy chobo. Do what you want."
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
    jump fS12CafeSceneTeamOrigins
    

label fboltlosegreed:
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
    unknown "Everyone knows your type: the foreigner out to make a name for herself. You fly out here on a whim and waste six weeks 'training.' You aren’t the first and unfortunately won’t be the last."
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
    b "I’ve got better things to do than offer advice to a mouthy chobo. Do what you want."
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
    jump fS12CafeSceneTeamOrigins
    

label fboltlosedrops:
    scene bg pcbang with dissolve:
        align(0, 0)
    play sound "sfx/apmsound.ogg." fadein 2.0 loop
    window show dissolve

    "I don’t have long to sulk in defeat before the KPGA player makes his way over to me with a smirk. As promised, Jett is nowhere to be seen."
    show rival smug at center with dissolve
    unknown "Hey. You actually know how to play. Wasn't expecting that I'd have to try."

    "It’s a compliment, regardless of how he said it. Though it’s difficult to be graceful in defeat, I try my best anyway."

    m "I played my game the best I could. Kept vision on you, dropped when I could..."

    unknown "But it wasn’t enough. Sucks. It’s one thing to lose carelessly, but it’s another when everything goes as planned and you fail anyway."
    stop sound fadeout 1.0
    play music "sfx/Greased Lightning Intro.ogg"
    queue music "sfx/Greased Lightning Loop.ogg"
    show rival fierce with dissolve
    "His grin darkens to one without humor. Is this guy serious?"
    m "What the hell is your problem?"
    show rival smug with dissolve
    unknown "You demand a game and whine when you get a little push-back? Look who's talking!"
    show rival fierce with dissolve
    unknown "Everyone knows your type: the foreigner out to make a name for herself. You fly out here on a whim and waste six weeks 'training.' You aren’t the first and unfortunately won’t be the last."
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
    b "I’ve got better things to do than offer advice to a mouthy chobo. Do what you want."
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
    jump fS12CafeSceneTeamOrigins
    
    
    

