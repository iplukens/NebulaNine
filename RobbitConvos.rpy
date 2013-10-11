image bg b_cc = "b_CC_bg.png"
define RB = Character(_("ROBBIT"), color="#00ff00")

label RB_init_values:
    $RB_relationship = 0
    $RB_findPart = 0
    $RB_eye = True
    $RB_frog_leg = True
    $RB_webbed_foot = True
    $RB_frog_brain = True
    image RB angry = "r_bust_angry.png"
    image RB angry eye = "r_bust_angry_eye.png"
    image RB sad = "r_bust_sad.png"
    image RB sad eye = "r_bust_sad_eye.png"
    image RB neutral = "r_bust_neutral.png"
    image RB neutral eye = "r_bust_neutral_eye.png"
    return

label RB_event:
    scene bg b_cc
    show gaius neutral at Position(xpos = 95, xanchor=0, ypos=1.0, yanchor=500)
    call display_character_left pass ("neutral")
    if not RB_first:
        $RB_first = True
        call RB_init_values
        call RB_first_meeting
    else:
        call RB_progress
    return
    
label RB_war:
    scene bg b_cc
    call dcl("angry")
    if RB_eye:
        show RB angry eye at right
    else:
        show RB angry at right
    S "You've got a few screws loose! If you won't yield, I'll have to turn you to scrap!"
    RB "Now you've got me hopping mad! I'm going to make sure you croak now!"
    hide RB angry
    scene black
    with Dissolve(0.5)
    centered "---You are now at war with the Bureau of Transformers---"
    $mRB.toWar()
    return
    
label RB_first_meeting:
    G "I sent out the summons, [miperson].  ROBBIT should be arriving any minute."
    S "What kind of name is ROBBIT, anyway?"
    G "I've been led to believe he is a robotic amphibian, of sorts." 
    G "You shall see for yourself; here he comes now."
    show RB neutral at right
    RB "Hello there, fellows. I'm ROBBIT. What brings you to the Bureau of Transformers?"
    RB "Come now, speak up. Don't just stand there gaping like you've got a frog in your throat."
    menu:
        "We're trying to cure my [l_title]":
            call RB_1Concern
        "...":
            call RB_1Puns
        "Let the dreams decide.":
            $dream_count += 1
            $num = renpy.random.randint(0, 1)
            if num > 0.5:
                call RB_1Concern
            else:
                call RB_1Puns
    return

label RB_1Concern:
    S "We're trying to cure my [l_title]. [l_cpronoun] has fallen ill with Space Pox, and we must obtain the Space Serum from Estelle if [l_pronoun] is to survive."
    RB "Oh no! That is terrible."
    hide RB neutral
    show RB sad at right
    RB "I wish I could help you, but I'm a bit occupied myself..."
    S "We don't need much help, merely safe passage through your lands."
    hide RB sad
    show RB angry at right
    RB "I toad you, I'm a bit occupied! Now guards, prepare...BZZT."
    S "Woah, whats going on!"
    hide RB angry
    show RB sad at right
    RB "I'm very sorry about that. I appear to be malfunctioning. I assure you, I mean no offense."
    menu:
        "We understand. Can we do anything to help?":
            call RB_1Thankful
        "I'm sorry, we'll take our leave.":
            return
        "Let the dreams decide.":
            $dream_count += 1
            $num = renpy.random.randint(0, 1)
            if num > 0.5:
                call RB_1Thankful
    return
    
label RB_1Puns:
    S "..."
    hide RB neutral
    show RB sad at right
    RB "The last time people visited this neck of the pond they didn't speak much either."
    hide RB sad
    show RB angry at right
    RB "I'm sure we could have a more ribbiting conversation if I pull a few weapons on you."
    S "Are you completely mad!?!"
    RB "Quickly, my guards, I need you to...BZZZT"
    hide RB angry
    show RB sad at right
    RB "I'm so sorry about that. As of late I've been unable to control myself. I carrot believe it."
    menu:
        "We understand. Can we do anything to help?":
            call RB_1Thankful
        "\"Carrot\"? What kind of trick are you pulling here":
            call RB_1Anger
        "Let the dreams decide.":
            $dream_count += 1
            $num = renpy.random.randint(0, 1)
            if num > 0.5:
                call RB_1Thankful
            else:
                call RB_1Anger
    return
    
