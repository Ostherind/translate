###Act 2


label S25ShowmatchOrganization:
    #elv sfx
    scene black with squares:
        align (0, 0)
    pause 1
    play sound "sfx/whirr.ogg" fadein 1.0 loop
    window show dissolve
    j  "Let me do most of the talking, but chime in if it makes sense."
    m  "Alright."
    j  "{w=.5}Nervous?"
    m  "No."
    j  "Don't lie to me. I’m nervous. It's fine to be nervous."
    m  "I’m fine."
    play sound "sfx/bell.mp3"
    "When elevator door opens, a well-dressed Enoch employee greets us with a smile and gestures down the hall."
    secretary "Mr. Kim has been anticipating your arrival. This way, please."
    window hide dissolve
    scene bg boardroom with dissolve:
        align (0, 0)
    window show dissolve
    show kim neutral at center with dissolve
    "I follow Jett through a typical corporate office. Inside, a table seats Mr. Kim, his attention set on a laptop."

    "He glances past the screen to acknowledge us with a beckon forward."
    show kim neutral2 with dissolve
    k "Jett, Mach. Please, sit."
    show kim at right
    show jett neutral at left
    with dissolve
    "We take our seats opposite him. The secretary closes the board room’s door, leaving the three of us on our own."
    "After a few more taps on his laptop’s touchscreen, Mr. Kim turns the computer towards us and gestures sharply to it."
    k "What is this?"
    show playxd:
        xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    with dissolve
    "On display is the comment section of a popular Korean eSports news site. Line after line portrays Jett and Accel as shady and unskilled."
    "... And I thought that the English sites were bad. Before I can read another comment, Mr. Kim forces the laptop shut with a grimace."
    #shut sfx
    show jett thinking
    show kim frust
    show playxd:
        alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
        easeout .2 ypos 0.6 alpha 0.0 subpixel True
    play voice "sfx/laptop.ogg"
    $ renpy.pause(.2)
    play music "sfx/Dusty Road A.ogg"
    queue music "sfx/Dusty Road B.ogg"
    k "When I spoke of my interest to sponsor your team with the board, most were hesitant to take the risk even with my assurance that the investment would be worth it in the end."

    k "Given the recent developments, I'll simply have to retract my recommendation and take the hit to my reputation. Your team has become a liability without having played a single game."

    "He rests a finger on his brow, expression fraught. This is worse than Jett and I planned for."
    show kim frust2 with dissolve

    k "Do you have anything to say?"
    show jett casual with dissolve
    j  "This wasn’t the reaction that we were hoping for. But it shows that people are paying attention to us."
    show kim frust5 with dissolve
    k "Not all attention is created equal. What is most important is that an Enoch team has a large number of supporters. Not slack-jawed or passive observers. Fans that are invested in the team's victory."
    show jett unimpressed with dissolve
    m  "You’ll immediately have five people invested in an Enoch squad if you sign us."
    show jett neutral with dissolve
    "Through narrowed eyes, Mr. Kim shifts his eyes in my direction."
    show kim frust3 with dissolve
    k "Mach. I should say that you are a large part of the doubt plaguing a possible sponsorship deal."
    show jett unimpressed with dissolve
    "I blink once, taken aback. Me?"
    k "Are you truly surprised? Your ability is completely unproven. While Accel and Jett may have their integrity questioned, it’s you whom the fans mock."
    show kim frust4 with dissolve
    k "If our fanbase doesn't have faith in your ability to win games, then of what use are you?"

    m  "What?! I’m a good player! I just need time to prove it."
    show kim frust3 with dissolve
    k "Time that you haven’t earned."
    
    "I hear myself tripping over my next protest. Right then, Jett cuts in."
    show jett neutral with dissolve
    j  "Mr. Kim, there must be something that we can do. Accel and I are high profile. Even with a rocky start, we both have loyal fans that will follow us to a new team."
    show kim frust5 with dissolve
    k "That may be so, but the public perception of Mach remains an issue. Is it worth the trouble of keeping him on when your reputation has been compromised?"
    show jett neutral with dissolve
    "He links his fingers together and glances between the two of us, awaiting an answer."
    show jett considering 
    show kim orly
    with dissolve
    "Jett closes her eyes and runs a hand through her hair. She takes a long moment to decide on what to say next, much to Mr. Kim's interest."
    $ renpy.pause(1)
    show jett neutral with dissolve
    j  "We could arrange something to fix that."
    show kim frust5 with dissolve
    k "Oh? Elaborate."
    show jett casual with dissolve
    j  "A showmatch. The perfect chance to showcase Mach’s ability to compete."
    show kim frust with dissolve
    k "Against someone from your team? Fans will assume that the match is fixed on his behalf."
    j  "No. I have someone else in mind. Someone who StarCraft fans know and respect, and that Mach owes a beating."
    show jett smile 
    show kim frust5
    with dissolve
    "She turns towards and locks eyes with me. Is she talking about…?"
    m  "A showmatch with Bolt? I mean…"
    show jett neutral3 with dissolve
    j  "You’re not allowed to turn this down."

    m  "I wasn’t planning on it. Just, how are you going to get him to agree?"
    show jett considering with dissolve
    j  "I know Bolt well. He’ll jump at the chance to publicly humiliate someone he doesn’t like."
    show jett smile with dissolve
    j  "A best of five will do nicely. And I think it would be fair for Enoch to put half a month’s worth of team funding in as the prize, wouldn’t you say?"
    show kim frust3 with dissolve
    "Jett turns away from me and towards Mr. Kim. For the first time since we stepped in the room, the businessman cracks a smile."
    show kim relieved with dissolve
    k "If you ever decide to leave StarCraft behind, you're welcome to interview for any open sales positions at Enoch, Jett."
    show kim orly with dissolve
    k "Very well. If Mach is victorious in this showmatch, I will consider your team’s reputation redeemed."

    "I don’t bother asking what will happen if I lose. God, what did I do to deserve this pressure?"
    show jett neutral with dissolve
    j  "Would you mind speaking with the producers at the VSL studio to see if they would be willing to host us? A week from today is short notice, but we don't have any longer to waste."
    show kim relieved with dissolve
    k "I’ll have it done."
    show kim frust3 
    with dissolve
    k "You’re very lucky to have someone like Jett as your team captain, Mach."
    show jett neutral2 with dissolve
    "When I don't respond, he smirks." 
    hide jett
    show kim orly at center
    with dissolve
    #sizeup
    "Satisfied, Kim rises from his leather office chair. Jett and I quickly follow suit and exchange handshakes with him."

    "As he meets his palm with mine, Mr. Kim leans forward and whispers to me."
    show kim relieved with dissolve
    k "For the record, I would greatly prefer to see you succeed. Don’t let a mistake in the next week end your career before it's begun."
    hide kim with dissolve
    "Nonchalantly, he parts from our grip and departs the conference room with long strides. His secretary skitters after him down the hallway, leaving Jett and me to find our own way back to the elevator."
    show jett unimpressed at center with dissolve
    j  "Well, you came to Golden Zonefire looking for a chance. Now you’ve got one. Happy?"
    m  "You stuck up for me."
    show jett casual with dissolve
    j "Yes. And?"
    m "I just... I guess I thought that you'd have done what was best for the team."
    show jett unimpressed with dissolve
    j "Who said I'm not? Mr. Kim? I don't recall putting him in charge of team management."
    j "What kind of team captain would I be if I tossed you out onto the street after recruiting Stunt and Reva?"
    m "I don't know. You said yourself that you wouldn't put the goals of a friendship ahead of the goals of your team."
    show jett pleased with dissolve
    j "Oh, in that case, it's not too late for me to go tell Mr. Kim I've changed my mind."
    show jett smile with dissolve
    j "If you insist on paying me back, do so by practicing hard and beating the shit out of Bolt. It's been way too long since I've seen him lose in person."
    stop music fadeout 5.0
    show jett thinking with dissolve
    j  "And, for the record, I know what I said. But the more I think about it, the more messed up it seems that we’d waste our careers with people we hate."
    show jett smile with dissolve
    j  "So, for now, I've decided that I like you. Don’t make me regret that."
    m  "So much for cold efficiency. And I'll do my best."
    j  "As is expected of anyone that wears my team's colors."
    show jett neutral with dissolve
    j  "Now c'mon. Before someone mistakes Accel for a bum."
    hide jett with dissolve
    play sound "sfx/door.ogg"
    stop music fadeout 1.0
    show blacksolid at center:
        xpos -.5
        linear 1.9 xpos 0.0
    show black at center:
        xpos 1.5
        linear 1.9 xpos 1.0
    with Dissolve(1)
    stop music fadeout 3.0
    "Just before the elevator doors close, Mr. Kim turns the corner of his office and watches us go."
    window hide dissolve
    jump S26MachNeedsPractice

