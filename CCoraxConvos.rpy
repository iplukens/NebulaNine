image corvida = "c_bust_neutral.png"
image corvida happy = "c_bust_neutral.png"
image corvida angry = "c_bust_neutral.png"
image bg n_cc = "n_CC_bg.png"
image black = "#000000"

init:
    $ CC_relationship = 3
    $ CC_believer = False
    $ CC_pendant = False
    $ CC_offer = 0
    $ CC_progress = 0

label CC_start:
    define CC = Character(_("Corvida Corax"), color="#5dd5d5")
    scene bg n_cc
    call display_character_left pass ("neutral")
    if CC_first == False and not mCC.atWar:
        show corvida happy at right
        jump CC_first_meeting
    elif mCC.atWar:
        show corvida angry at right
        jump CC_war_chat
    else:
        show corvida at right
        jump CC_diplomacy

label CC_first_meeting:
    CC "Tell me, are you a child of the Nebula?"
    menu:
        "Just go with it.":
            jump CC_nebulist
        "What does that mean?":
            jump CC_explanation
        "I don't have time for this.":
            jump CC_insult
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 1)
            if num > 0.5:
                jump CC_nebulist
            else:
                jump CC_insult

label CC_nebulist:
    S "um‚Ä¶ Yes, of course I am."
    CC "Ah, yes. I sensed you were one with the Mother."
    CC "It is always a pleasure to meet one of the Enlightened."
    $ CC_believer = True
    $ CC_relationship += 1
    jump CC_playitsafe

label CC_insult:
    S "I've never heard of such a thing. I am [c_name], [capital_title] of Dreamion, and I have no time for this foolishness."
    $ CC_relationship -=3
    jump CC_what

label CC_explanation:
    S "I'm sorry, I don't know what that means."
    CC "Oh! So you are among the unenlightened."
    S "Sorry, what?"
    CC "Ah yes. I often forget that not all of those who reside under Her are blessed with the Sight to recognize Her presence."
    CC "How tragic, do be unaware of one's own true Mother."
    CC "I wonder, how do you live without Her guidance?"
    S "..."
    CC "Was I rambling again? I apologize. Perhaps I could interest you in a brief history of our Faith?"
    menu:
        "Sure.":
            jump CC_explanation_2
        "I have more important business to attend to.":
            jump CC_leave
        "That sounds boring, just get her to leave.":
            S "I'm sorry, I really must go."
            jump CC_intro_end

label CC_explanation_2:
    CC "We are all children of the Nebula, for she is our Mother. All that we have is given by Her, and it is my cawling to serve Her and spread Her Truth."
    menu:
        "That sounds ridiculous.":
            jump CC_insult
        "It would be best not to insult her.":
            jump CC_playitsafe
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 1)
            if num > 0.5:
                jump CC_insult
            else:
                jump CC_playitsafe

label CC_playitsafe:
    if CC_believer == False:
        S "An intriguing idea. I shall think on it."
        CC "I trust that the Nebula will guide you to your true path. I sense that you have much potential."
        $ CC_relationship +=1
    CC "But, you seem greatly troubled. Tell me, my child, is there anything I can do for you?"
    jump CC_what

label CC_what:
    menu:
        "Tell her about your [l_title].":
            jump CC_help
        "Stop talking to the crazy bird-lady.":
            jump CC_leave
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 1)
            if num > 0.5:
                jump CC_help
            else:
                jump CC_leave

label CC_leave:
    S "I should be getting back to my quest."
    jump CC_intro_end

label CC_help:
    S "I am currently on a mission of great urgency. My [l_title] [l_name] has fallen gravely ill with Space Pox, and I fear that without the Space Serum [l_pronoun] will not survive much longer."
    CC "Do you require my assistance?"
    S "I need to reach Estelle, and to do so I must pass through your territory."
    CC "I see."
    if CC_relationship > 0:
        CC "[l_cpronoun_possessive] fate rests with the Mother. I shall aid you as I am able, for I am sworn to protect the Nebula and her children, but you must accept that your quest will succeed only if She wills it."
    else:
        CC "I have been entrusted with the protection of the Nebula."
        CC "I'm afraid that I cannot with good conscience offer aid to those who may seek to destroy Her or take advantage of Her resources."
    jump CC_intro_end

label CC_intro_end:
    if CC_relationship == 0:
        jump CC_war
    if CC_believer == False:
        CC "I believe I have left you much to think on. I am certain that we will meet again."
        S "It's been, uh, interesting."
    CC "I look forward to our future discussions. May the Nebula bring light to your path."
    $ CC_first = True
    "---End Diplomacy---"
    return

label CC_diplomacy:
    CC "Hello, child. What did you wish to speak about?"
    menu:
        "Give her something.":
            call CC_bribe
        "Ask about Nebulism.":
            jump CC_explanation_2
        "Threaten.":
            jump CC_war_insult
    return

label CC_bribe:
    S "I have a gift for you, in honor of the Nebula."
    CC "Is it shiny?"
    CC "...That is to say, what have you brought?"
    menu:
        "Offer ships.":
            jump CC_bribe_ships
        "Offer the Pendant." if CC_pendant == True:
            jump CC_bribe_pendant
    return

label CC_bribe_ships:
#thing that allows selection of type and number
    $ CC_offer_num = renpy.random.randint(1, 240)
    $ CC_type_num = renpy.random.randint(0, 5)
    if CC_type_num < 1:
        $ CC_offer_type = "Fighter Ships"
        $ CC_offer = CC_offer_num
    elif CC_type_num < 2:
        $ CC_offer_type = "Scout Ships"
        $ CC_offer = CC_offer_num
    elif CC_type_num < 3:
        $ CC_offer_type = "Row Shield Ships"
        $ CC_offer = (CC_offer_num * 2)
    elif CC_type_num < 4:
        $ CC_offer_type = "Shield Ships"
        $ CC_offer = (CC_offer_num * 3)
    elif CC_type_num < 5:
        $ CC_offer_type = "EMP Ships"
        $ CC_offer = (CC_offer_num * 4)

    if CC_offer > 300:
        jump CC_bribe_super_success
    elif CC_offer > 100:
        jump CC_bribe_success
    else:
        jump CC_bribe_fail

