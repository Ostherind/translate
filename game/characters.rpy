
define b = Character("Bolt", color="#cd2929",  window_background = "gui/boltdialog.png", ctc="ctc_blink", ctc_position="nestled")
define m = Character("Mach", color="#4d59b1", window_background = "gui/machdialog.png", ctc="ctc_blink", ctc_position="nestled") ## mach
define j = Character("Jett", color="#cd2929", window_background = "gui/jettdialog.png", ctc="ctc_blink", ctc_position="nestled") ## jett
define a = Character("Accel", color="#3f86c1", window_background = "gui/acceldialog.png", ctc="ctc_blink", ctc_position="nestled") ## accel
define unknown = Character("Unknown", color="#cd2929", window_background = "gui/unknowndialog.png", ctc="ctc_blink", ctc_position="nestled")
define r = Character("Reva", color="#35a212",  window_background = "gui/revadialog.png", ctc="ctc_blink", ctc_position="nestled") ## rival 
define s = Character("Stunt", color="#e7c512",  window_background = "gui/stuntdialog.png", ctc="ctc_blink", ctc_position="nestled") ## rival 

#clerk
define c = Character("Clerk", color="#51c082",  window_background = "gui/clerkdialog.png", ctc="ctc_blink", ctc_position="nestled") ## rival 
define y = Character("Yeon", color="#51c082",  window_background = "gui/yeondialog.png", ctc="ctc_blink", ctc_position="nestled") ## rival 

#mr. kim
define k = Character("Kim", color="#7e147a",  window_background = "gui/kimdialog.png", ctc="ctc_blink", ctc_position="nestled") ## rival 

define d = Character("Damen", color="#c8ffc8",  window_background = "gui/damendialog.png", ctc="ctc_blink", ctc_position="nestled") ## rival 
define ca = Character(None, color="#c8ffc8",  window_background = "gui/camerondialog.png", ctc="ctc_blink", ctc_position="nestled") ## rival 
define jo = Character(None, color="#c8ffc8",  window_background = "gui/jondialog.png", ctc="ctc_blink", ctc_position="nestled") ## rival 

define day9 = Character("Day9", color="#e38526",  window_background = "gui/day9dialog.png", ctc="ctc_blink", ctc_position="nestled") ## rival 
define timmy = Character("Timmy", color="#4853ab",  window_background = "gui/timmydialog.png", ctc="ctc_blink", ctc_position="nestled") ## rival 


define narrator = Character(None, color="#c8ffc8",  window_background = "gui/defaultdialog.png", ctc="ctc_blink",  ctc_position="nestled")


define analyst = Character("Analyst", color="#c8ffc8",  window_background = "gui/analystdialog.png", ctc="ctc_blink",  ctc_position="nestled")
define caster = Character("Caster", color="#c8ffc8",  window_background = "gui/casterdialog.png", ctc="ctc_blink",  ctc_position="nestled")
define commentator = Character("Commentator", color="#c8ffc8",  window_background = "gui/commentatordialog.png", ctc="ctc_blink",  ctc_position="nestled")

define dad = Character("Dad", color="#c8ffc8",  window_background = "gui/daddialog.png", ctc="ctc_blink",  ctc_position="nestled")

define mom = Character("Mom", color="#c8ffc8",  window_background = "gui/momdialog.png", ctc="ctc_blink",  ctc_position="nestled")

define secretary = Character("Secretary", color="#c8ffc8",  window_background = "gui/secretarydialog.png", ctc="ctc_blink",  ctc_position="nestled")

define somekid1 = Character("Some Kid 1", color="#c8ffc8",  window_background = "gui/somekid1dialog.png", ctc="ctc_blink",  ctc_position="nestled")
define somekid2 = Character("Some Kid 2", color="#c8ffc8",  window_background = "gui/somekid2dialog.png", ctc="ctc_blink",  ctc_position="nestled")
define somekid3 = Character("Some Kid 3", color="#c8ffc8",  window_background = "gui/somekid3dialog.png", ctc="ctc_blink",  ctc_position="nestled")

define stuntmom= Character("!!!", color="#c8ffc8",  window_background = "gui/stuntmomdialog.png", ctc="ctc_blink",  ctc_position="nestled")

define hostess = Character("Hostess", color="#c8ffc8",  window_background = "gui/hostessdialog.png", ctc="ctc_blink",  ctc_position="nestled")