label S26MachNeedsPractice:
    ##park
    scene black with fade:
        align (0, 0)
    pause 1
    scene bg streetday with squares:
        align (0, 0)
    $ renpy.music.set_volume(0.5, 0, channel="sound")
    play sound "sfx/Morning.ogg" fadein 2.0 loop
    window show dissolve
    "My legs are sore by the time we make it back to Namdan. Weeks of huddling up in my apartment obviously hasn’t been great for my personal fitness."
    window hide dissolve
    scene bg parkday with Dissolve(1):
        align (0, 0)
    window show dissolve
    "I catch sight of Stunt by his wild hair. He's the first to notice Jett and me and calls at us with a wave."
    show stunt fist at center with dissolve
    s "Yoooooooo! Is the team dead?"
    hide stunt
    show jett neutral at right:
        xpos 1.05
    show accel thinking at left:
        xpos -.1
    show reva neutral at left:
        xpos .2
    with dissolve
    j "Not yet, and not for a while if our plan works out."
    "Accel sits up from his reclined position, while Reva has hardly moved at all since she came into view."
    show accel neutral
    with dissolve
    a "Plan?"
    show jett casual with dissolve
    j "Mach is going to win a showmatch."
    show reva glasses
    show jett neutral
    with dissolve
    "Reva takes hold of her glasses, gears visibly turning in her head as she works out the point of a showmatch. Accel and Stunt simply look to me for the answer."

    m "Mr. Kim agreed to sponsor us if we can redeem the team's image. I have to win a series against Bolt."
    show accel thinking3
    show reva neutral2
    with dissolve
    a "Bolt? That surly protoss on Shock? He's a Brood War player, though."
    show jett neutral3 with dissolve
    j "He plays Star2 on his own time. With money and the chance to embarrass a foreigner on the line, he has to accept."
    show accel concerned with dissolve
    a "And you’re okay with this, Mach?"

    "Accel glances in my direction, genuine concern etched in his expression. He seems to be picking up on the doubt I’m feeling."

    m "Yeah. Of course. I mean, I’m going to practice as hard as I can for the next week."
    show reva expected with dissolve
    r "As will Bolt."

    "I don’t have anything to say to that. She’s right, after all."
    hide reva
    hide jett
    hide accel
    with dissolve
    "The five of us take a moment to reflect on the severity of the situation. Gradually, I find the eyes of my teammates drifting towards me."

    "I clean the sweat from my palms and steady myself with a breath."
    play music "sfx/Deep Thought Intro.ogg"
    queue music "sfx/Deep Thought Loop.ogg"
    stop sound fadeout 2.0
    m "I’m sure that I can handle this, but not all on my own."
    show stunt neutral grin at left
    show jett unimpressed at right
    with dissolve
    s "Obviously! Listen, if he's a protoss, I'm down to grind out endless games. You and me, Mach!"
    show jett considering with dissolve
    j "Bolt's play has more depth than proxies and one base all-ins."
    show stunt yell with dissolve
    s "Do you have a better idea!? What the hell would he get out of practicing with a terran or a zerg?"
    show jett casual
    show stunt phone
    with dissolve
    "Stunt pulls out his phone and dons a stubborn expression. Jett rolls her eyes and glances past him."
    
    j "Everyone has a role to play in making sure that this team lives on past a botched showmatch. Stunt may—"
    show jett unimpressed with dissolve
    "She winces and then glances begrudgingly in the young protoss’ direction."
    show jett neutral
    show stunt smug
    with dissolve
    j "—be the only one of us that plays protoss enough to spar with Mach, but this is still a group effort. Accel, you get to test out your coaching chops."
    hide jett
    hide stunt
    show accel confident at center
    with dissolve
    "He raises a thumb up without bothering to stand."

    a "You know it."
    hide accel
    show reva neutral2 at left
    show jett neutral at right
    with dissolve
    j "Reva, work with Mach on openings and strategies. And I’ll see what I can do to get my hands on a few of Bolt’s replays."
    show reva neutral with dissolve
    r "Affirmative."

    j "We don’t have any time to waste. Bolt’s going to be preparing for this match with a KPGA regimen."
    hide jett
    show accel confident at left:
        xpos -.05
    show reva at right:
        xpos .9
    with dissolve
    a "Think you can handle fourteen hours a day, Mach?"

    m"I don’t need to practice long, I just need to practice smart."
    show reva neutral2 with dissolve
    r "You need to do both."
    show accel thinking3 with dissolve
    a "Yeah, she's right. It’s only for a week, anyway."

    "The idea of fourteen hours of high-level StarCraft is enough to make my wrists sore. Still, I have to live up to my team's expectations."
    hide accel
    hide reva
    with dissolve
    m"Alright. Do we start tonight?"
    show stunt neutral at left:
        xpos .03
    show jett neutral at right:
        xpos .97
    with dissolve
    j "Obviously."
    show stunt surprised with dissolve
    s "..."
    show stunt embarassed 
    show jett unimpressed
    with dissolve
    s "Ehhhhhhh......."
    show stunt surprised with dissolve
    "Jett’s stare is enough to get him to spit it out."

    s "I kinda… maybe… sorta promised my mom that I’d make up all the chores I've been skipping out on at our PC bang."

    s "..."
    show stunt yell
    with Dissolve(.2)
    s "Look! I thought the team was definitely over, okay!? We’re StarCraft players, don’t pretend you guys don’t know the importance of time efficiency!"
    show stunt surprised 
    show jett considering
    with dissolve
    s "I need to start smoothing things over with her if I’m going to move out. C’mon, don’t look at me like that..."
    hide stunt
    show jett at center
    with dissolve
    j "Useless. Whatever, we’ll meet up at Golden Zonefire tomorrow and every day after that up until the showmatch. Mach, just ladder tonight."

    m "Right."
    show jett casual with Dissolve(.5)
    j "Reva, you free?"
    show reva neutral at left
    show jett at right
    with dissolve
    r "Yes. Why do you ask?"

    j "Go with Mach and watch him ladder for the rest of the day. See if you can pick up on any holes in his play."
    show reva surprised with dissolve
    $ renpy.pause(.5)
    show reva shy with Dissolve(.3)
    "The command seems to catch Reva off guard. She looks at the ground, at me, and then back at the ground."
    r "Very well."
    hide reva
    show accel neutral at left
    show jett neutral
    with dissolve
    j "I've got to go confirm the schedule with Bolt, among other things. With me, Accel."
    show accel thinking2 with dissolve
    a "Should have guessed. Right then."
    show jett neutral with dissolve
    j "Stunt, go handle your bullshit. Golden Zonefire tomorrow morning. Go. Everyone. Go."
    hide jett with dissolve
    hide accel with dissolve
    "Accel peels himself off of the bench and falls in line beside Jett. Stunt is quick to follow, though he turns out of the park in different direction."
    stop music fadeout 3.0
    play sound "sfx/morning.ogg" fadein 3.0 loop
    show reva neutral at center with dissolve
    "I share a glance with Reva and scratch behind my head."
    m"I was actually planning on going back to my apartment if I’m just going to ladder…"
    show reva neutral2 with dissolve
    r "Oh. Should I return home?"

    m "No, no. Uh. Why don’t you meet me there in an hour? You won't need to stay too long, I don’t think."
    show reva concerned with dissolve
    "It’s hard not to seem awkward about the proposal. Even the normally inexpressive Reva has trouble answering casually."
    $ renpy.pause(.8)
    show reva neutral2 with dissolve
    r "Very well. I will run an errand in the meantime."
    "After sharing the location of my apartment with a map from my phone, I bid her farewell. Reva fades along with green of Namdan when I trace back the path I took this morning."
    hide reva with dissolve
    stop sound fadeout 1.0
    window hide dissolve
    play sound "sfx/street2.ogg" fadein 2.0 loop
    scene bg streetday with Dissolve(1):
        align (0, 0)
    window show dissolve
    "My glazed-over eyes remain locked with the pavement as I amble my way home."

    "I know that I should feel relieved that our team still has a chance of coming together, but I can't help but worry."

    "I’m not carrying around the weight of my failed attempts to qualify for the VSL anymore. This is different."

    "It’s anxiety. A tightness in my chest that threatens to strangle me if I let everyone down."

    "I don’t know what I expected. It’s not like it’s going to get easier from here anyway. Every week in team league there’ll be a chance to cost my team a loss."

    "More than anything else, I’m frustrated by Mr. Kim's doubt. It's one thing for my friends and parents to misunderstand me, but Mr. Kim made an informed judgement that I'm not worth the trouble."

    "I jam my fists into my pockets and exhale deeply. If I ever doubted that eSports was brutal, I don’t any longer."

    jump S27GoGame

label S27GoGame:
    ##con store

    "Short as the walk is, I don’t find my nerves calming as I settle into my pace."

    "A pack of energy drinks might help me douse my angst, so I decide to cut a detour that’ll take me past Go-Mart."

    "I should probably pick up something for Reva, too. It’d be a pretty classless move to make her watch me grind out ladder games without offering anything in return."
    window hide dissolve
    $ renpy.music.set_volume(0.2, 2, channel="sound")
    scene black with squares:
        align(0,0)
    scene bg streetside2 with squares:
        align (0, 0)
    window show dissolve
    "My older brother used to always make me watch him play games back when we were kids." 
    "This is different though. She’s not watching me for fun, she’s watching to tell me how badly I suck."
    window hide dissolve
    stop sound fadeout 2.0
    play voice "sfx/storedoor2.ogg"
    scene bg store with Dissolve(1.0):
        align (0, 0)
    window show dissolve
    play sound "sfx/AC.ogg" fadein 1.0 loop
    show yeon neutral at center with dissolve
    window show dissolve
    "I brush past another customer on my way into Go-Mart and glance towards the register. Mr. Yeon smiles in my direction, but then immediately walks into the store’s back room."
    hide yeon with dissolve
    "I don’t waste time browsing and head straight for the refrigerators."
    show yeon neutral at center with dissolve
    "By the time I’m done shopping, Mr. Yeon comes out from the back room with a brown box in hand and makes his way back to the register." 
    play voice "sfx/cans.ogg"
    "I set my bottles and cans down on the counter and offer the old man a nod."

    m "Hello. This is all for today."
    show yeon smile with dissolve
    y "In a rush, are we?"
    m "Oh, uh. Not really. Why?"
    show yeon neutral with dissolve
    play voice "sfx/clatter.ogg"
    "With word that I won't run off, Mr. Yeon smiles wide and hoists the box up onto the counter, pushing aside my drinks in the process."
    "I blink, dumbfounded. But before I can ask what he’s doing, he clicks open a latch and reveals a wooden board on the underside of the box’s lid."
    play voice "sfx/can.ogg"
    "He flips it up and sets the box between us in the place where a customer might expect to have their groceries rung up."

    "A cloth sack rests beside the game board, the contents of which clack against one another and the counter. He pulls an object out of the bag and shows it to me."
    hide yeon
    show gob:
        xalign 0.5 yanchor 0.5 xpos .45 ypos 0.45 subpixel True
    show gow:
        xalign 0.5 yanchor 0.5 xpos .55 ypos 0.55 subpixel True
    with dissolve
    play music "sfx/Loading progress 1.ogg."
    y "Have you ever played Go?"


    "Go, huh? It’s a board game that’s played mostly in Asia, held in esteem similar to chess. Without meaning to, I ask the first question on my mind."
    show gob:
        alpha 1.0 ypos 0.45 xpos .45 subpixel True
        easeout .6 ypos 0.70 alpha 0.0 subpixel True
    show gow:
        alpha 1.0 ypos 0.55 xpos .55 subpixel True
        easeout .6 ypos 0.70 alpha 0.0 subpixel True
    show yeon neutral at center with dissolve
    m "Uh. Is this because I told you about my pro-gaming career?"
    show yeon smile with dissolve
    y "Let’s just say I wouldn’t be showing it to you if you didn’t. We’ll go over the rules and play a round. Just one, and my whim will be satisfied."

    m "Um. Alright."
    show yeon neutral with dissolve
    "This is strange. But if I want to keep shopping at Go-Mart, turning down Mr. Yeon will make our future interactions uncomfortable."

    "Better for one extremely awkward game of Go than an infinite amount of semi-awkward trips to the convenience store."
    window hide dissolve
    show image "bg/cg6_1a.jpg" at center with dissolve
    window show dissolve
    "Mr. Yeon pours the contents of the bag into a pair of wooden cups set beside the board. On closer inspection, they appear worn and scratched up."

    "The board itself isn’t in great condition either. The corners are chipped and its lacquer is long faded."

    "Even though I’ve never played, I’m familiar with the premise of Go. Mr. Yeon explains the basic rules thoroughly either way. "

    "The main objective is to control and capture space by surrounding your opponent’s pieces. It's not unlike StarCraft in that sense. Only, there’s no advantage in quick fingers."

    "Even if I’m aware of the basics, I don’t have the faintest clue about the game's strategy. What is this supposed to accomplish?" 
    "Once Mr. Yeon is finished explaining the rules, he motions towards my stones."

    y "Black takes the first move. You may begin whenever you're ready."

    m "Okay. For the record, I have no idea what I’m doing here."

    y "That’s alright. Just play on instinct."

    "It’s hard to hide the confusion I’m feeling, but I agree and shuffle a handful of black stones in my direction anyway."

    "If the point of Go is to control space, it seems like a good idea to form some sort of basic structure that I can play off of later."
    window hide dissolve
    show image "bg/cg6_2a.jpg" at center with dissolve
    window show dissolve
    "But not five turns into the game, Mr. Yeon begins placing his pieces dangerously close to mine. When I look up from the board, he answers me only with a smile."
    "Soon, he begins capturing my stones with relentless efficiency, never allowing me to challenge his position when I’m so focused on protecting my own."
    "I fight back to defend my territory, but the clerk's plan is always a step ahead. I fix the board with an intense stare, certain that I can somehow unlock the intricacies of Go by demanding it of myself."

    "When the board is halfway full, it becomes readily apparent that I’m going to lose."

    "Mr. Yeon glances up from the board with a raised eyebrow, smile ever-present."

    y "Would you care to stop? I don’t mean to keep you for too long."

    m "No, it's fine. Let’s finish."

    "After turning down the chance to concede, it feels appropriate that I’d somehow stage an amazing comeback. But the beatdown only continues."

    "Towards the end of the match, Mr. Yeon manages to capture more than half of my stones in a single move. My displeasure makes itself apparent with a groan."

    "I deliver my last few turns to the board hard enough to echo a clack throughout the store. Mr. Yeon scratches his chin casually, scanning the carnage he’s wrought upon my pieces."

    y "Hm. I don’t see any possible moves. I pass."

    m "And I pass too. That means the game is over, right?"

    y "That is correct."

    "I release the breath I’ve been holding in, relieved." 
    "I’m so glad to live in an era where video games exist."
    scene bg store at center
    show yeon neutral at center
    with dissolve
    "The old man replaces his Go set in the bag and box, and clears the counter of our diversion. Yet instead of reaching for my drinks to scan, he sets his eyes on me."

    y "You play to avoid losing."
    "I feel a frown form on my face. Why exactly am I getting a lesson on an Eastern board game from a cashier?" 
    "I don't say anything, so he continues."
    y "Specifically, you play to avoid the pain of a loss. It's clear to see when you have no learned habits or memorized strategies."

    y "There's nothing inherently wrong with playing that way, but you should be aware of the fact. I’m a firm believer that games showcase personality in its purest form."

    m "Was this whole thing just an excuse to share some wisdom you couldn't think of any other way to bring up?"

    "... Tch. I said that with way more disrespect than I should have. Nevertheless, Mr. Yeon’s slight smile doesn’t falter."

    y "Perhaps. Or perhaps I’m just looking for a conversation."
    show yeon smile with dissolve
    y "You didn’t quit when I gave you the chance. That’s good. But you can only go so far without playing for the win."

    y "StarCraft isn’t so different from Go. I know that because life isn’t so different from Go. Strive to win, Mach. Not to not lose."

    m "I don’t understand."
    show yeon serious with dissolve
    y "Try to. It's an important lesson."
    "A serious glint flickers across Mr. Yeon's face for a fraction of a second. When it's gone, he looks no different than before."
    show yeon smile with dissolve
    y "There’s no one else that moves those drinks off the shelf like you! I’m incentivized to have you succeed and stick around, you see."

    "He lets out a laugh, one that continues only until I smile politely in response. When he's done, Mr. Yeon rings up my drinks and hurries them into a bag."
    show yeon neutral with dissolve
    y "Right, off you go. I won’t ask you to play again with me—unless you'd like to."

    m "Um. Alright."

    "I lower my head in a bow. Not the type reserved for a venerable elder, but at least one to show that I’m thankful."

    "The door rings when I hurry through it, leaving Mr. Yeon to endure the sickly linoleum of his store alone. "
    window hide dissolve

    scene bg streetside2night with dissolve:
        align (0, 0)
    play sound "sfx/nightcricket.ogg" fadein 1.0 loop
    window show dissolve

    "In a roundabout way, I think Mr. Yeon’s little diversion might actually help."
    
    "It’s nice to know that he cares enough about me to offer advice, even if it’s just because I shop at his store."

    "Whether or not that business about Go and not losing is true remains to be seen. Is an aversion to losing really that ingrained in my DNA?"

    "... Go-Mart. Huh." 
    
    "Alright Mr. Yeon, I’ll admit that’s pretty clever."

    "It seems much darker outside than it was when I came into the store. I reach to check the time on—shit!"
    stop music fadeout 2.0
    "I have a half dozen missed calls from Reva. Did that Go match seriously take more than an hour?!"
    play music "sfx/Warsong.ogg"
    "An urgent need to get back to my apartment replaces my thoughts of Mr. Yeon and board games. "

    "I weave through pedestrians as best I can while simultaneously texting an apology to Reva."
    window hide dissolve
    play voice "sfx/run.ogg"
    scene black with squares:
        align (0,0)
    pause 1
    scene bg streetnight with squares:
        align (0, 0)
    window show dissolve
    "My feet carry me as fast as they can. If Reva got tired of waiting in front of my door and left, I’m screwed."
    play voice "sfx/StepDown.ogg"
    stop sound fadeout 2.0
    "I pant my way up my apartment’s stairs and pause in the hallway to find that she isn’t there. Frustrated, I sigh and force open my door."
    window hide dissolve
    play sound "sfx/doorclose.mp3"
    #show reva
    scene bg apartmentnight with dissolve:
        align (0, 0)
    window show dissolve
    "I'm dead. I'm so dead. Why didn't I keep track of the time? Why now, why when so much is on the line?"
    "As I rack my brain for an excuse I can offer Jett, I look up to find that my apartment is already occupied."
    stop music fadeout 1.0
    show reva expected at center with dissolve:
        ypos 1.1
    r "You are late."
    show reva at center:
        easein .5 ypos 1.0 subpixel True
        easeout .1 ypos 1.01 subpixel True
    $ renpy.pause(.6)
    "She rises from her seat on my bed and points at the computer."
    play music "sfx/Stunt.mp3"
    r "Ladder."

    m "How… How are you in my room?"
    show reva neutral2 with dissolve
    r "The door was not locked. I let myself in when you failed to answer my calls."

    m "You just… came in?"
    show reva glasses with dissolve
    r "{w=1}Yes."

    "My breathing calms as my panic subsides. I forgot to lock my door, huh? I guess this is better than showing up to find my computer missing."

    m "Right. Okay. Sorry, I got caught up with some old guy. Here."
    play voice "sfx/plasticbag.ogg"
    show charge:
        alpha 0.0 xalign 0.5 yanchor 0.5 xpos .7 ypos .6 subpixel True
        easein 1.0 alpha 1.0 ypos 0.5 subpixel True
    "With a rustle, I reach into the bag I’m carrying and hand a drink to Reva."
    show reva neutral2 with dissolve
    r "Caught up?"
    hide charge with dissolve
    "Reva takes my offering without so much as looking at it. Whether or not she’s actually going to drink it, I’ve done my due diligence as a host."

    m "It’s hard to explain."

    r "You do not need to explain your relationship with an old man if you would rather not."

    "Even though I’m pretty sure it’s a joke, Reva doesn’t smile to show it. I offer a nervous laugh and fall into my computer chair, trying to move on from the topic of my tardiness."

    m "So, uh. Right. Ladder. Is there something you think I need to practice?"
    show reva neutral with dissolve
    r "You will want to match against protoss players only. Quit the match if your opponent is terran or a zerg."

    m "Wait...{w=.3} But my ranking!"
    play voice "sfx/grandmaster.ogg"
    queue voice "sfx/beepboop.ogg"
    "With a few keystrokes, I display my proudly earned grandmaster badge accompanied by a rank in the double digits."

    m "If I leave two thirds of my games tonight, I’m going to lose a bunch of ladder points."
    show reva frown with dissolve
    r "Are your ladder points really that important?"

    "Absolutely."

    m "Well..."
    hide reva with dissolve
    play voice "sfx/login.ogg"
    "Without a word, Reva takes the mouse from me and logs out of StarCraft 2. Her fingers dance across the keyboard, and a second later we’re logged into her barcode account."
    play voice "sfx/beepboop.ogg"
    "The grandmaster badge accompanying Reva's anonymous username is ranked even higher than mine."
    show reva neutral at center with dissolve
    r "Play on this one then. I do not care about ladder rank, and neither should you."

    "I scratch behind my head and have the sense to look embarrassed. She’s right. It’s pretty dumb for me to worry about ladder rank at a time like this."
    stop music fadeout 2.0
    hide reva with dissolve
    "With a nod and a click, I search for my first match of the night. It takes a handful of games before I’m finally matched up against a protoss." 
    "Ugh, he’s got one of those weird names with random capitalization." 

    "Reva sits just over my shoulder from the edge of my bed, eyes fast on the monitor."
    window hide dissolve
    jump reva_ladder
    r "Your APM is low."

    "I wince and respond with a flurry of unneccesary keystrokes. I’ve never cracked 300 APM, even when I’m focused on doing so."

    "A minute or two passes without comment, though it’s hard to tell whether or not that means she thinks I’m playing well."

    r "Your engineering bays are late."

    "Are they? They are. Dammit. I whip my mouse hard, box a pair of SCVs, and slam down the two delayed structures."

    "Delayed upgrades or no, I manage to keep a close enough eye on my opponent’s tech that I have a massive swell of vikings by the time his colossus come into play."

    "His army gets caught in an awkward position when he tries to establish his third base, allowing me to power forward into his base. It’s a win I’d normally celebrate with a self-assured smile."
