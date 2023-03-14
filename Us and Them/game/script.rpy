# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protagonist = Character("Jinsol", color="#0185c9")
define inner_child = Character("", what_color="#ffffff")
define death_drive = Character("", what_color="#ff0000")

image bg darkness = im.Scale("bg darkness.jpg", 1920, 1080)

image bg test = im.Scale("bg test.jpg", 1920, 1080)

# The game starts here.

# Grey: {color=#808080}

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg test
    play music "audio/sample.mp3" fadein 1.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # Always include (multiple=2)
    death_drive"" (multiple=2)
    inner_child"" (multiple=2)

    death_drive "TRIGGER WARNING: depression, alcoholism, domestic violence, suicidal ideation, Korean historical trauma." (multiple=2) with dissolve
    inner_child ""(multiple=2) with dissolve

    death_drive "TRIGGER WARNING: depression, alcoholism, domestic violence, suicidal ideation, Korean historical trauma." (multiple=2)
    inner_child "Viewer’s discretion is advised."(multiple=2) with dissolve

    death_drive"" (multiple=2)
    inner_child"" (multiple=2)

    death_drive"Thank you for doing your best." (multiple=2) with dissolve
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

    death_drive"{i}Our moment in temporal suspension, if nothing else, must be death’s call, the tolling of the iron bell.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}So open your eyes and answer.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}March forward. {/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}They’ve already taken her. And millions of others by gunfire and empire.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{i}Your knife is in this room somewhere. This is it: bitter injustice. Your final act of rebellion shall-{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    stop music 

    death_drive"{color=#808080}{i}So open your eyes and answer it. Your knife is in this room somewhere. This is it: bitter injustice. Your final act of rebellion shall-{/i}" (multiple=2)
    inner_child"{i}Stop.{/i}" (multiple=2)

    death_drive"{color=#808080}{i}So open your eyes and answer it. Your knife is in this room somewhere. This is it: bitter injustice. Your final act of rebellion shall-{/i}" (multiple=2)
    inner_child"{i}Please.{/i}" (multiple=2)

    death_drive"{color=#808080}{i}So open your eyes and answer it. Your knife is in this room somewhere. This is it: bitter injustice. Your final act of rebellion shall-{/i}" (multiple=2)
    inner_child"She mustn't open her eyes. I won’t allow it." (multiple=2)

    death_drive"Damn." (multiple=2)
    inner_child"{color=#808080}She mustn't open her eyes. I won’t allow it." (multiple=2)

    death_drive". . ." (multiple=2)
    inner_child"{color=#808080}She mustn't open her eyes. I won’t allow it." (multiple=2)

    death_drive"Haven’t we grown past you? I thought you died, to be honest." (multiple=2)
    inner_child"{color=#808080}She mustn't open her eyes. I won’t allow it." (multiple=2)

    death_drive"{color=#808080}Haven’t we grown past you? I thought you died, to be honest." (multiple=2)
    inner_child"You forget yourself. In fact, I’ve never been more alive than in this very moment." (multiple=2)

    death_drive"{color=#808080}Haven’t we grown past you? I thought you died, to be honest." (multiple=2)
    inner_child"Her work is not yet done." (multiple=2)

    death_drive"{color=#808080}Haven’t we grown past you? I thought you died, to be honest." (multiple=2)
    inner_child"So I’m here to give her a little hope." (multiple=2)

    death_drive"Interesting." (multiple=2)
    inner_child"{color=#808080}So I’m here to give her a little hope." (multiple=2)

    death_drive"Well, you can try, but this has been a long-time coming. She doesn’t have anything to lose." (multiple=2)
    inner_child"{color=#808080}So I’m here to give her a little hope." (multiple=2)

    death_drive"{color=#808080}Well, you can try, but this has been a long-time coming. She doesn’t have anything to lose." (multiple=2)
    inner_child"That’s what you’d make her think, but I believe I still have a say in the matter." (multiple=2)

    death_drive"Why’s that?" (multiple=2)
    inner_child"{color=#808080}That’s what you’d make her think, but I believe I still have a say in the matter." (multiple=2)

    death_drive"{color=#808080}Why’s that?" (multiple=2)
    inner_child"She’s still shutting her eyes." (multiple=2)

    # This ends the game.

    return