#NVL
define m_nvl = Character("Mach",what_prefix=":  ", color="#4d59b1", kind=nvl) ## mach
define j_nvl = Character("Jett", what_prefix=":  ", color="#cd2929", kind=nvl) ## jett
define a_nvl = Character("Accel", what_prefix=":  ", color="#3f86c1", kind=nvl) ## accel
define r_nvl = Character("Reva", what_prefix=":  ", color="#35a212",  kind=nvl) ## rival 
define s_nvl = Character("Stunt", what_prefix=":  ", color="#e7c512",  kind=nvl) ## rival 
define o_nvl = Character("Opponent", what_prefix=":  ", color="#ffffff",  kind=nvl) ## rival 

image ctc_blink:
    "gui/ctc/ctc01.png"
    linear 0.15 alpha 1
    "gui/ctc/ctc02.png"
    linear 0.1 alpha 1
    "gui/ctc/ctc03.png"
    linear 0.1 alpha 1
    "gui/ctc/ctc04.png"
    linear 0.1 alpha 1
    "gui/ctc/ctc05.png"
    linear 0.1 alpha 1
    "gui/ctc/ctc06.png"
    linear 0.1 alpha 1
    repeat

image blacksolid = "char/blacksolid.jpg"
image white ="char/white.jpg"

image jett neutral = "char/Jett/JettCrossNormal.png"
image jett neutral2 = "char/Jett/JettCrossNormal2.png"
image jett neutral3 = "char/Jett/JettNeutralNormal.png"
image jett smile = "char/Jett/JettNeutralSmile.png"
image jett angry = "char/Jett/JettCrossMad.png"
image jett angst = "char/Jett/JettNeutralFrustrated.png"
image jett casual = "char/Jett/JettCrossCasual.png"
image jett casual2 = "char/Jett/JettThinkingCasual.png"
image jett unimpressed = "char/Jett/JettCrossUnimpressed.png"
image jett considering = "char/Jett/JettCrossConsider.png"
image jett thinking = "char/Jett/JettThinkingNormal.png"
image jett thinking2 = "char/Jett/JettThinkingConcerned.png"
image jett pleased = "char/Jett/JettNeutralSmug.png"
image jett kawaii = "char/Jett/girlprogamer.png"

image jett cold = "char/Jett/15abe.png"

image dummy ="char/sc2vn.png"
image dummy2 ="char/sc2vn.png"
image dummy3 ="char/sc2vn.png"
image dummy4 ="char/sc2vn.png"
image card ="char/card.png"
image usb = "char/bonus/usbs.png"
image gob = "char/bonus/gob.png"
image gow = "char/bonus/gow.png"
image charge = "char/bonus/charge.png"
image reddit ="bg/epicmeme1.jpg"
image playxd ="bg/playxd.jpg"
image TL ="bg/TL.jpg"

image accel neutral = "char/Accel/AccelHipNormal.png"
image accel neutral2 = "char/Accel/AccelNeutralNormal.png"
image accel thinking = "char/Accel/AccelHipThinking.png"
image accel thinking2 = "char/Accel/AccelHipThinking2.png"
image accel thinking3 = "char/Accel/AccelHipThinking3.png"
image accel laughing = "char/Accel/AccelCrossSmirk.png"
image accel concerned = "char/Accel/AccelHipConcerned.png"
image accel confident = "char/Accel/AccelCrossConfident.png"

image accel surprised = "char/Accel/03c.png"

image stunt neutral = "char/stunt/stunt_neutral.png"
image stunt neutral grin = "char/stunt/stunt_neutral_grin.png"
image stunt2 neutral grin = "char/stunt/stunt_neutral_grin.png"
image stunt embarassed = "char/stunt/stunt_hunched_embarassed.png"
image stunt phone = "char/stunt/stunt_phone.png"
image stunt surprised = "char/stunt/stunt_surprised.png"
image stunt fist = "char/stunt/stunt_fist_grin.png"
image stunt yell = "char/stunt/stunt_fist_yell.png"
image stunt eyebrow = "char/stunt/StuntEyebrow.png"
image stunt frown = "char/stunt/StuntFrown.png"
image stunt mouthy = "char/stunt/StuntMouthy.png"
image stunt notcool = "char/stunt/StuntNotCool.png"
image stunt smug = "char/stunt/stuntsmug.png"