label revaroom2:
    show bg apartmentnight:
        align (0,0)
    show reva neutral at center
    with dissolve
    window show dissolve
    "But with Reva over my shoulder, I’m forced to feign humility in my victory. I turn towards her and motion towards the screen."

    m "Well? What do you think?"
    show reva glasses with dissolve
    "She adjusts her glasses and purses her lips, taking a long moment to decide on her response."
    show reva neutral with dissolve
    r "{w=.5}He was bad. But you capitalized on his mistakes, so I have no major complaint."
    show reva neutral2 with dissolve
    r "A good player won’t let you obtain free information. Use your scans wisely."

    m "I thought I used them pretty well, didn’t I? Scouting is one of the things I’m best at."
    show reva neutral with dissolve
    r "Not particularly. And you should always aim to be even better."
    "I grumble and turn to queue up another game. Yet another thing to focus on, I guess."
    hide reva with dissolve
    jump reva_ladder2
    "I had thought that Reva’s low-key attitude might have made her a little bit lenient with my mistakes. But she’s not all that different from Jett, minus how she delivers her criticism."

    "My next match is on the largest map in the current ladder pool. I’ll have a pretty easy time defending my expansions with the way that the map’s choke points are constructed."
    #rewrite
    "Rather than poke and prod with marines or go for early aggression, I throw down a quick third base in a far-flung corner of the map shortly after I begin my first expansion."
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

    "Reva offer the advice too firm to be called a suggestion, and I find myself moving the mouse to do as instructed. This gaffe is going to set me back a fair bit."
    hide reva with dissolve
    "I gear up for a drawn out match by focusing on my upgrades and base defense. It’s not long before my protoss opponent and I have split the map in half and are jockeying for position."

    r "Build more defenses. You can afford a dozen planetary fortresses."

    m "Is that really necessary?"

    r "Mach, your opponent is protoss. Protoss players will stop at nothing to cheat an honest terran out of an earned win."

    "Funny. I typically imagine balance whiners as loud and obnoxious in real life. I wonder if she quit playing random out of guilt."

    "Still, I oblige her and cram as many static defense structures as I can into a vital choke point."

    r "There is an observer over your army."

    "I squint to find that she’s right. Damn, how did I not catch that earlier? With a scan, I pick off the protoss scout and reposition my units."

    "It takes a few minutes to adjust my army composition to one that better suits the extreme late game, but I’m soon ready to clash with my opponent."

    "At this point, StarCraft becomes less about strategy and more about patience. It's important to know when to stalk and when to pounce."

    "I sense an opening at last and rush into my opponent’s weak flank. Out of the corner of my eye I can see Reva tensing up, invested as much as I am in the outcome of the battle."

    "But try as I might, my snipes don’t connect with the high templar scattered amongst the protoss army." 
    "He drowns my units in psi storm and steamrolls down the center of the map, destroying my constructed defenses along the way."

    "I struggle pointlessly to mount a counteroffensive, but the damage is done. I’m forced to tap out a gg and quit the match with a huff."
