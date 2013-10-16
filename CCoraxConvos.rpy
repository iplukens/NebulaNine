image corvida = "c_bust_neutral.png"
image corvida happy = "c_bust_happy.png"
image corvida angry = "c_bust_angry.png"
image bg n_cc = "n_CC_bg.png"
image black = "#000000"

init:
    $ CC_relationship = 3
    $ CC_believer = False
    $ CC_knows_problem = False
    $ CC_pendant = False
    $ CC_offer = 0
    $ CC_offer_scaled = 0
    $ CC_progress = 0
    $ CCTurnsTilWar = 2
    $ CC_war_anger = 0
    $ CC_blasphemy_count = 0
    $ CC_negotiation_possible = True

label CC_start:
    define CC = Character(_("Corvida Corax"), color="#5dd5d5")
    scene bg n_cc
    call display_character_left pass ("neutral")
    if CC_first == False and not mCC.atWar:
        show corvida at right
        jump CC_first_meeting
    elif mCC.atWar:
        show corvida angry at right
        jump CC_war_chat
    else:
        show corvida at right
        jump CC_diplomacy
    return

label hide_corvida:
    hide corvida
    hide corvida happy
    hide corvida angry
    return

label CC_first_meeting:
    $ CCTurnsTilWar += 3
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
    call hide_character("neutral")
    call dcl("happy")
    S "Uh, yes, of course I am."
    call hide_corvida
    show corvida happy at right
    CC "Ah, indeed, I sensed you were one with the Mother."
    CC "It is always a pleasure to meet one of the Enlightened."
    $ CC_believer = True
    $ CC_relationship += 1
    jump CC_playitsafe

label CC_insult:
    $CC_blasphemy_count += 1
    call hide_character("neutral")
    call dcl("angry")
    S "I've never heard of such a thing. I am [c_name], [capital_title] of Dreamion, and I have no time for this foolishness."
    call hide_corvida
    show corvida angry at right
    $ CC_relationship -=3
    jump CC_what

label CC_explanation:
    S "I'm sorry, I don't know what that means."
    call hide_corvida
    show corvida happy at right
    CC "Oh! So you are among the unenlightened."
    CC "Perhaps I could interest you in a brief history of our Faith?"
    menu:
        "Sure.":
            jump CC_explanation_2
        "I have more important business to attend to.":
            jump CC_leave
        "That sounds boring, just get her to leave.":
            S "I'm sorry, I really must go."
            jump CC_intro_end
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 1)
            if num <= 0.33:
                jump CC_explanation_2
            elif num <= 0.67:
                jump CC_leave
            else:
                jump CC_intro_end
    return

label CC_explanation_2:
    call hide_corvida
    show corvida happy at right
    CC "We are all children of the Nebula, for she is our Mother. All that we have is given by Her, and it is my cawling to serve Her and spread Her Truth."
    call hide_corvida
    show corvida at right
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
    call hide_corvida
    show corvida at right
    if CC_believer == False:
        S "An intriguing idea. I shall think on it."
        CC "I trust that the Nebula will guide you to your true path. I sense that you have much potential."
        $ CC_relationship +=1
    else: 
        CC "But you appear greatly troubled. Tell me, my child, is there anything I can do for you?"
    jump CC_what

label CC_what:
    menu:
        "Tell her about your [l_title]." if CC_knows_problem == False:
            jump CC_help
        "Ask her for help." if CC_knows_problem == True:
            jump CC_help
        "Stop talking to the weird bird-lady.":
            jump CC_leave
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 1)
            if num > 0.5:
                jump CC_help
            else:
                jump CC_leave

label CC_leave:
    $ CC_relationship -= 1
    S "I have urgent business to attend to. I must be taking my leave."
    jump CC_intro_end

label CC_help:
    if CC_knows_problem == False:
        $ CC_knows_problem = True
        call hide_character("happy")
        call dcl("neutral")
        S "I am currently on a mission of great urgency. My [l_title] [l_name] has fallen gravely ill with Space Pox, and I fear that without the Space Serum [l_pronoun] will not survive much longer."
        CC "Do you require my assistance?"
        S "I need to reach Estelle, and to do so I must pass through your territory."
        CC "I see."
        if CC_relationship > 0:
            CC "[l_cpronoun_possessive] fate rests with the Mother. I shall aid you as I am able, for I am sworn to protect the Nebula and her children, but you must accept that your quest will succeed only if She wills it."
        else:
            CC "I have been entrusted with the protection of the Nebula."
            CC "I'm afraid that I cannot with good conscience offer aid to those who may seek to destroy Her or take advantage of Her resources."
        call CC_intro_end
    else:
        $CC_blasphemy_count += 1
        $CC_relationship = 0
        S "I have done my best to please you, but with every moment I waste my [l_title] grows weaker."
        S "I must reach Estelle before it is too late. Please, allow me to pass through your territories peacefully."
        call hide_corvida
        show corvida angry at right
        CC "Are you questioning the wisdom of the Mother? The Will of the Nebula Herself?"
        CC "My actions are guided not by my own choices, but by the One whom I serve!"
        menu:
            "Apologize as quickly as you can.":
                jump CC_apology
            "Give a gift and hope she calms down.":
                call CC_bribe
            "Go along with the Nebula stuff.":
                call CC_agreement
            "Let the dreams decide.":
                $ dream_count += 1
                $ num = renpy.random.randint(0, 1)
                if num <= 0.33:
                    jump CC_apology
                elif num <= 0.67:
                    jump CC_bribe
                else:
                    jump CC_agreement
