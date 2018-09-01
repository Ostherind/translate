#### Act 1 FEMACH
####Forming the team

label fS12CafeSceneTeamOrigins:
    pause 1
    play music "sfx/Loading progress 1.ogg"
    scene bg cafe with midfade:
        align (0, 0) 
    window show dissolve
    "I told Jett that I wasn’t feeling up to practice after we played a few more one-sided games. She seemed annoyed, but agreed with my suggestion to take a short break."
    "Back in high school, I used to spend most of my time at the library when class was over. To be honest, this is probably the most time I've willingly spent outside of my room since then." 
    "I’m not the type to read for fun or study diligently, but it was nice to have a place to go and be on my own. I've missed those afternoons since I graduated."
    
    "But Golden Zonefire is as good a replacement hangout as I could hope for. It's clean and comfortable, and has pretty much everything that I'd need to stay 24/7."
    "That isn't an exaggeration. Some of the patrons here look practically glued to their chairs."
    play voice "sfx/vending.ogg"
    pause .8
    show jett neutral at center with dissolve
    "With a milk tea from one of the vending machines in hand, I return to my seat across from Jett. She isn’t wearing the same scowl from earlier, but I can tell she’d rather be practicing."
    m "What are you drinking?"
    "She snatches up the can across from her and takes a long sip."
    show jett neutral3 with dissolve
    j "{w=.5}Coffee."
    m "What kind of coffee?"
    show jett unimpressed with dissolve
    j "Coffee is coffee. I don’t drink sugary junk."
    show jett considering with dissolve
    j "And, for the record, it’s obnoxious to challenge someone that you don’t know to a match."
    m "Is it really such a big deal? All I wanted was a practice game."
    show jett neutral with dissolve
    j "Do you know those types that stream snipe and start shit on message boards so that people pay attention to them?"

    "All too well, unfortunately."
    show jett unimpressed with dissolve
    j "That's you. Except you did it in real life."
    j "Bolt's a real tool though, isn't he? What kind of prick........ {w=.5}Tch."
    "Jett cuts herself off with a hiss and grits her teeth."
    m "How do you know him? His name is Bolt?"
    show jett neutral3 with dissolve
    j "Yes. He plays for Shock T1."

    "Shock, huh? Bolt must be a new recruit. I haven’t paid much attention to them or any other Brood War team since StarCraft 2 came out, but he definitely wasn't on their roster a year ago."

    m "Right. But how do you know him?"
    show jett considering with dissolve
    "Jett clicks her tongue and breaks her gaze away from me. I silently appreciate the reprieve from her death glare." 
    show jett neutral with dissolve
    j "If you must know, he and I went to the same middle school. I was in the class above him."

    m "Oh, okay. I was thinking he might have knocked you out of a tournament or something."
    show jett unimpressed with dissolve
    j "No. I've never played him in a StarLeague. You don’t need to overanalyze everything."
    show jett neutral with dissolve

    "Silence falls between us while Jett nurses what remains of her drink. I can’t tell if she’s really into the coffee or if she’s just trying to find something to occupy her lips other than our conversation."
    show jett considering with dissolve
    "I doubt Jett spends much time at PC bangs given that she's got a team house to practice from. I should consider myself lucky that she'd make time to come out here at all."
    show jett neutral2 with dissolve
    j "You know it makes zero sense for you to focus on qualifying for VSL, right?"
    
    "I blink myself from my thoughts to meet Jett's intense stare."

    m "What do you mean? What’s the point of us meeting up to practice then?"
    show jett unimpressed with dissolve
    j "No. I'm not saying— {w=.5}Listen."
    show jett considering with dissolve
    j "I want to round up some players."
    m "For what?"
    j "For VSTL."
    m "Team league? But you’re already on a team."
    show jett casual with dissolve
    $ renpy.pause(.5)
    show jett unimpressed with Dissolve(.2)
    j "Yeah."

    m "Yeah?"
    show jett thinking with dissolve
    $ renpy.pause(1)
    "She wavers, considering whether or not to tell me what I’ve already figured out."

    m "You’re leaving VIP?"
    play sound "sfx/ding.ogg"
    show jett neutral with Dissolve(.2)
    show jett considering with dissolve
    "Jett’s eyes jump to mine, brows raised in surprise and then furrowed in annoyance. She’s been on VIP for almost a year and is by far the team's best player."
    
    j "Management barely pays us and nobody is motivated. They're worse than bad, they're complacent. I want a fresh start."

    m "I’m not guilting you. It just isn’t something I expected to hear. Do you have a team house picked out?"
    show jett neutral with dissolve
    j "No. Not yet."

    m "What about a coach?"
    show jett considering with dissolve
    j "{w=.5}... No."

    m "Um, well, do you have players in mind?"
    play voice "sfx/interupt.ogg"
    show jett angry with Dissolve(.2)
    j "Look! It’s a work in progress, okay?!"
    "I edge away from her glare and raise my hands defensively."
    m "Err, alright! Sorry, it's not my business."
    show jett considering with dissolve
    "For awhile, silence. Jett does her best to avoid eye contact, but I can tell she’s thinking hard about something."
    "Just as I'm about to rise to replace my milk tea with another, she speaks."
    show jett thinking with dissolve
    j "You know about all of those new foreign teams popping up recently, right?"
    m "Err, yeah. What about them?"
    j "Isn't it strange? They're worse than almost every Korean squad, yet most of them have more sponsors."
    m "Well, there are a lot of eSports fans outside of Korea these days. People want to support their hometown heroes."
    show jett considering with dissolve
    j "I don't think it's that simple."
    m "Where would the money come from if not the fans?"
    j "Idiots."
    m "Er, what?"
    show jett unimpressed with dissolve
    j "Idiots. Idiots that call themselves investors. Idiots that throw away money keeping mediocre players afloat because it makes them feel good inside for whatever reason."
    "Well, she and Bolt agree on one thing, at least."
    m "Um. Okay. Are you going to find some idiots to sponsor you?"
    j "No{w=.2}.{w=.2}.{w=.2}. {w=1}{nw}"
    show jett thinking
    extend "Well."
    show jett thinking2 with dissolve
    "She takes a long moment to reconsider her answer."
    show jett considering with dissolve
    j "... No. It wouldn't work out in the end."
    show jett neutral with dissolve
    j"What I'm getting at is that too much of our scene ignores the foreign fanbase. It's a huge mistake."
    m "Well, there's the time zone difference and a language barrier. Also, I don't know if you know this, but lots of foreign fans don't find Korean players entertaining."
    show jett angry with Dissolve(.2)
    pause .2
    j "What?! How dare you! That's ridiculous!"
    m "I'm just relaying common knowledge! Don't hold me accountable for the opinions of silver-leaguers." 
    show jett neutral with dissolve
    m "Most Western fan support goes to the people who entertain well. Streamers, casters. Those kind of people."
    show jett neutral3 with dissolve
    j "The most famous players in your scene aren't the best? That's appalling."
    m "Hey, Brood War got popular on the backs of boys that looked good on camera. That's practically the same thing! If the PC bang was the ship, then the fangirls pulled the oars."
    show jett unimpressed with dissolve
    j "Not the same thing. They were pretty and skilled, not one or the other." 
    j "And show some damn respect, those 'boys' are the only reason that you and I are able to have this conversation."
    "The sharp response and equally sharp glare suggests that I shouldn't argue the point. Jett knows better than I do anyway."
    show jett neutral with dissolve
    j "We're getting off topic. There are tons of potential fans that most Korean teams ignore simply because they're too hard to connect with."
    m "Yeah. I agree."
    show jett casual with dissolve
    $ renpy.pause(.5)
    show jett considering with Dissolve(.2)
    "She lifts an eyebrow and stares at me for just a bit too long before glancing away. If I wasn't sure before, I am now."
    
    stop music fadeout 3.0
    m "Go on."
    show jett angst with dissolve
    j "Go on and what?"
    m "I know what you’re thinking."
    show jett unimpressed with dissolve
    j "No you don't."
    m "Yes I do."
    show jett considering with dissolve
    j "What am I thinking, then?"
    m "You want me to join a new team you're starting so that I can help you with the foreign fanbase." 
    m "Also, you invited me here to tryout under the guise of practice."
    show jett thinking with dissolve
    j "..."
    show jett thinking2 with dissolve
    j "....................."
    show jett considering with Dissolve(.2)
    play voice "sfx/footstep.mp3"
    show jett considering at center:
        xalign 0.5 ypos 1 subpixel True
        easein .2 ypos 1.1 subpixel True
        easeout .1 ypos 1.09
    $ renpy.pause(.4)
    play music "sfx/Loading progress 1.ogg"
    pause .1
    "Jett slumps back in her seat, defeated. I fight a losing battle against the urge to laugh."
    show jett angst with dissolve
    j "Don't look so smug. Ugh, I hate dealing with team management."
    m "You could hire a manager."
    show jett thinking at center with dissolve
    j "Before we have any players? Maybe I should just keep my head down and practice."
    m "No, don’t do that. It's a good idea."
    show jett unimpressed with dissolve
    j "You’re only saying that because I gave you an offer."
    m "Partially. But if you go through with this, I’ll do whatever I can to help."
    show jett considering with dissolve
    j "How are you the one convincing me to go after my own idea? Dammit."
    "She chews on her lip, likely considering the harrowing risk of leaving her team."
    pause 1
    show jett neutral with dissolve
    j "... I can’t make any commitments until we at least have some other players. It’d be stupid for me to move out of the VIP house without everything lined up."
    j  "This is something I’ve been thinking about for a while, even if I don’t have every detail hashed out yet." 
    show jett smile with dissolve
    j "I want to keep overhead low and practice time high. Lean and mean."
    "She aims a finger at me, her dull nail a hair’s breadth before my nose."
    show jett neutral3 with dissolve
    j "If you're going to be a part of this, you're going to pull your weight. You can start by searching for our players, unless you’d rather find me a coach and sponsor."
    "I cringe backwards and raise my hands."
    m "No, no. Uh. I’ll leave that to you."
    show jett smile with dissolve
    j "Good. It’ll work out better this way. The minimum number of players for team league is four, so you need to find at least two."
    m "You know, this isn’t exactly how I envisioned that I'd join a StarCraft team."
    show jett neutral3 with dissolve
    j "Walk away if you like. You have a long way to go if you want to be anything other than our translator mascot anyway."
    show jett casual with dissolve
    j "I'll admit though, Accel was right. I see glimpses of high level stuff in your play." 
    show jett unimpressed with dissolve
    j "But as of right now, you kind of suck, even by foreigner standards. Offense intended." 
    j "You seriously need to start busting your ass. Coming to Korea is pointless if you're still practicing Western hours."
    "Well. Nobody ever claimed that Jett wasn't honest."
    show jett pleased with dissolve
    j "I’m going to work you and everyone else like dogs. If this team comes together, I won't be happy with anything less than first place in VSTL."
    m "Well. I appreciate the chance."
    show jett smile with dissolve
    "I offer a smile that she's quick to match."
    show jett neutral with dissolve
    j "If we're going ahead with this, I've got a lot of stuff to do. The deadline to register for team league is in two weeks, so we can’t afford to waste time. Get moving on your search."
    m "Alright. Good luck. I’ll catch you online."
    show jett smile with dissolve
    j "Yeah. Later."
    hide jett with dissolve
    "When she's gone, I fall back into my chair and take a deep breath." 
    "Jett just asked me to join her team."
    "I pinch my forearm and judge the sensation that follows. With that, my disbelief dissolves into contemplation." 
    "... How the hell am I going to find two worthwhile, unsigned players?"
    stop music fadeout 2.0
    window hide dissolve

label fS13ConvenienceStore:
    scene black with midfade:
        align(0,0)
    pause 2
    scene bg streetside2night with squares:
        align (0, 0)
    play sound "sfx/nightcricket.ogg" fadein 1.0 loop
    window show dissolve
    "A mixture of guilt and pride led me to spend the rest of the day at Golden Zonefire. Between ladder games and a break for dinner, I scoped out the cafe’s best StarCraft players."

    "Unfortunately, it doesn't seem like any of Golden Zonefire’s regular patrons are much to write home about. There were good players there for All-Out Attack, sure, but today..."

    "Most of the cafe's patrons were playing Brood War. And of the ones that were actually laddering in StarCraft 2, there was only a single guy in master league."

    "I’ll have to extend my search outside of a single PC bang. I guess it'd have been a little too convenient to find a VSL-caliber player so easily."

    "I get the urge to stop at a convenience store on the way back to my apartment. There’s one I've been going to regularly for my nightly fix of sugar and caffeine."

    "The store’s blindingly bright signage is visible from more than a block away. Green capital letters spell out the store’s name in English on a backdrop of white. Go-Mart."
    stop sound fadeout 2.0
    window hide dissolve
    play voice "sfx/storedoor2.ogg"
    scene bg store with Dissolve(1.0):
        align (0, 0)
    window show dissolve
    play sound "sfx/AC.ogg" fadein 1.0 loop
    show yeon neutral at center with dissolve
    "The door’s familiar chime welcomes me, and the same clerk I’ve seen at least a dozen times before stands formally behind a cash register."

    "He looks a bit old to be working still. Maybe he owns the place and doesn't have help to work the night shift?"
    hide yeon 
    show storebig at center:
        xpos .5 ypos 1.1
        parallel:
            linear 10 xpos .6 subpixel True
        parallel:
            linear 10 ypos 1.0 subpixel True
    with dissolve
    "I see myself standing behind the counter in an unwanted mental image. It's a fate that could easily await me if I fail to make it as a professional gamer."
    hide storebig with dissolve
    "I shake my head free of the thought and make my way to the refrigerated section of the store to fill my fists with cans and bottles." 
    "Some of the drinks may have strange names, but I’ll be damned if they aren’t good."
    play voice "sfx/cans.ogg"
    show yeon neutral at center with dissolve
    "I drop them on the counter in front of the old man and briefly make eye contact with him. He seems to recognize me, but doesn’t say anything to indicate it."

    "He rings up my drinks slowly, not from age or callouses, but because he's in no great rush. The store's empty aside from me, after all."

    c "6,000 won."
    "I swipe my credit card in the reader and depart with a polite smile, anxious to return to my apartment."
    show yeon smile with dissolve
    "The clerk returns the expression and watches me go without another word."
    
    hide yeon with dissolve
    window hide dissolve
    stop sound fadeout 1.0
    scene bg streetside2night with Dissolve(1.0):
        align (0, 0)
    play sound "sfx/nightcricket.ogg" fadein 1.0 loop
    window show dissolve
    "The only top-tier player I’m on speaking terms with is Accel, but how would I even approach the subject of getting him to leave his team for a new and untested one?"

    "Maybe it would be better for me to simply get a lead from him. If I can’t manage that, then I’m left to scour local PC bangs and message boards on my own."
    "Whatever. I'll figure this out tomorrow."
    window hide dissolve
    stop sound fadeout 1.0
label fS14FindingStuntPlayer:
    scene black with midfade:
        align (0,0)
    play music "sfx/Blue Pineapple.ogg" fadein 4.0
    pause 1
    scene bg cafe:
        align (0, 0)
    show accel neutral at center
    with midfade
    window show dissolve
    a "And you had to convince her? Seriously? She’s been talking this up to me for the past two months."

    m "It’s a big change, plus I just met you guys. I'd be hesitant too."
    show accel thinking2 with dissolve
    a "Hmm!"

    "Accel grins, no doubt replaying Jett’s angst in his mind’s eye."
    show accel thinking with dissolve
    a "Getting in at the ground floor is a major plus. You were in the right place at the right time. If it works out, that is."
    show accel thinking3 with dissolve
    "Accel glances over his shoulder before returning his attention to me."
    show accel concerned with dissolve
    a "Most teams barely pay their players anything. I’ve got it good for someone my age, but even I have part of my winnings taken for the team’s benefit."
    show accel neutral with dissolve
    "Ouch. Luckily for Westerners, that isn’t a trend that has caught on outside of South Korea."

    m "So..."

    m "......."

    "... I can’t do it. It’s impossible. The words simply will not come."
    show accel concerned with dissolve
    a "What?"
    show accel neutral with dissolve
    a "... Oh!"
    show accel laughing with dissolve
    "Accel lets out a laugh, genuine and highly amused. He tries to get his words out and, unlike me, eventually ends up succeeding."
    show accel neutral with dissolve
    a "Sorry Mach, but no can do. I’m signed with Crash until the end of the year. I’m not allowed to play for anyone else until my contract is up."

    "As I expected. Really, it shouldn’t come as a surprise. I sigh, fall back into my chair, and rest my palms atop my head."

    m "I had to ask. Jett’s expecting me to pick up our players while she handles the management and sponsorship side of things."
    show accel confident with dissolve
    a "Hey, well. I can help you with the next best thing." 

    m "I’d be thankful for any help at all."

    a "Don’t you worry. I’ve got a shortlist of easy pick-ups. An extremely short list."
    show accel thinking with dissolve
    "He clears his throat."
    show accel thinking2 with dissolve
    a "There’s only one person on it. But hey! Better than nothing, right?"
    m "Who is it?"
    show accel neutral with dissolve
    a "Ooh, straight to business. Eager for your bunkbed, I see. Trust me Mach, you’ll want the bottom bunk."
    m "You know from experience?"
    show accel laughing with dissolve
    a "Sure do. When I was sixteen, some upjumped Brood War clan scraped me from the bottom of the barrel and set me up in their overcrowded sweatshop of a team house."
    $ persistent.en13_locked = False
    $ encyclopaedia.unlockEntry(en13, persistent.en13_locked)
    a "Had to sleep above someone at least two years past a graceful retirement. I’ve seen solitaire players with better {color=#FF5E5E}APM{/color}. He snored. A lot."
    show accel thinking2 with dissolve
    "As horrible as he’s trying to make it seem, Accel sounds closer to wistful than bitter as he recounts his first years as a professional gamer." 
    m "What happened to the team?"
    show accel neutral with dissolve
    a "Sponsor flaked. Team didn't have the money for legal action." 
    a "Coach didn't tell us until twenty minutes before rent was due. Someone stole my mousepad as we were moving out. And that was the end of my StarCraft career."
    show accel thinking with dissolve
    a "Wait, no, it kept going for seven years after that and somehow still isn't over. Always forget that part."
    show accel laughing with dissolve
    "Accel. Top Korean terran, master storyteller."
    show accel neutral with dissolve
    a "Anyway. This guy's name is Stunt. Plays protoss. He's pretty good."
    m "... But?"
    show accel thinking3 with dissolve
    a "But? Does there have to be a but?"

    m "I’m sensing a but."
    show accel neutral with dissolve
    a "It’s a small but. He’s incredibly cheesy and maybe a touch arrogant. And he's a high schooler. But, he's good."

    m "Why haven't any other teams picked him up in that case?"
    show accel thinking with dissolve
    "He shrugs. I get the feeling that Accel genuinely doesn’t know, but I'm left anxious nonetheless. "

    "Still, it’s important to have at least some kind of racial distribution on the team." 
    "... Not in terms of foreigner or Korean mind you, but rather of zerg, protoss, and terran."

    m "Hm. Do you know how I could get in touch with him?"
    show accel confident with dissolve
    a "I could give you his info for a friend request, but he’d probably block you on the assumption that you’re a goldseller or something."

    a "Your best bet is to find him in person at Stomping Grounds."

    m "... His stomping grounds? What do you mean? Where?"
    show accel neutral with dissolve
    a "No, no. Stomping Grounds. That’s the name of the PC bang he’s usually at."

    "Ugh. Another trek across Seoul. I’ve never heard of the place, much less been to it. Accel takes note of my frown and wags a finger at me."
    show accel thinking with dissolve
    a "What, you fly halfway across the world and can’t be bothered to walk for half an hour? Take the subway if you’re that lazy."

    m "No, no. It’s fine. I shouldn’t expect this to be easy."
    show accel neutral with dissolve
    a "Now we’re talking. Get going. I’ll keep an eye out for your next player in the meantime."
    stop music fadeout 3.0
    window hide dissolve