label revaroom3:
    scene bg apartmentnight with dissolve:
        align (0,0)
    play sound "sfx/nightcricket.ogg" loop
    window show dissolve
    r "He controlled his army better than you did."
    show reva neutral at center with dissolve
    "I spin in my chair to face Reva with a frown."

    m "If he didn’t, I would have won. Ugh, that was so close!"
    show reva glasses with dissolve
    r "Yes, it was."

    "At least she can concede a point to my credit when it’s deserved. But damn, that match took a while. As long as Go with Mr. Yeon, if not longer."

    m "What time do you need to leave?"
    show reva neutral with dissolve
    r "{w=1}Are you throwing me out?"

    m "What? No. I’m just saying if you need to be home at a certain time, let me know."

    r "I do not."

    m "Okay."
    $ renpy.pause(2)
    "Sheesh. Why does talking to her feel so unnatural? This has to be intentional on her part."

    m "I need a break."
    show reva2 neutral2 at center 
    hide reva
    with dissolve

    r "Your opponents will use every wasted moment to become better than you. Breaks are dangerous."

    m "Just a short one! I’m thirsty, anyway. We’ll be back on the ladder with a vengeance afterwards."
    $ renpy.pause(.5)
    r "Hm... {w=1.0}{nw}"
    extend "Thirsty... {w=1.0}{nw}" 
    show reva expected at center:
        alpha 0.0
        linear .1 alpha 1.0
    show reva2 at center:
        alpha 1.0
        linear .2 alpha 0.0
    stop sound fadeout 1.0
    play music "sfx/Stunt.mp3"
    extend "I see."
    play voice "sfx/hit.ogg"
    "My fist clenches involuntarily as I reach for a can, nearly forcing me to knock it over. I offer Reva an exhausted look before cracking open my drink."
    show reva smile with dissolve
    "Not to be outdone, I take a poised sip before glancing casually in her direction."

    m "So, why do you pretend to be a guy on the internet?"
    show reva surprised with dissolve
    "Now it’s Reva’s turn to tense up. Her face contorts, eyes glazing over as if scanning her internal database for a scathing comeback."
    $ renpy.pause(1)
    show reva sweat with dissolve
    "404, comeback not found."
    r "I do no such thing! Details about my private life are kept just so: private. Others simply assume."
    m "Well, that’s all coming to an end if we’re going to be on Team Enoch, isn’t it?"
    show reva neutral with dissolve
    r "I suppose."

    m "Excited about living in a team house?"
    show reva glasses with dissolve
    r "As long as it is being paid for, yes."

    m "Oh, in it for that eSports money, eh?"
    show reva neutral with dissolve
    r "Of course. Since primary school I have dreamed of my own bunk bed and free cup noodles."
    show reva smile with dissolve
    "Reva is refreshingly realistic about pro-gamer living conditions. Maybe she can talk some sense into Stunt."
    stop music fadeout 3.0
    show reva neutral with dissolve
    r "To be frank, anything is better than life back at home."

    m "Oh? Trouble with your parents?"
    r "No. My parents worked hard to give me the opportunities they never had, and for that I will always be grateful. But they live far from Seoul, so I was isolated from my friends for most of my life."
    m "You mean your online friends?"
    show reva shy with dissolve
    $ renpy.pause(.7)
    show reva neutral with dissolve
    r "Yes. But now, I have the chance to make my own way. I take pride in the fact that I have turned my skills into a living, no matter how meager."

    m "You should be. Most people living off of StarCraft do it with the support of a team, but you've managed on your own. You have the right to be proud."
    show reva concerned with dissolve
    play music "sfx/Searching For Game Master.ogg" fadein 1.0
    r "Maybe. But sometimes, even though I am happy with my accomplishments, I lack the confidence to devote more of myself to this game."

    m "Really? I wouldn’t have expected to hear something like that from you."
    show reva neutral2 with dissolve
    r "Why?"

    m "I don’t know. You kinda seem like the resolute type. No regrets. That sort of thing."
    show reva neutral with dissolve
    "I’m bad at putting into words my impression of Reva, but she seems to understand what I mean by the nod she offers."
    show reva glasses with dissolve
    r "You are correct that I always give full effort to my pursuits."
    r "However, this is not a matter of regret. Normally, I can be satisfied even in failure if I have done my best."
    show reva neutral2 with dissolve
    r "But what if the task was not worth working towards in the first place?"

    m "What do you mean? eSports is like anything else, isn’t it? It’s a climb to the top."
    show reva neutral with dissolve
    r "It is. But StarCraft is inherently less valuable than most other things. Art, athletics, education, science, a corporate career. Objectively, my time is better spent on almost anything other than pro-gaming."
    r "But I do not believe I can truly distinguish myself at any of those things, while it is possible as a pro-gamer." 
    show reva glasses with dissolve
    r "I was born in the right country, I am the correct age, and I have enough required talent."
    show reva neutral with dissolve
    r "Even then, it is not logical for me to spend so much time and effort on what should statistically prove unrewarding. Yet I cannot bring myself to turn down the chance to compete."
    m "I have the same drive, so I can at least understand that. But you really won't do something if you can’t be the best at it? And the way you talk about your motivation..."

    m "Do you even like StarCraft?"
    show reva concerned with dissolve
    $ renpy.pause(1.5)
    r "{w=.5}No. {w=.5}I don't."

    "She answers bluntly and then looks away. I have nothing to say to that."
    "High level StarCraft isn't always fun in the traditional sense of the word, but it sounds like Reva genuinely doesn't enjoy the game." 
    "For her to be as good as she is with that holding her back is hard to understand."
    "StarCraft's greatest players have always credited their love of the game as a major factor in their success. How far can she hope to go without that advantage?"
    show reva neutral with dissolve
    play sound "sfx/canopen.ogg"
    "With silence filling the space between us, Reva takes the opportunity to try out the drink I brought for her. On the first taste, she screws her face up and hurries to set it down."
    show reva frown with dissolve
    r "How can you stand something so sugary?"

    "I shrug, since I don’t have a good answer. It’s not like I can explain why something tastes good."
    show reva neutral2 with dissolve
    m "Where are you living if not with your parents?"
    show reva neutral with dissolve
    r "Do you know what a goshiwon is?"

    m "... No way. Really?"

    "That’s a term that showed up in one of my online lessons. If I remember correctly, it’s an absurdly tiny type of apartment. Literally the size of a closet, with a low price to match."

    r "I live on the edge of Seoul, so rent is inexpensive. I pay with my winnings from online tournaments."
    show reva glasses with dissolve
    r "Matches on the last week of every month if I have not yet hit my quota can be very stressful. That has been my life since I graduated from high school."

    m "Damn. You don’t mind the lack of space?"
    show reva smile at center with dissolve
    r "I do. I am enjoying the chance to stretch while it lasts."
    show reva at center:
        easein .3 ypos 1.1
        easeout .1 ypos 1.09
    play voice "sfx/bed.ogg"
    "She demonstrates by falling back onto my bed and fully extending her legs. I shake my head and try not to laugh."
    $ renpy.music.set_volume(0.2, .5, channel="sound")
    m "It’ll last. The team house will be a nice upgrade for the both of us."
    show reva at center:
        easein .5 ypos 1.0
    "Reva sits up and rests her arms on her knees."
    show reva neutral with dissolve
    r "Break time is over. Return to the ladder."

    m "Alright, alright."

    "I spin my chair back towards my computer and resume my training."
    hide reva with dissolve
    "The blue light from my computer monitor shines in Reva’s glasses, her advice and my grumbling all that is said between us."

    "The matches bleed into each other, one foe falling after another. I’m in a protoss-slaying groove."

    "I don’t often find myself on winning streaks on ladder. Part of me wonders if I’m playing this well only to impress her."
        
    "Reva goes quiet in the middle of a particularly intense game, leaving only the sounds of my keyboard and mouse clicks to mingle with the game sounds blasting from my headphones."

    "I manage to prolong my win streak with a multi-pronged attack that forces my opponent to tap out. With a triumphant grin, I push off the desk and turn."

    m "Boom! Three in a…"
    stop music
    play sound "sfx/nightcricket.ogg" loop
    "... And find that Reva has fallen asleep on duty."

    "Well. That explains why she didn’t point out that my dropships were delayed. Is it really that late?"

    "I rest my hand against my cheek. Should I wake her up and tell her to go home?"

    "Ugh. She looks too peaceful for me to do that in good conscience. I can just sleep on the floor, I guess."

    "I bunch up a hoodie from my dresser into a makeshift pillow and ease myself into the space under my desk. The ground isn’t exactly comfortable, but with enough shifting around I find a decent spot."
    "Not long after, my eyelids grow heavy and sleep claims me."
    window hide dissolve
    stop sound fadeout 2.0
    scene black with midfade:
        align (0,0)
    pause 1
    play sound "sfx/Morning.ogg" fadein 4.0 loop
    scene bg apartmentday with midfade:
        align (0, 0)
    window show dissolve
    "I'm on the floor. Why am I on the floor?"

    "The trash on my desk is gone and my bed is made. I literally never make my bed."
    "... Right. Reva."
    "When I stand, an ache in my back forces me to wince. It’s nothing serious, but I must have turned over in my sleep onto a weird angle."

    "A text message from Reva awaits me when I check my phone for the time."

    #DISPLAY TEXT MESSAGE SOMEHOW. make a joke here too with the old texts
    #female mach, she steals clothes
    r "I apologize for falling asleep. I will see you later."
    play voice "sfx/lock.ogg"
    "Terse, as I’ve come to expect from her. I lock my phone's screen and slip it into my pocket."

    "The week ahead is going to be tough. Six days probably isn’t enough time to make any sort of serious breakthrough in terms of my mechanics or game sense."

    "But it’s long enough to craft a game plan that might edge out Bolt. My biggest issue with the matchup is that I have no idea what to expect from him."

    "How does a Brood War player go about learning StarCraft 2? Maybe I should ask Jett or Accel."

    "Whatever the case, the team is probably waiting for me at Golden Zonefire. I should hurry over."
    stop sound fadeout 2.0
    window hide dissolve

    
    jump S28PracticeWithStunt