label RB_1Thankful:
    hide RB sad
    show RB neutral at right
    RB "If you happen upon my missing parts, bring them here. Maybe we can work out a deal."
    S "If that will help me save my [l_title], I guess I could try to help you out."
    RB "Thanks so much. I hop to see you again!"
    $RBTurnsTilWar = 4
    return
    
label RB_1Anger:
    hide RB sad
    show RB angry at right
    RB "That's it! I don't have to wart around here and listen to you guys taunt me!"
    RB "Remove them from my presence. We will right this wrong with war!"
    "---You are now at war with the Bureau of Transformers---"
    $mRB.toWar()
    return
    
label RB_1A:
    scene bg b_cc
    show gaius neutral at Position(xpos = 95, xanchor=0, ypos=1.0, yanchor=500)
    call display_character_left pass ("neutral")
    G "Are you prepared to see ROBBIT, [miperson]? He seems rather... unstable, to put it kindly."
    S "Gaius, you worry too much. He is in great need of our help. If we assist him, we have a chance of securing safe passage through his terrority and reaching Estelle before it's too late to save [l_name]."
    G "It is far too risky!"
    S "To save my love, no risk is too great."
    G "If you say so, [miperson]. All the same, be on your guard."
    G "Ah, ROBBIT approaches."
    show RB neutral at right
    RB "I had hopped to see you all again. Have you had any luck in tracking down my missing parts? It's not easy being half-blind and green."
    menu:
        "We found a robotic eye!" if RB_eye:
            call RB_1A_Success
        "Not yet.":
            call RB_1A_Failure
    return

label RB_1A_Success:
    S "Yes, we recently discovered this robotic eye."
    RB "Oh thank you! Ribbit. I'll take that."
    scene black
    with Dissolve(0.5)
    centered "A few moments later..."
    scene bg b_cc
    with Dissolve(0.5)
    show gaius neutral at Position(xpos = 95, xanchor=0, ypos=1.0, yanchor=500)
    call display_character_left pass ("happy")
    show RB neutral eye at right
    RB "How ribbiting! I can feel my senses coming back already."
    RB "As a show of faith, I'll divert some funds from a nearby star to give you guys a jump."
    hide RB neutral eye
    show RB angry eye at right
    RB "If you dare try to take advantage of this, I will be very unhoppy...BZZT"
    hide RB angry eye
    show RB sad eye at right
    RB "Oh no. I still appear to be malfunctioning. Try to find some more pieces and hop me out?"
    S "We shall try to hop - I mean help, you out. Thank you for aiding me in my quest."
    scene black
    with Dissolve(0.5)
    centered "You have improved your relationship with BoT"
    centered "In return for your aid, ROBBIT has granted you a star system."
    $RB_relationship += 1
    $territory.setOwner(mPlayer)
    $RBTurnsTilWar = 4
    return
    
label RB_1A_Failure:
    S "Not yet, I'm afraid."
    hide RB neutral
    show RB sad at right
    RB "That is truly disappointing. However, I don't believe I will croak anytime soon, so perhaps you can continue searching and return when you are successful."
    S "We will resume the search immediately. Finding a way to repair you is in both of our best interests."
    return
    
label RB_TimeLimitWar:
    ##TODO call this:
    scene bg b_cc
    show RB angry at right
    RB "It has been a while since I've heard from those vistors from Dreamion. I can't just wart around. They could be plotting something... I mustn't be caught off guard by croak and dagger."
    RB "That leaves me one choice, and only one choice. I must jump into the fray and strike them down before they come for me!"
    scene black
    with Dissolve(0.5)
    centered "---You are now at war with the Bureau of Transformers---"
    $mRB.toWar()
    return 

label RB_2A:
    scene bg b_cc
    show gaius neutral at Position(xpos = 95, xanchor=0, ypos=1.0, yanchor=500)
    call display_character_left pass ("neutral")
    show gaius neutral at Position(xpos = 95, xanchor=0, ypos=1.0, yanchor=500)
    G "ROBBIT appears to be on the mend. Hopefully we can continue full steam ahead."
    S "I have high hopes as well."
    G "ROBBIT is now arriving, [miperson]."
    show RB neutral eye at right
    RB "I had hopped to see you all again. Have you made any progress in the search for my missing parts? I really miss having both of my legs..."
    menu:
        "We have found a frog leg." if RB_frog_leg:
            call RB_2A_Success
        "No such luck.":
            call RB_1A_Failure
    return