return

label CC_apology:
    S "I meant no disrespect. I am merely concerned for the wellbeing of my [l_title]."
    CC "No earthly desires should be more important than the Mother Herself."
    CC "Your love may live, or [l_pronoun] may die. Accept that this is not in your power to control."
    S "I can't just watch [l_pronoun] waste away when I could have done something about it!"
    CC "It is not our place to question Fate! Our futures are decided for us. In fact, it has long been clear to me that [l_name] is doomed to die. You ought to accept [l_pronoun_possessive] passing with dignity."
    S "You've lost your mind, bird-brain!"
    call CC_war
    return

label CC_agreement:
    $CC_relationship = 2
    S "Of course, I respect the will of the nebula."
    S "My concern for my love drove me to foolishly lose my head. I meant no disrespect. It won't happen again."
    CC "For your sake, I hope not."
    CC "You come dangerously close to blasphemy, child. The Nebula is not always forgiving to those who disregard Her wisdom."
    if CC_first == False:
        call CC_intro_end
    return

label CC_intro_end:
    if CC_relationship == 0:
        jump CC_war
    if CC_believer == False:
        call hide_corvida
        show corvida at right
        CC "I believe I have left you much to think on. I am certain that we will meet again."
        S "It's been, uh, interesting."
    CC "I look forward to our future discussions. May the Nebula bring light to your path."
    $ CC_first = True
    return

label CC_diplomacy:
    $ CCTurnsTilWar += 3
    CC "Hello, child. What did you wish to speak about?"
    menu:
        "Give her something.":
            call CC_bribe
        "Ask about Nebulism.":
            jump CC_explanation_2
        "Ask for her help.":
            jump CC_help
        "Threaten.":
            jump CC_war_insult
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 1)
            if num <= 0.25:
                jump CC_bribe
            elif num <= 0.5:
                jump CC_explanation_2
            elif num <= 0.75:
                jump CC_help
            else:
                jump CC_war_insult
    return

label CC_bribe:
    S "I have a gift for you, in honor of the Nebula."
    call hide_corvida
    show corvida happy at right
    CC "Is it shiny?"
    call hide_corvida
    show corvida at right
    CC "...That is to say, what have you brought?"

    $undeployedScoutCount = shipScoutCount - deployedScoutCount
    $undeployedFighterCount = shipFighterCount - deployedFighterCount
    $undeployedGeneratorCount = shipGeneratorCount - deployedGeneratorCount
    $undeployedDGeneratorCount = shipDGeneratorCount - deployedDGeneratorCount
    $undeployedEMPCount = shipEMPCount - deployedEMPCount
    $undeployedCommandCount = shipCommandCount - deployedCommandCount
