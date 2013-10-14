image bg game_over = "game_over.png"
image bg fin = "fin.png"
image bg credits = "credits.png"
image bg palace = "d_palace.png"

label end_game:
    $ worstest = False
    if territories[17].owner == mPlayer:
        if not mAH.atWar and not mCC.atWar and not mRB.atWar and not mJS.atWar:
            call good_ending
        elif not mJS.atWar:
            call bad_ending
        else:
            call worst_ending
    if territories[0].owner != mPlayer:
        G "The capital has fallen, [miperson]!  It's all over!  I can't believe I put my faith in you."
        call game_over
    return

label check_defeated:
    $conquered_someone = False
    if not gaius_takeover:
        $string = "no one"
        if mAH.atWar and not has_territories(mAH) and not AH_conquered:
            $conquered_someone = True
            $string = "Masters of Space"
            scene bg m_cc
            call dcl("angry")
            show AH angry at right
            S "Any last words you pathetic Loser of Space?!"
            AH "None.  Just get it over with."
            S "Alright.  TASTE MY DREAM BEAM!!!"
            $AH_conquered = True
            play sound "longlaser.wav"
            show eyelasersleft
            show eyelasersright
            pause(1.0)
            hide eyelasersleft
            hide eyelasersright
            hide AH
            pause(0.5)
        elif mRB.atWar and not has_territories(mRB) and not RB_conquered:
            $conquered_someone = True
            $string = "BoTs"
            scene bg b_cc
            call dcl("angry")
            if RB_eye:
                show RB angry eye at right
            else:
                show RB angry at right
            S "Anything left to say you malfunctioning amphibian?"
            RB "Froggit about it!"
            S "Annoying until the end.  TASTE MY DREAM BEAM!!!"
            $RB_conquered = True
            play sound "longlaser.wav"
            show eyelasersleft
            show eyelasersright
            pause(1.0)
            hide eyelasersleft
            hide eyelasersright
            hide RB
            pause(0.5)
        elif mCC.atWar and not has_territories(mCC) and not CC_conquered:
            $conquered_someone = True
            $string = "Nebulists"
            scene bg n_cc
            call dcl("angry")
            show corvida angry at right
            S "Time to make me some fried chicken!"
            S "DREAM BEAM!!!"
            $CC_conquered = True
            play sound "longlaser.wav"
            show eyelasersleft
            show eyelasersright
            pause(1.0)
            hide eyelasersleft
            hide eyelasersright
            hide corvida
            pause(0.5)
        if conquered_someone:
            scene black
            with Dissolve(0.5)
            centered "--- You have succesfully conquered the [string] ---"
    return


    
label game_over:
    window hide None
    scene bg game_over
    with Dissolve(1.0)
    pause(8.0)
    while(True):
        scene black
        with Dissolve(0.5)
        centered "-- Either load game or start a new game --"
        
label good_ending:
    scene bg e_cc
    show gaius neutral at right
    S "GAIUS!  GAIUS WHERE ARE YOU!"
    call dcl("angry")
    S "Gaius!  Where's the Space Serum?"
    G "Eh, [miperson], calm down, I, I..."
    S "NOW GAIUS!"
    G "Here, here it is."
    centered "-- Got the Space Serum! --"
    S "Alright, now for you..."
    menu:
        "Spare him.":
            call best_ending
        "Kill him.":
            call kill_gaius
        "Let the dreams decide one last time.":
            call best_ending
    call over
    
label kill_gaius:
    S "Gaius..."
    G "Sir?"
    S "TASTE MY DREAM BEAM!!!"
    play sound "longlaser.wav"
    show eyelasersleft
    show eyelasersright
    pause(1.0)
    hide eyelasersleft
    hide eyelasersright
    hide gaius
    S "Now to attend to my love."
    call loved_betrayed
    
label best_ending:
    S "Gaius..."
    G "Yes, [miperson]?"
    S "I'm going to let you live."
    G "Really?  Thank you, [miperson].  THANK YOU!"
    G "I will be forever grateful."
    S "Say that after you've rotted in the dungeons a bit.  Friends, take him away!"
    hide gaius
    S "Now to attend to my love."
    call beginning_of_the_end
    call dcl("happy")
    S "By making new friends actually."
    S "The Masters of Space, the BoTs, the Nebulists... Even James Stirspear."
    S "The whole Nebula is now united."
    L "I can't believe it.  Incredible.  Oh, [c_name]..."
    S "My love..."
    call over
    