label fS15RecruitingStuntPlayer:
    
    scene black with squares:
        align (0,0)
    pause 2
    play sound "sfx/street1.ogg" fadein 1.0
    scene bg streetside2 with squares:
        align (0, 0)
    window show dissolve
    "I check the map on my phone for the second time after reading the sign for a third. This is definitely Stomping Grounds."
    
    "A deep breath helps calm my nerves. Seconds later, I push open the glass door and make my way inside."
    
    window hide dissolve
    stop sound fadeout 1.0
    play music "sfx/Full Server Intro.ogg"
    queue music "sfx/Full Server Loop.ogg"
    scene bg darkpcbang with Dissolve(1.0):
        align (0, 0)
    play sound "sfx/apmsound.ogg" fadein 2.0 loop
    window show dissolve
    "Pretty much as expected. Computers, vending machines, tables, and the sound of two dozen mice and keyboards. PC bangs are nothing if not similar to one another."
    "When a shiver runs down my back, I realize that the A/C in here is cranked up ridiculously high."
    "I read somewhere that casinos pump in extra oxygen to keep their patrons awake and alert. Maybe this place has tried to adapt the same tactic to their cafe?"
    "A middle aged woman sits behind the front desk. She glances up at me when I pass by and then returns her attention to the magazine splayed out in front of her."
    "A quick scan of heads lined up in front of monitors offers me a few potential Stunts amidst the sea of scrubs. By Accel’s description, he’s short and has bleached hair."
    "I’m able to narrow it down quickly and confirm his identity with a look at his monitor. He’s in the middle of ladder match."
    "… And he’s playing StarCraft 2 with one hand. The other is occupied with a game on his cell phone."
    "All the same, Stunt's crushing his opponent with a rush build. And by the look on his face, he takes great pleasure in that fact."
    "His enemy sends a salty one liner before dropping out of the game without a gg. Stunt grins wide and puts his hands behind his head, satisfied."
    "After checking the post-game stats, he glances over his shoulder and then spins his chair around to find me watching him."
            
    show stunt phone at center with dissolve

    s "Sup. Something you want?"
        
    m "Yeah. You're Stunt, right?"
    show stunt smug with dissolve
    s "That's me. And who are you?"
    
    m "I'm Mach."

    show stunt neutral at center with Dissolve(.3)
    pause .2
    "Stunt lights up, stands upright, and plants his hands on his hips all at once."

    s "Right! The foreigner that Accel messaged me about. Was starting to think you wouldn’t show up. Let’s get this betmatch going."

    show stunt neutral grin at center with dissolve
    

    s "HEY EVERYONE! THE BETMATCH IS ON!"
    play voice "sfx/zealotslash.ogg"
    show bg darkpcbang with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8)
    "What."
    pause .5
    "... Dammit. Really Accel?"
    "Before I can attempt an explanation, a crowd of six or seven middle school-aged kids forms behind Stunt. I don’t see myself talking my way out of this."
    
    m "Betmatch. Right. That’s me, yes. That’s what I’m here for."

    somekid1 "A foreign girl is going up against Stunt? Is this a betmatch or a donation?!"

    somekid2 "When will they learn? He's the cafe’s best player! Hey Stunt, will you buy me a juice with your winnings?"
    
    show stunt yell at center with dissolve

    "Stunt ignores the peanut gallery and takes a step forward, sizing me up. Judging by his appearance, it looks like he just started high school. I’m almost a head taller than him."
    
    s "Accel said you were down for a fifteen thousand won bet, but c’mon. You can do better than that, right?"

    m "How much were you thinking?"

    show stunt fist at center with dissolve

    s "Twenty-five thousand is a much better number, wouldn’t you say? C’mon, you had to drag your ass all the way over here to play. Let's make it interesting."

    "That’s what, twenty dollars or so? I’d have to skip a few trips to Go-Mart, but I can’t risk having him turn me down."

    m "Okay, fine. Twenty-five thousand. What are we going to do about maps? Best of three, right?"

    show stunt smug with dissolve

    s "Nah, best of one is fine. My time’s too valuable. And in a show of good faith, you can pick the map."

    "Accel wasn’t kidding about this kid's cockiness. Whatever, at least I can choose a map with a long rush distance."

    hide stunt neutral with dissolve

    "I find a seat at a computer nearby, though not so close that we could catch a glimpse at one another’s screen."

    "A locked window stares back at me as I sit down—of course, I need to pay to use the PC. But before I can head back to the front desk, Stunt slides in front of me and takes the mouse."

    show stunt neutral at center with dissolve

    s "Yo, I got it. Consider it an investment for the money you’re about to give me."
    play voice "sfx/StuntKeyboard.ogg"
    "He unlocks the machine with a few clicks and the entry of a password. Huh, that works."

    hide stunt neutral with dissolve
    stop music fadeout 3.0
    "After I thank him, he slinks back over to his setup. Stunt shares a few confident words with the underage crowd behind him and then throws his headphones on."

    "I host up a game and toss him an invite. It’s not long after that I’m staring down my base and six workers."
    stop sound fadeout 2.0
    window hide dissolve
jump fstuntgame
    
label fstuntlose:
    stop music fadeout 1.0
    window hide dissolve
    scene bg darkpcbang with dissolve:
        align (0, 0)
    play music "sfx/Warsong.ogg"
    window show dissolve
    "My mouse creaks under my grip before I release it and push away from the PC."
    "Even though I was mentally prepared for a rush, he made it work anyway. What a stupid loss."
    show stunt smug at center with dissolve
    "Judging by the swagger in Stunt’s walk as he makes his way over to me, he either doesn’t notice the frustration I’m feeling or doesn’t care."
    s "Heh, easy. I call that one the Stunt Special."
    "I rub my forehead. Admittedly, the kid is pretty good. Accel was right to put me on his trail."
    show stunt neutral with dissolve
    s "Right, time to pay up."
    m "Oh, yeah. So listen, I’m thinking of start--"
    "I reach for my wallet mid-sentence and then freeze. It's not there."
    m "Hold up."
    show stunt frown with dissolve
    "I pat down all my pockets to discover that I simply don't have it. Did I leave it back at my apartment? I didn’t know I was showing up to a betmatch!"
    show stunt yell with Dissolve(.2)
    pause .2
    s "... Are you serious? You don’t have any money?"
    "With a blanched expression, I confirm his suspicion with a nod."
    show stunt notcool with dissolve
    m "I can explain this, really. I didn’t know I was showing up to a betmatch. Accel put me on your trail because I’m recruiting for a new team."
    "With a gaggle of middle schoolers egging him on with jeers, he thumbs his nose at me."
    show stunt mouthy with dissolve
    s "You’re just trying to get out of paying for your loss. That’s low. Real low."
    show stunt notcool with dissolve
    s "You couldn’t hold my all-in and don’t bring your wallet to a betmatch, and I’m supposed to expect you to organize a team? Yeah, I don’t think so."
    m "Stunt, wait. We’ve got—"
    "Shit. Jett is technically still on VIP… Can I tell him that she’s planning to leave? What if he tells someone? Why didn’t I think of this ahead of time!?"
    m "We… have some good players about to sign and a sponsor in the works. Nothing official, we’re trying to keep everything under wraps until then."
    show stunt yell with dissolve
    s "Yeah, people have tried this sketchy shit with me before. It’s not happening. I paid for your PC, and now you repay me with this crap? Get lost, lady."
    m "Wait! This is a great opportunity, I’m serious!"
    hide stunt with dissolve
    "But any hope I have of getting Stunt to change his mind is drowned out by the boos of the middle schooler cadre."
    somekid1 "You suck! You lost to Stunt, he’s the best!"
    somekid2 "Loser! Now he can’t buy me a juice!"
    somekid3 "Pay up, loser!"
    "I glance past the chest-high crowd to search out Stunt, but it’s too late. He’s gone."
    "How did I mess this up so bad?"
    window hide dissolve
    scene black with Dissolve(2.0):
        align (0,0)
    stop music fadeout 6.0
    $ renpy.pause(5.0, hard=True)
    scene image "char/bonus/dead.jpg" at center with Dissolve(2.0)
    pause 2.0
    menu:
        "Retry?":
            jump fS15RecruitingStuntPlayer
        "Quit":
            return
label fstuntwin:
    stop music fadeout 1.0
    window hide dissolve
    scene bg darkpcbang with dissolve:
        align (0, 0)
    play music "sfx/Warsong.ogg"
    window show dissolve
    "Stunt pushes through the dumbfounded crowd and comes stomping over, fury in his eyes. He really didn’t expect to lose."
    play sound "sfx/interupt.ogg"
    show stunt yell at center with Dissolve(.2)
    pause .3
    s "YOU BLINDLY SCOUT THE SMOKE IN YOUR BASE!? AFTER A CANNON RUSH!? ARE YOU KIDDING ME?! WHO DOES THAT?!"

    "I raise my hands defensively and skirt away from the victory screen splashed across my monitor."

    m "Woah, woah! Calm down. It takes like five seconds. And you have a reputation for those kind of builds, you know."
    show stunt frown with Dissolve(.2)
    pause .3
    "He makes a disgruntled sound and stares hard at me."
    show stunt mouthy with Dissolve(.1)
    play voice "sfx/shing2.ogg"
    s "You got lucky! Typical terran players. And I'm taking back my—{w=.5}{nw}"
    
    stop music
    play voice "sfx/StuntMom.ogg"
    show white with Dissolve(.1):
        align (0,0)
    show stunt surprised with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8)
    stuntmom "What are you yelling back there for? Didn’t I tell you to sweep up the backroom an hour ago? Stop screaming at our customers and go do something useful! Lord have mercy!"
    hide white with Dissolve(.2)
    "Without warning, the woman at the front desk paints Stunt a bright red from across the room."
    show stunt embarassed at center with dissolve
    "She glares at him for a moment longer before ducking back behind the counter. Talk about lousy bosses."


    play music "sfx/Stunt.mp3"
    "His anger replaced with modesty, Stunt scratches behind his head. The middle-schoolers have mostly dispersed, evidently destroyed by the cruel realization that their protoss god can bleed."

    s "... Ehh. Sorry. That’s my mom. Anyway, you beat me. Lemme go get your cash."

    "His mom? Egh, even worse. I guess I can see the resemblance, minus the bleached hair. Explains how he unlocked my PC, at least."

    m "Actually, wait. I didn’t come here for a betmatch."

    show stunt surprised at center with dissolve

    s "What? But we just played one."
    pause .4
    show stunt neutral at center with Dissolve(.3)

    s "... I don’t have to pay you then?"

    m "What? No. I’m recruiting for a new team. Accel mentioned that you were a free agent, and I wanted to see if you’d join up."

    m "I guess he thought it’d be funny to trick me into a betmatch with you."
    show stunt frown with dissolve
    s "A foreign team? Why didn’t you just send me a message or something?"

    m "No, a Korean one. And Accel said you’d probably assume I was a fangirl and block me. Although, I get the feeling that was just an excuse for this whole setup..."
    "Couldn't we have just kept this simple? What if I had lost?!"

    show stunt phone at center with dissolve

    "Stunt pauses and reaches for his phone. Distracted or no, he manages to carry on the conversation."
    show stunt eyebrow with dissolve
    s "Nah, blocking you sounds like something I’d do. Anyway, who else have you got?"

    m "We’ve got—"

    "Wait. Jett is technically still on VIP… Can I tell him that she’s planning to leave? What if he tells someone? Why didn’t I think of this ahead of time!?"
    show stunt phone with dissolve
    s "You've got...?"

    m "We… have some good players about to sign and a sponsor in the works. Nothing official, we’re keeping everything under wraps until then."
    show stunt frown with dissolve
    s "Sounds sketchy. A mystery sponsor and mystery players."

    "He doesn’t seem convinced. I can hardly blame him. This sort of thing is unfortunately common in eSports."
    show stunt neutral with dissolve
    $ persistent.en16_locked = False
    $ encyclopaedia.unlockEntry(en16, persistent.en16_locked)
    s "But Accel did vouch for you. That’s worth something. {i}And{/i} you beat me, the future protoss {color=#FF5E5E}bonjwa{/color}."

    m "Once we’ve got four players and some management, we’re going to pick out a team house. You'll need to live and practice with us."
    "I blink once, look away, and take a tactical pause."

    m "Oh, uh, if your mom will let you move out, that is."
    play sound "sfx/interupt.ogg"
    show stunt yell at center with Dissolve(.2)
    pause .3
    "He rises to my bait and straightens up, both fists clenched."

    s "You're damn right she's going to let me!"
    show stunt fist with dissolve
    s "Alright, consider me signed. If I've got a room and enough money to pay for food, we’re in business."
    show stunt neutral at center with dissolve
    "Stunt pauses and lowers himself from the tips of his toes."

    s "What’s the team called, by the way?"

    m "Like I said, it’s a work in progress. I’ll let you know when it’s picked out."
    show stunt smug with dissolve
    s "If we’re not named yet, I want a say in it." 
    show stunt neutral grin with dissolve
    s "How about AzureBlaze Phoenix Snipers?"
    "What even...? Kid, this isn't a shonen anime."
    m "Yeah. Probably not."
    "While Stunt revels in the afterglow of being signed to a StarCraft team, a thought occurs to me."
    m "Wait, don’t you go to school?"
    show stunt surprised at center with dissolve
    s "Uhh. Let's just say I'm between schools right now."

    "I don’t bother trying to divulge anymore information. If he can live in the team house and perform, that's good enough for me."
    "Some promising young pros deferred school for Brood War back in the day. And if StarCraft doesn’t work out for him, at least he's got a future cleaning up Stomping Grounds."

    m "Right. The mysteries won’t last for long, I promise. I’ll be in touch if I need you to show up somewhere."
    show stunt neutral with dissolve
    s "Okay. I’m going to hit you up for practice games tonight, if that’s cool. Be online."

    m "Sounds good. Welcome aboard."

    show stunt neutral grin with dissolve

    "The fiery protoss player lifts his chin for a final grin before heading into one of the PC bang’s back rooms, probably to gather a broom and dustpan."
    hide stunt neutral with dissolve
    "I grace Stunt’s mom with an innocent expression on my way out. She answers my smile with a glare sharp enough to make the hair on the back of my neck stand up."
    stop music fadeout 2.0
    stop sound fadeout 2.0
    window hide dissolve
    scene bg streetside2 with Dissolve(1.0):
        align (0, 0)
    window show dissolve
    "I step outside and suck in a deep breath, relieved. The warm, afternoon air is sweet and feels good in my lungs."

    "One down."
    window hide dissolve