label S28PracticeWithStunt: 
    scene black with squares:
        align (0,0)
    pause 1
    play music "sfx/Blue Pineapple.ogg" fadein 4.0
    scene bg cafe with squares:
        align (0, 0)
    window show dissolve

    #____

    #BACKGROUND: PC cafe
    show accel neutral at left
    show stunt phone at right
    with dissolve
    a "Morning, Mach."

    m "Morning."

    "An oblivious Stunt fails to notice my arrival. He's too focused on his white whale."

    m "Where’s Jett?"
    show accel thinking2 with dissolve
    a "Trying to wrangle some of Bolt’s replays I’d guess. We couldn't find him at the Shock team house yesterday, so I spent the rest of the evening moving out of the Crash house."
    m "That sounds awkward."
    show accel confident with dissolve
    a "You're not wrong."

    m "Well, Reva’s probably gonna be late today. She probably needs to go back home after—"
    show accel concerned
    show stunt neutral grin
    with dissolve
    "I try and fail to stop myself in time. The allure of {i}PopPop Safari{/i} now fails to hold Stunt's attention."

    s "She slept at your place? Did you bang her?!"

    m "No! It wasn’t like that at all. We just practiced."
    show stunt smug with dissolve
    s "Ooh, genius move Mach! She seems pretty inexperienced, smart to let her practice a bit before she—{w=.5}{nw}"
    play sound "sfx/punch.ogg"
    show stunt surprised at Shake((0.77, 1.02, 0.5, 1.0), .15, dist=8)
    s "Ow! {w=.5}Okay, okay! Sheesh!"
    "I follow up the shoulder punch with a pat and then take note of Accel's serious expression."
    show stunt neutral at right with dissolve
    a "Mach. You didn’t actually do anything, right?"
    m "No, I didn’t."
    show accel thinking with dissolve
    a "Good. Don't get involved with your teammates."
    show stunt surprised with dissolve
    s "Eh? Why?"
    show accel thinking2 with dissolve
    a "Seriously? I'm sure you can figure this one out on your own."
    show stunt neutral with dissolve
    s "If you break up, things get awkward?"
    show accel neutral with dissolve
    a "If you get together, things get awkward. If you break up, the team loses a player. It’s bad news, even in the best case scenario."

    m "She came over to watch me ladder. It got late, and she fell asleep during a long game. That’s all."
    show accel thinking2 with dissolve
    a "Then there’s no problem."
    show accel laughing 
    show stunt phone
    with dissolve
    a "Being a coach means I get to deal with fun stuff like telling you who you can and can’t date."
    play sound "sfx/snap.ogg"
    show accel neutral with Dissolve(.2)
    show stunt surprised
    with dissolve
    "Stunt’s hand slinks for his phone, but Accel snaps for attention before the protoss can get back to tapping away at animal bubbles."
    show accel laughing with dissolve
    a "Enough, Stunt. Time for practice. Mach, you too."
    show stunt neutral with dissolve
    m "Right."

    window hide dissolve
    scene black with squares:
        align (0,0)
    pause 1
    scene bg pcbang with squares:
        align (0, 0)
    play sound "sfx/apmsound.ogg" fadein 2.0 loop
    window show dissolve
    "By noon, my wrists are sore from a morning of anti-rush defense. Without anything specific to practice against, Stunt spammed me with game after game of proxy gates, cannon rushes, and one base all-ins."

    "I feel prepared in the incredibly unlikely case that Bolt risks the match on something like a two gate. Stunt’s a one-note protoss, but he plays that note pretty damn well."
    show stunt neutral at center with dissolve
    m "Can you try something else for a change? My brain is starting to fry."
    show stunt neutral grin with dissolve
    s "Heh, I’m not even warmed up yet. You're only able to defend against these builds because you're expecting them."

    m "Obviously! The point of a cheese is to catch the opponent off guard! What's the point of cheesing when it's literally all you can do?!"
    show stunt yell with dissolve
    s "Ugh, you don’t understand. Cheesing is an art. An art that I will be the first to master."

    show accel thinking3 at left:
        xpos .02
    show stunt at right:
        xpos .98
    with dissolve

    a "Seriously though, Mach needs to prepare for more than just your one-base all-ins. Try playing standard for a change."
    show stunt frown with dissolve
    s "Ehh. Fine."
    hide stunt
    hide accel
    with dissolve
    show jett unimpressed at center with dissolve
    "Just then, Jett steps through the doors of Golden Zonefire at a fierce pace, saving me from more of Stunt’s abusive builds."

    "But the relief I feel at her arrival shatters when I catch sight of the figure at her heels."
    play music "sfx/Greased Lightning Intro.ogg"
    queue music "sfx/Greased Lightning Loop.ogg"
    hide jett
    show jett unimpressed at center:
        xpos .5
        easein .5 xpos .25
    show rival smug at center behind jett with dissolve:
        xpos .5
        easein .5 xpos .7
    "Before I can form a question at Bolt’s presence, both he and Jett are standing before us. She shoots an annoyed glance at him before speaking."
    show jett considering with dissolve
    j "He insisted on speaking with you before he would agree to play."

    "Bolt lifts his chin at me, savoring the moment. I need something from him—a showmatch—and he’s well aware of the power it grants him."
    hide jett
    show rival bored at center
    with dissolve
    b "So, Mach. Still desperate to make a name for yourself?"
    "I match his aloof expression with a hard one, determined to show that he can't intimidate me."
    m "Our sponsor needs a demonstration of the team’s potential. It’s not about me."
    show rival smug with dissolve
    b "Don’t kid yourself, this is all about you. I’d be facing Jett, Accel, or one of the wannabe dishwashers you managed to clown into signing if it wasn't. Do you think I haven't read what they're saying online?"

    "I draw in a sharp breath, to Bolt’s amusement. He shakes out his wrist and offers a shrug."
    show rival fierce with dissolve
    b "I normally have better things to do than play out a showmatch in a lesser game. But hey, you’ve caught me at a good time."
    show rival smug with dissolve
    b "My next Brood War match isn’t for a few weeks. Got just enough time to brush up on my SC2 and ship you back across the Pacific."

    b "Did you know that my team manager won’t even let me play Star2 in the Shock team house? They say it’s distracting to the other players."

    "I reach for another calming breath, but find myself choking on rage instead. It’s that smile of his."

    m "What, you came here just to talk some trash? Quit wasting my time and accept the match."
    show rival bored with dissolve
    b "I accept. And I’ll do you one better than you’ll do me. Catch."
    hide rival with dissolve
    "Bolt pulls something out of his pocket and tosses it at me. My reflexes don’t fail me and I snag the small, black object in midair."
    show usb:
        alpha 0.0 xalign 0.5 yanchor 0.5 ypos .7 subpixel True
        easein 1.0 alpha 1.0 ypos 0.5 subpixel True
    with dissolve
    "When I open my hand, I find a thumb drive."

    hide usb with dissolve
    m "What…?"
    show rival fierce at center with dissolve
    b "Fifty replays. Study them all you like. You'll have no excuse when you lose."
    show rival bored with dissolve
    b "By the way Jett, let me give you a tip. Next time you go behind my back for replays, don't try to get them from someone that shares my feelings on your opportunist bullshit." 
    show rival smug with dissolve
    b "Your foreigner mascot is lucky that I'm feeling generous."
    hide rival
    show stunt notcool at center
    show jett unimpressed at right
    show accel concerned at left
    with dissolve
    "With an infuriating air of superiority, Bolt turns to leave. My teammates visibly share my frustration, but none of them rush to my defense."

    "Maybe it’s for good reason. I can't keep relying on Jett or Accel to bail me out of trouble."

    "Beating Bolt isn't their responsibility. It's mine."
    #choice?
    hide jett
    hide stunt
    hide accel
    with dissolve
    stop music fadeout 5.0
    m "Hey, Bolt."
    show rival bored at center with dissolve
    "He turns, mild surprise showing on his face when I flick the thumb drive out of my hand and at his feet."
    m "I won't lose to you again. Remember it."
    show rival smug with dissolve
    b "Tell yourself that."
    "He shows his teeth in a smirk and crushes the flash drive under his heel." 
    show rival at Shake((0.5, 1.0, 0.5, 1.0), .2, dist=4)
    play voice "sfx/crunch.ogg"
    $ renpy.pause(.15)
    show rival fierce at center with dissolve
    b "Just like you told yourself you could qualify for VSL."
    window hide
    show image "char/bolt/picnic.jpg":
        align(0,0)
    play voice "sfx/heartbeat.mp3"
    play sound "sfx/muffledapm.ogg" fadein 1.0 loop
    $ renpy.pause(1.0)
    hide image "char/bolt/picnic.jpg" with Dissolve(.2)
    window show dissolve
    pause .4
    hide rival with dissolve
    "Bits of plastic and metal are all that remains of the USB when he lifts his foot to continue on his way out."
    "The tension remains long after Bolt's departure. Finally, Jett enters my personal space, eyes sharp and locked with mine."
    show jett angry at center with Dissolve(.2)
    j "Why did you do that?! We needed his replays!"
    hide jett
    show accel thinking at center:
        xpos .7
    show jett angry at center
    with dissolve
    "Accel steps forward and places a hand on Jett’s shoulder."
    show jett neutral with dissolve
    a "Bolt was trying to get into Mach’s head. You know that, Jett. It was the right call."
    #he did
    hide accel
    hide jett
    show stunt neutral at center:
        xpos .35
    with dissolve
    s "Dang. He really didn’t feel like leaning over to pick it up, huh? Those things are like ten thousand won."
    show stunt at center:
        easein .5 xpos .2
    show accel concerned at right:
        xpos 1.3 alpha 0.0
        easein .5 xpos 1.05 alpha 1.0
    show jett unimpressed at right:
        xpos 1.2 alpha 0.0
        easein .5 xpos .8 alpha 1.0
    $ renpy.pause(.5)
    "The quip earns him a perplexed stare from Accel and Jett. I'm too distracted to even react."
    show jett neutral3 
    show accel neutral
    with dissolve
    j "Whatever. Mach, if you’re going to be a showman, save it for when it’ll gain you some fans."
    show stunt neutral grin with dissolve
    s "That gives me an idea for a ceremony after you beat this guy! Get like ten flash drives and—"
    show accel thinking2 with dissolve
    a "Hey Stunt, I’ve got a better idea for a ceremony. We sign a contract with Enoch and move into our team house. How’s that sound?"
    show stunt frown with dissolve

    s "That’s not as funny as what I had in mind."
    show jett neutral with dissolve
    j "Enough banter. Get back to practicing."
    m "... Can we take a break or something? I need a minute."
    show jett unimpressed with dissolve
    j "We don't have a minute, especially without replays. Practice. Now."
    hide stunt 
    show accel thinking3
    with dissolve
    "I quietly follow Stunt's lead back towards the PCs. Accel and Jett move in and take their seats behind us."
    show jett neutral with dissolve
    j "From the top. And no rushes, Stunt."
    window hide dissolve
    stop sound fadeout 2.0
    jump S29GettingDinner
#YOU CANT WIN
label S29GettingDinner:
    scene black with midfade:
        align (0,0)
    play sound "sfx/street3.ogg" fadein 4.0 loop
    pause 1
    scene bg streetsidenight with squares:
        align (0, 0)
    $ renpy.music.set_volume(.2, 1, channel="sound")
    play music "sfx/Blue Pineapple.ogg" fadein 2.0
    window show dissolve
    "I have absolutely no clue how anyone can practice for more than ten hours a day."

    "My wrists ache. My eyes hurt. My subconscious won’t consider anything but unit compositions and attack timings. And I can't get Bolt's stupid smirk out of my head."

    "Worse still, with Jett forcing Stunt to play standard, our practice wasn't productive at all."

    "She didn't seem happy with me when she left to meet with the producers at the VSL studio. But after so many games, it becomes impossible for me to focus."

    "What else are we supposed to do? Reva doesn’t seem like she’s in practice for any race but terran."

    "Do I even have a chance against Bolt? Did I ever in the first place?"
    show stunt yell at left:
        xpos .02
    show accel neutral at right:
        xpos .98
    with dissolve
    s "Dude. How does anyone macro!? It’s boring, exhausting, and makes you consider zillion variables. Economy management is so stupid."
    show accel thinking2 with dissolve
    a "You just described what StarCraft is supposed to be, minus the boring part."
    show stunt neutral
    with dissolve
    s "Well I don’t like it. I’m at my best when I can focus microing. Who says I should have to play a game past the ten minute mark?"
    show accel laughing with dissolve
    a "No one, as long as you're okay with an awful winrate."
    window hide dissolve
    scene bg streetside2night2 with dissolve:
        align (0, 0)
    play sound "sfx/frying.ogg" loop
    window show dissolve
    "With practice done for the day, I agreed to join Accel and Stunt for dinner while Jett deals with logistics and setup for the match."
    "I’m led down a smoky side street where greasy and fragrant smells mingle. My experience with street food so far hasn’t been great, but I trust the judgement of Stunt and Accel."

    "Row after row of stalls are thick with customers clamoring for a hot meal. The three of us browse the various offerings before Stunt insists on one in particular."
    show stunt neutral at center with dissolve:
        xpos .4
    s "Do you like bindaetteok, Mach?"

    m "{w=.5}Sure, yeah. Whatever's fine."
    hide stunt with dissolve
    "The single cook manning the stall cleaves through customer orders faster than I think possible. It isn’t long before we’re walking away from the stall, paper wrapped pancake in hand."
    stop sound fadeout 2.0
    show stunt neutral at left:
        xpos .02
    show accel neutral at right:
        xpos .98
    with dissolve
    "We settle for a seat on the curb, far enough away from the foot traffic to avoid being trampled."
    show accel thinking with dissolve
    a "Reva’s going to run into trouble with Jett if she doesn’t show at Golden Zonefire again this week."
    show stunt neutral grin with dissolve
    s "Eh. She can only help Mach so much. Besides, it’s not like she can skip out on practice at the team house."
    show accel neutral with dissolve
    a "Have you ever even been inside a team house, Stunt?"
    "The protoss forces down his food with a thump to the chest."
    show stunt neutral
    with dissolve
    s "No. But I’ve seen pictures."
    show accel thinking2 with dissolve
    a "It’s an informal setting. It isn't hard to sleep in or slack off, but the type of people that do that usually don’t become pro-gamers. Or, at the least don’t last long as one."
    show stunt frown with dissolve
    s "We still don’t have any subs. Isn't that going to be a problem?"
    show accel neutral with dissolve
    a "Let’s worry about one thing at a time. There won’t be much need for subs if we don’t do our best this week."

    "Still, the team is tiny. Five people, including management? Jett wasn’t kidding when she said she wanted a lean team."

    "The sudden thought of a team goshiwon is almost enough to make me smile."
    show stunt smug with dissolve
    s "Yo, Accel. What did you do with all of your prize money from Brood War?"
    show accel laughing with dissolve
    m "That’s kind of a personal question, isn’t it?"
    show accel neutral with dissolve
    a "I don’t mind answering. Spent about half of it on general living expenses and stuff for my family. The rest I’ve got saved."
    show stunt yell with dissolve
    s "Lame. What’s the point of winnings if you don’t spend them?"
    show accel thinking with dissolve
    a "I've earned forty million won or so, not counting salary. That may sound like a lot, but it’s easy to go through if you aren’t responsible."
    show stunt neutral grin with dissolve
    "Deaf to the sense Accel is trying to talk into him, Stunt stares off into space with stars in his eyes."

    s "If I won the VSL Grand Final, I’d buy a car, a house, a new PC........"
    show accel thinking2 with dissolve
    "He continues, rattling off a list of a dozen superfluous objects in a way that only someone who has lived without worrying about paying rent can." 
    
    "Accel and I both take the chance to eat without interruption."
    show stunt neutral with dissolve
    s "Jett’s still got the hundred million won from the first VSL Championship, yeah?"
    show accel neutral with dissolve
    a "That plus some, probably. Why?"
    show stunt fist with dissolve
    s "I wonder if I could convince her to trick out the team house..."
    show accel laughing with dissolve
    a "Feel free to ask. Just make sure I'm there for her reaction."
    show stunt neutral 
    show accel neutral
    with dissolve
    s "What about you, Mach? What would you do with your big winnings?"

    m "I don't know. Save it or something."
    show stunt yell with dissolve
    s "And I thought that only the chicks on our team were boring."
    show accel thinking2 with dissolve
    a "Don’t forget that all the time you spend climbing StarCraft's ladder, someone else spends climbing the corporate ladder. If you're only in eSports for the money, just get a real job."
    show stunt neutral grin with dissolve
    s "Psh, it’s no big deal. After I make it big as the next protoss bonjwa, I’ll just get a job as a coach or a team owner. I’ve got it all planned out."

    "There’s no convincing Stunt at this rate, not that I can blame him. I wasn’t any more responsible when I was his age."
    hide stunt
    hide accel
    with dissolve
    "With a final bite, what’s left of my bindaetteok is little more than grease on a napkin. I’m joined by my teammates when I move to toss away the trash."
    show accel neutral at left:
        xpos .15
    show stunt neutral at left:
        xpos -.1
    with dissolve
    a "Heading home, Mach?"

    m "Yeah. Gonna ladder for a bit and then sleep."
    show accel thinking2 with dissolve
    a "Gotcha. I’ll be at the cafe by ten. Don’t be late."
    show stunt neutral grin with dissolve
    s "Not like we have anything better to do."
    hide stunt
    hide accel
    with dissolve
    stop music fadeout 2.0
    "The three of us turn separate ways out of the alley. I endure the walk back to my apartment in silence."
    stop sound fadeout 2.0
    window hide dissolve
    jump S30Reflection2