label CC_bribe_super_success:
    "You offered [CC_offer_num] [CC_offer_type]!{p}Offer was [CC_offer]"
    $ CC_relationship += 4
    jump CC_bribe_finish

label CC_bribe_success:
    "You offered [CC_offer_num] [CC_offer_type]!{p}Offer was [CC_offer]"
    $ CC_relationship += 2
    jump CC_bribe_finish

label CC_bribe_fail:
    "You offered [CC_offer_num] [CC_offer_type]!{p}Offer was [CC_offer]"
    $ CC_relationship += 1
    jump CC_bribe_finish

label CC_bribe_finish:
    if mCC.atWar == True and CC_relationship > 2:
        CC "Perhaps we could learn to see eye to eye."
        $mCC.makePeace()
        jump CC_relationship_check
    elif mCC.atWar == True and CC_relationship <= 2:
        CC "I will accept your gift, but it cannot compensate for the damage you have done to my people or our Mother."
        $ CC_relationship = 0
        jump CC_relationship_check
    elif mCC.atWar == False and CC_relationship >= 11:
        CC "Oh my!"
        CC "I sense that the Mother has approved your quest. I will allow you passage through our territory."
        $ CC_relationship = 1
        $ CC_progress += 1
        call CC_negotiation_end
    elif mCC.atWar == False and CC_offer >= 200:
        CC "excellent!"
    elif mCC.atWar == False and CC_offer >=100:
        CC "okay."
    elif mCC.atWar == False and CC_offer >=20:
        CC "not very impressive."
    elif mCC.atWar == False and CC_offer < 20:
        CC "insignificant."
    call CC_relationship_check
    return

label CC_bribe_pendant:
    CC "{size=-3}It sparkles‚Ä¶{/size}"
    CC "Y-yes, I will take it."
    CC "{size=-3}So shiny‚Ä¶{/size}"
    if mCC.atWar == True:
        CC "Perhaps we could learn to see eye to eye."
        $mCC.makePeace()
        return
    else:
        CC "In exchange for the gift, I will share some of my resources with you."
        $ CC_progress += 1
        call CC_negotiation_end

label CC_negotiation_end:
    $territory.setOwner(mPlayer)
    if CC_progress == 1:
        $ CC_relationship = 5
        call CC_progress_1
    if CC_progress == 2:
        $ CC_relationship = 3
        call CC_progress_2
    if CC_progress == 3:
        $ CC_relationship = 1
        call CC_progress_3
    if CC_progress == 4:
        $ CC_relationship = 1
        call CC_progress_4
    return

label CC_progress_1:
    "CC event 1"
    scene black
    with Dissolve(0.5)
    jump RB_4A_Item
    return

label CC_progress_2:
    "CC event 2"
    return

label CC_progress_3:
    "CC event 3"
    return

label CC_progress_4:
    "CC event 4"
    return

label CC_relationship_check:
    "---Relationship is at [CC_relationship]---"
    return

label CC_find_pendant:
    S "Wait, I think there's something shiny in the corner there..."
    menu:
        "Investigate":
            scene black
            with Dissolve(0.5)
            centered "You found a shiny pendant necklace!"
            $ CC_pendant = True
            return
        "Leave it.":
            return

label CC_ally_success:
    G "Congratulations, [miperson], you have successfully allied with the Nebulists!"
    G "They have allowed you full access through their territories, and shared some of their ships with you."
    G "This is a great victory for Dreamion!"
    return

label CC_TimeLimitWar:
    CC "I have suspected all along that you were hatching a plot to destroy our Faith."
    CC "We will not tolerate fowl play. Did you think you could escape our notice by amassing your armies in secret?"
    $mCC.toWar()
    centered "The Nebulists have declared war"
    return

label CC_war:
    scene bg n_cc
    show corvida angry at right
    CC "It is clear to me that you will never see the Truth. Those who walk in blindness pose a great danger to those who would walk in the light."
    CC "We have nothing more to speak on."
    hide corvida angry
    $mCC.toWar()
    centered "The Nebulists have declared war"
    return

label CC_declare_war:
    scene bg n_cc
    call dcl("angry")
    show corvida at right
    S "blah blah fight me"
    CC "fine"
    $mCC.toWar()
    centered "You have declared war on the Nebulists"
    return

label CC_war_chat:
    scene bg n_cc
    show corvida angry
    CC "What do you want?"
    menu:
        "Make a peace offering.":
            jump CC_bribe
        "Insult her.":
            jump CC_war_insult
        "Give up":
            return

label CC_war_insult:
    $num = renpy.random.randint(0, 4)
    if num < 1:
        S "You and your fowllowers are absolutely cracked."
    elif num >= 1 and num < 2:
        S "Your common sense flew the coop a long time ago, huh?"
    elif num >= 2 and num < 3:
        S "Something tells me your tweet is worse than your peck."
    elif num >= 3:
        S "insult4"
    hide corvida
    hide corvida happy
    show corvida angry
    CC "You're making an EGGregious mistake. Such insolence will not be tolerated."
    S "Don't get your feathers all ruffled, beaky."
    $ CC_relationship = 0
    if mCC.atWar == False:
        $mCC.toWar()
        return
    elif mCC.atWar == True:
        return