label fS16Reflection1:
    scene black with squares:
        align (0, 0)
    pause .8
    play music "sfx/Searching for Game Master.ogg" fadein 2.0 loop
    pause .8
    play voice "sfx/doorclose.mp3"
    pause .4
    scene bg apartmentnight with squares:
        align (0, 0)
    window show dissolve
    "The stairway to my apartment was empty as usual. Sometimes it feels like I’m the only person living in this building."
    "Isolation was a major concern when I was first thinking about coming overseas. If my Korean wasn’t passable, it’d practically impossible for me to be anything but lonely." 
    "That's something I don't need to worry about anymore, I suppose. Seoul's proven to be vibrant, crowded, and busy. Everything my life back home wasn’t."

    "Something as simple as crossing the street can be exciting for someone who has never been in an urban environment for more than a few hours at a time. It sounds stupid, but it’s true."

    "Still, before meeting Accel and Jett, I barely talked to anyone offline. StarCraft’s one on one nature doesn’t exactly lend itself to social introductions."
    "It'd be easy to get in touch with the foreigner community out here. But I have very little desire to skulk around bars with jaded English teachers and washed-up businessmen. Why bother?"
    play voice "sfx/jam.ogg"
    "I sink into my chair and jam the spacebar a few times to wake up my PC. I practiced enough at Golden Zonefire after recruiting Stunt, so I don’t bother loading up StarCraft."
    "Jett was pleased to hear about my new pickup. Told me it was smart to hold off on telling Stunt who she was, too."

    "I’m sure she’ll announce her plans on her own time. She’ll have to once we’ve picked up our last player at any rate."
    play voice "sfx/clickclick.ogg"
    "With a few clicks I’m staring at a common StarCraft fan site. The most interesting stuff that goes on in the scene gets posted here, and what people vote as best rises to the top of the page."

    "I don’t often visit the Korean community sites. I like them just fine, but I prefer to read English when I get the chance."

    "But no matter where you choose to get your StarCraft news, you’ll find no shortage of netizens sure in their opinions on which player is awful or why the game is imbalanced."
    play voice "sfx/click.ogg"
    show reddit:
        xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    with dissolve
    "Today seems to be no exception. A foreign pro-gamer just called it quits, and the comments about him are ridiculously scathing."
    "Sure, he was underperforming recently. But people forget just how much time and passion gets put into even a mediocre professional’s career."
    "The worst part is that most of the people talking smack are either low leaguers or don’t play the game at all."
    hide reddit with dissolve
    play voice "sfx/unlock.ogg"
    "I take out my phone, hoping to find something on it to distract me from the mindless masses. No texts, no new emails. Same as when I last checked fifteen minutes ago."
    play voice "sfx/lock.ogg"
    "It’s been awhile since I’ve chatted with my friends from back home. Most of them know about my eSports aspirations, but none of them really get it."
    "There’s two reactions when someone learns that you play video games full time: Either they roll their eyes, or they tell you how lucky you are."
    "I’ve tried to explain to the latter that playing StarCraft really isn’t fun in the traditional sense. Winning can be satisfying, but the game is too stressful to actually be called fun. At least, for me." 
    "It beats a boring minimum wage job, but it sure as hell isn’t easy and pays less for all but the best. Yeah, they don't mention that between games on StarLeague streams."
    "Pretty much everyone I went to high school with is enrolled in college. When I hear about their great social lives and internships, I can't help but feel jealous."
    "I’ll probably end up going eventually. It’s not like I can make a living from games when I’m thirty."
    "Five or six years of StarCraft, and then you’re left with the dregs of your prize money and sore wrists. And hopefully some friends and fond memories."
    "With a look back at the computer screen, I notice that my inbox has a message awaiting. A click, and I’m staring and at a piece of hatemail, one of several I’ve already received this month."
    play voice "sfx/click.ogg"
    show image "bg/jerk.jpg":
        xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    with dissolve
    "It's something I've had to deal with for pretty much my entire life, but things really amped up when my stream hit five hundred viewers for the first time."
    "There's not much to say other than that I'm used to this sort of thing by now. I quit streaming to focus on improving for my own sake, not for the idiots that send me shit like this."
    "At least, that's what I tell myself. It's hard to know for sure."
    show image "bg/jerk.jpg":
        alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
        easeout .5 ypos 0.6 alpha 0.0 subpixel True
    $ renpy.pause(.5)
    "Most of the people who follow StarCraft know less about the game itself than they do about the people playing it. I don't like that I'm expected to constantly bear the scrunity of strangers."
    "The community is what keeps the scene alive. I know it's wrong to loathe it. But simply knowing that doesn't make it any easier not to."
    "With an impatient click, my PC groans off. I climb under my sheets and settle in for an early night’s rest."
    play voice "sfx/bed.ogg"
    pause .5
    "The search continues tomorrow."
    window hide dissolve
    stop sound fadeout 2.0
    stop music fadeout 2.0

label fS17AccelsTipAboutRevaPlayer:
    scene black with midfade:
        align(0,0)
    pause 1
    play sound "sfx/rain.ogg" fadein 4.0 loop
    pause 1
    scene bg rain with midfade:
        align (0, 0)
    window show dissolve
    "I wake to the sound of rain against my window. Judging by the light, it's morning."

    "It dawns on me that I was supposed to play Stunt in a few practice games last night. Whoops. Probably not a great move to blow off the player I just recruited."
    play voice "sfx/eating.ogg" loop
    "Breakfast this morning is cold as usual, or at least since I took a chance on some street food. "

    "It was actually pretty good, but I ended up sick for a few days. I’ve stuck with cereal in the mornings since then."

    "I hope everything is working out on Jett’s end. Good management and even a single sponsor will take us a long way. "

    "All I can do is focus on the task at hand: finding talent."

    "I put away my bowl once I’ve emptied it and lock my apartment on the way out."
    stop voice fadeout 1.0
    window hide dissolve
    play voice "sfx/doorclose.mp3"
    scene black with squares:
        align (0, 0)
    stop sound fadeout 1.5
    pause 1
    scene bg pcbang with squares:
        align (0, 0)
    play sound "sfx/apmsound.ogg" fadein 2.0 loop
    window show dissolve
    "My jacket's hood held up against the rain for most of the way, but my hair ended up soaked in the end." 
    "I shake my head dry once I'm inside, much to the annoyance of the guy at Golden Zonefire's front desk."

    "The cafe is largely empty on most weekdays, at least before schools let out. "

    "With a bit of searching, I find Accel reclined drowsily in a computer chair that he must have wheeled over to the lounge area. "
    window hide dissolve
    stop sound fadeout 2.0
    scene bg cafe:
        align (0, 0)
    show accel neutral at center
    with dissolve
    play music "sfx/Full Server Intro.ogg"
    queue music "sfx/Full Server Loop.ogg"
    window show dissolve
    "I'll bet he'd rather be sleeping in at the Crash team house, but Accel said that he didn’t have time to meet me any later."
    show accel thinking with dissolve
    "He yawns and waves me over. I pull up a chair from a nearby PC and sit beside him—plenty to choose from when the place is this empty."
    show accel neutral with dissolve
    a "Do they not have umbrellas outside of Korea?"
    m "No. Everyone just sprints from place to place if it rains."
    show accel laughing with dissolve
    a "Ha. So, anyway, Stunt agreed?"
    m "Yeah. It’ll make the next pick-up even easier since I’ve actually got another player to point to. I wish Jett would hurry up and ditch her team already."
    show accel concerned with dissolve
    "Accel raises an eyebrow and shakes his head at me."

    a "She can’t do that yet. Jett has a contract."

    m "It has to be over soon though, right? Why else would she be putting together a team if she wouldn’t be able to play on it?"
    show accel thinking3 with dissolve
    a "They vary, but most contracts last either six months or a year. Best case scenario, she’ll be free at the end of the month."

    "That makes sense. The Victory StarLeague won’t let anyone with a contract play without their team's approval, but maybe there’s no rule against registering ahead of time?"

    "Whatever, I’m sure that Jett has this figured out already."

    m "Right. Anyway, you said you’ve got a lead on the next player, yeah?"
    show accel neutral with dissolve
    a "Yep. Guy named Reva. Flits in and out of top eight on the ladder. He’s won at least a dozen online tournaments this year."

    m "Wow. What race does he play?"
    show accel thinking2 with dissolve
    a "Here’s the best part. He plays all three. His terran is his strongest, but he’s been known to switch between races during a long set. He'll even play random."

    "Reva plays zerg, terran, and protoss? Woah. That sounds too good to be true."
    show accel thinking with dissolve
    a "But this is where it gets weird. He’s never turned up to a tournament in person. Only plays online. Some people speculate that Reva is just an alias for a top player." 
    show accel thinking2 with dissolve
    a"I’m not convinced, though." 
    $ persistent.en8_locked = False
    $ encyclopaedia.unlockEntry(en8, persistent.en8_locked)
    a "He’s got a very specific playstyle. It’s almost like playing against a highly advanced A.I. Strong mechanically, but only goes for standard {color=#FF5E5E}macro games{/color}."

    m "So how am I going to get in touch with him? Other teams have to have gone after a player that good."
    show accel confident with dissolve
    a "It won’t be easy, but I’ve got a plan."

    m "Not another betmatch, please…"
    show accel neutral with dissolve
    a "Heh. It worked, didn’t it? No, no. Not this time."
    show accel thinking with dissolve
    a "Reva’s on a mean win streak in an online king of the hill. Twelve wins in a row."
    show accel thinking3 with dissolve
    a "Granted, most of his games have been against foreigners. It's based in Europe so it's at a weird hour for us..."
    show accel neutral with dissolve
    a "Point is, you’re going to enter tonight."

    m "Tonight? So I beat him, and then use that to convince him to join the team?"
    show accel thinking2 with dissolve
    a "Hold on. I didn’t say anything about beating him. I mean, if you do, I’m not going to complain." 
    show accel confident with dissolve
    a "You’re going to play an {nw}"
    play voice "sfx/yoo.ogg"
    extend "{w=.4}{i}honorable macro game.{/i}"
    show accel neutral with dissolve
    a "Reva hates anything that’s non-standard. Cheese, rushes, aggressive timings, all-ins, one-base builds... That sort of thing. So you're going to play a slow, economy-based game instead."

    m "But if I play a game in the exact style he’s used to, won't I get stomped?"
    show accel thinking with dissolve

    a "Maybe. But it’s your only chance to get on his good side. Play him, show off your skill, chat him up, and recruit him."

    m "You make it sound so easy."
    show accel neutral with dissolve
    a "Hey, find your own players if you don’t like it. I’m sure there are tons of strategy forum scrubs willing to tryout."
    show accel thinking2 with dissolve
    "He does have a point. Guess I’m staying in tonight."

    m "Fair enough. By the way, what are you so busy with this afternoon?"
    show accel concerned with dissolve
    a "Team league practice. Gotta drill a zerg of ours to snipe the Team KaiNE terran ace."
    show accel neutral with dissolve
    a "The match is half a week away. Until then, practice, practice, practice. That’s how we do it."

    "Beneath his easy facade, I can tell that Accel doesn’t seem too pleased by the circumstance."

    m "Right then. Any final tips against Reva before I go practice for tonight?"
    show accel laughing with dissolve
    a "Yeah. Hope you like mech."
    "It's all I can do not to groan."
    m "My favorite."
    window hide dissolve
    stop music fadeout 2.0

label fS18BattleRevaOnline:
    scene black with squares:
        align (0, 0)
    pause 1
    play sound "sfx/nightcricket.ogg" fadein 4.0 loop
    pause 1
    scene bg apartmentnight with squares:
        align (0, 0)
    window show dissolve
    "The admin said it shouldn’t be more than five minutes now. Reva just got finished extending his record to thirteen wins."

    "I’m already warmed up from practicing all day, so there’s no point of loading up a map to drill my micro or anything like that. "

    "The only thing I’ve got to focus on before the game is my build and my nerves."

    "Most players, myself included, tend to get a little bit jittery before a high stakes match. "

    "It’s a more serious issue at live events with all the lights and cameras and cheering fans, but it can happen in an online setting just as easily."

    "This king of the hill is broadcast on a commentated livestream. The channel hosting it isn’t particularly popular, but the exposure can’t hurt."

    "Unless I get beat really, really badly."

    #(SFX) game invite
    play voice "sfx/clickclick.ogg"
    "Looks like the game is getting started. In the pre-game lobby, Reva remains utterly silent even after I offer a friendly glgl."

    "Whatever. Let’s get this going."
    stop sound fadeout 2.0
    window hide dissolve
jump frevabattle1


label frevalose:
    play music "sfx/Warsong.ogg" fadein 2.0
    scene bg apartmentnight with dissolve:
        align (0,0)
    window show dissolve
    "Phew. That didn’t go so bad. Reva went down a little easier than I expected, though."
    "Does this mean I need to continue with the King of the Hill? I hadn’t considered that. Gotta wrap up a conversation with Reva quickly in that case."
    "I open up a chat and fire off a message."
    nvl clear
    m_nvl "{cps=0}gg. lucky hard counter for me lolol;;"
    "… Nothing."
    "Even after thirty seconds, there’s still no response. Adamantly, I try once more."
    m_nvl "{cps=0}hey listen, you play pretty well. would you be interested in some practice?"
    "What follows my second message is not a response, but a notification that Reva has gone offline."
    nvl clear
    "What! What is this guy in such a hurry for? Because I rushed him?! How the hell am I supposed to get into contact with this guy now?"
    "I think to ask through one of the tournament organizers for him to unblock me. But before I can do so, I receive an invite to the next game."
    "In the pre-game lobby, my new opponent takes a few subtle jabs at my strategy from last game."
    o_nvl "{cps=0}keke, you haven’t watched this koth’s stream before have you?"
    m_nvl "{cps=0}? no, why"
    o_nvl "{cps=0}take my advice, dont cheese again if you like your reputation ^^"
    "Rather than pry an answer out of this stranger, I decide to turn on the stream and see what he’s talking about for myself."
    "… And I find that the casters are talking trash about me. Seriously? Just because I did a rush build?"
    "What kind of arrogant assholes are these commentators? Screw this. If Reva couldn’t handle a rush and frequents a King of the Hill like this, then why would I bother recruiting him?"
    "Frustrated, I make my opponent aware that I’m forfeiting the match and shut off my PC in a huff."
    window hide dissolve
    scene black with Dissolve(2.0):
        align (0,0)
    $ renpy.pause(5.0, hard=True)
    scene image "char/bonus/dead.jpg" at center with Dissolve(2.0)
    pause 2.0
    stop music fadeout 2.0
    menu:
        "Retry":
            jump fS18BattleRevaOnline
        "Quit":
            return

label frevawin:
    scene bg apartmentnight with dissolve:
        align (0,0)
    play sound "sfx/nightcricket.ogg" fadein 1.0 loop
    window show dissolve
    play voice "sfx/keyboard2.ogg"
    "Okay… Can’t screw this up. I pop open a chatbox and fire off a message."
    play voice "sfx/chatbeep.ogg"
    nvl clear
    m_nvl "{cps=0}your macro is too good lolol"

    "For a while, no response. But just when I’ve given up hope that he’ll message me back..."

    r_nvl  "{cps=0}Thank you. You play well. You made only a few key mistakes."

    "Perfect capitalization and grammar? Ugh, whenever anyone does this to me, I feel obligated to fix my typing. "

    "Screw it, I’m way too tired after forty minutes of positional play."

    m_nvl "{cps=0}oh ya? well thanks. im actually looking for some practice partners, kinda."

    r_nvl "{cps=0}Kind of? How?"

    m_nvl "{cps=0}well, im starting a team with a few friends. we’re gonna try to qualify for team league."

    r_nvl  "{cps=0}I see."

    m_nvl "{cps=0}im actually looking to pick up another player atm. would you be interested?"
    "For almost ten seconds, nothing. Each second ticking by feels longer than the last. But then..."
    r_nvl  "{cps=0}I am willing to discuss the possibility."

    m_nvl "{cps=0}oh awesome, we’re gonna meet up at golden zonefire tomorrow afternoon. you’re in seoul, ya? you know where it is?"

    r_nvl  "{cps=0}Oh. You wish to meet in person?"
    window show dissolve
    nvl clear
    "C’mon! I’ve already come this far! Keep it together!"

    m_nvl "{cps=0}ya just gonna hang with the team and practice a bit. we’re nice, I swear."

    "Another pause, this time longer. I find myself drawing closer and closer to the screen in anticipation of Reva’s reply."
    r_nvl  "{cps=0}Very well. I will see you and your teammates at Golden Zonefire tomorrow. How do you suggest I find you?"

    m_nvl "{cps=0}kk. look for the foreigner lol."

    r_nvl  "{cps=0}I will do so. Goodbye."

    "With that, Reva exits our chat and prepares for his next king of the hill match."

    play music "sfx/brooding.ogg"
    stop sound fadeout 2.0
    "Did I do it? Did I recruit our last player? Can I celebrate yet?"

    "No. Better to wait. I mean, he’s never even been to an event in person before. There’s a chance that he won’t show."

    "I step out of my chair and fall onto my bed, simultaneously tired and restless. I shut my eyes, but there’s no way I’m going to sleep tonight with this hanging over my head."

    "Maybe I should go to Go-Mart. It’s not a good idea to drink caffeinated stuff this late at night, but a walk might get my mind off of the stress."
    play voice "sfx/keys.ogg"
    window hide dissolve
    play voice "sfx/doorclose.mp3"
    scene bg streetnight with fade:
        align (0, 0)
    pause .2
    play voice "sfx/StepDown.ogg"
    pause 1.0
    window show dissolve
    "Since meeting Accel and Jett, the pangs of homesickness haven’t been nearly as bad."

    "Should I feel guilty that I only want to update my old friends or my parents now that I’ve actually got something going my way? Is it better to keep these small victories to myself?"

    "When was the last time I even spoke English? I honestly can’t remember."

    "I never had to move around or switch schools when I was a kid, but maybe this is the same thing. You find a group and stick with it. Keeping in touch with your old friends becomes too difficult."

    "It could be a good thing. More focus on making my eSports career work than on what so and so switched his major to."
    window hide dissolve
    scene bg streetside2night with Dissolve(1.0):
        align (0, 0)
    window show dissolve
    "I can’t help but feel a little unsure. Putting my old life down isn’t easy knowing that I’ll have to pick it back up eventually."
    stop sound fadeout 2.0
    stop music fadeout 2.0
    "My thoughts of home fade as the green and white signage comes into view."
    window hide dissolve
    play voice "sfx/storedoor2.ogg"
    scene bg store with Dissolve(1.0):
        align (0, 0)
    play music "sfx/Loading progress 1.ogg"
    window show dissolve
    play sound "sfx/AC.ogg" fadein 1.0 loop
    "The old man is behind the counter as always, this time restocking the shelf on his side beneath the cash register."

    "I take my usual fare from the refrigerators in the back of the store and step to the counter. The clerk’s haggard eyes linger on me for a moment before he returns to his shelf-stocking."
    show yeon neutral at center with dissolve
    c "Just a moment."
    hide yeon with dissolve
    "I’m in no rush so I answer him with a nod. I let the drinks rest on the laminated counter and turn to take a closer look at the convenience store."
    play voice "sfx/cans.ogg"
    "It’s compact and clean, like pretty much everything else in Seoul. If it has any employees other than the old man on duty, I don’t see them."

    "Most stores don't have foreign snacks or drinks aside from their localized variants, and Go-Mart is no exception to that. I’ve had to be bold in trying new food."

    "Just as I'm about to step towards a bag of strange looking trail mix, the clerk’s voice sounds from behind."

    c "You’ve been in here quite often, haven’t you?"
    show yeon neutral at center with dissolve
    "I turn, surprised. He’s staring right at me."

    m "Err, yeah. I’m not… That’s okay, isn’t it?"

    "He pauses in surprise, likely at my language proficiency, and then presses right on."
    show yeon smile with dissolve
    c "More than okay. Those drinks don’t buy themselves. What’s your name?"
    m "I'm Mach.{w=.6}.. Uh, wait a second. That's not right."
    "Strangely enough, I haven’t had to share my real name with anyone since I came overseas. It feels unfamiliar on my tongue as I prepare to correct myself."
    "But before I can, the clerk furrows his eyebrows at me."
    show yeon neutral with dissolve #seems wrong
    c "Mach? That doesn’t sound like any kind of foreign name I’ve heard before."
    "How am I in this situation? Dammit."
    m "It’s hard to explain. Um, do you know what StarCraft is?"

    "The elderly cashier’s eyes light up in understanding."
    show yeon smile with dissolve
    c "I’ve heard of it. You’re a pro-gamer then?"

    m "Yeah. Working at it, at least."
    show yeon neutral with dissolve
    c "I suppose that explains your late night shopping trips. How long have you been in Seoul?"

    m "A little more than a month. I like it here."

    c "Good. It’s a fine city." 
    
    c "You can call me Mr. Yeon, by the way. It's good to meet you, Mach."
    
    "I simply nod and then look away. I'm not particularly good at talking to strangers about anything other than StarCraft."

    "The conversation between us doesn’t lead anywhere else, so he starts ringing up my drinks. With the bottles bagged and offered, he smiles."
    show yeon smile with dissolve
    y "Take care now."
    window hide dissolve
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene bg streetside2night with Dissolve(1.0):
        align (0, 0)
    window show dissolve
    "I make my way back to my apartment for an evening of StarCraft and little sleep."
    window hide dissolve
    jump  fS19MeetupWithRevaPlayer

