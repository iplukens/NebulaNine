image JS neutral = "j_bust_neutral.png"
image JS happy = "j_bust_happy.png"
image JS angry = "j_bust_angry.png"
image bg e_cc = "e_CC_bg.png"

init:
    $ JS_relationship = 2
    $ JS_progress = 0

label JS_event:
    define JS = Character(_("James Stirspear"), color="#FFFFFF")
    scene bg e_cc
    call display_character_left pass ("angry")
    if JS_first == False and not mJS.atWar:
        show JS happy at right
        jump JS_first_meeting
    else:
        show JS neutral at right
        call JS_diplomacy

label JS_first_meeting:
    JS "It's been a long time, [c_name]."
    S "James."
    JS "Why so inhospitable?"
    S "If you recall, we were never the best of friends."
    JS "Why don't you just let bygones be bygones?"
    menu:
        "Try to make pleasant conversation.":
            jump JS_nice
        "Just get this over with.":
            jump JS_help
        "Tell him what you really think.":
            jump JS_rude
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 1)
            if num < 0.33:
                jump JS_nice
            elif num < 0.67:
                jump JS_help
            else:
                jump JS_rude
    return

label JS_nice:
    S "being nice"
    JS "whatever"
    return

label JS_rude:
    $ JS_relationship -= 1
    S "insult"
    JS "You know, that really hurts. I thought you would have grown up a bit since our school days, but you're just as hot-headed as ever."
    JS "Did you want something from me, or did you come here just to dredge up old grudges?"
    menu:
        "I'm just trying to save [l_name].":
            jump JS_help
        "I wasn't finished yet.":
            jump JS_rude_2
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 1)
            if num < 0.5:
                jump JS_help
            else:
                jump JS_rude_2
    return

label JS_rude_2:
    $ JS_relationship -= 1
    S "more insults"
    JS "Look, You're clearly trying to pick a fight, and I know I can't dissuade you from something once you've set your mind to it."
    S "You made the decision yourself, the day you decided to poison [l_name]!"
    call JS_war
    return

label JS_help:
    S "Look, I just want to save my [l_title] [l_name]. [l_cpronoun]'s terribly ill with Space Pox, and I'm not sure how long [l_pronoun] has to live without the Serum."
    JS "Sorry to hear it! I remember [l_name] from the Academy days. I always thought [l_pronoun] was kinda cute. Sorry I didn't show up to the wedding, by the way, but I do have a territory to run."
    S "You weren't invited."
    JS "Ah, but I've never been above a little wedding-crashing."
    menu:
        "But you aren't above assassination and kidnapping, apparently.":
            jump JS_suspicious

label JS_suspicious:
    S "It's interesting that [l_pronoun] contracted an Estellian disease, don't you think? One for which you hold the only cure."
    JS "I know what you're trying to imply, and I'm quite insulted."
    JS "If I were trying to assassinate your darling [l_title], I would have been a good deal more subtle. Despite what you may think, it is not my usual practice to go around starting quarrels."
    menu:
        "That's not how you were in the Space Academy.":
            jump JS_academy
    return

label JS_academy:
    S "That's not how I remember it. You were always tormenting me in school."
    JS "\"Tormenting\" is such a strong word. I like to think of it as‚Ä¶ \"building character.\""
    S "You switched my cocoa with space goose poo. Twice!"
    JS "We were kids! And come on, in hindsight, don't you think it was rather amusing?"
    S "For you and your group of friends, maybe. Pranks like that made my life miserable!"
    JS "Alright, alright, calm down."
    menu:
        "Sorry, I overreacted.":
            jump JS_apology
        "I will not!":
            jump JS_rude_2
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 1)
            if num < 0.5:
                jump JS_apology
            else:
                jump JS_rude_2
    return

label JS_apology:
    $JS_relationship += 1
    S "I'm sorry. I shouldn't get so upset."
    JS "No, it's understandable. I was a real brat, years ago."
    S "No, it's my fault. There's really no evidence that [l_name]'s sickness is your fault, and it would be quicker to get to the Serum with your cooperation."
    JS "I'm glad you're starting to see reason. I'm not sure I can trust you yet, but I might help you. I really was rather fond of [l_name], anyway."
    JS "We'll have to see."
    scene black
    with Dissolve(0.5)
    centered "Your relationship with Estelle has improved!"
    return

label JS_diplomacy:
    menu:
        "Give him something.":
            "give stuff"
            return
        "Talk.":
            "talk"
            return
        "Insult.":
            "insult"
            return
    return

label JS_war:
    S "We've never been close, but hurting my [l_title] was the last straw. There's no chance of peace between us - not now, not ever!"
    JS "If you feel that way, I suppose that's how it's going to be."
    scene black
    with Dissolve(0.5)
    centered "You are now at war with Estelle"
    $mJS.toWar()
    return