#thing that allows selection of type and number
    $ CC_offer_num = 0
    $ CC_type_num = renpy.random.randint(0, 5)
    menu:
        "Fighter ships: [undeployedFighterCount] available" if undeployedFighterCount > 0:
            $CC_type_num = 0
        "Scout ships: [undeployedScoutCount] available" if undeployedScoutCount > 0:
            $CC_type_num = 1
        "Row shield ships: [undeployedGeneratorCount] available" if undeployedGeneratorCount > 0:
            $CC_type_num = 2
        "Shield ships: [undeployedDGeneratorCount] available" if undeployedDGeneratorCount > 0:
            $CC_type_num = 3
        "EMP ships: [undeployedEMPCount] available" if undeployedEMPCount > 0:
            $CC_type_num = 4
        "The pendant necklace." if CC_pendant == True:
            jump CC_bribe_pendant
    if CC_type_num < 1:
        $ CC_offer_type = "Fighter Ships"
        python:
            CC_offer_num = renpy.input("How many fighter ships do you wish to give her?  You have [undeployedFighterCount] fighters to give.")
            CC_offer_num = CC_offer_num.strip()
            try:
                CC_offer = int(CC_offer_num)
            except:
                CC_offer = undeployedFighterCount + 10
        if CC_offer > undeployedFighterCount:
            jump bribe_no_ships
        else:
            $shipFighterCount -= CC_offer
            $CC_offer_scaled = CC_offer
    elif CC_type_num < 2:
        $ CC_offer_type = "Scout Ships"
        python:
            CC_offer_num = renpy.input("How many scout ships do you wish to give her?  You have [undeployedScoutCount] scouts to give.")
            CC_offer_num = CC_offer_num.strip()
            try:
                CC_offer = int(CC_offer_num)
            except:
                CC_offer = undeployedScoutCount + 10
        if CC_offer > undeployedScoutCount:
            jump bribe_no_ships
        else:
            $shipScoutCount -= CC_offer
            $CC_offer_scaled = CC_offer
    elif CC_type_num < 3:
        $ CC_offer_type = "Row Shield Ships"
        python:
            CC_offer_num = renpy.input("How many row shield ships do you wish to give her?  You have [undeployedGeneratorCount] ships to give.")
            CC_offer_num = CC_offer_num.strip()
            try:
                CC_offer = int(CC_offer_num)
            except:
                CC_offer = undeployedGeneratorCount + 10
        if CC_offer > undeployedGeneratorCount:
            jump bribe_no_ships
        else:
            $shipGeneratorCount -= CC_offer
            $CC_offer_scaled = CC_offer + 30
    elif CC_type_num < 4:
        $ CC_offer_type = "Shield Ships"
        python:
            CC_offer_num = renpy.input("How many shield ships do you wish to give her?  You have [undeployedDGeneratorCount] ships to give.")
            CC_offer_num = CC_offer_num.strip()
            try:
                CC_offer = int(CC_offer_num)
            except:
                CC_offer = undeployedDGeneratorCount + 10
        if CC_offer > undeployedDGeneratorCount:
            jump bribe_no_ships
        else:
            $shipDGeneratorCount -= CC_offer
            $CC_offer_scaled = CC_offer + 80
    elif CC_type_num < 5:
        $ CC_offer_type = "EMP Ships"
        python:
            CC_offer_num = renpy.input("How many emp ships do you wish to give her?  You have [undeployedEMPCount] emps to give.")
            CC_offer_num = CC_offer_num.strip()
            try:
                CC_offer = int(CC_offer_num)
            except:
                CC_offer = undeployedEMPCount + 10
        if CC_offer > undeployedEMPCount:
            jump bribe_no_ships
        else:
            $shipEMPCount -= CC_offer
            $CC_offer_scaled = CC_offer + 100
    call CC_bribe_finish
    return

label bribe_no_ships:
    call hide_corvida 
    show corvida angry at right
    CC "Very funny.  Words are words. Shinies are shinies. And I want shinies, not words."
    if not mCC.atWar:
        $mCC.toWar()
        scene black
        with Dissolve(0.5)
        centered "The Nebulists have declared war"
    return

label CC_bribe_finish:
    G "You offered [CC_offer_num] [CC_offer_type]!"
    if mCC.atWar == True and CC_offer_scaled >= 80:
        CC "Perhaps we could learn to see eye to eye."
        scene black
        with Dissolve(0.5)
        centered "The Nebulists have declared a truce"
        $mCC.makePeace()
        $ CC_war_anger = 0
        $ CCTurnsTilWar = 4
    elif mCC.atWar == True and CC_offer_scaled < 80:
        CC "I will accept your gift, but it cannot compensate for the damage you have done to my people or our Mother."
        $ CC_relationship = 0
        $ CC_war_anger -= 1
    elif CC_offer_scaled >= 140:
        CC "Oh my, what a generous donation! We will put these to use in defense of the Nebula at once."
        if CC_progress < 4:
            CC "Perhaps you are more trustworthy than I thought. I will allow you passage through our territory."
            scene black
            with Dissolve(0.5)
            centered "Your relationship with the Nebulists has improved!"
            centered "In return for your aid, the Nebulists have shared some of their resources."
            $ CC_relationship = 1
            $ CC_progress += 1
            call CC_negotiation_end

    elif CC_offer_scaled >= 120:
        CC "What lovely, shiny ships! We will put these to use in defense of the Nebula at once."
        if CC_progress < 3:
            $CC_progress += 1
            CC "Perhaps you are more trustworthy than I thought. I will allow you passage through our territory."
            scene black
            with Dissolve(0.5)
            centered "Your relationship with the Nebulists has improved!"
            centered "In return for your aid, the Nebulists have shared some of their resources."
            call CC_negotiation_end 
        else:
            centered "Your relationship with the Nebulists has improved!"

    elif CC_offer_scaled >=80:
        if CC_progress < 2:
            $CC_progress += 1
            CC "Perhaps you are more trustworthy than I thought. I will allow you passage through our territory."
            scene black
            with Dissolve(0.5)
            centered "Your relationship with the Nebulists has improved!"
            centered "In return for your aid, the Nebulists have shared some of their resources."
            call CC_negotiation_end
        else:
            CC "I suppose these will do."
            centered "Your relationship with the Nebulists has slightly improved!"

    elif CC_offer_scaled >=20:
        if CC_progress < 1:
            $CC_progress += 1
            CC "Perhaps you are more trustworthy than I thought. I will allow you passage through our territory."
            scene black
            with Dissolve(0.5)
            centered "Your relationship with the Nebulists has improved!"
            centered "In return for your aid, the Nebulists have shared some of their resources."
            call CC_negotiation_end
        else:
            CC "Is this really the best Dreamion has to offer?"
            scene black
            with Dissolve(0.5)
            centered "Your relationship with the Nebulists has not improved…"

    elif CC_offer_scaled < 20:
        CC "Child, do you take me for a fool?"
        CC "This gift is hardly worthy of my time. I trust that you can do better."
        if mCC.atWar == True:
            $ CC_war_anger += 1
        elif CC_relationship >= 2:
            $ CC_relationship -= 2
        elif CC_relationship > 0:
            $ CC_relationship = 0
        centered "Your relationship with the Nebulists has not improved..."
    return

