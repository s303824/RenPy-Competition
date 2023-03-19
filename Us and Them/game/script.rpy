# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protagonist = Character("Jin-sol", what_color="#B01E68", color="#B01E68")
define inner_child = Character("", what_color="#ffffff")
define death_drive = Character("", what_color="#ff0000")
define mentor = Character("", what_color="#ffe15d")

define flash = Fade(0.5, 1.0, 0.5, color="#fff")
define blood = Fade(0.5, 1.0, 0.5, color="#ff0000")

image jinsol = "jinsol.png"
image jinsol outline = "jinsol blood.png"
image jinsol mouth closed = "jinsol mouth closed.png"
image jinsol enough =  im.Scale("bg jinsol enough.png", 1920, 1080)

image kyeongae = "kyeongae neutral.png"
image kyeongae happy = "kyeongae happy.png"

image bg darkness = im.Scale("bg darkness.jpg", 1920, 1080)
image bg test = im.Scale("bg test.jpg", 1920, 1080)
image bg printing room = im.Scale("bg printing room.png", 1920, 1080)

image bg jinsol eyes wide = im.Scale("bg jinsol eye wide.png", 1920, 1080)
image bg jinsol eyes closed = im.Scale("bg jinsol eyes closed.png", 1920, 1080)
image bg jinsol eyes forward = im.Scale("bg jinsol eyes forward.png", 1920, 1080)

image bg jinsol and knife guy = im.Scale("bg assailant and jinsol.png", 1920, 1080)
image bg knife grab = im.Scale("bg knife grab.png", 1920, 1080)
image bg hand = im.Scale("bg hand.png", 1920, 1080)

image bg backwall = im.Scale("bg backwall.png", 1920, 1080)
image bg parents = Movie(size=(1920,1080), play="bg parents.webm")
image bg bar:
    "bg drink 1.png" with dissolve
    pause 1.5
    "bg drink 2.png" with dissolve
    pause 1.5
    "bg drink 3.png" with dissolve
    pause 3.0
    "bg drink 2.png" with dissolve
    pause 1.5
    "bg drink 1.png" with dissolve
    pause 1.5
    repeat
    
# The game starts here.

# Grey: {color=#808080}

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg darkness   

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # Always include (multiple=2)

    death_drive "{cps=0}TRIGGER WARNING: depression, alcoholism, domestic violence, suicidal ideation, Korean historical trauma." (multiple=2)
    inner_child "{cps=0}Viewer’s discretion is advised."(multiple=2)

