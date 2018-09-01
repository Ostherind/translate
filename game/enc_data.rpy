# In the following example, an encyclopaedia is created inside an "init python" block.
# This allows an encyclopaedia's content to be independent of the saved games. 
# ie: Whenever encyclopaedia content is unlocked, it's unlocked for all save games.
# If you want an encyclopaedia that is bound to a save game file, create the encyclopaedia in a "python" block inside the "start" label.
# Then, for the "locked" argument in each entry, don't use a persistent variable.    

init python:

    #Variables to hold the text.
    ladder = "Shorthand for online ranked play. Ranked from the lowest to the highest, the leagues in StarCraft 2 are: Bronze, Silver, Gold, Platinum, Diamond, Master and Grandmaster. Grandmaster rank is awarded to the top two hundred players from each region."
    pcb = "A PC bang is a type of LAN gaming center where patrons can play multiplayer computer games for an hourly fee. PC bangs remain popular despite the spread of household computers as they provide a meeting place for gamers (especially school-aged gamers) to play together with their friends."
    bw = "The expansion pack to the original StarCraft, released in 1998. The eSports industry in South Korea was built entirely around Brood War and its wild success with both players and spectators. It remains relatively popular and a cultural mainstay."
    rush = "A powerful attack made early in the game. A rush sacrifices late-game stability in favor of a strong early army. Against a fast teching or greedy opponent, the attacker may decide execute a one-chance attack that must end the game, also known as an all-in."
    stand = "Standard refers to a balanced playstyle meant to cover as many of the opponent's options as possible. Favors a solid, well-rounded skillset. Top players utilize standard play for the majority of their games."
    gg = "Good game. A verbal handshake offered at the end of a match. Failure to offer a gg is seen as disrespectful and is an offense that some leagues will fine players for."
    chobo = "The Korean term for a new player, equivalent to newb." 
    barc = "An account used for anonymous ladder play. Barcode accounts generally use a random combination of i and l (e.g.: llIIllIlI). Generally used to practice certain strategies or tactics without the risk of identification."
    nat = "Shorthand for natural expansion. Refers to the expansion located closest to a player's main base, thus taken naturally. Most natural expansions have a narrow path, or choke point, at their entrances and exits for easier defense."
    drop = "Refers either to a dropship or the act of unloading units from a dropship. Dropships are capable of quickly transporting units across the map and into the opponent's base."
    micro = "Control of local, specialized events and unit control. Though necessary for every player, those that favor aggressive or tricky strategies tend to focus on micro."
    macro = "Control of economic timings and the game's flow. Though necessary for every player, those that favor passive or defensive strategies tend to focus on macro."
    apm = "The average number of actions made every minute. Top players generally have at least 300 APM and often more."
    cheese = "An unexpected strategy that relies on lack of information to surprise the opponent. Cheese builds typically revolve around an early attack that, if undetected, is more difficult to defend than to execute."
    tech = "Shorthand for technology. Refers to the production of powerful and expensive units."
    bonjwa = "The Korean term for a player who dominates the StarCraft scene for a long period of time. A bonjwa has a very high winrate and successive championship wins. So far, StarCraft's only bonjwas have been Terran and Zerg players."
    meta = "Literally means 'beyond the game' and refers to anything outside of actual gameplay that still has an impact on play. Examples include exploiting strategic trends, an opponent's style of play, or a map's qualities."
    proxy = "A building constructed in the proximity of the opponent's base. Proxies are typically used to perform rush and all-in strategies."
    builds = "Shorthand for build order, or the order in which structures and units are created. Typically rigid and drilled to execution perfection. Players that innovate and succeed with a certain build will sometimes have it named for them (e.g.: Bisu Build)."
    expansion = "To construct an additional base. It is impossible to support an army past the early game on the resources from a single base, therefore expanding is necessary to perform any mid/late-game or economy-focused strategy."
    harass = "Shorthand for harassment. The act of using a small number of units to cause damage without a large engagement. Harass is usually performed with high-mobility units and targeted at the enemy's economy or tech."
    scout = "The act of revealing (either with a unit's line-of-sight or scans) remote areas of the map to gain information about the opposing player."
    


    #Variables to hold the image paths.


    #Define an encyclopaedia object.
    #showLockedButtons=False will not display locked "???" entries on the list screen.
    #showLockedEntry=False will prevent the player from viewing the locked entry.
    encyclopaedia = Encyclopaedia(showLockedButtons=True, showLockedEntry=False) 
    
    #If the encyclopaedia is save game independent, run this function to generate the persistent status variables. 
    #If the encyclopaedia is unique for each save game, comment out or delete this.
    #entries_total is the total number of EncEntries the Encyclopaedia will hold.
    #master_key and name are what determines the name of the status variables and the name of each key.
    #only change master_key and name if you need multiple encyclopaedias in a game.
    encyclopaedia.setPersistentStatus(entries_total=24, master_key="new", name="new")
    
    #Add all the subjects the Encyclopaedia will have.
    encyclopaedia.addSubjects("Game", "Scene")

    #Here we define each Encyclopaedia Entry
    #The arguments are: number, name, text, subject, status, locked, image
    #status should always be from the persistent.new_dict or it won't save
    #if locked=False, entry will always be visible, even if new game hasn't been started
    en1 = EncEntry(1,"Ladder",ladder, "Game", status=persistent.new_dict["new_01"], locked=persistent.en1_locked)
    en2 = EncEntry(2,"PC bang",pcb, "Scene", status=persistent.new_dict["new_02"],  locked=persistent.en2_locked)
    en3 = EncEntry(3,"Brood War",bw, "Game", status=persistent.new_dict["new_03"], locked=persistent.en3_locked)
    #en4 = EncEntry(4,"Rush",rush, "Game", status=persistent.new_dict["new_04"], locked=persistent.en4_locked)
    en5 = EncEntry(5,"Standard",stand, "Game", status=persistent.new_dict["new_05"], locked=persistent.en5_locked)
    en6 = EncEntry(6,"GG",gg, "Game", status=persistent.new_dict["new_06"], locked=persistent.en6_locked)
    #en7 = EncEntry(7,"Chobo",chobo, "Scene", status=persistent.new_dict["new_07"], locked=persistent.en7_locked)
    en8 = EncEntry(8,"Macro",macro, "Game", status=persistent.new_dict["new_08"], locked=persistent.en8_locked)
    en9 = EncEntry(9,"Barcode",barc, "Scene", status=persistent.new_dict["new_09"], locked=persistent.en9_locked)
    en10 = EncEntry(10,"Scout",scout, "Game", status=persistent.new_dict["new_010"], locked=persistent.en10_locked)
    en11 = EncEntry(11,"Drop",drop, "Game", status=persistent.new_dict["new_011"], locked=persistent.en11_locked)
    en12 = EncEntry(12,"Micro",micro, "Game", status=persistent.new_dict["new_012"], locked=persistent.en12_locked)
    en13 = EncEntry(13,"APM",apm, "Game", status=persistent.new_dict["new_013"], locked=persistent.en13_locked)
    en14 = EncEntry(14,"Cheese",cheese, "Game", status=persistent.new_dict["new_014"], locked=persistent.en14_locked)
    en15 = EncEntry(15,"Tech",tech, "Game", status=persistent.new_dict["new_015"], locked=persistent.en15_locked)
    en16 = EncEntry(16,"Bonjwa",bonjwa, "Scene", status=persistent.new_dict["new_016"], locked=persistent.en16_locked)
    en17 = EncEntry(17,"Metagame",meta, "Game", status=persistent.new_dict["new_017"], locked=persistent.en17_locked)
    en18 = EncEntry(18,"Proxy",proxy, "Game", status=persistent.new_dict["new_018"], locked=persistent.en18_locked)
    en19 = EncEntry(19,"Build",builds, "Game", status=persistent.new_dict["new_019"], locked=persistent.en19_locked)
    en20 = EncEntry(20,"Expand",expansion, "Game", status=persistent.new_dict["new_020"], locked=persistent.en20_locked)
    #en21 = EncEntry(21,"Harass",harass, "Game", status=persistent.new_dict["new_021"], locked=persistent.en21_locked)
    #en20 = EncEntry(22,"Harass",expansion, "Game", status=persistent.new_dict["new_021"], locked=persistent.en21_locked)




  
    #Add all entries and sub-entries in an init block.
    encyclopaedia.addEntries(en1,en2,en3,en5,en6,en8,en9,en10,en11,en12,en13,en14,en15,en16,en17,en18,en19,en20) 
    #addEntry auto-sorts when adding.
    #en4 and en6 won't be viewed at the start because they're locked by persistent data.
    #After they're unlocked, they'll be available whenever the game loads. 

    #When creating sub-entries, the main entry is considered page 1, always start at 2