label fS19MeetupWithRevaPlayer:
    scene black with midfade:
        align(0,0)
    pause 2
    play music "sfx/Blue Pineapple.ogg" fadein 4.0
    scene bg cafe:
        align (0, 0)
    show stunt notcool at center
    with midfade
    window show dissolve
    s "Remind me why we have to meet up here again? I get to play for free at my mom’s, you know."
    m "And you probably get yelled at if the toilet clogs up too."
    show stunt phone at center with dissolve
    "Stunt rolls his eyes and pulls out his cell phone, thumb soon jamming away at some weird puzzle game."
    m "What is it exactly that you're always playing on your phone?"
    show stunt neutral with dissolve
    s "I'm glad you asked! It's called {i}PopPop Safari{/i}. It's one of those casual games meant to sucker morons out of their money."
    m "And you're playing it why...?"
    show stunt neutral grin with dissolve
    s "It's my own way of fighting back against something I hate. I'm going to defeat this game in its entirety without paying a single cent!"
    m "I don't understand how that stops anything. They're still making money from everyone else, aren't they?"
    "I steal a glance at his phone."
    m "... And there are tons of ads all over your screen. Look."
    show stunt yell with dissolve
    s "You don't understand. It's about the principle!" 
    show stunt phone with dissolve
    s "And I wouldn't be playing it in the first place if this dude had showed up when you said he would."
    hide stunt with dissolve
    "Admittedly, Reva should be here by now, but I can’t do anything except wait for him to arrive."
    "I texted back and forth with Jett a bit earlier today. She’s too busy wrapping things up with her contact to make it to Golden Zonefire until way later. "
    "From the tone of her messages, it seemed like talks with the sponsor were going well."
    "With word that I managed to pick out our fourth player, she gave me the go ahead to divulge her identity to Stunt and Reva. Helpful, since we still have a coach and practice partners to recruit."
    "I hear the door to Golden Zonefire slide open and I glance over, hopeful."
    play sound "sfx/slidingdoor.ogg"
    scene bg pcbang with dissolve:
        align (0, 0)
    show reva shy at center with dissolve
    "... Only to find a bespectacled girl walk inside and look around. Tch, no dice. Where the hell is he?"
    show reva neutral with dissolve
    "The girl stands at the cafe's entryway for a while, apparently searching for something. Eventually, her eyes catch and then stay on me."
    "Huh. It looks like she’s coming our way."
    scene bg cafe:
        align (0, 0)
    show stunt phone at right:
        xpos .97
    with dissolve
    show reva neutral at left with dissolve:
    "Stunt glances up from his cell phone once I turn to address the newcomer. She hesitates before speaking and delivers her words quietly."
    r "{w=1}Excuse me, are you Mach?"

    m "Oh, hi. That’s me."
    show reva neutral2 with dissolve
    r "I apologize for the delay. I disembarked the subway a stop too early. Is this one of the teammates that you mentioned?"
    show stunt frown with dissolve
    "She shifts her focus from me to Stunt. His expression is no doubt as perplexed as my own. Is she…?"

    m "Wait a second. Are you Reva?"
    show reva neutral with dissolve
    r "Yes, I am."
    show stunt neutral with dissolve
    m "Oh, I’m sorry! I didn’t realize that you were also... Uh, I just assumed..."

    "I trail off quietly. If the mix-up bothered Reva, she doesn’t show it. She tilts her head slightly and edges closer to our table."
    show reva at left:
        easein .5 xpos 0.06
    $ renpy.pause(.5)
    r "May I sit?"

    m "Of course. Reva, this is Stunt. He’s the team’s only protoss."
    show stunt smug with dissolve
    s "Sup."

    "He silences the obnoxious bleeps and bloops of his phone’s game in his pocket and bobs his head at Reva."
    show stunt neutral grin with dissolve
    s "Reva, huh? Doesn’t sound too familiar. You must be some online hero."
    show reva glasses with dissolve
    r "Stunt. I am familiar with you."
    show stunt surprised with dissolve
    s "Eh? How? {w=.5}{nw}"
    show stunt2 neutral grin at right:
        xpos .97 alpha 0.0
        linear .2 alpha 1.0
    show stunt at right:
        alpha 1.0 xpos .97
        linear .3 alpha 0.0
    extend "I mean, of course you are! {w=.2}I'm the god of protoss after all!"
    show reva neutral with dissolve
    hide stunt
    r "No. We have matched on ladder several times. Your play is predictable and unproductive."
    show stunt yell at right:
        xpos .97
    hide stunt2
    with dissolve
    $ persistent.en20_locked = False
    $ encyclopaedia.unlockEntry(en20, persistent.en20_locked)
    s "Woah, hey! To {color=#FF5E5E}expand{/color} is to give mercy, barcode scum! Don’t be a hater."
    show reva frown with dissolve
    $ persistent.en17_locked = False
    $ encyclopaedia.unlockEntry(en17, persistent.en17_locked)
    r "You should aspire to more than rush builds and gimmicks. The {color=#FF5E5E}meta{/color} no longer favors aggressive play."
    show stunt notcool with dissolve
    s "Mach, you didn’t tell me that this chick was so uptight. Is the rest of the team this lame?"
    show reva neutral with dissolve
    "Both of them rest their eyes on me, expectant. Now or never, I guess."

    m "You won’t need to worry about lackluster teammates. Jett is actually the one who’s setting this whole thing up."
    play sound "sfx/ding.ogg"
    show stunt surprised
    show reva surprised
    with Dissolve(.2)
    pause .2
    r "Jett?!"

    m "That's right."
    show stunt neutral grin
    show reva glasses
    with dissolve
    "With crossed arms, I beam a confident grin at the two of them. Stunt wears a mixture of surprise and excitement, while Reva seems to simply be processing the development."

    s "But isn’t she on VIP?"

    m "For now. But she’s not happy with her practice environment or how much they’re paying her, so she’s not going to renew her contract at the end of the month."
    show reva expected with dissolve
    r "Interesting."

    "Reva pushes her glasses against the bridge of her nose, silent. Stunt looks like he wants to simultaneously call me a liar and a genius."
    show stunt yell with dissolve
    s "How exactly did you end up recruiting for Jett? It’s not like she has any need for some mediocre foreigner."

    m "Mediocre foreigner that slapped down your terrible cheese build, Stunt. And I’ll be the first to admit I’m lucky to sit where I am. The same is true for the two of you."
    show stunt surprised
    show reva neutral2
    with dissolve
    m "Practice hard and maybe we can make something of ourselves and this team. Sound good?"

    "I’m in no way the captain of this squad, so it feels a little weird to take such an authoritative tone. Still, Stunt backs down and dons a thoughtful expression."
    show stunt neutral with dissolve
    s "Yeah, alright. You’re right. This could be big."
    show reva neutral with dissolve
    r "I agree. Your offer had piqued my interest, but word that a player as accomplished as Jett will be among us has secured it. I will join."

    m "Perfect. She’ll be happy to hear it. That leaves only the matter of a sponsor, which Jett is taking care of as we speak, and a coach." 

    m "We’ll obviously want to keep an eye out for anyone else with some talent… But for now, this is our roster."

    "The three of us share a long look at one another. Before any other thought can come to mind, Stunt ends the silence."
    show stunt frown with dissolve
    s "Wait a second. I'm going to live with a bunch of girls? This isn't one of those sponsor-bait teams, is it?"
    show stunt yell with dissolve
    s "MACH! Did you trick me into signing on as a practice drone?! This was not part of the future protoss bonjwa's plan!"
    m "Uh, no. Does Jett strike you as the type of person to run a team like that? Also, I thought Reva was a guy."
    show stunt neutral with dissolve
    s "Oh. Right."
    show reva glasses with dissolve
    r "What is the name of our team?"
    m "Oh. Uh. We haven’t picked one out yet."

    r "That is troublesome. Should not such a thing been taken care of by now?"

    "I really should have gotten around to asking Jett. Stunt shares in Reva’s indignation with a gesture towards her."
    show stunt fist with dissolve
    s "Thank you! We need to get this done already. How about we call ourselves the Lamenting Reapers?"

    "The hell? What is it with this kid and terrible team names?"

    m "I’ll talk with Jett tonight, okay? All you guys need to do is practice and wait for the announcement. You also need to be prepared to move out."
    show stunt neutral
    show reva neutral
    with dissolve
    "It’s pretty short notice, but neither of them protest so it hopefully won’t be a problem. Stunt definitely lives with his mom... It’s harder to tell with Reva."

    "She seems to be about my age, maybe a bit younger. It’s possible she lives on her own."

    r "Very well, as long as the matter is not being neglected. Was there more of importance to go over?" 

    r "If not, I would prefer to return home. A PC bang is an improper practice environment."
    show stunt neutral grin with dissolve
    s "Pft, you’re just a shut-in. Don’t deny it, it’s written all over you."
    show reva frown with dissolve
    r "I am not. What right do you have—"
    play sound "sfx/lurch.ogg"
    show stunt at right:
        easein .2 xpos .8
        easeout .1 xpos .82
    show reva surprised with Dissolve(.2)
    "But before she can say anything else, Stunt lurches forward, grabs Reva by the wrist, and begins dragging her towards the PCs."

    s "If you’re going to live in our team house, you better get used to practicing next to other people."
    show stunt smug with dissolve
    s "Let me show you one of my favorite ‘unproductive’ builds."
    hide stunt
    hide reva
    with dissolve
    stop music fadeout 2.0
    stop sound fadeout 2.0
    window hide dissolve

