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
    $ CC_progress = 0
    $ CCTurnsTilWar = 3
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
    $ CCTurnsTilWar += 1
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
    S "Sorry, what?"
    call hide_corvida
    show corvida at right
    CC "Ah yes. I often forget that not all of those who reside under Her are blessed with the Sight to recognize Her presence. How tragic, do be unaware of one's own true Mother."
    S "..."
    CC "Was I rambling? I apologize. Perhaps I could interest you in a brief history of our Faith?"
    menu:
        "Sure.":
            jump CC_explanation_2
        "I have more important business to attend to.":
            jump CC_leave
        "That sounds boring, just get her to leave.":
            S "I'm sorry, I really must go."
            jump CC_intro_end

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
        CC "I believe I have left you much to think on. I am certain that we will meet again."
        S "It's been, uh, interesting."
    CC "I look forward to our future discussions. May the Nebula bring light to your path."
    $ CC_first = True
    "---End Diplomacy---"
    return

label CC_diplomacy:
    $ CCTurnsTilWar += 2
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
    $undeployedScoutCount = shipScoutCount - deployedScoutCount
    $undeployedFighterCount = shipFighterCount - deployedFighterCount
    $undeployedGeneratorCount = shipGeneratorCount - deployedGeneratorCount
    $undeployedDGeneratorCount = shipDGeneratorCount - deployedDGeneratorCount
    $undeployedEMPCount = shipEMPCount - deployedEMPCount
    $undeployedCommandCount = shipCommandCount - deployedCommandCount
#thing that allows selection of type and number
    $ CC_offer_num = 0
    $ CC_type_num = renpy.random.randint(0, 5)
    G "What type of ships do you wish to offer?"
    menu:
        "Fighter ships: [undeployedFighterCount] available":
            $CC_type_num = 0
        "Scout ships: [undeployedScoutCount] available":
            $CC_type_num = 1
        "Row shield ships: [undeployedGeneratorCount] available":
            $CC_type_num = 2
        "Shield ships: [undeployedDGeneratorCount] available":
            $CC_type_num = 3
        "EMP ships: [undeployedEMPCount] available":
            $CC_type_num = 4
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

    if CC_offer > 40:
        jump CC_bribe_super_success
    elif CC_offer > 15:
        jump CC_bribe_success
    else:
        jump CC_bribe_fail
    return

label bribe_no_ships:
    show corvida angry
    CC "Very funny.  Words are words.  Shinies are shinies.  And I want shinies.  Not words."
    hide corvida
    call hide_character("neutral")
    if not mCC.atWar:
        $mCC.toWar()
        centered "The Nebulists have declared war"
    return
    

label CC_bribe_super_success:
    "You offered [CC_offer_num] [CC_offer_type]!{p}Offer was [CC_offer]"
    $ CC_relationship += 3
    jump CC_bribe_finish

label CC_bribe_success:
    "You offered [CC_offer_num] [CC_offer_type]!{p}Offer was [CC_offer]"
    $ CC_relationship += 1
    jump CC_bribe_finish

label CC_bribe_fail:
    "You offered [CC_offer_num] [CC_offer_type]!{p}Offer was [CC_offer]"
    $ CC_relationship -= 2
    jump CC_bribe_finish

label CC_bribe_finish:
    if mCC.atWar == True and CC_relationship > 2:
        CC "Perhaps we could learn to see eye to eye."
        $mCC.makePeace()
        $ CC_war_anger = 0
    elif mCC.atWar == True and CC_relationship <= 2:
        CC "I will accept your gift, but it cannot compensate for the damage you have done to my people or our Mother."
        $ CC_relationship = 0
    elif mCC.atWar == False and CC_relationship >= 11:
        CC "Oh my!"
        CC "I sense that the Mother has approved your quest. I will allow you passage through our territory."
        $ CC_relationship = 1
        $ CC_progress += 1
        call CC_negotiation_end
    elif mCC.atWar == False and CC_offer >= 40:
        CC "What a wonderful donation to our cause! We will put these to use in defense of the Nebula at once."
    elif mCC.atWar == False and CC_offer >=15:
        CC "I suppose this will do."
    elif mCC.atWar == False and CC_offer >=10:
        CC "Is this really the best Dreamion has to offer?"
    elif mCC.atWar == False and CC_offer < 10:
        CC "Child, do you take me for a fool?"
        CC "This gift is hardly worthy of my time. I trust that you can do better."
    return

label CC_bribe_pendant:
    CC "{size=-10}It sparkles...{/size}"
    CC "Y-yes, I will take it."
    CC "{size=-10}So shiny...{/size}"
    if mCC.atWar == True:
        CC "Perhaps we could learn to see eye to eye."
        $mCC.makePeace()
        $ CC_war_anger = 0
        return
    else:
        CC "In exchange for the gift, I will share some of my resources with you."
        $ CC_progress += 1
        call CC_negotiation_end
    return

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
    G "Congratulations, [miperson], you have successfully allied with the Nebulists!"
    G "They have allowed you full access through their territories, and shared some of their ships with you."
    G "This is a great victory for Dreamion!"
    return

label CC_TimeLimitWar:
    scene bg n_cc
    show corvida angry
    CC "I have suspected all along that you were hatching a plot to destroy our Faith."
    CC "We will not tolerate fowl play. Did you think you could escape our notice by amassing your armies in secret?"
    hide corvida
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
        $ CC_war_anger += 1
        return