label CC_bribe_pendant:
    $ CC_pendant = False
    call hide_corvida
    show corvida happy at right
    CC "{size=-10}It sparkles...{/size}"
    CC "Y-yes, I will take it."
    CC "{size=-10}So shiny...{/size}"
    if mCC.atWar == True:
        CC "Perhaps we could learn to see eye to eye."
        scene black
        with Dissolve(0.5)
        centered "The Nebulists have declared a truce!"
        $mCC.makePeace()
        $ CC_war_anger = 0
        return
    else:
        CC "In exchange for the gift, I will share some of my resources with you."
        scene black
        with Dissolve(0.5)
        centered "Your relationship with the Nebulists has improved!"
        centered "In return for your aid, the Nebulists have shared some of their resources."
        $ CC_progress += 1
        call CC_negotiation_end
    return

label CC_negotiation_end:
    $territory.setOwner(mPlayer)
    if CC_progress == 1:
        call CC_progress_1
    if CC_progress == 2:
        call CC_progress_2
    if CC_progress == 3:
        call CC_progress_3
    if CC_progress == 4:
        call CC_progress_4
    return

label CC_progress_1:
    return

label CC_progress_2:
    return

label CC_progress_3:
    return

label CC_progress_4:
    call CC_ally_success
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
    scene black
    with Dissolve(0.5)
    centered "You have successful allied with the Nebulists."
    centered "They have shared their resources in return for your aid."
    return

label CC_TimeLimitWar:
    if mCC.atWar == False:
        scene bg n_cc
        show corvida angry at right
        CC "Did you think you could escape our notice by amassing your armies in secret?"
        CC "I have suspected all along that you were hatching a plot to destroy our Faith. The Nebulists will not tolerate this sort of fowl play."
        scene black
        with Dissolve(0.5)
        $mCC.toWar()
        centered "The Nebulists have declared war"
    return

label CC_war:
    scene bg n_cc
    show corvida angry at right
    CC "I had hoped that Dreamion would come to understand the wisdom of the Nebula, but it has now become clear to me that you will never see the Truth."
    CC "We have nothing more to speak on."
    hide corvida angry
    scene black
    with Dissolve(0.5)
    $mCC.toWar()
    centered "The Nebulists have declared war"
    return

label CC_declare_war:
    scene bg n_cc
    call dcl("angry")
    show corvida at right
    S "I've had enough of your bird-brained religion. I can get through your territories faster by force!"
    call hide_corvida
    show corvida angry at right
    CC "So be it."
    $mCC.toWar()
    centered "You have declared war on the Nebulists"
    return

label CC_war_chat:
    scene bg n_cc
    show corvida angry at right
    if CC_war_anger <= 2:
        CC "What do you want?"
        menu:
            "Make a peace offering.":
                jump CC_bribe
            "Insult her.":
                jump CC_war_insult
            "Give up":
                return
    else:
        CC "You have shown your true colors. You have rejected your Mother, and in doing so you have sealed your fate."
        $CC_negotiation_possible = False
    return

label CC_war_insult:
    $num = renpy.random.randint(0, 3)
    if num < 1:
        S "You and your fowllowers are absolutely cracked."
    elif num >= 1 and num < 2:
        S "Your common sense flew the coop a long time ago, huh?"
    elif num >= 2:
        S "Something tells me your tweet is worse than your peck."
    call hide_corvida
    show corvida angry
    CC "You're making an EGGregious mistake. Such insolence will not be tolerated."
    S "Don't get your feathers all ruffled, beaky."
    $ CC_relationship = 0
    if mCC.atWar == False:
        $mCC.toWar()
        return
    elif mCC.atWar == True:
        $ CC_war_anger += 1
        return