label fS20MeetMrKim:
    scene black with squares:
        align(0,0)
    pause 1
    play music "sfx/Full Server Intro.ogg"
    queue music "sfx/Full Server Loop.ogg"
    scene bg pcbang with squares:
        align (0, 0)
    window show dissolve
    #screenshots
    "Hours of games together serve the three of us well. Most professional gamers have a certain level of respect for someone that can put up strong matches, even if they don’t have great results. "

    "While Stunt and Reva have playstyles as wildly different as their personalities, both are formidable opponents."

    "Golden Zonefire’s peak time passed about an hour ago. While it’s not nearly as empty as it was when Reva arrived, there’s enough room that we have a relatively quiet section to ourselves."

    m "Hey Reva, Accel told me that you know all three races. Why are you only playing terran?"
    show reva glasses at center with dissolve
    r "Terran is the best choice given the current metagame. It is also the only race that earns one hundred percent of its wins."

    "Blunt, but I can’t deny her logic. Especially when she puts up such a strong match. She’s pretty biased when it comes to game balance, though."
    hide reva with dissolve
    "I’ve got to say, Stunt’s unit control is ridiculously precise. It’s a shame he only puts it to use with his so-called innovative strategies."

    "Jett’s on her way with some good news, or so a text from her says. The only thing that’s keeping my mind off of her imminent arrival is the game between Stunt and Reva unfolding ahead of me."
    window hide dissolve
    scene bg revastunt intro with dissolve:
        align(0,0)
    window show dissolve
    "Stunt’s going proxy two gate yet again. Reva scouted it four of the last five times he’s tried it. He’s just being stubborn at this point."

    "Still, the map is well-suited for the build, and he’s already managed to kill an SCV with some good probe micro."

    play sound "sfx/battle/marinegroupshooting.ogg" fadein 1.0
    show bg revastunt zealotrush with Dissolve(.3):
        align(0,0)

    "Reva’s defense is formulaic as always. So far it’s working, but she’s in for a bit of a surprise after I sneak a glance at Stunt’s screen."
    show revastunt proberush with easeintop:
        xalign 0.4
        yalign -0.1
    "A half-dozen probes stream up Reva’s ramp and cut off an exit for the two marines kiting a pair of zealots."

    stop sound fadeout 1.0
    hide revastunt with dissolve

    window hide dissolve
    play sound "sfx/fastslash.ogg"
    show blacksolid at right:
        xpos 2.0
        linear .1 xpos 1.0 subpixel True
    pause .3
    play sound "sfx/zealotslash.ogg"
    show swoosh1 yellow at center behind blacksolid
    show blacksolid at right:
        linear .1 xpos 0.0 subpixel True
    show swoosh1 yellow  at center  with Shake((0.5, 1.0, 0.5, 1.0), .3, dist=8)
    show bg revastunt surround behind swoosh1:
        align(0,0)
    hide swoosh1 with Dissolve(0.1)
    play sound "sfx/battle/zealprobesattacking.ogg" fadein 1.0
    window show dissolve
    "The protoss units close the distance and slice the pair of marines to pieces, securing a massive advantage that Stunt carries into a victory."
    scene bg pcbang with dissolve:
        align (0,0)
    play sound "sfx/apmsound.ogg" fadein 2.0 loop
    play voice "sfx/clack.ogg"
    show stunt neutral grin at center with Dissolve(.2)
    pause .2
    "Stunt pushes away from his monitor and stands, hands on his hips."
    s "Easy!"
    "Reva doesn’t let it faze her. She rotates in her chair and shrugs."
    show stunt at right:
        xpos 0.95
    show reva neutral at left:
        xpos 0.05
    with dissolve
    r  "Unorthodox and inconsistent. But it worked, I will admit."
    show stunt frown with dissolve
    "Stunt basks in the glory of victory for a moment longer before something behind me catches his attention."
    hide stunt
    hide reva
    with dissolve
    show jett neutral at left
    show kim neutral at right 
    with dissolve
    "I follow his gaze to find Jett and a man in a business suit walking towards us. He seems out of place dressed so well in a PC bang."
    show jett neutral3 with dissolve
    j  "Mach and… Reva, right? This is Mr. Kim, VP of partnerships at Enoch Group. His company is looking to get into eSports."
    show jett considering with dissolve
    "The casual timbre of her voice and the pained look on her face says it all: Do not screw this up. I tighten up my posture and lower my head in a bow at the exec."
    hide jett
    show kim neutral at center
    with dissolve
    m "It’s nice to meet you, Mr. Kim. What does your company do?"

    "... And realize too late that I probably shouldn't have admitted that I've never heard of Enoch."
    show kim confident with dissolve
    "Jett seethes through her teeth, but Mr. Kim takes my question with an easy smile and offers me his business card."
    hide kim
    show card:
        xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    with dissolve
    "I give the card a brief once-over before placing it carefully in my pocket."

    show card:
        alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
        easeout .6 ypos 0.65 alpha 0.0 subpixel True
    show kim confident behind card at center with dissolve
    k "We’re in a handful of markets and offer a variety of business services. Consulting, marketing, and a few other things."

    m "Oh. That sounds important."
    show kim neutral2 with dissolve
    "And vague, though I don’t say that. Truth be told, I’m pretty much clueless when it comes to business related things." 
    "Stunt and Reva’s deer-in-the-headlight silence isn’t exactly helping, either."
    show kim neutral with dissolve
    k "But it’s as Jett says. eSports is a fascinating industry with strong potential for continued growth. I'm particularly interested in strategic opportunities based on its unique qualities."

    k "I’ve proposed the idea of sponsoring a fresh team to Enoch’s board, but for now we’re just shopping around."
    show kim smug with dissolve
    "He pauses to observe my reaction. I get a strong feeling that this guy is a pro at negotiation."

    "As if she suspects the very same thing, Jett steps forward to prevent me from saying anything that could take away her leverage."
    show jett casual at left
    show kim at right 
    with dissolve
    j  "As I said before, we’re still not ready to accept any offers. You have our interest, but we're keeping our options open for the time being."
    show kim neutral with dissolve
    k "Of course, there's no rush. I merely wanted the chance to introduce myself."
    show jett smile with dissolve
    j  "Mm. And we’ve got plenty to discuss. Thank you for the ride, Mr. Kim."
    k "It was no trouble. We’ll be in touch."
    hide kim with dissolve
    "And with that, the businessman departs just as quickly as he arrived. It’s only once he’s gone that I realize just how tense my shoulders are."
    show stunt neutral grin at right
    show jett neutral at left:
        xpos -.05
    with dissolve
    s "That guy looks like a secret agent or an insider. Can we name our team that? Secret Agentz?"
    show jett neutral3 with dissolve
    j "Is this Stunt, Mach?"
    "She thumbs in his direction and turns back to him when I nod."
    show jett unimpressed with dissolve
    j  "Shut up, Stunt. We’re probably going to have to name our team after his company."
    show stunt surprised with dissolve

    s "Man. I’ve been coming up with all kind of mascots and taglines... Team Enoch? That’s so lame."

    "With a sigh, Stunt sinks down in his chair. Jett does her best to ignore him."
    hide stunt
    show jett unimpressed at center
    with dissolve
    j  "So, these are the two you managed to pick up? Stunt and Reva. A cafe whelp and a ladder hero... and a literal 'who' foreigner."
    hide jett
    show stunt surprised at right
    show reva neutral2 at left
    with dissolve
    "The three of us don’t have anything to say to that, so she continues."
    hide stunt
    hide reva
    show jett neutral at center
    with dissolve
    j  "Alright, whatever. We’re going to make this work one way or another. All that’s left for us to do is recruit a coach."

    m "Got anyone in mind?"
    show jett neutral2 with dissolve
    j  "Not particularly. VIP hasn’t exactly been great for networking outside of the team. They're pretty much done for as soon as I leave."
    
    "The ease with which she delivers that judgement leaves me taken aback." 
    show jett neutral with dissolve
    "I guess if she's going to sever ties with her old teammates, she can't afford to second guess herself. A brutal and unfortunate necessity."

    m "How did you know Mr. Kim then?"
    show jett neutral3 with dissolve
    j  "We’ve only just met. I asked around if anyone knew of decent sponsorship opportunities, and an old Brood War friend pointed me in his direction."
    show jett at right
    show reva glasses at left
    with dissolve
    r  "Fortunate. A coach should be relatively easy to acquire with word that a sponsor is ready to back us."
    show jett unimpressed with dissolve
    "Reva stares unblinking at no one in particular. It’s a little bit creepy just how calculating she looks."
    show jett at center
    hide reva
    with dissolve
    j  "Right. Anyway, I can handle the rest. You three just need to focus on practice, hear me?"
    hide jett
    show reva neutral2 at left:
        xpos .03
    show stunt neutral grin at right:
        xpos .97
    with dissolve
    s "Yup!"
    show reva neutral with dissolve
    r  "Yes."
    m "Yeah."
    hide stunt
    hide reva
    show jett smile at center
    with dissolve
    j  "Good. I’ll keep you posted on developments. If everything goes as planned, we’ll be registered and ready to rock by week’s end. The next VSTL starts two weekends after that."

    "The fire burning in Jett’s eyes is a refreshing sight. I can only promise so much to Stunt and Reva, but for them to see a proven player like Jett get behind the team has to be motivating."
    show jett neutral with dissolve
    stop music fadeout 4.0
    j  "I need to get back to the VIP team house. It’s about time I let them know that I’m not re-signing. Mach, give these two my number. Text me if you need something."
    hide jett with dissolve
    "Before I can even respond, Jett is halfway to the door."

    "Rather than dwell on her words or sit in silence, Stunt bounds to his feet and clenches a fist forward."
    play music "sfx/Blue Pineapple.ogg"
    show reva neutral2 at left:
        xpos .03
    show stunt fist at right:
        xpos .97
    with dissolve
    s "You heard her, chumps! More practice!"
    show reva neutral with dissolve
    r  "I am afraid not. I must be getting home. Jett is not the only one with preparations to make."

    m "Yeah, same. Don’t let us stop you, though."
    show stunt surprised with dissolve #wrong
    s "Tch, fine. Let it be known that when I begged and pleaded for practice partners, I was cruelly denied by my own teammates."
    stop sound fadeout 2.0
    hide reva with dissolve
    window hide dissolve
    scene bg streetsidenight with dissolve:
        align (0, 0)
    play sound "sfx/street3.ogg" fadein 2.0 loop
    window show dissolve
    "Stunt’s theatrical complaints don’t end until I follow Reva out onto the street. Through the door’s window, he gives us a sour face and then returns to his PC."
    show reva neutral at center with dissolve
    r  "He is a bit childish."

    m "Well, he's still a kid."

    "The two of us start heading in the same direction by coincidence, though neither of us bring it up as we share simple conversation."
    hide reva with dissolve
    window hide dissolve
    scene bg streetnight with Dissolve(1.0):
        align (0, 0)
    window show dissolve
    "I ask about her build orders, and she asks me about foreign tournaments. Reva reacts with surprise when I inform her on the antics of foreign FPS pro-gamers."
    show reva surprised at center with dissolve
    r "Would shouting insults at each other mid-match not disrupt their ability to communicate?"
    m "No idea. All I know is that they get loud enough to hear from the open bracket area."
    show reva glasses with dissolve
    r "{w=.5}Curious."
    hide reva with dissolve
    "Our small talk is cut short when she heads for a subway tunnel located along my route home."
    "But just before she descends the tile steps, Reva turns and offers a rare smile."
    show reva smile at center with dissolve
    r  "Goodbye, Mach. It was nice to meet you."

    m "Bye. Catch you online."
    hide reva with dissolve
    "When she’s gone, I’m left to think over the day’s events alone. Mr. Kim, Enoch... This is all too good to be true."

    "It feels right to be wary. Too many aspiring pro-gamers have had their fledgling careers dashed to pieces by stupid mistakes and broken promises. I can’t let myself be one of them."

    "Maybe I’ve earned the chance to rest, to congratulate myself." 
    
    "But I won’t. Not yet."
    window hide dissolve
    stop sound fadeout 4.0
    stop music fadeout 4.0

label fS21StuntAndJettPlayers:
    scene black with slowfade:
        align(0,0)
    pause 2
    #section worthy of an interlude
    play sound "sfx/street1.ogg" fadein 4.0 loop
    scene bg streetside with midfade:
        align (0, 0)
    window show dissolve
    "Lately, the streets haven’t seemed so foreign or confusing." 

    "It might just be because I stick to the same route every time I walk to Golden Zonefire, but I like to think I’ve really started to figure out life as a foreigner."

    "I’ve settled into a routine that works for me. A few hours of ladder in the morning, then I hang out at the cafe with whoever shows up that day."

    "Practice, talk strategy, maybe grab some food, and then we go our separate ways."

    "It’s enough to satisfy me, while still offering plenty of free time to keep from burning out. It’s not a champion’s regimen, but it should suffice. Hopefully."
    
    "Jett is always pushing me to practice longer, but it's hard to see the point. What's ten hours going to do for me that six hours doesn't?"

    "I haven’t seen that Bolt guy at Golden Zonefire since I challenged him, luckily. I was anxious about the possibility of running into him again."

    "A confrontation when I’m supposed to be training is the last thing I need."

    "Familiar landmarks crop up one by one. It’s not long before the cafe comes into view, busy as it always is on the weekends."

    "I squeeze past a half dozen middle schoolers and make my way to our quiet corner."
    stop sound fadeout 1.5
    window hide dissolve
    scene bg cafe with dissolve:
        align (0, 0)
    play music "sfx/Full Server Intro.ogg"
    queue music "sfx/Full Server Loop.ogg"
    window show dissolve
    show jett neutral at left
    show stunt neutral grin at right
    with dissolve
    s "Yo! What took ya? We’ve been waiting on you for sooooooo long."
    show jett considering with dissolve
    j "Don’t listen to him. He got here just before you did."
    show stunt notcool with dissolve
    "Stunt scowls and sinks down in his chair. I try not to smile."
    m "Reva’s a no-show again. Messaged me this morning that she wanted to stay in and ladder. Is Accel coming? I know Crash has team league tonight."
    show jett neutral with dissolve
    j "Nope. He mentioned that he has some last minute build prep to take care of. Who are they playing again?"
    
    m "KaiNE, I think."
    show jett considering with dissolve
    j "Right."
    show stunt phone with dissolve
    "There are a lot of advantages for players on a team. Recognition, housing, practice, salary—but getting to play in team league is one of the biggest perks, period."
    show jett neutral with dissolve
    "A lot of young StarCraft talent breaks out in VSTL. Matches against top players are usually rare for those that aren't qualified for VSL, but not in team league."
    show jett unimpressed with dissolve
    "For an amateur, a win there is more than a sign of good things to come."
    m "Did Accel tell you anything about his team’s plan?"
    play sound "sfx/yoink.ogg"
    show jett pleased with Dissolve(.2)
    show stunt surprised with dissolve
    "Jett shakes her head before successfully snatching Stunt’s phone out of his hand. She rolls it in the space between her fingers and turns back to me."
    show jett neutral3 with dissolve
    j "Don’t be so naive, Mach. Accel and I may be friends, but that sort of information isn’t something you can give away freely."
    show stunt yell
    show jett smile
    with dissolve
    "Stunt gropes for his phone, a pout set across his face. Jett dodges a few times before willingly relinquishing the device."

    j "Stop ignoring us. It’s rude."
    show stunt frown with dissolve
    s "Tch, whatever. You quit lecturing Mach."
    show jett unimpressed
    show stunt neutral
    with dissolve
    "Their eyes battle briefly before Jett concedes, glancing away with a dismissive gesture. Stunt savors his fleeting victory with a grin before dropping the phone to the table."
    play sound "sfx/phonedrop.ogg"
    show stunt frown with dissolve
    s "It's rare to find someone willing to share their strategies openly. Maybe it’s different in the foreign scene, but not here."
    show stunt smug with dissolve
    s "I lost to an amazing one base all-in build on ladder a week back. Sent the guy a message asking for a few replays. He told me to kill myself."
    "You don't need to look so pleased about it. Sheesh."
    show jett neutral
    show stunt neutral
    with dissolve
    j "However, there's one exception." 
    m "That being?"
    show jett casual with dissolve
    j "If a foreigner eliminates a Korean player, our scene will sometimes band together and send replays for his next opponent to study." 
    j "It's a matter of national pride at that point. Been that way since Brood War."
    show jett thinking2 with dissolve
    "That's a rumor I've heard before. Replays can be invaluable in preparing for a specific player. What could be more useful than an exact recording of someone's strategies and tactics?"
    "At least Jett has the courtesy to look vaguely apologetic. I nod, doing my best not to look too surprised."
    show jett neutral with dissolve
    m "How much do Korean players practice for team league? The same as the individual leagues or...?"
    show jett unimpressed with dissolve
    j "Depends. Not less, if they aren't taking home at least top eight in solo league. StarCraft may be a one on one game, but teams can't always be sponsored on the backs of individuals."
    show jett considering with dissolve
    j "Don’t think that gives you the right to neglect your solo league. Admittedly, VSTL is secondary to VSL. If any of you fail to qualify, I’ll make you a slave of my practice house."
    show stunt yell with dissolve
    s "Cool your jets, Jett, and have a little confidence in us."
    show jett unimpressed with dissolve
    j "When you inspire confidence, I will. Remind me again how you placed in the last qualifier?"
    show stunt phone 
    with dissolve
    "Stunt wrinkles his nose and takes the opportunity to return to his cell phone game. Even between teammates, StarCraft’s competitive nature thrives."

    "Silence lingers until I decide to speak up, if only to break the tension."
     
    m "Why don’t we go watch Accel play tonight? I’m sure he’ll appreciate the support."
    show jett neutral
    show stunt notcool
    with dissolve
    "They simultaneously glance up at me, and then at each other. More silence." 
    "I’m just about ready to give up when Jett speaks."
    show jett casual 
    show stunt neutral
    with dissolve
    j "That's a good idea. I've been meaning to speak with Accel anyway."
    show stunt neutral grin with dissolve
    s "Sounds like fun. Let’s bet on the games, though."
    show jett pleased with dissolve
    j "Gambling? I shouldn't be surprised. You play protoss, after all."
    show jett smile with dissolve
    j "Twenty-five thousand on Crash."
    show stunt fist with dissolve
    s "Hah! I’ll take that bet any day."
    show jett neutral3 with dissolve
    j "Wait, I’m not done. Twenty-five thousand won on Crash. But if Accel all-kills, you pay double."
    show stunt frown with dissolve
    "Stunt pauses, chewing over the odds with a contorted look on his face. All-kills are incredibly rare. It’s hard enough for one player to single-handedly defeat more than one opponent, let alone an entire team."
    "With his decision made, Stunt slams a fist down hard enough to draw a few glances from a nearby table."
    play voice "sfx/deskslam.mp3"
    show stunt yell with Dissolve(.2)
    $ renpy.pause(.3)
    s "Deal. The match won’t be for another few hours, so you’ll have plenty of time to regret your mistake while I’m kicking your ass."
    show stunt neutral grin
    show jett neutral
    with dissolve
    s "I wanna try out this new build making the rounds called the two-base immortal all-in. It crushes zerg, or they're saying on the forums."
     
    s "Let’s go. Hey Mach, come watch and learn a thing or two about how to PvZ like a pro."

    m "That's useless to me. And I need to message Reva anyway. She’s gotta come—{w=1}{nw}"
    play sound "sfx/run.ogg"
    show stunt:
        easein 0.25 xpos .92 subpixel True
        easeout 0.5 xpos 1.5 alpha 0.0 subpixel True
    $ renpy.pause(.6)
    "He doesn’t wait for me to finish my thought before bolting for an open PC. I’m left with Jett, who takes her time in joining Stunt."
    show jett neutral at center with dissolve
    m "He’s funny."
    show jett unimpressed with dissolve
    j "Funny doesn’t win games."
    show jett considering with dissolve
    stop music fadeout 4.0
    "Jett seems conspicuously pensive as she rises to head over to a machine. Just as she turns to leave, she stops and looks back at me."
    show jett thinking with dissolve
    j "{w=.5}Mach. {w=.5}Do you think that teammates have to be friends?"
    m "Eh? What do you mean?"
    play music "sfx/Dusty Road A.ogg" fadein 2.0
    queue music "sfx/Dusty Road B.ogg"
    show jett neutral with dissolve
    j "The question is straightforward. Yes or no, do teammates need to be friends?"
    window hide dissolve
    menu:

        "Yes":
            window show dissolve
            m "What? Of course they should. Why wouldn’t you be friends with the people you live and practice with?"
            show jett unimpressed with dissolve
            j "It’s not that simple. What are you supposed to do if your teammate can’t perform and needs to be replaced?"
               
            j "What if your friendship keeps you from offering honest criticism, the type that hurts to hear?"
            show jett neutral with dissolve
            j "Nobody is expected to be friends with their coworkers at an office job. You act cordial and work together to get something done. That’s it. There’s no reason that eSports should be any different."

            m "It’s not the same. Can you honestly say that you’d be as motivated to turn around a losing set for a bunch of strangers than for your friends?"
            show jett unimpressed with dissolve
            j "... Hmph. You’re not being realistic."

        "No":
            window show dissolve
            m "Err. Teammates should be civil, but it isn’t necessary that they be friends."
            show jett casual with dissolve
            j "I agree. The goals of a friendship and the goals of a team don’t always align. It can complicate things and make life more difficult for everyone."
            j "If only more people saw it that way. eSports isn't a game for people afraid to face the real world."
            show jett unimpressed with dissolve
            j "Too many losers retreat to StarCraft and expect everything outside of the game to be easy and fun. People like that aren't cut out for eSports. Or anything, really."

    show jett neutral with dissolve
    j "In any case, you did well to recruit Stunt and Reva. I appreciate it."
    show jett neutral3 with dissolve
    j "I’ll take care of the rest. Be around Golden Zonefire every single day for the next week or so. And practice. Practice a lot."
    "She answers my nod by taking off in Stunt's direction."
    stop music fadeout 4.0
    hide jett with dissolve
    window hide dissolve

