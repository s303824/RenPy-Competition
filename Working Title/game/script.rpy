# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protagonist = Character("Jinsol", color="#0185c9")
define kid = Character("Inner Child", color="#ffffff")
define adult = Character("Death Drive", color="#ff0000")

image bg club = im.Scale("bg club.jpg", 1920, 1080)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg club

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sylvie green smile

    # These display lines of dialogue.

    # Always include (multiple=2)

    protagonist "Oh thank god, you're here. Now we can get to work."
    "The creature awakes." (multiple=2)
    "" (multiple=2)

    "{color=#808080}The creature awakes." (multiple=2)
    "{color=#ff0000}..." (multiple=2)

    "What now?" (multiple=2)
    "{color=#808080}..." (multiple=2)

    "{color=#808080}What now?" (multiple=2)
    "{color=#ff0000}Now we begin our work." (multiple=2)

    # This ends the game.

    return