label S30Reflection2:
    scene black with squares:
        align (0, 0)
    pause 2
    scene bg apartmentnight with squares:
        align (0, 0)
    play music "sfx/Searching For Game Master.ogg" fadein 2.0
    window show dissolve
    "I stare at my cellphone, the light coming from its screen bright enough to make my eyes glaze."

    "Then, it goes dark, and I slide my thumb over its screen to wake it." 
    play voice "sfx/unlock.ogg"
    "I’ve repeated this ritual four times now."
    "My head falls back against my chair, and I close my eyes. Why do I feel like this?"

    "It’s been almost two weeks since I last spoke with my parents. Admittedly, I’ve been busy with StarCraft since I met Accel and Jett, but I’m still overdue for a call."

    "My finger hovers over the contact number. Before it can fall to dial them, the phone escapes my hand and falls back onto the desk."
    play voice "sfx/can.ogg"
    "Does it really matter? I don’t have much to say. "

    "‘Hi Mom, is Dad there? Yes everything is fine. No, I’m not dead. No, I haven’t given up yet.’"

    "Telling them about the team might be for nothing. They'll pretend to share my happiness in a victory, but there’s always an underlying cynicism to every congratulation from them."

    "A win isn’t a win. It’s another crumb leading me to chase a pointless eSports dream and away from the life they think I should be living."

    "It feels wrong to be cross with them. They raised me, paid for my existence. I’d be an ingrate to ask for more."

    "And yet, I do. I want them to accept my goals for what they are. To hope for more than that I’ll grow out of StarCraft."
    "It’s the same with my friends from high school. They pretend not to, but I know that they look down on me." 
    "'It’s a video game. Why do you care so much? C'mon man, it's time you grew out of this.'"
    "When is it right to give up on a dream? How many failures does it take before you say: Alright, I’m done trying. I’ll just take a job at the family business."

    "If I lose to Bolt, should I quit StarCraft? Would it be nothing but pride to continue on?"

    "Even if I win, what then? What if the team does poorly? What if the team does well, but I hold them back?"

    "Will StarCraft 2 even last as long as Brood War? What if there isn’t any prize money left in the scene in a year from now? What if I start to hate the game?"

    "It's wrong to think this way before such a high stakes match, but I can’t help it. I know what matters, and I know what I have to do. Why can't I just do it?"

    "I carry myself onto the bed and bury my face in my pillow." 
    "Somehow, I think I’m finally starting to understand what Mr. Yeon was saying."
    window hide dissolve
    stop music fadeout 4.0
    scene black with slowfade:
        align(0,0)
    play sound "sfx/Morning.ogg" fadein 6.0 loop
    scene bg apartmentday with slowfade:
        align (0, 0)
    window show dissolve
    "I’m awake." 
    "I’ve been awake, actually, but I don’t feel like getting up." 
    "I tell myself to for the third time, but I don’t."

    "'We have to practice.'"

    "But I don’t feel like practicing."

    "'Dude. Get up. The team is waiting for you.'"

    "I just want to lie here though. Can’t I just do that?"

    "'No.'"

    "I’m probably sick from the street food. I’m just going to lie here until I feel better."

    "'You aren’t sick. Get up.'"

    "Not now. Soon, though."

    "'Don’t you want to beat Bolt? That guy is a total prick. If you don’t practice, he’ll beat you and you’ll feel terrible.'"
    #choices here
    "I already feel terrible though. I'm just going to lay here."
    "'Get up. {w=1}Get up. {w=.5}Get up. Get up. Get up. Get up. {w=0}Get up. Get up. Get up. Get up. Get up. Get up. {w=0}Get up. Get up. Get up. Get up. Get up. Get up. Get up. {w=0}Get up. Get up. Get up. Get up. {w=0}Get up.{nw}"
    stop sound fadeout .05
    window hide
    scene black:
        align (0, 0)
    $ renpy.pause(4.0)
    play voice "sfx/knock2.ogg" loop
    $ renpy.pause(3.0, hard=True)
    scene bg apartmentday with slowfade:
        align (0, 0)
    window show dissolve

    "The sound of repeated, unrelenting knocks wakes me. A glance at my phone answers my immediate question. It’s 2:00 PM."

    "I shamble my way to my door and glance through the peephole into the hallway."

    "It’s Jett. She doesn’t look happy."
    stop voice fadeout .2
    play voice "sfx/dooropen.ogg"
    "I turn the knob and crack the door open, offering no resistance when she forces it the rest of the way open."
    show jett unimpressed at center with Dissolve(.25)
    $ renpy.pause(.25)
    "She glances over me, not bothering to veil the disgust in her expression."

    j "What are you doing? The entire team has been waiting for you to show up."

    "Her tone demands an answer, and I rush to oblige it with an excuse."

    m "I don’t feel well."
    show jett neutral with dissolve
    j "You look fine. Get dressed and get your ass to Golden Zonefire."

    "I run a hand through my matted hair and glance away."

    m "I’m serious, I feel awful. I don’t think practicing today {nw}"
    show jett unimpressed
    extend"makes much since considering I might burn myself out. It's important that I{nw}"
    show jett angst
    play voice "sfx/slap.ogg"
    show bg apartmentday:
        xpos 0.0
        easein .06 xpos 0.08 subpixel True
        easeout .12 xpos 0.0 subpixel True
    show jett:
        xpos 0.5
        easein .06 xpos 0.48 subpixel True
        easeout .12 xpos 0.5 subpixel True
    show white at center
    hide white with Dissolve(.3)
    $ renpy.pause(.3)
    "Jett's palm cracks against the left side of my face. I call out in a mixture of pain and shock and try to step back."
    play sound "sfx/stumble.ogg"
    show jett with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8)
    "Instead, Jett catches me by my shirt and pulls me forward, visibly restraining herself from bringing the back of her hand across my other cheek."
    play music "sfx/Pull Yourself Together Intro.ogg"
    queue music "sfx/Pull Yourself Together Loop.ogg"
    scene bg cg3:
        align (0,0) zoom 1.0
        linear 30 xpos -.15
    show image "bg/cg3male.png" at center:
        zoom 1.0 xpos .5
        linear 30 zoom 1.2 xpos .45
    with dissolve
    "I gasp for breath and bring a hand to where she struck me. Her eyes, hard and determined, refuse to leave mine."

    m "What... why... did you do that..."

    j "Why are you here, Mach? Why did you come to Korea?"

    m "What…? To… to play StarCraft. You already know the answer..."

    j "No, you didn’t. You have some natural talent for StarCraft, but you didn’t come here to make use of it."

    "What on Earth is she talking about? I feel my voice harden in my throat when I argue back."

    m "You just hit me for nothing! I came to Korea because I want to play in the VSL! Because I want to be a champion."

    j "And yet you can’t drag your sorry ass out of bed to prep for the showmatch that an entire team is counting on you to win."

    j "Stop lying to yourself. Or at the very least, stop lying to me. I put a lot of trust in you, Mach. I honestly hoped that you’d prove you have what it takes to make something of yourself."

    j "But you clearly don’t. You quit when it gets hard, and your minor accomplishments help fuel the lie that you're capable something great without putting in the work."
    play voice "sfx/push.ogg"
    scene bg apartmentday:
        align (0, 0)
    show jett unimpressed at center
    with Dissolve(.3)
    "The ferocity in Jett’s eyes dies out as she relinquishes her vice on my undershirt. I stumble back, clutching at the wall to keep from falling over."
    show jett angst with dissolve
    j "You have less than a week to pretend that you care about what happens to yourself and to this team."
    j "If you can't do that for your own sake, then do it for ours."
    show jett unimpressed with dissolve
    $ renpy.pause(2.0)
    "After ten long, sobering seconds of unanswered silence, she turns, stalks into the hallway, and slams the door."
    hide jett with Dissolve(.2)
    play sound "sfx/doorslam.ogg"
    show image "bg/daybig.jpg" at center:
        zoom .6666666666666666666666666666666666666666666666666666
    $ renpy.pause(1)
    play sound "sfx/slide.mp3"
    pause .2
    show image "bg/daybig.jpg" at center:
        linear 1.0 zoom .9 subpixel True
    "The wall is rough against my side as I slide down it and onto the floor."
    window hide dissolve
    show image "bg/nightbig.jpg" at center with Dissolve(3.0):
        zoom .9
    pause 1
    stop sound fadeout 2.0
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
    "It's not long before I'm tired of replaying my stale reasoning." 
    "My apartment's view of the Seoul skyline offers a moment's relief. It makes the decision a little bit easier." 
    "One way or another, I'm not coming home."
    "The looks of disdain, the fake reassurances. It's all that's left for me once I step on that plane and admit that I'm a failure."
    "If I can't swing a single match victory with four other people carrying me, what can I possibly hope to accomplish with the rest of my life?"
    "I let out a long breath. I'm tired. And even though I wouldn't mind falling asleep against this wall, I find myself rising to my feet."
    "Is it narcissism or masochism? It would be so much easier for me to just accept that I was never cut out for this in the first place." 
    "I really just can't quit, huh?"
    "This is such a joke."
    
    window hide dissolve
    show sky6 at center:
        easeout 3 ypos 2.0 subpixel True
    show sky5 at center:
        easeout 3 ypos 1.1 subpixel True
    show sky4 at center:
        easeout 3 ypos .9 subpixel True
    show sky3 at center:
        easeout 3 ypos .8 subpixel True
    show sky2 at center:
        easeout 3 ypos .7 subpixel True
    show sky1 at center:
        easeout 3 ypos 1.0 subpixel True
    pause 2.0
    jump S31TheValueOfWinning