label intro:
    play sound "audio/heartbeat.mp3" fadein 1.0 volume 0.25 loop
    show bg darkness
    #[FLASH: JINSOL & KNIFE ASSAILANT]
    show bg jinsol and knife guy with flash
    
    #[FLASH: JINSOL TAKING KNIFE]
    show bg knife grab with flash

    play audio "audio/knife.mp3" noloop
    show bg hand with blood

    #[JINSOL: EYES OPEN]
    show bg jinsol eyes wide with blood
    pause(0.3)

    show bg jinsol eyes forward
    pause(0.3)
    #[JINSOL: EYES CLOSED]
    show bg jinsol eyes closed

    show bg darkness with blood
    #stop sound fadeout 1.0
    #play music "audio/sample.mp3" fadein 1.0

    voice "audio/intense adult.mp3"
    death_drive"Thank you for doing your best." (multiple=2) with Dissolve(1.0)
    inner_child"" (multiple=2)

    death_drive"But I think we both know that we're at our limit here." (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}It could be the blood loss. It could be the adrenaline. It is likely both. But you feel your body unstuck from time and space.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)
    
    death_drive"{i}The only indication you have that you’re still alive is how loud you can hear your heart, pounding inside your head.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}But more than anything, you can sense that THIS is the moment.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)
    
    death_drive"{i}Do you feel it?{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}The lack thereof anything?{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}This moment in temporal suspension, if nothing else, must be death’s call, the tolling of the iron bell.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}So open your eyes and answer.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}March forward.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}They’ve already taken her. And millions of others by gunfire and empire.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}Your knife is in this room somewhere. This is it: bitter injustice. Your final act of rebellion shall-{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)
    
    stop sound fadeout 1.0

    voice "audio/sad child.mp3"

    death_drive"{color=#808080}{i}{cps=0}Your knife is in this room somewhere. This is it: bitter injustice. Your final act of rebellion shall-{/i}" (multiple=2)
    inner_child"{i}Stop.{/i}" (multiple=2)

    death_drive"{color=#808080}{i}{cps=0}Your knife is in this room somewhere. This is it: bitter injustice. Your final act of rebellion shall-{/i}" (multiple=2)
    inner_child"{i}Please.{/i}" (multiple=2)
    
    play music "audio/Renpy2Loop.mp3" fadein 2.0 loop

    death_drive"{color=#808080}{i}{cps=0}Your knife is in this room somewhere. This is it: bitter injustice. Your final act of rebellion shall-{/i}" (multiple=2)
    inner_child"She mustn't open her eyes. I won’t allow it." (multiple=2)

    death_drive"Damn." (multiple=2)
    inner_child"{color=#808080}{cps=0}She mustn't open her eyes. I won’t allow it." (multiple=2)

    death_drive"..." (multiple=2)
    inner_child"{color=#808080}{cps=0}She mustn't open her eyes. I won’t allow it." (multiple=2)

    death_drive"Haven’t we grown past you? I thought you died, to be honest." (multiple=2)
    inner_child"{color=#808080}{cps=0}She mustn't open her eyes. I won’t allow it." (multiple=2)

    death_drive"{color=#808080}{cps=0}Haven’t we grown past you? I thought you died, to be honest." (multiple=2)
    inner_child"You forget yourself. In fact, I’ve never been more alive than in this very moment." (multiple=2)

    death_drive"{color=#808080}{cps=0}Haven’t we grown past you? I thought you died, to be honest." (multiple=2)
    inner_child"Her work is not yet done." (multiple=2)

    death_drive"{color=#808080}{cps=0}Haven’t we grown past you? I thought you died, to be honest." (multiple=2)
    inner_child"So I’m here to give her a little hope." (multiple=2)

    death_drive"Interesting." (multiple=2)
    inner_child"{color=#808080}{cps=0}So I’m here to give her a little hope." (multiple=2)

    death_drive"Well, you can try, but this has been a long-time coming. She doesn’t have anything to lose." (multiple=2)
    inner_child"{color=#808080}{cps=0}So I’m here to give her a little hope." (multiple=2)

    death_drive"{color=#808080}{cps=0}Well, you can try, but this has been a long-time coming. She doesn’t have anything to lose." (multiple=2)
    inner_child"That’s what you’d make her think, but I believe I still have a say in the matter." (multiple=2)

    death_drive"Why’s that?" (multiple=2)
    inner_child"{color=#808080}{cps=0}That’s what you’d make her think, but I believe I still have a say in the matter." (multiple=2)

    death_drive"{color=#808080}{cps=0}Why’s that?" (multiple=2)
    inner_child"She’s still shutting her eyes." (multiple=2)

    death_drive"So she is." (multiple=2)
    inner_child"{color=#808080}{cps=0}She’s still shutting her eyes." (multiple=2)

    death_drive"A fruitless effort." (multiple=2)
    inner_child"{color=#808080}{cps=0}She’s still shutting her eyes." (multiple=2)

    death_drive"Her suffering is imminent. Shielding her from reality won’t protect her from what will happen once she leaves this room." (multiple=2)
    inner_child"{color=#808080}{cps=0}She’s still shutting her eyes." (multiple=2)

    death_drive"And neither will listening to you." (multiple=2)
    inner_child"{color=#808080}{cps=0}She’s still shutting her eyes." (multiple=2)

    death_drive"You should have learned by now: hope isn’t sustainable- it hasn’t been for the twenty-six shitty years she’s been alive." (multiple=2)
    inner_child"{color=#808080}{cps=0}She’s still shutting her eyes." (multiple=2)

    death_drive"{color=#808080}{cps=0}You should have learned by now: hope isn’t sustainable- it hasn’t been for the twenty-six shitty years she’s been alive." (multiple=2)
    inner_child"Stop discrediting me." (multiple=2)

    death_drive"I’m truly hard-pressed to think of a time in which you haven’t existed just to crush her spirits." (multiple=2)
    inner_child"{color=#808080}{cps=0}Stop discrediting me." (multiple=2)

    death_drive"{color=#808080}{cps=0}I’m truly hard-pressed to think of a time in which you haven’t existed just to crush her spirits." (multiple=2)
    inner_child"Stop! I’m tired of everyone ignoring what I have to say!" (multiple=2)

    death_drive"Shut up- hold on. She’s noticing a sensation." (multiple=2)
    inner_child"{color=#808080}{cps=0}Stop! I’m tired of everyone ignoring what I have to say!" (multiple=2)

    death_drive"{color=#808080}{cps=0}Shut up- hold on. She’s noticing a sensation." (multiple=2)
    inner_child"Ah!" (multiple=2)

    # [FADE IN: BLOODY HANDS, BLOODY FACE JINSOL SPRITE]
    show jinsol outline with Fade(0.5, 1.0, 0.5)

    voice "audio/intense adult.mp3"
    death_drive"{i}Even without looking at yourself, you can feel it: little streams of blood, trickling down your forehead. Pooling in your hair. And dripping down your jaw. It’s warm.{/i}" (multiple=2)
    inner_child"" (multiple=2)

    death_drive"{i}The blood caked on your fingers, though, has long been dried. After all, it’s not yours.{/i}" (multiple=2)
    inner_child"" (multiple=2)

    voice "audio/normal child.mp3"
    death_drive"{color=#808080}{i}{cps=0}The blood caked on your fingers, though, has long been dried. After all, it’s not yours.{/i}" (multiple=2)
    inner_child"{i}Don’t think about that.{/i}" (multiple=2)

    death_drive"Then what the hell do you want her to think about?" (multiple=2)
    inner_child"{color=#808080}{i}{cps=0}Don’t think about that.{/i}" (multiple=2)

    death_drive"{color=#808080}{cps=0}Then what the hell do you want her to think about?" (multiple=2)
    inner_child"Not this. Something uplifting. Something like..." (multiple=2)

    # [FLASH: KYEONG-AE]
    hide jinsol outline
    show kyeongae happy with flash
    hide kyeongae happy
    # [THEN BACK TO BLACK SCREEN]
    show bg darkness with flash
    show jinsol outline

    death_drive"{color=#808080}{cps=0}Then what the hell do you want her to think about?" (multiple=2)
    inner_child"No, not that. I don’t know. I don’t know. It hurts." (multiple=2)

    death_drive"Idiot." (multiple=2)
    inner_child"{color=#808080}{cps=0}No, not that. I don’t know. I don’t know. It hurts." (multiple=2)

    jump part_1