label beginning_of_the_end:
    scene bg palace
    call dcl("neutral")
    S "My love, drink this..."
    call hide_character("neutral")
    pause(1.0)
    call dcl("neutral")
    call dll("neutral")
    L "[c_name], I... What's going on?  Where am I?  What happened?"
    S "It's okay, my love.  You had Space Pox, but you're fine now.  I got you the Space Serum."
    L "Space Serum?  Space Pox?"
    L "That's on the whole other side of the Nebula!"
    S "And it was a long journey to get there, but for you... anything for you..."
    L "Oh, [c_name], you're so gallant!  But how did you do it?"
    return
    
label bad_ending:
    scene bg e_cc
    show gaius neutral at right
    S "GAIUS?!  GAIUS WHERE ARE YOU?!"
    call dcl("angry")
    S "Gaius!  Where's the Space Serum?"
    G "Eh, [miperson], calm down, I, I..."
    S "NOW GAIUS!"
    G "Here, here it is."
    centered "-- Got the Space Serum! --"
    S "Alright, now for you..."
    call kill_gaius
    call over
    
label loved_betrayed:
    call beginning_of_the_end
    call dcl("angry")
    S "Through the power of dreams and my DREAM BEAM."
    S "None could stand before my might!"
    #if not mAH.atWar and not mCC.atWar and not mRB.atWar and not mJS.atWar:
    if mAH.atWar:
        S "I took down those idiot ruffians the Masters of Space without a care."
    if mCC.atWar:
        S "I tarred and feathered those cuckoo relgious fanatics the Nebulists."
    if mRB.atWar:
        S "I short circuited those robotic BoTs freaks."
    if mJS.atWar:
        S "And I even took down my old nemesis James Stirspear and his stuffed up Estelle."
    else:
        S "And I even took out the treacherous Gaius!"
        L "Gaius was a traitor!?"
        S "Yes, but no matter.  He couldn't stand up to my DREAM BEAM either!"
    L "You... you're a monster!"
    call dll("angry")
    call dcl("neutral")
    S "What?"
    L "You conquered and killed across the entirety of Nebula Nine?!  Think of the millions you've killed!"
    S "It was actually [kill_count], but it was all for you!"
    L "For me?!?!"
    L "What makes you think I could ever love such a terrible, horrid creature!"
    call dcl("angry")
    S "Take that back.  Take it back!"
    L "NO! You're a monster!"
    S "TAKE IT BACK!"
    L "NO!"
    S "Then... TASTE MY DREAM BEAM!  RRRRRRAAAAGGGGGHHHHHHH!!!!"
    play sound "longlaser.wav"
    show eyelasersleft
    show eyelasersright
    pause(1.0)
    hide eyelasersleft
    hide eyelasersright
    if worstest:
        call hide_lcharacter("angry")
        show gaius happy at right
        G "And now it's my turn!"
        $ double_vision_on("bg palace")
        call hide_character("angry")
        S "But... but Gaius... why?"
        G "For control of the whole Nebula of course.  Now rest your eyes and go to sleep, [miperson]."
        S "Yes, Gaius... Dreams... I will Dreamion forver..."
        G "No, [miperson].  No more dreams for you.  Only nightmares."
        $double_vision_off()
    scene bg fin
    with fade
    centered "--- No more dreams now - only nightmares ---"
    pause(5.0)
    call over
    
label worst_ending:
    $ worstest = True
    scene bg e_cc
    show JS neutral at right
    S "JAMES?!  JAMES WHERE ARE YOU?!"
    call dcl("angry")
    S "JAMES!  Where's the Space Serum?"
    JS "Calm down, [c_name].  Here it is."
    centered "-- Got the Space Serum! --"
    S "Alright, now for you..."
    play sound "longlaser.wav"
    show eyelasersleft
    show eyelasersright
    pause(1.0)
    hide eyelasersleft
    hide eyelasersright
    S "And now to save my love!"
    call beginning_of_the_end
    call loved_betrayed
    jump over
    
label over:
    scene bg fin
    with Dissolve(1.0)
    centered "Thanks for playing!  You finished the game in [turn_count] cycles!  Try to beat that in more playthroughs and unlock all the endings!"
    scene bg credits
    with Dissolve(0.5)
    scene bg credits
    pause(5.0)