label S31TheValueOfWinning:

    scene black with midfade:
        align (0,0)
    pause 1
    play voice "sfx/storedoor2.ogg"
    scene bg store with Dissolve(1.0):
        align (0, 0)
    window show dissolve
    play sound "sfx/AC.ogg" fadein 1.0 loop
    window show dissolve
    "Go Mart’s chime sings out as I push my way into the store. Snow white hair and a wrinkly forehead perk up from behind the counter as I stand in the doorway of his store."
    show yeon neutral at center with dissolve
    m "Mr. Yeon."
    show yeon smile with dissolve
    y "Hmm? Come for another round of Go, Mach? Or just here to take your drinks and scram?"

    "It isn’t until he gets a good look at me that the smile drops off his face."
    show yeon concerned with dissolve
    y "Something the matter?"

    m "Did you play Go professionally?"
    show yeon neutral with dissolve
    "He nods once, so I continue."
    m "Why did you play? What kept you going? How did you stop yourself from quitting?"
    show yeon concerned with dissolve
    y "A little philosophical, don’t you think? Take a breath, Mach. What's going on?" 

    "At first, I try to explain as vaguely as I can. But as Mr. Yeon nods along, allowing me to ramble uninterrupted, I find myself divulging more and more details. "

    "I stop only when it comes time to explain my encounter with Jett this afternoon and the evening I spent sitting in my apartment."
    stop music fadeout 5.0
    m "You're right. I go to whatever lengths I can to avoid pain, and I’ve done it all my life."
    m "StarCraft is the only thing I’ve ever been decent at, and I can’t commit to it because I'm afraid I'll fail."
    m "But it's not just that. I can't quit either. My biggest fear of all is admitting to myself that I'm not good enough. I want to believe that as long as I try, I'm not worthless."
    m "I ran away to South Korea with the stupid idea that I could make something of myself. Like the world owed me something just for showing up."
    m "I'm just tired. I don't want to run anymore."
    show yeon neutral with dissolve
    "Despite my ragged voice and slumped shoulders, Mr. Yeon finds himself a nonchalant smile."
    play music "sfx/Wrest.ogg"
    y "Then don’t. It’s much easier to walk."
    show yeon smile with dissolve
    "A slight chuckle escapes him. When it ends, he gestures past me to his store."
    show yeon neutral with dissolve
    y "Mach. I’m closing in on seventy and work at a convenience store at two in the morning. Some would call that failure. But I don’t regret the days I spent studying and competing in Go."
    y "If we live without pursuing our passions, what good is living at all?"
    y "Prizes, fame, status… These things are achieved by few. But every competitor must play for a love of the game and the pride of a well-earned victory."
    show yeon smile with dissolve
    y "Competition is a noble thing. It drives us to improve, innovate, and test the limits of who we are and what we can do. It took humans into space."
    y "You wouldn’t seek a reason to keep at it if you didn’t already know there's value in that."

    "I lean onto the counter separating us, the tension in my chest softening."

    m "I do. And you’re right. But I can’t stop worrying that it won’t be worth it in the end. Or that even if I try my best, I’ll fail."
    show yeon neutral with dissolve
    y "You might not achieve everything you set out to, even if you work as hard as you can. No success worth chasing is ever guaranteed."
    y "But do you want to spend the rest of your life wondering what you were capable of? My own answer to that was no."
    "I glance away and rake my hand through my hair. There’s no way that I’ve come this far only to give up now."
    "When I straighten up, he beams a pleased smile at me."
    show yeon smile with dissolve
    y "Now then. If I were you, I would head home and get some rest. You’ve got a match to prepare for, after all."
    "I find myself at an utter loss for words. Gratitude forms and falls apart between my lips a handful of times before I simply settle for a deep bow."
    m "Thank you, Mr. Yeon."
    show yeon neutral with dissolve
    y "You're welcome, Mach." 
    show yeon smile with dissolve
    y "By the way, the next time you come by for an old man’s wisdom, you'll have to buy something first."
    "For the first time today, I catch myself smiling."
    m "Heh. Okay, deal."
    play voice "sfx/storedoor2.ogg"
    hide yeon with dissolve
    "Just then, a customer pushes open the door to the store. Though there wasn’t much else I had to say, now is probably an appropriate time to depart."
    "As I turn to leave, Mr. Yeon lifts his fist at me."
    show yeon neutral at center with dissolve
    y "Work hard."
    "I raise mine to match his."
    m "I will."
    stop music fadeout 4.0
    stop sound fadeout 4.0
    window hide dissolve

    jump S32RevaStuntArchon

label S32RevaStuntArchon:
    scene black with midfade:
        align (0,0)
    pause 2
    scene bg streetside with midfade:
        align (0, 0)
    window show dissolve
    "Apprehension hangs over me as I stand before the doors to Golden Zonefire. Waiting won’t make this any easier."
    window hide dissolve
    scene bg cafe with dissolve:
        align (0, 0)
    window show dissolve
    stop sound
    "With a stride belying my frantic heart rate, I make my way to a table seating the four teammates I neglected the day before."
    play music "sfx/Blue Pineapple.ogg"
    show accel neutral at center 
    show reva neutral at right
    show stunt neutral grin at left
    with dissolve
    "But whatever reason I have to worry disappears when Accel catches sight of me. He rises from his chair and waves me over, leading Reva and Stunt to follow suit."
    hide accel
    hide reva
    hide stunt
    show jett unimpressed at left:
        xpos .1
    with dissolve
    "It’s only Jett that refuses eye contact with me. Even then, though she’s trying to hide it, I can tell that she’s relieved I’m here."
    hide jett
    show accel neutral at center
    with dissolve
    a "Hey, Mach. Ready for practice?"
    m "Yeah. And sorry about yesterday. It won’t happen again."
    show accel thinking2 with dissolve
    a "No sweat. Let’s make the most of the time we have left, yeah?"

    m "Yeah."
    show accel neutral with dissolve
    a "Alright. Stunt, Mach. Go setup your PCs and get to work."
    hide accel with dissolve
    show stunt neutral at center with dissolve
    "Stunt jumps up from the table and steers himself to my side as we make our way to the setups."
    show stunt neutral grin with dissolve
    s "Me and Reva played 2v2s while Jett was gone yesterday. I'm pretty sure we could be ranked number one on the ladder with enough time."

    m "No one takes 2v2s seriously, much less on ladder."
    show stunt smug with dissolve
    s "Pft, says you. But hey, good that you're already feeling better. If you puke, I'll know it's because my strategy is what's sick." 

    "I lift an eyebrow, trying to unravel Stunt's meaning. It's only with a glance back at Jett and then Accel that it clicks."

    m "Yeah. I'm all better."
    hide stunt with dissolve
    "He snerks and peels away from my side to pick out a PC. Jett, Accel and Reva follow at a distance, the latter two setting up chairs behind me to observe and make comments."
    window hide dissolve
    scene black with squares:
        align (0,0)
    play sound "sfx/apmsound.ogg" fadein 1.0 loop
    scene bg pcbang with squares:
        align (0, 0)
    window show dissolve
    "Even with my renewed focus and drive, it becomes readily apparent after a few matches that our practice is still going to be suboptimal."
    "Stunt’s trying his best, but it doesn’t mean much with less than a week until the showmatch."
    "He simply doesn't execute standard builds very well. Accel says as much after I trip my way through another clumsy win."
    show accel concerned at right
    show reva neutral2 at left
    with dissolve
    a "We might need to look into finding someone else for Mach to practice with. But there really isn’t enough time..."
    show reva glasses with dissolve
    r "It may be more productive for him to face opponents on ladder."
    show accel thinking3 with dissolve
    a "It won’t be possible for Mach to prepare against certain builds that way, but at this rate you might be right."
    hide reva
    show accel at left
    show stunt frown at right
    with dissolve
    a "Stunt, no one’s going to deny your unit control, but you just don't have the strategic breadth of someone like Bolt."
    show stunt surprised at right with Dissolve(.1):
        ypos 1.0
        easein .4 ypos 1.11 subpixel True
        easeout .2 ypos 1.09 subpixel True
    pause .5
    "The young protoss player slumps in his chair and stares off into space."
    s "I know. Sorry."
    hide accel
    hide stunt
    with dissolve
    "Did I really come this far just to face Bolt unprepared? There has to be a solution."
    window hide dissolve
    #add more maybe
    $pc_reva = False
    $pc_protoss = False
    
label PCChoice:
    menu:
        "Practice with Reva" if pc_reva == False:
            jump RPrac
        "Look for another protoss" if pc_protoss == False:
            jump LookFor
        "Something else":
            jump gogo
label RPrac:
    window show dissolve
    show reva neutral at center with dissolve
    m "Reva, do you think you could play in place of Stunt?"
    show reva glasses with dissolve
    r "I have not played protoss in more than a month. Without a week's worth of practice, I would be a lesser opponent than Stunt."
    "Damn. Truth be told, even her terran micro isn’t all that great. I’d hate to see her try to control something like blink stalkers without the time to get back in shape."
    "Still, it seems wasteful that we haven’t been putting her game knowledge to good use."
    $ pc_reva = True
    hide reva with dissolve
    window hide dissolve
jump PCChoice
label LookFor:
    window show dissolve
    m "Could we look around the cafe for a protoss, maybe?"
    show jett considering at center with dissolve
    "Jett is first to answer, and does so without acknowledging me."
    
    j "Look around. Half the people in here are playing this new MOBA bullshit. Decent StarCraft players only show up for All-Out Attack."
    show accel neutral at right
    show jett at left
    with dissolve
    a "Unless they need a practice space for a showmatch, apparently."
    show accel laughing with dissolve
    "He laughs to lighten the mood, but Jett is right. Looking for someone outside of the cafe will probably take too long as well."

    "None of Jett or Accel’s old teammates will want to help either, especially with the PR surrounding the team."
    "C'mon... Think. Be resourceful."
    window hide dissolve
    hide jett
    hide accel
    with dissolve

    $ pc_protoss = True

jump PCChoice
label gogo:
    window show dissolve
    stop music fadeout 2.0
    "If Stunt isn’t providing enough strategies for me to prepare for, and Reva can’t put the strategies that she knows into action…"
    "Wait a second! What Stunt said earlier..."    
    m "What if we practiced 1v2?"
    play music "sfx/Brooding.ogg." fadein 2.0
    show accel concerned at center with dissolve
    a "Eh. What?"

    m "Stunt handles the units, and Reva handles the base management and picks the build order. That way, I can face the best of them both."
    show accel thinking3 with dissolve
    a "Will that even work?"
    show accel thinking3 at left
    show reva surprised at right
    with dissolve
    "Accel glances to Reva, who seems as surprised by my plan as he is."

    m "I don’t see why it wouldn’t. It won’t be a perfectly realistic game condition, but it’s better than anything else I can think of."
    show stunt neutral grin at right:
        xpos 1.3 alpha 0.0
        easein .5 xpos 1.2 alpha 1.0 subpixel True
    pause .5
    s "That sounds kinda fun, actually. C’mon, Reva."

    "Stunt pats the seat of the station next to him. With a shrug, she rises to join him."
    show reva neutral with dissolve
    r "Very well."
    hide reva
    hide stunt
    with dissolve
    show jett unimpressed at right
    show accel neutral
    with dissolve
    "Jett replaces herself in Reva’s vacated seat, arms crossed and expression fierce. She’s intent on seeing for herself whether or not this will work."
    hide jett
    hide accel
    with dissolve
    "When Stunt is done joking about doing a fusion dance with Reva, we load up a game with Reva and Stunt on the same team and a setting enabled to keep Reva’s base from spawning."
    #add more
    s "So I don’t have to worry about anything except destroying Mach? This is going to be great. Hey, Reva, build two gateways by his base for me."
    r "No. We are playing standard."
    s "Come on... Okay, how about a proxy stargate then?"
    r "No."
    m "I can hear you, you know."
    r "It will not matter. Such is the beauty of standard play."
    jump archonbattle1
    $ persistent.en21_locked = False
    $ encyclopaedia.unlockEntry(en21, persistent.en21_locked)
    "I soon find that her confidence is well placed. Even with Reva's economy-focused build order, Stunt's stalker {color=#FF5E5E}harass{/color} soon makes my life difficult."

    "He dances the single unit back and forth at the entrance to my natural, all of his focus devoted to its control."

    "It's a painfully effective frustration that succeeds in slowing down my attempts at establishing economy and tech."

    "My multitasking and micro are brought to their limits, and we haven’t even hit the five minute mark. This is insane."
    "And very, very good practice."

    "I don’t have the chance to spare a glance over my shoulder at Accel or Jett, but I’d make a pretty sure bet that they’re just as intent on the game as Stunt, Reva, and I are."

    "The match drags on until the Stunt and Reva archon rolls over my paltry force with a well-timed and perfectly controlled two-base push. It wasn't even close."