label fS22AccelsMatch:
    scene black with squares:
        align (0, 0)
        linear 2
    play sound "sfx/vocal.ogg." fadein 2.0 loop
    $ renpy.pause(1)
    scene bg hallway with squares:
        align (0, 0)
    window show dissolve
    "Where is she? After all it took to convince her, Reva better not have changed her mind without telling me. Maybe she's the type to always be running late."
    "This is the first time I've been back at the VSL studio since the qualifier. Reva's not the only one who feels out of place."
    "I'm just about to send her another text when I catch the top of her head coming up the stairs."
    show reva neutral at center with dissolve
    m "Get lost in the subway again?"
    show reva glasses with dissolve
    r "My apologies. This is my first time at the VSL studio."
    m "Oh. Really? You've never tried to qualify or come to spectate?"
    show reva neutral2 with dissolve
    "She shakes her head. That's a huge surprise, considering she's local." 
    "It's easy enough to follow the VSL online, but nothing beats the live experience. Watching the round of four in person was one of the first things I did here in Seoul."
    m "Jett and Stunt are probably waiting for us. C'mon."
    hide reva with dissolve
    window hide dissolve
    scene bg studio with dissolve:
        align (0, 0)
    window show dissolve
    ###open in the hallway, talk with reva
    #SPOTLIGHTS
    "Nearly every seat in the spectator area of the VSL studio is taken. It’s only with a wave from Jett that Reva and I are ushered past the back rows and into our seats over on the side."

    "Stunt is seated beside Jett and acknowledges us with a smile. With how differently the four of us are dressed, it’d be hard for anyone to tell that we’re actually a team."
    "Well, I guess technically we’re not a team yet. Not officially, anyway. With the thought on my mind, I look to Jett and keep my voice low."
    show jett neutral at right with dissolve:
        xpos .9
    m "Do we have a uniform planned?"
    show stunt neutral grin at right:
        xpos 1.15
    with dissolve
    s "Oh, hell yeah! I want a team jacket."
    show jett unimpressed with dissolve
    j "The uniform we pick comes out of the team's warchest. It’s stupid for us to splurge when we don't have any results."
    show stunt surprised with dissolve
    "Stunt’s longing stare doesn’t fade away until Jett focuses a glare in his direction."
    hide stunt
    hide jett
    with dissolve
    "The production crew is busy at work behind the scenes. There are way more VSL staff members than the stream lets on."

    "People with clipboards and headsets pace the studio frantically, moving from team benches to behind the booths and then back again."

    "Accel sits on the end of the bench with the rest of Crash. Their coach, a balding man with small eyes, a red nose, and a clip on tie, paces back and forth with his hands in the pockets of his blazer."

    "Most coaches are usually retired players or have management experience. This guy has got either the latter or nothing—it wouldn’t surprise me to learn that he’s never played a game of StarCraft in his life."

    "The players of Team KaiNE sit on the opposite side of the studio. Their coach is far more subdued and one that I actually recognize: An old B-tier Brood War pro that aged out of his ability to compete."
    show stunt neutral grin at left:
        xalign 0.5 yanchor 0.0 xpos 1.0  ypos 0.22 subpixel True
        easein 1.0 xpos 0.9
    with dissolve
    "Stunt leans over Jett to whisper something,{w=.5}{nw}"
    play music "sfx/alt.ogg"
    show stunt surprised
    extend " but before he can open his mouth, the Victory StarLeague's theme song cuts in to announce that the broadcast is about to get started."
    hide stunt with dissolve
    stop sound fadeout 2.0
    "Korean StarLeagues have a weird fascination with alt rock. The same songs from my embarrassing freshman year playlist blast unabashedly to stadiums of eSports fans."
    "The crowd’s cheers die down only once the commentators give their introductions. When I look over my shoulder, I can see the table where they keep the two English casters."

    "The duo is loved more for their laidback banter than their game analysis, not that it's anything I'd change." 
    "There’s no way for me to hear them without getting a headpiece that'll make me look like a tourist. I'll have to settle for the Korean commentators."
    
    caster "Welcome to the VSTL! Today's first match is an exciting duel between Crash and KaiNE."
    commentator "Ah, both are very solid teams that have been around from the very beginning of StarCraft 2. I am eager to see whether or not they show us good games."
    analyst "This is the furthest that KaiNE has been since the beginning of the StarCraft 2 team league. Crash will need to make it to VSTL finals if they wish to share that accomplishment!"
    caster "Indeed! They have a challenging path ahead of them, but I am certain that they are capable of returning to their former glory."
    commentator "My thoughts are the same. Only one of KaiNE's players remains in the VSL, so they should have had plenty of time to practice for this match. Can the same be said for Crash?"
    analyst "Certainly so. Crash's lineup is well-tested and proven in the VSL. It's a sure bet that they have not neglected to prepare accordingly."
    "... Well. There won't be any jokes about cartoons from the 90s, but I should stay pretty well informed throughout the series."
    
    "An array of multicolored overhead lights announce the first match. Polished motion graphics and meticulously collected player statistics whiz around the display at the front of the studio."

    "The VSL studio really has hype-building down to a science."

    m "Who do you think Crash is going to send out first, Jett?"
    show jett casual at right with dissolve
    j "Not Accel, unless they want him getting sniped right off the bat."

    "I nod. A common strategy in team league is to have a mid-tier player spend all of his practice time preparing specifically for one heavy hitter."
    show jett neutral with dissolve
    "There are other things to take into account too, like the map or remaining opponents. But there’s no doubt that Team KaiNE has one of their players ready to take down Accel."
    hide jett with dissolve
    "By the time I glance back up at the stage, the first two players are headed into the booths. Accel remains on the bench, eyes set on the same screen as the crowd."
    show reva neutral at left with dissolve:
        xpos -.1
    r "It is starting."
    stop music fadeout 5.0
    hide reva with dissolve    
    "Sure enough, once the players have their settings prepared and the coaches give the go-ahead, the match begins."
jump fstudio_game1
label fCrashLose:
    scene bg studio with dissolve:
        align(0,0)
    window show dissolve
    "Luckily, Stunt has the sense not to gloat about the money that he just won from Jett."
    play music "sfx/Dusty Road A.ogg" fadein 1.0
    queue music "sfx/Dusty Road B.ogg"
    "The four of us sit in silence as we watch Accel agonize over his loss. "

    "While KaiNE is huddled together with smiles and cheers, all of Crash sit with their heads down save Accel, who still hasn’t left the booth."

    "His coach looks furious. He barges in through the booth’s back door and raves at Accel from behind his back."

    "I can’t believe what I’m seeing. Frustration is one thing, but Accel won two games before he went out."

    "Even if he had gone down without a win, there’s no reason to yell at him. How is that supposed to help?"

    "Just as my anger on Accel’s behalf reaches the point that I think to say something to Jett, Accel rises from his seat and slides past his coach without so much as a glance in his direction."
    show reva neutral2 at left
    show stunt surprised at right
    with dissolve
    s "Should we go talk to him?"

    m "Yeah. C’mon."
    hide reva
    hide stunt
    with dissolve
    "The three Korean commentators are in the middle of winding down the series with post-match analysis when we rise and exit through the studio’s backdoor."
    window hide dissolve
    scene bg hallway with Dissolve(1.0):
        align (0, 0)
    window show dissolve
    show accel concerned at center with dissolve
    "We find Accel standing alone with a palm on his forehead. When he catches our footsteps, Accel turns to regard us all with his typical grin."
    show accel neutral with dissolve
    a "I lost. Oh well."
    "His carefree attitude is unique among professional gamers. If the average pro isn't angry or depressed by a loss, they’re at least frustrated."
    "Part of me wonders whether or not Accel is covering up his true feelings, but he seems genuinely fine."
    show accel at right:
    show jett neutral at left:
    with dissolve
    j "Bad luck, Accel. You played well."
    show accel thinking2 with dissolve
    a "Yeah. Thanks."
    m "What’s the deal with your coach? He seemed really upset with you."
    show accel concerned with dissolve
    "Accel scoffs, allowing the disgust in his voice to show on his face."

    a "He’s useless, especially considering that I do his job for team league. Busted my ass preparing for tonight—picked out the builds and the snipers and everything. Drilled the team for more than a week."
    hide jett
    hide accel
    show reva neutral at center
    with dissolve
    r "And your coach has laid the blame for the loss at your feet."
    hide reva
    show accel thinking3 at right
    show jett neutral at left
    with dissolve
    "Accel nods and glances away. Spectators begin filtering out of the studio, offering us curious looks as they head outside. Looks like the studio is done for the night."
    show accel concerned with dissolve
    a "It’s ridiculous. And not a single person on Crash had the guts to back me up. I didn’t switch from Brood War to suffer spineless teammates and a coach with an ongoing mid-life crisis."
    show accel at right:
    show jett neutral3 at left:
    with dissolve
    j "And you shouldn’t have to. Accel, ditch Crash and come coach for us."
    
    "Four pairs of eyes land on Jett, all but Reva’s bewildered. Accel recovers quickly before crossing his arms."
    show accel laughing with dissolve
    a "You know I can’t. I have a contract. It’s not up until next year."
    show jett neutral with dissolve
    j "A player contract, one that bars you from playing in StarLeagues for any team but Crash."
    show accel thinking with dissolve
    a "Even so, I can’t break the terms. I'm required to play for them. They can take legal action against me if I don't."
    show jett smile with dissolve
    j "And you will, if they insist on it. Live, train, and coach at our team house. All you have to do is show up once a week to play your matches at the studio, and Crash can’t do anything."
    hide jett
    hide accel
    show stunt surprised at right:
        xpos .97
    show reva expected at left:
        xpos .03
    with dissolve
    "Reva pushes her glasses up against the bridge of her nose, pensive. Stunt stares wide-eyed, as if a pivotal scene in a drama is playing out. As for me…"
    hide reva
    hide stunt
    show accel thinking3 at center
    with dissolve
    m "We could really use you, Accel. You deserve better."
    show accel concerned with dissolve
    a "... If I do this and the team doesn’t work out, my career is over."
    stop music fadeout 2.0
    "He says it as much to himself as he does the rest of us. It’s true, and probably true for everyone else as well."
    show accel thinking3 with dissolve
    "Accel stares at the floor for a while, deep in thought. When he finally looks up, it’s with a casual shrug."
    show accel thinking2 with dissolve
    a "Screw it. I’ve put off my mandatory military training for too long anyway. I’m down."
    hide accel
    play music "sfx/Blue Pineapple.ogg" fadein .2
    show stunt fist at right:
        xpos .97
    show reva surprised at left:
        xpos .03
    with dissolve
    "Stunt lets loose an ear-shattering cheer and flings his arms into the air. Reva's glasses nearly fall off in surprise, though she manages to catch them by the frame."

    s "HELL YEAH! TEAM ENOCH NUMBAH ONE!!!"
    hide reva
    hide stunt
    show accel neutral at right:
    show jett casual at left:
    with dissolve
    j "What a motley crew. A cafe whelp, a ladder hero, a no-name foreigner, and now some laidback hyung."
    show accel laughing with dissolve
    a "You forgot the washed-up champ."
    show jett smile with dissolve
    "Try as she might, Jett can’t hide the satisfied grin showing on her face. Everything has really come together."

    "This is it. This is what I came to Korea for. The months of endless ladder, the late-night online tournaments. I’m on a team. A real team."

    m "We need to celebrate."
    show jett pleased with dissolve
    j "Oh, you want to treat the team? How kind of you, Mach."
    show accel confident 
    with dissolve
    "Jett glances around to see if her quip earned a laugh, only to find Accel wagging a finger at her."

    a "Have you already forgotten who convinced you to take the risk and form your own team? I’d say that’s worth a bottle of soju or two. Or ten."
    show jett unimpressed with dissolve
    j "Tch."
    show jett thinking with dissolve
    "Jett brings a finger to her lip, either considering which bar to take us to or how to get out of paying."
    pause .5
    show jett neutral2 with dissolve
    j "Alright, enjoy the hell out of tonight. It’ll be the last time until we’ve got a championship trophy that we celebrate anything. Got that?"
    show accel neutral with dissolve
    a "Good choice."
    hide jett
    hide accel
    show stunt neutral grin at right:
    show reva neutral at left:
    with dissolve
    s "HELL YEAH!"
    r "Understood."
    hide stunt
    hide reva
    with dissolve
    "With a nod from Jett, the five of us walk shoulder to shoulder in high spirits. But just as we’re about to descend the stairs, Jett pauses."
    show jett neutral at center with dissolve
    j "Wait. Accel. Do you need to go talk to your team or anything?"
    show accel thinking2 at right
    show jett at left
    with dissolve
    "That stops the rest of us in our tracks. We turn and find Accel at complete ease."
    show accel neutral with dissolve
    a "Nah. I'll take care of it later."
    "With a knowing smile, he leads us down the stairs and out onto the street."
    stop music fadeout 3.0
    window hide dissolve