label RB_2A_Success:
    S "Yes, we have found a frog leg!"
    RB "Oh thank you! I hop you guys didn't try to take a bite out of this. Haha."
    $RB_frog_leg = False
    scene black
    with Dissolve(0.5)
    centered "A few moments later..."
    scene bg b_cc
    with Dissolve(0.5)
    call display_character_left pass ("neutral")
    show gaius neutral at Position(xpos = 95, xanchor=0, ypos=1.0, yanchor=500)
    show RB neutral eye at right
    RB "I know I've toad you before, but I really appreciate this."
    RB "As a show of faith, I'll divert some funds from a nearby star to give you guys a leap."
    hide RB neutral eye
    show RB angry eye at right
    RB "Now hang on a tadpole. I'm get the feeling you are trying to exploit my situation for your own personal gain."
    RB "You guys keep bugging me and BZZT..."
    hide RB angry eye
    show RB sad eye at right
    RB "Please ignore that outburst. I am still incomplete."
    S "Have no fear. We will continue our search."
    scene black
    with Dissolve(0.5)
    centered "You have improved your relationship with BoT"
    centered "In return for your aid, ROBBIT has granted you a star system."
    $RB_relationship += 1
    $territory.setOwner(mPlayer)
    $RBTurnsTilWar = 4
    return

label RB_3A:
    scene bg b_cc
    show gaius neutral at Position(xpos = 95, xanchor=0, ypos=1.0, yanchor=500)
    call display_character_left pass ("neutral")
    G "This errand to repair ROBBIT is draining our resources. I think it might be faster to simply fight our way to Estelle."
    S "Gaius! What has gotten into you? ROBBIT is on the mend. At this point barely any of his screws are loose."
    G "I know, but every time we come here your life is put on the line. That erratic frog could leap at any moment."
    call CC_find_pendant
    scene bg b_cc
    show gaius neutral at Position(xpos = 95, xanchor=0, ypos=1.0, yanchor=500)
    call display_character_left pass ("neutral")
    G "Oh dear. Here he comes..."
    show RB neutral eye at right
    RB "Hello, my friends. I had hopped to see you all again. Have you had any luck in tracking down parts to aid me? The leg you gave me works great, but it's a bit unstable..."
    menu:
        "We have found a webbed foot." if RB_webbed_foot:
            call RB_3A_Success
        "Sadly, we have had no luck.":
            call RB_1A_Failure
    return

label RB_3A_Success:
    S "Yes, we tracked down this webbed foot!"
    RB "Oh, thank you! With this I am nearly complete."
    scene black
    with Dissolve(0.5)
    centered "A few moments later..."
    scene bg b_cc
    with Dissolve(0.5)
    show gaius neutral at Position(xpos = 95, xanchor=0, ypos=1.0, yanchor=500)
    call display_character_left pass ("neutral")
    show RB angry eye at right
    RB "Now you've done it! With this I can take a strike at you!"
    ### Character sliding animation should go here
    ### Possibly make the people frown here?
    S "Woah! I'm lucky I'm so quick - that could've ended poorly!"
    G "I told you! This frog is nothing more than an accident waiting to happen."
    menu:
        "Gaius is right, let's go!":
            call RB_3A_War
        "He'll calm down.":
            call RB_3A_Peace
    return


label RB_3A_Peace:
    S "We should wait, I'm sure he'll calm down soon."
    G "It's too dangerous! You may do as you please, but I won't foolishly risk my own life."
    hide gaius neutral
    $renpy.pause(0.5)
    S "ROBBIT, CALM DOWN!!!"
    RB "BZZT..."
    hide RB angry eye
    show RB sad eye at right
    RB "What happened? I lost control for a second and..."
    S "It's alright, you appear to be in control now."
    RB "That is true, but only a moment ago I tried to strike at Gaius, and you were caught in the middle..."
    RB "My memory banks appear to leap out of control whenever I see him, but I can't seem to remember why. I'm worried that my memory banks may have been tampered with..."
    S "What are you implying? Gaius is my most trusted advisor."
    RB "Listen, I am no amFIBian. Be careful."
    RB "Allow me to grant you another star system. Maybe then you'll trust me."
    scene black
    with Dissolve(0.5)
    centered "You have improved your relationship with BoT"
    centered "In return for your aid, ROBBIT has granted you a star system."
    $RB_relationship += 1
    $territory.setOwner(mPlayer)
    $RBTurnsTilWar = 4
    return
    