image reva neutral = "char/Reva/reva.png"
image reva neutral2 = "char/Reva/RevaNeutralNormal2.png"
image reva smile = "char/Reva/RevaNeutralSmile.png"
image reva concerned = "char/Reva/RevaTurnConcerned.png"
image reva glasses = "char/Reva/RevaFrame.png"
image reva expected = "char/Reva/Revashine.png"
image reva shy = "char/Reva/RevaTurnConcerned.png"
image reva2 shy = "char/Reva/RevaTurnConcerned.png"
image reva sweat = "char/Reva/RevaTurnSweat.png"
image reva surprised = "char/Reva/RevaNeutralSurprised.png"
image reva frown = "char/Reva/RevaNeutralFrown.png"

image reva2 neutral = "char/Reva/reva.png"
image reva2 neutral2 = "char/Reva/RevaNeutralNormal2.png"

image rival annoyed = "char/Bolt/RivalAnnoyed.png"
image rival bored = "char/Bolt/RivalBored.png"
image rival fierce = "char/Bolt/RivalFierce.png"
image rival evil = "char/Bolt/RivalMacab.png"
image rival smug = "char/Bolt/RivalSmug.png"
image rival casual = "char/Bolt/RivalCasual.png"

image yeon concerned = "char/Yeon/yeonconcerned.png"
image yeon neutral = "char/Yeon/yeonneutral.png"
image yeon smile = "char/Yeon/yeonsmile.png"
image yeon serious = "char/Yeon/yeonserious.png"

image kim smug = "char/Kim/KimConfidence.png"
image kim frust = "char/Kim/KimFrustNormal.png"
image kim frust2 = "char/Kim/KimFrustOpen.png"
image kim frust3 = "char/Kim/KimNeutral2Narrow.png"
image kim frust4 = "char/Kim/KimNeutral2Frustrated.png"
image kim frust5 = "char/Kim/KimNeutral2Frustrated2.png"
image kim orly = "char/Kim/KimNeutral2Confident.png"
image kim relieved = "char/Kim/KimNeutral2Normal.png"
image kim neutral = "char/Kim/KimNeutralNormal.png"
image kim neutralsleeve = "char/Kim/KimNeutral2Normal.png"
image kim neutral2 = "char/Kim/KimNeutralNormal2.png"
image kim neutral2sleeve = "char/Kim/KimNeutral2Normal2.png"
image kim confident = "char/Kim/KimNeutralConfident.png"


image aptextra = "char/aptextra.jpg"

image timmy happy = "char/TimmyHappy.png"
image timmy sad = "char/TimmySad.png"
image timmy neutral = "char/TimmyNeutral.png"
image timmy surprised = "char/TimmyWoah.png"
image timmy think = "char/TimmyThink.png"

image day happy = "char/DayHappy.png"
image day eyebrow = "char/DayEyebrow.png"
image day hmm = "char/DayHmm.png"
image day instruct = "char/DayInstruct.png"
image day instruct2 = "char/DayInstruct2.png"
image day neutral = "char/DayNeutral.png"

image cam neutral = "char/cam.png"
image cam smile = "char/cam2.png"
image cam intense = "char/cam3.png"
image cam thinking = "char/cam4.png"

image damen phone = "char/dam.png"
image damen neutral = "char/dam2.png"
image damen smile = "char/dam3.png"
image damen calm = "char/dam4.png"

image jon neutral = "char/jon.png"
image jon smile = "char/jon2.png"
image jon shrug = "char/jon3.png"


init:
    image day bonus = im.Flip("char/DayEyebrow.png", horizontal=True)
    image jett smugflip = im.Flip("char/Jett/JettNeutralSmug.png", horizontal=True)


image day animated:
    "char/DayInstruct.png"
    pause .15
    "char/DayInstruct2.png"
    pause .15
    repeat
    
image foreground = "char/bonus/springforeground.png"
image jettoutline = "char/bonus/springoutline.png"
image steambig = "char/bonus/Steambig.png"
image steamsmall = "char/bonus/steamsmall.png"
image steamsmall2 = "char/bonus/steamsmall.png"
image steamsmall3 = "char/bonus/steamsmall.png"
image spring = "char/bonus/spring.jpg"