label fS23Bar:
    #bar
    scene black with squares:
        align (0, 0)
    pause 2
    scene bg trendy with squares:
        align (0, 0)
    play sound "sfx/bar.ogg" fadein 2.0 loop
    play music "sfx/Loading progress 1.ogg" fadein 2.0
    window show dissolve
    "The bar that Jett had in mind was halfway across the city, though after a subway ride it doesn’t take us more than thirty minutes to arrive. "
    "The trendy-looking lounge is packed with twentysomethings, most of them older than even Accel."
    show stunt neutral at center with dissolve
    "Stunt walks ahead of us with a swagger, noting with pride on the way over to our table that he has a fake-id and goes to bars all the time."
    
    m "With who, your mom?"
    show stunt yell with Dissolve(.2)
    s "With your mom, bitch!"

    m "My mom is in the U.S. though."
    show stunt smug with dissolve
    s "Oh, her flight landed already?"
    "I can’t help but laugh. Stunt is incredibly immature, even for his age. But there’s something undeniably uplifting about his enthusiasm."
    hide stunt with dissolve
    "With all of the booths full, we pick out a table close to an empty dance floor. It’s cramped with the five of us, but we make do."
    show jett neutral at right:
    show accel neutral at left:
    with dissolve
    a "Man, I can’t remember the last time I went out like this. Spent so much of this year cooped up in the Crash team house."
    show jett casual with dissolve
    j "Mm. Same. VIP’s mandatory hours were brutal by Star2 standards. No one even made good use of them."
    "A scruffy waiter dressed no differently than the bar’s patrons stops by to take our drink orders before Stunt can return to bragging about his iron stomach."
    "Jett shows three fingers for the number of soju bottles she wants. With a click of his tongue, the waiter departs with our order in hand."
    show jett neutral with dissolve
    m "There’s five of us though, Jett."
    show jett unimpressed with dissolve
    j "You think I can’t count? You don’t drink soju from the bottle."
    m "Oh. Well, I’ve never had it before."
    show jett at right:
        easein .5 alpha 0.0 xpos 1.5 subpixel True
    show accel at left:
        easein .5 xpos 0.4 subpixel True
    show reva neutral at left:
        alpha 0.0 xpos -0.3
        easein .5 alpha 1.0 xpos 0.0 subpixel True
    $ renpy.pause(.5)
    r "That is not a surprise. Soju is unpopular outside of Korea."
    show accel confident with dissolve
    hide jett
    a "We’ll show you how to do it right, Mach."
    "While awaiting the server's return, I notice Accel glancing repeatedly in Reva's direction."
    show accel neutral with dissolve
    a "Mach, what ended up happening with Reva? And who's our friend here?"
    show reva shy with dissolve
    r "........."
    play voice "sfx/interupt.ogg"
    show reva glasses 
    with Dissolve(.2)
    r "{fast}I am Reva! {w=.2}And, allow me to say that it is a great pleasure to meet you in person!{w=.2}{nw}"
    extend " Your play has been.....{w=.8}{nw}"
    show reva2 shy at left:
        alpha 0.0
        linear .2 alpha 1.0
    show reva:
        alpha 1.0
        linear .3 alpha 0.0
    extend " a{w=.1}n{w=.1} i{w=.1}n{w=.1}s{w=.1}p{w=.1}i{w=.1}r{w=.1}a{w=.1}t{w=.1}i{w=.1}o{w=.1}n{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.2}.{w=.2}. {w=.2}t{w=.2}o{w=.2}.{w=.2}.{w=.2}.{w=.2}.{w=.2}.{w=.2} {w=.3}m{w=.3}.{w=.3}.{w=.3}.{w=.3}e{w=.3}.{w=.3}.{w=.3}.{w=.3}"
    hide reva2
    show reva shy:
        alpha 1.0
    show accel laughing
    with dissolve
    "Uh. Is Reva an Accel fangirl? She'd have been maybe fifteen at the prime of his Brood War career..."
    show accel neutral with dissolve
    a "Well. A shame that these punks didn't have the decency to introduce us properly. It's nice to finally meet you, Reva." 
    show reva neutral2 with Dissolve(1)
    a "No lie, your mech is the best I've seen outside of VSL. You've got to show me the timings on your double armory build at some point."
    play voice "sfx/drop.ogg"
    show reva surprised with Dissolve(1)
    $ renpy.pause(1)
    show reva shy with Dissolve(.2)
    $ renpy.pause(.4)
    r "Y-{w=.5}You too."
    show reva sweat
    show accel laughing
    with dissolve
    "I think he broke her. It's okay Reva, I've been there."
    show reva neutral 
    show accel neutral
    with dissolve
    "Reva manages to (mostly) pull herself out of her fangirl shock by the time our waiter returns."
    show image "char/bonus/soju.png":
        xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    with dissolve
    "When he's gone, Accel pours out a shot-glass worth of soju and hands it to me."
    show image "char/bonus/soju.png":
        alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
        easeout .6 ypos 0.65 alpha 0.0 subpixel True
    play voice "sfx/glassware.ogg"
    show accel confident with dissolve
    a "Go on. In one gulp."
    "There isn’t much liquid in the glass, so I throw it back without a second thought. It takes a few seconds for my tastebuds to react."
    play voice "sfx/hiss.ogg"
    show bg trendy with hpunch
    pause .3
    "Ugh, this stuff is awful. It’s all I can do not to retch."
    show reva neutral2 with dissolve
    m"It’s... {w=.5}good..."
    show accel laughing with dissolve
    a "How does a girl learn Korean without coming across soju at least once? It's kind of impressive, actually."
    m "I learned online. Wasn't ever a part of my lessons, I guess."
    show reva glasses with dissolve
    r "That is one of the most difficult ways to learn a language. How did you manage?"

    m "K-pop and StarCraft. They didn’t offer Korean as a language option at my high school, so I studied it in my spare time."
    show reva:
        easein .5 xpos .5 subpixel True
    show accel:
        easein .5 alpha 0.0 xpos 1.0 subpixel True
    show stunt yell at left:
        xpos -.3 alpha 0.0
        easein .5 alpha 1.0 xpos 0.05 subpixel True
    $ renpy.pause(.5)
    s "K-pop? Disgusting. I knew you were Koreaboo scum."
    show reva neutral with dissolve
    m "At least I did something useful with my dumb hobbies. Can you say the same? How's your English?"
    show stunt surprised with dissolve
    s "..."
    show stunt neutral grin with Dissolve(.2)
    s "<H-{w=.2}Hello!{w=.3} I am Stunt!{w=.2} Protoss!{w=.3} I am one!>"
    show reva neutral2 with dissolve
    r "<Very bad. Used two names to help, and said lies. Bad student and player needs to work harder.>"
    show reva neutral with dissolve
    "Reva asks for my approval with a look. I give it with a nod."
    show stunt surprised 
    show reva smile
    with dissolve
    s "Bad what? What'd she say, Mach?"
    m "Bad luck. You were almost perfect."
    show stunt neutral grin with dissolve
    s "Hah! Knew it, I'm a natural."
    hide stunt 
    hide reva
    with dissolve
    "I pour out a shot for Accel, relieved when the culture test is over. Jett's three bottles are soon emptied and then replaced." 
    "The soju-fueled conversations range from StarCraft and team houses to fashion and college, and whatever else in between."
    show stunt yell at center with dissolve
    s "You three are so lucky. Korean guys drop two of our golden years on the military! It’s totally unfair! Tell 'em, Accel!"
    show stunt:
        easein .5 xpos -.2 subpixel True
    show jett unimpressed at right:
        xpos 2.0
        easein .5 xpos 1.0 subpixel True
    show reva neutral at left:
        xpos 1.0
        easein .5 xpos 0.0 subpixel True
    $ renpy.pause(.5)
    "Stunt points at Jett, me, and then Reva. Neither of them seem particularly ruffled."
    hide jett
    hide reva
    hide accel
    show accel laughing at center 
    with dissolve
    "Accel only watches, slightly drunk and highly entertained."
    hide accel
    show jett unimpressed at right:
    show reva neutral at left:
    with dissolve
    r "I would gladly spend two years in our military to reap the benefits of your gender."
    show jett considering with dissolve
    j "Seriously. Do you have any idea how uncomfortable being pressured into some braindead photoshoot with a pink keyboard is?"
    show jett kawaii with dissolve
    j "'Smile agasshi! Headphones don't sell themselves you know! Why don't you lose the team jacket and pull down your shirt a bit? Oh, I want to see you with double eyelids by next time!'"
    show jett unimpressed
    show reva neutral2
    with dissolve
    j "It's just like that. Literally the worst."
    "... Dear god. Jett, please, never do that again."
    show stunt:
        easein .5 xpos .3 subpixel True
    show jett unimpressed at right:
        easein .5 xpos 1.5 alpha 0.0 subpixel True
    show reva neutral at left:
        easein .5 xpos .5 subpixel True
    $ renpy.pause(.5)
    hide jett
    s "Sponsors pay you to sit in front of a camera. How terrible!"
    show stunt frown with dissolve
    s "Don’t tell me that there aren’t advantages for girls in eSports! It’s SO much easier to get on a team, and you get way more fans!"
    show reva frown with dissolve
    r "You cannot understand without experiencing it firsthand, so you only see the good."
    show stunt fist with dissolve
    s "Come on, Mach! Back me up here."
    m "... Uh, what could possibly have made you think I'd be on your side in this argument?"
    show stunt yell with dissolve
    s "You three are so dramatic! What could possibly be worth trading away the free popularity?"
    hide stunt
    show jett considering at center
    hide reva
    with dissolve
    j "When I was an amateur back in Brood War, some gross KPGA pen-pusher said he’d help me get my pro license if I spent the night at his place. I had just turned 17."
    "All of our eyes shift to Jett, surprised—though Stunt’s most of all. I take a moment to silently appreciate that StarCraft 2 doesn’t require a pro license to play in StarLeagues."
    show stunt neutral grin at left:
        xpos -.5
        easein .5 xpos 0.0
    show jett at center:
        easein .5 xpos .7
    $ renpy.pause(1)
    s "... Did you do it?"
    play voice "sfx/interupt.ogg"
    show jett angry with Dissolve(.1)
    pause .2
    j "NO! What the hell is wrong with you!?"
    play voice "sfx/glassware.ogg"
    show jett angst with Dissolve(.2)
    show stunt surprised:
        easein .2 ypos 1.15 subpixel True
    "Jett snatches her glass off the table and snaps her arm back. When Stunt recoils and shrinks beneath the table, she returns her drink to her lips with a scowl."
    show stunt yell
    with dissolve
    s "Is it a crime to wonder?!"
    #femach story about what happened after
    #femach
    "Jett grinds her teeth back and forth with her eyes on Stunt, only turning away when she notices Reva and I watching her."
    show jett neutral3 with dissolve
    j "For the record, I reported him and he was fired. Push back or be pushed around."
    hide reva
    hide jett
    hide stunt
    show accel confident at center
    with dissolve
    play voice "sfx/deskslam.mp3"
    stop music fadeout 2.0
    "Accel drops his fist to the table with thump, ending the argument and earning our attention."
    play music "sfx/Time Off.ogg"
    stop sound fadeout 2.0
    a "We are going to play a drinking game."

    m "Why?"
    show accel neutral with dissolve
    a "Why? Because we’re about to condemn ourselves to lives of timing attacks, hard contains, and positional play." 
    show accel thinking2 with dissolve
    a "We’ve got one night to get hammered and we’re going to make the most of it."

    m"You’ve convinced me. What do you want to play?"
    hide accel
    show stunt neutral grin at left:
    show jett neutral at right:
    with dissolve
    s "Oh! Let’s play the King’s Game!"
    show jett unimpressed with dissolve
    j "Shut up. The King’s Game is for desperate teenagers."
    show jett smile with dissolve
    $ renpy.pause(.5)
    show stunt surprised with dissolve
    "She glances over Stunt and offers a smile to make her point."
    show jett:
        easein .5 xpos 1.2 alpha 0.0
    show stunt:
        easein .5 xpos -.2 alpha 0.0
    show accel laughing at center with dissolve
    a "Nah, nah. Chopsticks. It’s really simple. I say something that might describe one of us more than the others, and we point at who we think what’s said describes best."

    m"Eh. I don’t follow."
    show accel neutral with dissolve
    a "Okay, it’s like this: Which of us is most likely to hate soju?"
    hide accel
    hide jett
    hide stunt
    show reva smile at center
    show jett pleased at right
    show stunt neutral grin at left
    with dissolve
    "Accel takes a chopstick from the table and points it at me, as do Jett, Reva, and Stunt."
    hide jett
    hide stunt
    hide reva
    show accel neutral at center 
    with dissolve
    a "And then you drink. But we won’t count that one."

    m"Oh. That makes sense."

    a "Mhm. Why don’t you start us off with a few?"
    hide accel with dissolve
    window hide dissolve
label fchoicestart:
    menu:
        "Most likely to end up a NEET" if fbar_choice_reva == False:
            jump fRevaBar
        "Most likely to have the worst fans" if fbar_choice_jett == False:
            jump fJettBar
        "Most likely to bang a fan" if fbar_choice_accel == False:
            jump fAccelBar
        "Most likely to be a virgin" if fbar_choice_stunt == False:
            jump fStuntBar
    jump fBarEnd
label fRevaBar:
    window show dissolve
    m"Which of us is most likely to end up a NEET?"
    show accel laughing at center
    show jett pleased at right:
        xpos 1.05
    show stunt neutral grin at left
    with dissolve
    "Four sets of chopsticks immediately fall onto Reva. One of her sticks slips out from between her fingers and onto the floor."
    show reva surprised at center
    hide stunt
    hide jett
    hide accel
    with dissolve
    play voice "sfx/chopstick.ogg"
    r "{w=.5}M-{w=.5}Me?"
    show stunt smug at left:
        xpos -.4 alpha 0.0
        easein .5 xpos -.1 alpha 1.0 subpixel True
    show reva:
        easein .5 xpos .6 subpixel True
    $ renpy.pause(.3)
    s "C’mon, you give off a powerful shut-in vibe."
    show reva concerned with dissolve
    r "I do not understand."
    show stunt yell with dissolve
    s "You’re doing it right now! It’s like you learned how to communicate from a text-to-speech program."
    show reva:
        easein .5 xpos 0.25
    show accel neutral at right:
        xpos 1.3 alpha 0.0
        easein .5 xpos 1.0 alpha 1.0
    show stunt:
        easein .5 xpos -.5 alpha 0.0 subpixel True
    $ renpy.pause(.5)
    a "Reva, what do you like besides games and eSports? Do you have any hobbies?"
    show reva shy with dissolve
    r "{w=1}... I watch anime."
    show accel concerned with dissolve
    a "... Anything else?"
    show reva sweat with dissolve
    r ".{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.1}.{w=.1}."
    hide stunt
    show stunt neutral grin at left:
        xpos -.4 alpha 0.0
        easein .5 xpos -.2 alpha 1.0 subpixel True
    show jett pleased at right:
        xpos 1.3 alpha 0.0
        easein .5 xpos 1.2 alpha 1.0 subpixel True
    $ renpy.pause(.5)
    s "See."
    "Jett is doing her best to keep from piling on, but the urge is evident on her face."
    hide stunt
    hide jett
    hide accel
    show reva glasses at center 
    with dissolve
    r "But I have StarCraft, so I cannot be a NEET. That should be considered employment."
    m "Sure, but the question was who was most likely. If you washed out of professional gaming, I could totally see you as an MMO addict."
    show reva neutral2 with dissolve
    r "I have max level characters in the most popular three, but that does not qualify me as an addict on its own."
    show reva:
        easein .5 xpos .2 subpixel True
    show accel concerned at right:
        xpos 1.3 alpha 0.0
        easein .5 xpos .9 alpha 1.0 subpixel True
    show jett neutral at right:
        xpos 1.6 alpha 0.0
        easein .5 xpos 1.1 alpha 1.0 subpixel True
    $ renpy.pause(.5)
    j "God. How? Those games are disgustingly grindy. You really aren’t helping your case."
    show accel thinking with dissolve
    a "Okay, answer this: What StarCraft community site do you read and post on the most?"
    show reva sweat with dissolve
    r "{w=1}It is an imageboard."
    show jett pleased 
    show accel concerned
    with dissolve
    j "Drink, Reva."
    hide jett
    hide accel
    hide reva
    with dissolve
    $ fbar_choice_reva = True
    window hide dissolve
jump fchoicestart
label fStuntBar:
    window show dissolve
    m"Which of us is most likely still a virgin?"
    show jett pleased at right:
    show accel laughing at left:
    with dissolve
    "Before he can even react, Accel, Jett, and I point our chopsticks in Stunt’s direction. He jumps in his seat, aghast."
    show jett:
        easein .5 xpos 1.6 alpha 0.0
    show accel:
        easein .5 xpos .8 alpha 0.0
    show reva neutral at right:
        xpos 0.2 alpha 0.0
        easein .5 xpos 1.0 alpha 1.0 subpixel True
    show stunt surprised at left:
        xpos -0.5 alpha 0.0
        easein .5 xpos 0.0 alpha 1.0 subpixel True
    $ renpy.pause(.5)
    "He senses weakness in Reva and aims his answer towards her, only to have her repay the favor."
    play voice "sfx/interupt.ogg"
    show stunt yell
    show reva smile
    with dissolve
    s "THIS IS BULLSHIT!"
    hide jett
    show stunt:
        easein .5 xpos -.1
    show reva:
        easein .5 xpos 0.7
    show jett smile at right:
        xpos 1.5
        easein .5 xpos 1.0 alpha 1.0
    $ renpy.pause(.5)
    j "Calm down. You’re like, what. Twelve?"
    s "You guys have NO idea! I’m a playa, you hear me?"
    show reva glasses with dissolve
    r "Doubtful."
    show stunt surprised with dissolve
    m"You were hanging out with middle schoolers at a PC bang when I found you. Be honest with us."
    show reva neutral with dissolve
    "Stunt scrunches up his face, allowing his rage to stew momentarily before bursting out with another protest."
    play voice "sfx/shing2.ogg"
    show stunt yell with Dissolve(.2)
    s "This is a rigged question. You guys all have like, at least four years of extra time to luck out."
    hide stunt
    hide accel
    hide reva
    show jett pleased at right:
        xpos 1.03
    show accel laughing at left:
    with dissolve
    j "Virginity confirmed. Drink."
    show accel confident with dissolve
    a "Oh, cut the kid some slack. It’d be kinda weird if he wasn’t."
    hide jett
    hide accel
    show stunt yell at center
    with dissolve
    play voice "sfx/shingshingshing.ogg"
    s "A breach of trust!{w=.3} Ethically unsound!{w=.3} Harassment on an unreasonable scale!"
    show stunt frown with dissolve
    "He makes a box on the table with his finger, continuing his exaggerated and antiquated protests all the while."
    show stunt yell with dissolve
    s "This is a no bullying area. If you enter the DMZ, I will retaliate with full force."
    hide stunt with dissolve
    $ fbar_choice_stunt = True
    window hide dissolve
jump fchoicestart
label fJettBar:
    window show dissolve
    m"Which of us has the worst fans?"
    show jett casual at center with dissolve
    j "Pft, it’s not like anyone but Accel and I even—"
    hide jett
    show reva smile at center
    show stunt neutral grin at left:
    show accel laughing at right:
        xpos 1.05
    with dissolve
    "Jett’s train of thought shatters when she notices four chopsticks pointed in her direction."
    hide reva
    hide stunt
    show jett angst at right:
    show accel laughing at left:
    with dissolve
    j "What!?"
    show jett unimpressed 
    show accel neutral
    with dissolve
    "Defiantly, Jett aims her own at Accel. He merely grins in response."
    a "Be honest. When was the last time you had a meet and greet session where some fanboy didn’t slobber all over you?"
    hide jett
    hide accel
    show reva neutral2 at right:
        xpos .97
    show stunt neutral at left:
        xpos .03
    with dissolve
    r "Your brusque attitude attracts a certain type of fan, Jett."
    hide reva
    hide stunt
    show jett angry at right:
    show accel laughing at left:
    with dissolve
    j "What’s that supposed to mean?"
    hide jett
    hide accel
    show reva neutral2 at right:
        xpos .97
    show stunt neutral grin at left:
        xpos .03
    with dissolve
    s "It means they like it when you call someone trash! C’mon, you’re the one that gives those blunt pre-game interviews."
    hide reva
    hide stunt
    show jett neutral3 at right:
    show accel confident at left:
    with dissolve
    j "I simply say what’s on my mind. If that happens to be how confident I am, then so what? And what does that have to do with my fans?"
    show accel neutral with dissolve
    a "Let’s put it like this. Reva, what would you say to the crowd before a big finals match?"
    show jett:
        easein .5 xpos 1.6 alpha 0.0
    show accel:
        easein .5 xpos 1.0 alpha 0.0
    show reva neutral at center:
        xpos -.3 alpha 0.0
        easein .5 xpos .5 alpha 1.0
    $ renpy.pause(.5)
    play voice "sfx/spotlight.ogg"
    show image "char/bonus/overlay.png" with Dissolve(.1):
        align (0,0)
    pause .5
    r "I would like to thank my fans for cheering for me. I have worked hard to improve my condition and will send my opponent to Andromeda. I promise to show you good games."
    play voice "sfx/twinkle.ogg"
    show reva expected with Dissolve(.2)
    pause .8
    play voice "sfx/klappa.ogg"
    pause 2
    hide image "char/bonus/overlay.png"
    hide reva
    hide jett
    hide accel
    show jett unimpressed at right:
    show accel neutral at left:
    with dissolve
    a "So you'll get earnest supporters that love to see you do well."
    show accel thinking2 with dissolve
    a "But Jett, your fans want you to lose almost as much as they want you to win."
    show jett casual with dissolve
    j "That’s absurd. People that cheer for my losses aren’t my fans."
    show accel laughing with dissolve
    a "Whatever you want to call them, they’re yours and yours alone. Don't pretend like you don't know what we're talking about."
    show jett smile with dissolve
    j "I have plenty of very nice and well-intentioned fans. You’re just focusing on the minority of terrible ones."
    show accel confident with dissolve
    a "Oh, like the guy who brought a bodypillow with your picture to an autograph session? How could I forget!"
    play voice "sfx/deadly.ogg"
    show jett angst with Dissolve(.2)
    show accel laughing
    with Dissolve(.4)
    "Jett’s expression flashes a mixture of anger and embarrassment. She looks ready to throw a punch."
    play voice "sfx/interupt.ogg"
    show jett angry with Dissolve(.2)
    j "GOD DAMMIT ACCEL, I TOLD YOU ABOUT THAT IN CONFIDENCE."
    j "IF ANY OF YOU EVER BRING THIS UP AGAIN, YOU DIE."
    ".................."
    window hide dissolve
    menu:
        "Indulge my curiosity":
            jump fduck
        "Value my safety":
            jump fcoward
