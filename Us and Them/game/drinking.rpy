label part_1:

    death_drive"Actually, I just had an idea." (multiple=2)
    inner_child"{color=#808080}{cps=0}No, not that. I don’t know. I don’t know. It hurts." (multiple=2)

    death_drive"Do you want to know what could REALLY help in this situation?" (multiple=2)
    inner_child"{color=#808080}{cps=0}No, not that. I don’t know. I don’t know. It hurts." (multiple=2)
    
    death_drive"{color=#808080}{cps=0}Do you want to know what could REALLY help in this situation?" (multiple=2)
    inner_child"Oh, god." (multiple=2)

    death_drive"Listen." (multiple=2)
    inner_child"{color=#808080}{cps=0}Oh, god." (multiple=2)

    death_drive"Listen listen listen..." (multiple=2)
    inner_child"{color=#808080}{cps=0}Oh, god." (multiple=2)

    death_drive"{i}You could go for a drink right now.{/i}" (multiple=2)
    inner_child"{color=#808080}{cps=0}Oh, god." (multiple=2)

    death_drive"{i}You wanna know why?{/i}" (multiple=2)
    inner_child"{color=#808080}{cps=0}Oh, god." (multiple=2)

    menu:
        "\“Tell me.\”":
            voice "audio/intense adult.mp3"
            death_drive"{i}Because these are some strong things you’re feeling right now. You’re WAY too uncomfortable with what happened tonight.{/i}" (multiple=2)
            inner_child"{color=#808080}{cps=0}Oh, god." (multiple=2)

            death_drive"{i}You need to wash them out. Completely.{/i}" (multiple=2)
            inner_child"{color=#808080}{cps=0}Oh, god." (multiple=2)

            death_drive"{i}Like you did yesterday. And the day before that. And the day before that. And uh… ha, your memory these past four years has gotten so hazy.{/i}" (multiple=2)
            inner_child"{color=#808080}{cps=0}Oh, god." (multiple=2)

        "\“I’m afraid of what you’ll have to say.\”":
            voice "audio/sad child.mp3"
            death_drive"{color=#808080}{i}{cps=0}You wanna know why?{/i}" (multiple=2)
            inner_child"{i}You should be. You sound like your father when you think things like that.{/i}" (multiple=2)

            death_drive"Ha! Please, this has nothing to do with him." (multiple=2)
            inner_child"{color=#808080}{i}{cps=0}You should be. You sound like your father when you think things like that.{/i}" (multiple=2)

            death_drive"{color=#808080}{cps=0}Ha! Please, this has nothing to do with him." (multiple=2)
            inner_child"It does, more than you think." (multiple=2)

            death_drive"Still, it’s not worth it." (multiple=2)
            inner_child"{color=#808080}{cps=0}It does, more than you think." (multiple=2)
    
    hide jinsol outline fadeout 1.0
    # [FADE TO ALCOHOL MEMORY GIF]
    play sound "audio/bar.mp3" loop volume 0.25 fadein 1.0
    show bg bar with fade

    voice "audio/intense adult.mp3"
    death_drive"{i}Do you remember the first time you got drunk?{/i}" (multiple=2)
    inner_child"" (multiple=2)

    death_drive"{i}1945. You and some reporters were treating yourselves at the Iron Gullet, Seoul’s most miraculously mediocre bar.{/i}" (multiple=2)
    inner_child"" (multiple=2)

    death_drive"{i}You had just published your first big piece and the backseats were packed so you all sat upfront along the windows, drinking as the night celebrated liberation.{/i}" (multiple=2)
    inner_child"" (multiple=2)

    death_drive"{i}The winds of change were moving and in that small window of opportunity, it felt like history was going to be made BY Korea.{/i}" (multiple=2)
    inner_child"" (multiple=2)

    voice "audio/sad child.mp3"
    death_drive"{color=#808080}{i}{cps=0}The winds of change were moving and in that small window of opportunity, it felt like history was going to be made BY Korea.{/i}" (multiple=2)
    inner_child"{i}Not just that. There was pride in your comrades. They were proud of you.{/i}" (multiple=2)

    death_drive"They were? I must have forgotten. But it’s not like how they thought of me really changes anything anymore." (multiple=2)
    inner_child"{color=#808080}{i}{cps=0}Not just that. There was pride in your comrades. They were proud of you.{/i}" (multiple=2)

    death_drive"Anyways." (multiple=2)
    inner_child"{color=#808080}{i}{cps=0}Not just that. There was pride in your comrades. They were proud of you.{/i}" (multiple=2)

    death_drive"{i}You felt unstoppable. Like you could face whatever the world threw at you. You could capture the hearts and minds of the new nation with just a typewriter and your voice.{/i}" (multiple=2)
    inner_child"{color=#808080}{i}{cps=0}Not just that. There was pride in your comrades. They were proud of you.{/i}" (multiple=2)

    death_drive"{color=#808080}{i}{cps=0}You felt unstoppable. Like you could face whatever the world threw at you. You could capture the hearts and minds of the new nation with just a typewriter and your voice.{/i}" (multiple=2)
    inner_child"{i}But also, you felt like you belonged somewhere.{/i}" (multiple=2)

    death_drive"Yeah?" (multiple=2)
    inner_child"{color=#808080}{i}{cps=0}But also, you felt like you belonged somewhere.{/i}" (multiple=2)

    death_drive"{i}And where are those people now?{/i}" (multiple=2)
    inner_child"{color=#808080}{i}{cps=0}But also, you felt like you belonged somewhere.{/i}" (multiple=2)

    death_drive"{color=#808080}{i}{cps=0}And where are those people now?{/i}" (multiple=2)
    inner_child"{i}...they left.{/i}" (multiple=2)

    death_drive"Exactly." (multiple=2)
    inner_child"{color=#808080}{i}{cps=0}...they left.{/i}" (multiple=2)

    death_drive"A pleasant memory turned awry by dead romantics and sellout cynics." (multiple=2)
    inner_child"{color=#808080}{i}{cps=0}...they left.{/i}" (multiple=2)

    death_drive"That’s why we drink." (multiple=2)
    inner_child"{color=#808080}{i}{cps=0}...they left.{/i}" (multiple=2)

    death_drive"To escape the end of everything for just one evening." (multiple=2)
    inner_child"{color=#808080}{i}{cps=0}...they left.{/i}" (multiple=2)

    death_drive"{color=#808080}{cps=0}To escape the end of everything for just one evening." (multiple=2)
    inner_child"Only to wake up, remember, and do it all over again." (multiple=2)

    death_drive"Such is our sacrifice to this world: to die with your heart on your sleeve and to share a grave with the truth. She drinks to forget that this too will be her fate." (multiple=2)
    inner_child"{color=#808080}{cps=0}Only to wake up, remember, and do it all over again." (multiple=2)

    # [FLASH: KYEONG-AE]
    show bg darkness with flash
    show kyeongae happy
    pause (0.5)
    # [THEN BACK TO BLACK SCREEN]
    hide kyeongae happy
    show bg bar with blood


    death_drive"..." (multiple=2)
    inner_child"{color=#808080}{cps=0}Only to wake up, remember, and do it all over again." (multiple=2)

    death_drive"What I’m trying to say is that if she doesn’t die now, she’ll die of despair with a bottle in her hand- give her a year and the poison will do its work." (multiple=2)
    inner_child"{color=#808080}{cps=0}Only to wake up, remember, and do it all over again." (multiple=2)

    death_drive"Is that what you want? Do you want to confine us to that life of quiet desperation?" (multiple=2)
    inner_child"{color=#808080}{cps=0}Only to wake up, remember, and do it all over again." (multiple=2)

    stop sound fadeout 1.0
    show bg darkness with fade
    show jinsol outline

    death_drive"{color=#808080}{cps=0}Is that what you want? Do you want to confine us to that life of quiet desperation?" (multiple=2)
    inner_child"..." (multiple=2)
    
    jump part_2