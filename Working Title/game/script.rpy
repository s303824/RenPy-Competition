# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protagonist = Character("Jinsol", color="#0185c9")
define inner_child = Character("", color="#ffffff")
define death_drive = Character("", color="#ff0000")

image bg darkness = im.Scale("bg darkness.jpg", 1920, 1080)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg darkness
    play music "audio/sample.mp3" fadein 1.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # Always include (multiple=2)
    death_drive"" (multiple=2)
    inner_child"" (multiple=2)

    death_drive"{color=#ff0000}{i}Do you feel it?{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{color=#ff0000}{i}The lack thereof anything?{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)


    death_drive"{color=#ff0000}{i}It could be the blood loss. It could be the adrenaline. It is likely both. But you feel your body unstuck from time and space. The only indication you have that you’re still alive is how loud you can hear your heart, pounding inside your head.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{color=#ff0000}{i}But more than anything else, you can sense that THIS is the moment.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{color=#ff0000}{i}Our moment in temporal suspension, if nothing else, must be death’s call, the tolling of the iron bell.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{color=#ff0000}{i}So open your eyes and answer.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{color=#ff0000}{i}March forward. {/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{color=#ff0000}{i}Avenge her. Avenge the millions dead by gunfire and empire.{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)

    death_drive"{color=#ff0000}{i}Your knife is in this room somewhere. This is it: bitter injustice. Your final act of rebellion shall-{/i}" (multiple=2) with dissolve
    inner_child"" (multiple=2)
    stop music 
    death_drive"{color=#808080}{i}So open your eyes and answer it. Your knife is in this room somewhere. This is it: bitter injustice. Your final act of rebellion shall-{/i}" (multiple=2)
    inner_child"{i}Stop.{/i}"

    death_drive"{color=#808080}{i}So open your eyes and answer it. Your knife is in this room somewhere. This is it: bitter injustice. Your final act of rebellion shall-{/i}" (multiple=2)
    inner_child"{i}Please.{/i}"
    # This ends the game.

    return