label fcoward:
    window show dissolve
    show jett angst with dissolve
    "... There's no way I'm asking. I'm smarter than that."
    show accel thinking2 with dissolve
    "Jett seethes in displeasure at Accel. He's trying hard to keep from cracking up."
    hide jett neutral
    hide accel neutral
    with dissolve
    $ fbar_choice_jett = True
    window hide dissolve
jump fchoicestart
label fduck:
    window show dissolve
    m "... Did you sign it?"
    show jett angry
    show accel laughing
    with dissolve
    "Without consciously realizing it, I find myself dodging something."
    show white with Dissolve(.1):
        align(0,0)
    hide white
    show bg trendy:
        xpos 0.0 subpixel True
        easeout 0.15 xpos -0.1 subpixel True
        easein 0.1 xpos -0.08 subpixel True
    show accel:
        xpos 0.0 subpixel True
        easeout 0.15 xpos -0.05 subpixel True
        easein 0.1 xpos -.03 subpixel True
    show jett angst:
        xpos 1.0 subpixel True
        easeout 0.15 xpos 0.97 subpixel True
        easein 0.1 xpos 0.98 subpixel True
    play voice "sfx/zing.ogg"
    queue voice "sfx/break.mp3"
    $ renpy.pause(1)
    "Jett's shotglass whizzes past my head and shatters on the wall behind me. From across the room, a few of the bar’s patrons laugh drunkenly at the absurdity."
    show bg trendy:
        easein 1.0 xpos 0.0 subpixel True
    show accel:
        easein 1.0 xpos 0.0 subpixel True
    show jett:
        easein 1.0 xpos 1.0 subpixel True
    play sound "sfx/glassware.ogg"
    "She reaches for another, apparently intent on making sure she gets her point across. I’m left with no choice but to raise my hands and surrender."
    m"I don’t need to know! I don’t need to know!"
    show jett unimpressed with dissolve
    "She sets the glass down and looks away from the rest of us, still hot-faced from the negative attention."
    hide accel
    hide jett
    with dissolve
    $ fbar_choice_jett = True
    window hide dissolve
jump fchoicestart
label fAccelBar:
    window show dissolve
    m"Which of us is the most likely to bang a fan?"
    show jett neutral at right:
    show accel neutral at left:
    with dissolve
    a "Rushing right out the gate, are we? You’re supposed to do a few more warm up questions before you to get to the raunchy stuff."
    show jett smile with dissolve
    j "You say that only because you know you’re going to lose this one."
    hide accel
    hide jett
    show reva smile at center
    show jett smile at right
    show stunt neutral grin at left
    with dissolve
    "Despite finding himself staring down four pairs of chopsticks, Accel never loses his easygoing smile."
    hide reva
    hide stunt
    hide jett
    show accel neutral at center
    with dissolve
    a "I freely admit I’ve slept with one of my fans before. This question is more like winning than losing anyway since I'm not a lech."
    m "Do you have a story to go along with it?"
    show accel thinking2 with dissolve
    a "Pretty much what you’d expect. This one girl used to show up to all my Brood War matches. She cheered for me, brought gifts, and led the fanchants. Managed my fanclub too."
    show accel thinking 
    with dissolve
    a "I was knocked out of a StarLeague pretty early a few years back. She was the only person that showed up to my meet and greet afterwards."
    show accel thinking2 with dissolve
    a "I asked her if she’d like to go to dinner, and she said yes. It went from there. We dated for more than a year. Had to break it off when she went abroad for university."
    show accel confident with dissolve
    a "Ah, now you’ve got me feeling nostalgic. Thanks, Mach."
    hide accel
    show reva frown at right:
        xpos .97
    show stunt neutral at left:
        xpos .03
    with dissolve
    r "W{w=.05}h{w=.05}a{w=.05}t{w=.05} {w=.05}a{w=.05} {w=.05}b{w=.05}e{w=.05}a{w=.05}u{w=.05}t{w=.05}i{w=.05}f{w=.05}u{w=.05}l{w=.05} {w=.05}s{w=.05}t{w=.05}o{w=.05}r{w=.05}y{w=.05}.{w=.05}"
    "It’s hard to tell if the complete lack of emotion in Reva’s voice is intentional."
    show stunt fist
    show reva neutral2
    with dissolve
    s "I know those kind of fans. They’re always like, ‘oh, when I imagine him practicing all day, my heart aches and I want to make him hot soups!’"
    show stunt:
        easein .5 xpos -.1
    show reva:
        easein .5 xpos .7
    show jett unimpressed at right:
        xpos 1.3 alpha 0.0
        easein .5 xpos 1.0 alpha 1.0
    $ renpy.pause(.5)  
    j "Literally no one has said or ever will say that."
    show stunt yell with dissolve
    s "They’re gonna be saying it when I take my place as the protoss bonjwa. Can't wait to have my legion of loyal fangirls called Stunt's C—{w=1}{nw}"
    show stunt fist:
        xpos -.1
        easeout 1.0 ypos 2.0 subpixel True
    $ renpy.pause(.8, hard=True)
    play voice "sfx/deskslam.mp3"
    $ renpy.pause(.4)
    "A well-timed hiccup stops Stunt in his tracks. He laughs obnoxiously when his head hits the table."
    show jett considering 
    show reva neutral2
    with dissolve
    "Someone should really confiscate this kid's fake."
    hide stunt
    hide reva
    hide jett
    with dissolve
    $ fbar_choice_accel = True
    window hide dissolve
jump fchoicestart
label fBarEnd:
    window show dissolve
    "We finish out our game of chopsticks with a slew of highly inappropriate questions and equally bold answers."

    "I like soju way more in my stomach than on my lips. Though, I’m not sure I’ll feel the same way in the morning."

    "Our celebration goes late into the night, long enough that we’re practically the only patrons left. "
    show stunt neutral at left:
        ypos 1.7
    show reva sweat at right:
    with dissolve
    "A tendril of drool collects at the corner of an unconscious Stunt's lip. Reva’s eyes are unfocused behind her glasses."
    hide reva
    hide stunt
    show jett neutral at right:
    show accel neutral at left:
    with dissolve
    "But while there’s a bit extra to Accel’s typical grin, both he and Jett look as collected as ever."
    m "... It’s late."
    show accel confident with dissolve
    "Accel pulls the phone out of Stunt's pocket and checks the time."

    a "Oh. It is."
    show accel thinking2 with dissolve
    "He then replaces the expensive-looking electronic on the young protoss player’s head."
    a "Jett, the next time you travel for a European tournament, make sure you show up to the afterparty." 
    a "Say what you will about their play, but those guys know how to have a good time."
    show jett casual with dissolve
    j "Pass. I go for easy prize money, not discotec with Lars and Jørgen."
    show jett neutral3 with dissolve
    j "You guys ready to leave?" 
    m "Yeah. Should, if we don’t want to wake up after noon."
    show jett considering with dissolve
    j "This is the worst part of every night out. How the hell are we supposed to get Stunt home?"
    show accel neutral with dissolve
    a "Don’t forget Jett, the bill is all yours."
    show jett angst with dissolve
    j "Aaaaaaaaaaaah... Why’d you remind me?"
    show jett considering with dissolve
    m"I can hail a cab for Stunt, I guess."
    j "That sounds-- {w=.5}{nw}"
    show jett unimpressed
    extend "Wait, no. Accel, you're in charge of getting Stunt home."
    show accel thinking2 with dissolve
    a "Am I?"
    show jett neutral3 with dissolve
    j "You are. Got team business with these two."
    "Jett thumbs over her shoulder at me and Reva. The two of us share a look, while Accel accepts the order with an easy smile."
    show accel neutral with dissolve
    a "On it, then. Wake up kid."
    show stunt surprised at center:
        ypos 1.9
        easeout 1.5 ypos 1.15
        easein 0.3 ypos 1.19
    s ".................................................................................................. Huhwhat?"
    "Stunt stares through Accel, unresponsive to his offered hand. So much for his iron stomach." 
    hide stunt
    hide accel
    with dissolve
    "Rather than wait out Stunt's stupor, Accel takes the young protoss under his arm and simply carries him out the front door, oblivious to the stares that follow."
    show reva neutral at left with dissolve
    j "Now then. Let's talk."
    m "Are we in trouble?"
    show jett neutral with dissolve
    j "What? No. What would make you think that?"
    m "I don't know. I'm getting a parent-teacher conference vibe."
    show jett unimpressed with dissolve
    j "God, will you just let me... Look, I'm trying to acknowledge the fact that it's unusual for three girls to be on the same team."
    show reva glasses with dissolve
    r "How is that relevant?"
    m "Yeah, I'm with Reva. If we're not playing in female-only leagues, does it really matter?"
    show jett angst 
    show reva neutral2
    with dissolve
    j "Will you two just shut up and listen? It's not going to change how I run things, but I wanted to at least pass along some things I've learned."
    show jett neutral with dissolve
    j "Your job is to train hard and win at StarCraft. Nothing else. The only person you have to represent is yourself."
    show jett considering with dissolve
    j "Don't let anyone guilt you into being an activist. I mean, if it's what you want to do, then go for it. But you have no obligation to pick up a megaphone because you succeeded."
    show reva frown with dissolve
    r "That seems somewhat selfish."
    show jett unimpressed with dissolve
    j "Yeah, well, when you win a VSL and find out that people care more about your gender than your play, let me know if you change your mind."
    show reva neutral2 with dissolve
    "I get where Jett's coming from, especially considering her history. But I don't think that's all there is to it."
    show reva glasses with dissolve
    r "Regardless, my main focus is and always will be on winning games."
    show jett neutral3
    show reva expected
    with dissolve
    "Reva doesn't elaborate any further, even with a probing stare from Jett. I'm left to fill her silence."
    m "Um. I'm just here to play video games."
    show jett smile with dissolve
    j "Win at video games. Not play."
    show jett considering 
    show reva smile
    with dissolve
    "Our waiter glides by the table and slips the check in front of Jett, spoiling her grin instantly."
    "When she's done begrudgingly signing her actual name at the bottom, the three of us head out of the bar and share a cab home."
    window hide dissolve
    stop music fadeout 2.0
    scene black with midfade:
        align (0,0)
        pause 2
    play sound "sfx/Morning.ogg" fadein 4.0 loop
    scene bg apartmentday with midfade:
        align (0, 0)
    window show dissolve
    "I wake to the taste of stale soju on my breath. My apartment is mostly dark, save the crack of light coming through my window."

    "It takes a great deal of effort to dredge myself out of bed, but the need to rinse my mouth is enough motivation."

    "The first time I ever drank too much, I swore to myself I’d never touch alcohol again." 
    "Even if that was a pledge I knew that I wouldn’t keep, it seems like I won’t get another chance to for a while now."
    "Well, at least until there’s a trophy in our team house."
    "I return from the sink with a glass of water and fall into my computer chair. It’s too early for ladder, but I might see what's going on——"
    "Wait a second. WHAT?"
    play music "sfx/brooding.ogg" fadein 1.0
    stop sound fadeout 1.0
    show TL:
        xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    with dissolve
    "Oh my god. Accel, what did you do?"

    "Every StarCraft fansite is abuzz with the news that Jett and Accel are ditching their teams. Accusations of collusion, conspiracy, and corruption abound among Korean and Western fans alike."
    "A laundry list of the Crash coach's missteps ranks second to an interview where he shifts the blame onto Accel. With the scent of drama in the air, debate rages wildly on both sides." 
    "When Accel said he had a better idea in mind, I had no idea he meant something like this. Jett’s new team is the talk of the entire StarCraft community."
    hide TL with dissolve
    play voice "sfx/clickclick.ogg"

    "I rush into the game client, abusing the login button with a dozen clicks a second until I'm finally in. Accel is online, as is the rest of our team."
    play voice "sfx/keyboard.ogg"
    "Before I can even open a chat window, an invite from Jett throws me into an underway group conversation."

    "Text messages appear almost as quickly as I can read them."
    #Computer text
    play voice "sfx/chatbeep.ogg"
    nvl clear
    j_nvl "{cps=0}what the hell is wrong with you!?" 

    a_nvl "{cps=0}heyhey relax. you know what they say about publicity" 

    s_nvl "{cps=0}LOOOOOOL HOLY SHIT DUDE THIS IS HILARIOUS ROFL" 

    r_nvl  "{cps=0}Word that Stunt, Mach and I are joining is out. I’ve received multiple requests for interviews." 

    a_nvl "{cps=0}you should do it" 

    j_nvl "{cps=0}you don’t understand! the deal with enoch wasn’t official, this is going to screw us!" 
    play voice "sfx/keyboard2.ogg"
    a_nvl "{cps=0}heyhey. I didn’t mention enoch by name. just finish the deal and we’ll be fine" 

    m_nvl  "{cps=0}yeah, what’s stopping kim from signing us? accel is kind of right. we have buzz going now." 

    s_nvl "{cps=0}KEKEKEKEKEKEKEKEK"
    
    j_nvl "{cps=0}they're saying i poached you! couldn’t you have gotten back at your coach some other way???" 
    nvl clear
    a_nvl "{cps=0}nop. and I’ll get back at him more when I stomp Crash in team league" 

    r_nvl  "{cps=0}It would be prudent to speak with Mr. Kim as soon as possible, Jett." 

    j_nvl "{cps=0}I KNOW. UGH. ok, we’re meeting at namdan asap, the park by the VSL studio. everyone. no exceptions." 

    s_nvl "{cps=0}KK LOLL"
    play voice "sfx/keyboard.ogg"
    "The diamond next to Jett’s portrait changes from green to black. Accel quickly follows suit and then Stunt, leaving me in the chatroom alone with Reva."

    m_nvl "{cps=0}be fast, jett’ll blow up your phone with texts otherwise." 

    r_nvl  "{cps=0}I will. Goodbye." 

    #chat over

    "With nothing else keeping me at home, I hurry to shut off my PC and dress. I take the stairs of my apartment building two at a time and make my way onto the street."
    window hide dissolve
    play voice "sfx/doorclose.mp3"
    pause .5
    scene bg streetday with Dissolve(1.0):
        align (0, 0)

    window show dissolve

    "What a mess. How terrible would it be to have spent all of last night celebrating for nothing?"

    "Truth be told, whether Accel leaked the information now or let it come out on its own, we’d eventually get this reaction."

    "Enoch wouldn’t have signed us without doing proper background research anyway. Maybe it's alright for this to be out in the open ahead of time."

    "I set those thoughts aside when Namdan Park comes into view. The crowded treeline and trimmed green is a welcome departure from Seoul’s endless concrete."
    window hide dissolve
    scene bg parkday with Dissolve(1.0):
        align (0, 0)
    window show dissolve
    show accel neutral at right:
    show jett angst at left:
    with dissolve
    "Jett didn’t specify where at the park she wanted us to meet, but it doesn’t take long before I find her staring down a seated Accel."

    "She’s in the middle of chewing him out, though it'd be hard to tell by the grin he’s wearing."
    show jett angry with dissolve
    j "Have you seen what they’re saying online?!" 
    show accel thinking2 with dissolve
    a "The team has to stand out somehow. Better this than limping into scene and wallowing in obscurity." 
    show jett considering with dissolve
    j "We should stand out by winning games, not by stirring up shit. This wasn't your decision to make." 
    show accel confident
    show jett neutral
    with dissolve
    "Accel’s the first to notice my arrival and waves me over. Jett’s acknowledgement follows, though it’s far less welcoming."
    play voice "sfx/interupt.ogg"
    show jett angry with Dissolve(.2)
    j "Did you know he was going to pull something like this?" 

    m  "What? No." 
    show accel neutral with dissolve
    a "Relax, Jett. Seriously. Worrying will give you grey hairs." 
    show jett angst with dissolve
    j "I’ll relax the moment that I’m staring at a contract for six months of funding." 
    play voice "sfx/Cell.ogg"
    show jett thinking with Dissolve(.2)
    $ renpy.pause(.3)
    "Jett’s stance goes rigid at the buzz of her phone. She rips it out of her pocket and stares at the screen."
    m  "Who is it?" 
    stop voice
    show jett neutral with dissolve
    j "Kim. He wants us to meet at the Enoch office to sort out this mess." 

    m  "That’s a good thing, right? He wouldn’t bother to have us come out if the answer is going to be no." 
    show jett considering with dissolve
    "She doesn’t seem to agree given the time it takes her to reply. I share a glance with Accel before Jett shoves the phone back into her pocket and turns to me."
    show jett neutral with dissolve
    j "We need to get moving. Accel, wait here for Stunt and Reva." 
    show accel thinking2 with dissolve
    a "Fine by me." 
    show accel confident with dissolve
    "Accel takes in a deep breath and returns to his bench, no doubt happy to relax while someone else handles the stress of a meeting."
    hide accel
    show jett neutral at center
    with dissolve
    m  "I’m coming with you?" 
    show jett unimpressed with dissolve
    j "I’m not enough of a jerk to leave Stunt and Reva alone at the park for an hour, but I need someone at my back." 
    m  "When you put it that way, alright." 
    show jett considering with dissolve
    j "Then come on. It’s not that far." 
    "Without a moment to spare, Jett storms off."
    hide jett with dissolve
    "Accel offers me a leisurely wave as I hurry after her."
    stop music fadeout 2.0
    window hide dissolve
    jump fS25ShowmatchOrganization

###END OF ACT 1