label postarchon1:
    scene bg pcbang:
        align (0,0)
    show accel neutral at center
    with dissolve
    window show dissolve
    a "Well. They make for a tough opponent, that’s for sure. You three down to keep at this?"
    hide accel
    show stunt neutral grin at right:
        xpos .97
    show reva neutral at left:
        xpos .03
    with dissolve
    s "Are you kidding?! This is amazing!"
    show reva glasses with dissolve
    r "I am enjoying myself as well."
    hide reva
    hide stunt
    show jett unimpressed at center
    with dissolve
    j "The point isn’t to have fun, it’s to practice."
    show jett neutral3 with dissolve
    j "Run a nexus first. I want to see how Mach handles it."
    window hide dissolve
    stop music fadeout 1.0
    stop sound fadeout 2.0
    scene black with squares:
        align (0,0)
    pause 1
    play music "sfx/Mod Hop A.ogg"
    queue music "sfx/Mod Hop B.ogg"
    play sound "sfx/battle/archonsfightmm.ogg" fadein 5.0
    show bg montage battle1 with squares:
        align(0,0)
    #battle scene material missing
    window show dissolve


    hide white with Dissolve(0.05)

    "It’s incredible. Playing an opponent at this level allows me to see the game in an all new way."
     
    "Stunt’s control is precise and crashes against my defense like a wave, while Reva directs the flow of battle like a symphony's conductor."
    stop sound fadeout 1.0
    play sound "sfx/battle/stalkersshootingcc.ogg"
    $ show_stalker_lasers()
    show white with Dissolve(0.1):
        align(0,0)
    show bg montage battle2:
        align(0,0)
    hide white with Dissolve(0.05)
    "They have achieved purity of form. Through these repeated losses, I can see just how outmatched I am in nearly every aspect of StarCraft."
    "The moments of weakness for an opponent that plays such a clean style are scant and short-lived, but they exist. I can create them by taking risks, using mind games, or forcing mistakes."
    stop sound fadeout 1.0
    play sound "sfx/battle/colossus.ogg"
    scene bg black with Dissolve(0.01):
        align(0,0)
    show colossus_beams:
        align (0.5,0.0)
    show colossus_beams_mask at beam_masks
    show colossus_beams_head at beam_head(435)
    show colossus_beams_head as right_head at beam_head(845)
    pause 0.1
    hide colossus_beams_head
    hide right_head
    show screen colossus_particles
    show white with Dissolve(0.1):
        align(0,0)
    show bg montage battle3:
        align(0,0)
    hide white with Dissolve(0.05)
    pause .5
    hide colossus_beams
    hide colossus_particles
    $ show_protoss_blast()
    pause 0.5

    "I've felt these things on instinct before, but I can now see them for the truths they are."
     
    "The element of human error is practically zero between Stunt and Reva."
    stop sound fadeout 1.0
    play sound "sfx/battle/archonsfightmm.ogg"
    $ show_protoss_blast()
    show white with Dissolve(0.1):
        align(0,0)
    show bg montage battle4:
        align(0,0)
    hide white with Dissolve(0.05)
    "But StarCraft is a game of imperfect information. Anyone, even a perfect machine, is capable of being defeated."
    "I'm done being afraid of you, Bolt."
    stop sound fadeout .5
    scene bg pcbang with dissolve:
        align(0,0)

    "It’s late in the evening when Accel calls our practice quits. Twelve hours straight, minus breaks for lunch and dinner."
    show accel thinking2 at right
    show jett neutral at left
    with dissolve
    a "Four more days of that, and he’ll be as ready as he possibly can be in that amount of time."
    show jett considering with dissolve
    j "We risk Stunt and Reva falling out of practice, but there really isn’t any other choice. At least it won’t be for long."

    "Jett still hasn’t acknowledged me with direct eye contact, but the animosity I felt coming from her this morning is all but gone."
    hide accel
    hide jett
    show stunt neutral grin at left:
        xpos .1
    show reva neutral at right:
        xpos .9
    with dissolve
    "Neither Stunt or Reva seem even a fraction as out of it as I am. Yet as tired as I am, I find myself eager for practice tomorrow."
     
    "I can only hope it lasts until the end of the week."
    hide stunt
    hide reva
    show accel thinking2 at right
    show jett neutral at left
    with dissolve
    j "I’ve got a few more things to take care of before the weekend. The VSL studio managed to fit us in a time slot right before the semi finals for team league."
    show accel confident with dissolve
    a "I’ve seen some of the promotion they’re doing online. It’s being hyped as a KPGA vs. foreigner match."
    show accel neutral with dissolve
    a "Mach's been cast as the villain. A last minute way of hyping up the match since it was on such short notice."
    hide accel
    hide jett
    show reva expected at center
    with dissolve
    r "The Korean Pro-Gamer Association would not have allowed one of their players to compete otherwise."

    r "It seems they are beginning to sow the seeds for the transition from Brood War to StarCraft 2."
    hide reva with dissolve
    "It’s hard to imagine that the talent pool for StarCraft 2 could get any more deep. Bolt is only one of a few dozen top-tier players being held back by the floodgates of KPGA’s regulations."
    show accel thinking at right
    show jett neutral2 at left
    with dissolve
    j "A win against Bolt ought to show KPGA players and their fanboys not to shrug off those of us who switched to StarCraft 2 early."
    show accel thinking2 with dissolve
    a "No need for so much bite, Jett. We switched because we were ready for a new challenge, right?"
    show jett thinking2
    show accel concerned
    with dissolve
    "She glances away, failing to match Accel’s now wavering grin."
    stop music fadeout 4.0
    show jett neutral with dissolve
    j "I need to go. The rest of you, get some rest."
    hide accel
    hide jett
    show stunt neutral grin at left:
        xpos .1
    show reva neutral at right:
        xpos .9
    with dissolve
    s "Yo, Reva. Wanna grab some dinner? We can practice our fusion dance for tomorrow."
    show reva glasses with dissolve
    r "A potara earring is necessary for fusion between two distinct beings, Stunt. And the hyperbolic time chamber is a more apt metaphor for Mach’s training regimen regardless."
    hide stunt
    hide reva
    with dissolve
    "A bickering Stunt and Reva exit shortly behind the stone-eyed Jett, leaving only me and Accel to the half-empty cafe."
    play music "sfx/Blue Pineapple.ogg"
    show accel neutral at center with dissolve
    a "Don’t bother worrying about yesterday."

    m "Jett told you, huh?"
    show accel thinking2 with dissolve
    a "Even if she didn’t, it’d be an easy guess. You weren’t giving it your all when we called it quits the day before."

    m "Figures."

    "A sigh escapes me, leading Accel to drop a hand on my shoulder."
    show accel confident with dissolve
    a "Just focus on the showmatch. If you still want to worry about sleeping in after winning, you can mope around the team house for a day."

    "Despite my best efforts, I can’t keep myself from spitting out a laugh."

    m "Things have changed so much since I met you and Jett."
    show accel neutral with dissolve
    a "For the better, I hope?"

    m "Yeah. You guys are so goal driven. It's kind of mindblowing, actually."
    show accel thinking with dissolve
    a "Best way to live, if you ask me. And good practice for the real challenge."
    show accel thinking2 with dissolve
    a "Don’t think Jett will be satisfied with a little bit of money from Enoch. You won't have time to pick the confetti out of your hair before hearing all about next season's plan."
    m "If she ever finds a reason to talk to me again, that is."
    show accel neutral with dissolve
    a "Jett has her way of dealing with things. Don't sweat it too much and just focus on your practice."

    m "Right, I will."

    "I rise from my chair at last, checking my pockets on the way up for my key and wallet."
    show accel laughing with dissolve
    a "Take care. I'm going to stick around and ladder for a while. Coach has to keep his skills current, you know."

    m "Will you join the team as a player when your contract with Crash is up at the end of the year?"
    show accel thinking2 with dissolve
    a "Who knows? Let’s just worry about the next few days, yeah?"

    m "Fair enough. Later, Accel."
    hide accel with dissolve
    "He falls right back into his chair after a fist bump, leaving me to stalk the neon lit streets alone."
    stop sound fadeout 2.0
    window hide dissolve
    scene bg citybig at left with Dissolve(1):
        linear 40 xpos -.5 subpixel True
    window show dissolve
    "The city lights have never been so beautiful. I have no desire to leave Seoul’s electric embrace now that things are finally starting to make sense."
    "What if I hadn’t run into Accel at Golden Zonefire? I’d probably be booking my ticket for a flight home at the end of the month right about now."
    "And without Jett, there would be no team. No goal, past the vague dream to qualify for the VSL."
    "If not for Stunt or Reva, I’d have no sparring partners. No teammates. Not to mention, no way to have earned Jett's confidence in front of Mr. Kim."
    "... Mr. Kim. No matter how he rubs me the wrong way, he's as much a part of my chance to stay here as my teammates." 
    "And Mr. Yeon. Who’d have thought that the convenience store clerk I’d been avoiding eye contact with would be the one to bring me back from the brink?"
    "By whatever means necessary, I’ll repay those that have helped me stand where I do now."
    stop music fadeout 4.0
    stop sound fadeout 4.0
    window hide dissolve
    jump S33TrainingMontage

label S33TrainingMontage:
    scene black with slowfade:
        align(0,0)
    pause 2
    play sound "sfx/apmsound.ogg" fadein 1.0 loop
    play sound "sfx/battle/scan.ogg" fadein 1.0
    scene bg archon2 twogas with dissolve:
        align(0,0)
    window show dissolve
    j  "For the third time, if you scout the second gas, build a damn bunker! Don’t be so greedy!"
    stop sound fadeout 1.0
    scene bg black with dissolve: 
        align(0,0)
    play sound "sfx/battle/medivacloada.ogg" fadein 1.0
    show archon2 dropship:
        yalign 0 alpha 0.0
        easein 0.2 alpha 1.0 yalign 0.35 subpixel True
    a "Make sure you stay clear of his vision if you’re going to take that kind of drop path."
    show archon2 vikings:
        yalign 0.4 alpha 0.0
        xalign 1
        easein 0.6 alpha 1.0 xalign 0.4 subpixel True
    j  "They’ll try to roll over you with colossus if they manage to pick off your dropships. Prioritize your viking production first!"
    scene bg black with dissolve:
        align(0,0)
    show archon2 snipe:
        yalign 0.4 alpha 0.0
        xalign 1
        crop(0,0, 180, 720)
        easein 0.6 alpha 1.0 xalign 0.4
        easein 0.6 crop(-200,0, 1280, 720) subpixel True
    play sound "sfx/battle/ghostkillhightemplar.ogg" fadein 1.0
    a "... Yes! Just like that."

    "With a couple of snipes on the Stunt + Reva combination’s high templar, the protoss army is left bereft any kind of area of effect damage, allowing me to charge forward and go for the jugular."
    stop sound fadeout 1.0
    $ show_tank_blast()
    show white with Dissolve(0.1):
        align(0,0)
    play sound "sfx/battle/protossdeathballvsterran.ogg" fadein 1.0
    scene bg archon2 engage:
        align(0,0)

    hide white with Dissolve(0.2)
    "Even with Stunt’s top tier control and Reva’s highly efficient production, I manage to push my way into their base and secure not one, but two ggs."
    stop sound fadeout 1.0
    scene bg pcbang with dissolve:
        align (0,0)
    play sound "sfx/apmsound.ogg" fadein 2.0 loop
    "I leap out of my seat in triumphant victory. Out of almost a hundred games, that’s the third win I’ve managed to clinch."

    "It feels amazing. I wasn't sure that I'd be able to manage a breakthrough as a result of this kind of practice, but my control has noticeably improved."

    "A good thing, considering the match with Bolt is tomorrow."
    show stunt yell at left:
        xpos .1
    show reva neutral at right:
        xpos .9
    with dissolve
    s  "Gaaaah! She insisted on building more high templar when I asked for colossus!"
    show reva frown with dissolve
    r "It was strategically unsound to push onto the map. You should have allowed our upgrades to complete and used the high templar as drop defense."
    play voice "sfx/lurch.ogg"
    show stunt:
        easein .3 xpos .14 subpixel True
    s  "What do you know?! You don’t even play protoss!"
    show stunt surprised with dissolve
    show stunt:
        linear .5 xpos .1 subpixel True
    "Reva places her index finger on Stunt’s forehead, easily keeping him at arm’s length."      
    hide reva
    hide stunt
    with dissolve
    show jett neutral at center
    with dissolve
    "The pair quiets their harmless squabbling when Jett rises."
    j  "That’s enough for today."
    m  "Eh? But it’s barely six o’clock."
    show jett neutral2 with dissolve
    j  "The day before an important match is the most important. Not in terms of practice, but to prepare mentally."
    show jett considering with dissolve
    "Jett says so to no one in particular, making it a point to ignore me when I turn to look at her."
    show accel thinking2 at right
    show jett at left
    with dissolve
    a "A new age method, huh? Better than the all-night cram sessions from the Brood War days, I suppose."
    show jett casual with dissolve
    j  "It’s scientifically proven to work. Besides, it’s not like I’m giving him the rest of the day to do as he pleases."

    "Damn. With Jett, even relaxation is ordained."
    show jett neutral with dissolve
    j  "C'mon. We’re going to Namdan."
    show stunt yell at right
    show accel at left
    hide jett
    with dissolve
    s  "Again with Namdan? Pro-gamers don’t belong in a place without computers."
    show accel laughing with dissolve
    a "Would you rather spend the rest of the day cleaning ashtrays at your mom's?"
    show stunt surprised with dissolve
    pause .5
    show stunt yell with dissolve
    s  "You know what! You’re all just jealous that you don’t have a PC bang in the family!"
    show stunt surprised with dissolve
    "The rest of us share a laugh on the way out with Stunt trailing after us begrudgingly."
    stop sound fadeout 1.0
    window hide dissolve
    #___

    #BACKGROUND: PARK

    

    jump S34DayBeforeLan

### ENd of Act 2