label RB_3A_War:
    hide RB angry eye
    S "Gaius, you're right, let's go!"
    G "I will rally the troops. A strike against you is a strike against all of Dreamion."
    scene black
    with Dissolve(0.5)
    centered "---You are now at war with the Bureau of Transformers---"
    $mRB.toWar()
    return
    
label RB_4A:
    scene bg b_cc
    call display_character_left pass ("neutral")
    S "ROBBIT, are you here?"
    show RB neutral eye at right
    RB "I had hopped to see you all again. Have you found my final part? Only my brain is missing now, and I would very much like to have it back..."
    menu:
        "Yes, I found it!" if RB_frog_brain:
            call RB_4A_Success
        "Sadly, we have had no luck.":
            call RB_1A_Failure
    return

label RB_4A_Success:
    S "Yes, I found it!"
    RB "Oh, thank you! I'm so hoppy I could jump for joy."
    S "You seem much calmer now that Gaius is missing."
    RB "I hadn't considered that. It might just be my new parts, you know."
    scene black
    with Dissolve(0.5)
    centered "A few moments later..."
    scene bg b_cc
    with Dissolve(0.5)
    call display_character_left pass ("neutral")
    show RB neutral eye at right
    RB "Ribbit Ribbit Ribbit. All systems seem to be fine."
    S "That's ribbiting - I mean, RIVETING news!{p}{size=-3}great, now I'M doing it.{/size}"
    RB "My memory banks are still fuzzy. Something foul seems to be hoppening."
    RB "Perhaps you can discover what it is. I'll give you the full support of BoT to help you out."
    scene black
    with Dissolve(0.5)
    centered "You have allied completely with BoT. Congrats!"
    centered "In return for your aid ROBBIT has granted you a star system."
    $RB_relationship += 1
    $territory.setOwner(mPlayer)
    return

###These events should be triggered at the start of a turn and will set flags for all the other events
### I will do them soon. The written concept should be final!
### Backgrounds for all of these should probably change too, not sure yet though

label RB_1A_Item:
    scene bg b_cc
    call display_character_left pass ("neutral")
    show gaius neutral at right
    S "What is this metal disc doing here?"
    G "It looks like some kind of eye. What could that be doing here?"
    S "I'm not sure. Let's hold onto it, just to be safe."
    $RB_eye = True
    return

label RB_2A_Item:
    scene bg d_cc
    call display_character_left pass ("neutral")
    show gaius neutral at right
    S "Gaius, when are we eating? I'm starving."
    G "The food should be here any moment now, [miperson]."
    S "I hope it gets here soon!"
    "Ring Ring Ring, Dinner!"
    S "Hang on chef, is there supposed to be something shiny in this?"
    if RB_first:
        G "Don't eat that, it looks like it could be ROBBIT's!"
        S "Oh wow, I think you're right!!"
    scene black
    with Dissolve(0.5)
    centered "You nearly broke your teeth trying to eat metal"
    centered "You have acquired a metal frog leg!"
    $RB_frog_leg = True
    return

label RB_3A_Item:
    scene bg b_cc
    call display_character_left pass ("neutral")
    show gaius neutral at right
    S "Ouch!"
    G "Are you okay, [miperson]?"
    S "I just stubbed my toe on something."
    S "Is that a foot?"
    if RB_first:
        G "It must belong to ROBBIT! Let's bring it to him."
    else:
        G "I believe so, your highness."
    scene black
    with Dissolve(0.5)
    centered "You got a webbed foot!"
    $RB_webbed_foot = True
    return

label RB_4A_Item:
    scene bg n_cc
    call display_character_left pass ("neutral")
    S "Ick! I think I just stepped on something squishy."
    S "This looks like... a brain?"
    if RB_first:
        S "This must belong to ROBBIT!"
        S "What is it doing in the Nebulist's star system, though? I don't think ROBBIT would have ventured here..."
    else:
        S "I guess I should hold onto it. Someone might be looking for this."
    scene black
    with Dissolve(0.5)
    centered "You got a frog brain!{p}‚Äö√Ñ¬∂gross"
    $RB_frog_brain = True
    return
    
label RB_progress:
    if RB_relationship == 0:
        call RB_1A
    elif RB_relationship == 1:
        call RB_2A
    elif RB_relationship == 2:
        call RB_3A
    elif RB_relationship == 3:
        call RB_4A
    return