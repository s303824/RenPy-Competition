label part_4:

    death_drive"..." (multiple=2) with Dissolve(1.0)
    inner_child"..." (multiple=2) with Dissolve(1.0)

    death_drive"{color=#808080}..." (multiple=2)
    inner_child"{i}Kyeong-Ae was really special.{/i}" (multiple=2)

    death_drive"{color=#808080}..." (multiple=2)
    inner_child"{i}Working with her- sometimes you couldn’t drown the thought that your work mattered. You were wrapped up in her fervor.{/i}" (multiple=2)

    death_drive"{color=#808080}..." (multiple=2)
    inner_child"{i}And she was kind. She cared about you.{/i}" (multiple=2)

    death_drive"{i}She was a selfless knight. Someone to look up to.{/i}" (multiple=2)
    inner_child"{color=#808080}{i}And she was kind. She cared about you.{/i}" (multiple=2)

    death_drive"{i}A martyr for the truth...{/i}" (multiple=2)
    inner_child"{color=#808080}{i}And she was kind. She cared about you.{/i}" (multiple=2)

    death_drive"{i}We wanted her so painfully.{/i}" (multiple=2)
    inner_child"{color=#808080}{i}And she was kind. She cared about you.{/i}" (multiple=2)

    death_drive"{color=#808080}{i}We wanted her so painfully.{/i}" (multiple=2)
    inner_child"{i}To keep her safe.{/i}" (multiple=2)

    death_drive"{i}But who is anyone to keep her from her life’s work?{/i}" (multiple=2)
    inner_child"{color=#808080}{i}To keep her safe.{/i}" (multiple=2)

    death_drive"{color=#808080}{i}But who is anyone to keep her from her life’s work?{/i}" (multiple=2)
    inner_child"{i}We didn’t tell her about what we've been going through.{/i}" (multiple=2)

    death_drive"No." (multiple=2)
    inner_child"{color=#808080}{i}We didn’t tell her about what we've been going through.{/i}" (multiple=2)

    death_drive"{color=#808080}No." (multiple=2)
    inner_child"But I think Kyeong-Ae knew. She wasn’t completely sane either. Nobody in their right mind would beckon their own death like that." (multiple=2)

    death_drive"I guess not. The world got to her too." (multiple=2)
    inner_child"{color=#808080}But I think Kyeong-Ae knew. She wasn’t completely sane either. Nobody in their right mind would beckon their own death like that." (multiple=2)

    death_drive"{color=#808080}I guess not. The world got to her too." (multiple=2)
    inner_child"..." (multiple=2)

    death_drive"{color=#808080}I guess not. The world got to her too." (multiple=2)
    inner_child"It’s hard." (multiple=2)

    death_drive"{color=#808080}I guess not. The world got to her too." (multiple=2)
    inner_child"If they had switched places, I would like to think that Kyeong-Ae would have asked Jinsol to reconsider too." (multiple=2)
        
    death_drive"Maybe. I don’t know." (multiple=2)
    inner_child"{color=#808080}If they had switched places, I would like to think that Kyeong-Ae would have asked Jinsol to reconsider too." (multiple=2)

    death_drive"I don’t know what to think of her anymore. There was so much to do." (multiple=2)
    inner_child"{color=#808080}If they had switched places, I would like to think that Kyeong-Ae would have asked Jinsol to reconsider too." (multiple=2)

    death_drive"{color=#808080}I don’t know what to think of her anymore. There was so much to do." (multiple=2)
    inner_child"And so much to say." (multiple=2)

    menu:
        "Remember her valor.":
            death_drive"{i}Then do as much as you can before you burn out.{/i}" (multiple=2)
            inner_child"" (multiple=2)
            
            death_drive"{i}You still have some good work left in you.{/i}" (multiple=2)
            inner_child"" (multiple=2)

        "Remember her wish.":
            death_drive"" (multiple=2)
            inner_child"{i}Then take care of yourself.{/i}" (multiple=2)

            death_drive"" (multiple=2)
            inner_child"{i}Everyone is waiting with bated breath to hear what you have to say.{/i}" (multiple=2)


    death_drive"..." (multiple=2) with Dissolve(1.0)
    inner_child"..." (multiple=2) with Dissolve(1.0)

    death_drive"I still want that drink." (multiple=2)
    inner_child"{color=#808080}..." (multiple=2)

    death_drive"{color=#808080}I still want that drink." (multiple=2)
    inner_child"I know." (multiple=2)

    death_drive"..." (multiple=2)
    inner_child"..." (multiple=2)

    death_drive"{color=#808080}..." (multiple=2)
    inner_child"{i}Hey...{/i}" (multiple=2)

    death_drive"{color=#808080}..." (multiple=2)
    inner_child"{i}When you get out of here.{/i}" (multiple=2)

    death_drive"{color=#808080}..." (multiple=2)
    inner_child"{i}Take on her torch. Be the light that guides us from ruin.{/i}" (multiple=2)

    death_drive"{color=#808080}..." (multiple=2)
    inner_child"{i}Publish Kyeong-Ae’s exposé.{/i}" (multiple=2)

    death_drive"{color=#808080}..." (multiple=2)
    inner_child"{i}Keep a low profile and survive.{/i}" (multiple=2)

    death_drive"{color=#808080}..." (multiple=2)
    inner_child"{i}And just maybe there will come a day when you don’t need to drown yourself.{/i}" (multiple=2)

    death_drive"Heh, that’s awfully optimistic." (multiple=2)
    inner_child"{color=#808080}{i}And just maybe there will come a day when you don’t need to drown yourself.{/i}" (multiple=2)

    death_drive"{color=#808080}Heh, that’s awfully optimistic." (multiple=2)
    inner_child"Yeah, it is." (multiple=2)

    death_drive"Do you think she has enough energy to get up right now?" (multiple=2)
    inner_child"{color=#808080}Yeah, it is." (multiple=2)
    
    stop music
    protagonist"Quiet."
    # [BACKGROUND: PRINTING PRESS]
    scene bg printing room

    protagonist"You’re both so damn loud."

    protagonist"I’ve heard enough."

    protagonist"I know now what I must do."

    menu:
        "Pick up the briefcase":
            play sound "audio/door.mp3"
            show bg darkness with Fade(0.5, 1.0, 0.5)
            pause(2.0)
            return
        "Close your eyes again":
            return
    return