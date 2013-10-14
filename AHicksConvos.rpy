image bg m_cc = "m_CC_bg.png"
define AH = Character(_("Alfred Hicks"), color="#ffa500")
image AH angry = "a_bust_angry.png"
image AH neutral = "a_bust_neutral.png"
image AH happy = "a_bust_happy.png"

label AH_init_values:
    $AH_relationship = 0
    $ship_count = 2
    $repetitions = 0
    return

label AH_event:
    $hicks_timeout = 0
    scene bg m_cc
    show gaius neutral at Position(xpos = 95, xanchor=0, ypos=1.0, yanchor=500)
    call display_character_left pass ("neutral")
    if not AH_first:
        $AH_first = True
        call AH_init_values
        call AH_first_meeting
    elif AH_relationship == 0:
        call AH_lukewarm
    else:
        call AH_progress
    return

label AH_first_meeting:
    G "I sent out the summons [miperson], and they've agreed to meet with us.  Ser Alfred Hicks should be here any moment."
    scene black
    with Dissolve(0.5)
    centered "30 minutes later"
    scene bg m_cc
    with Dissolve(0.5)
    show gaius neutral at Position(xpos = 95, xanchor=0, ypos=1.0, yanchor=500)
    call display_character_left pass ("neutral")
    S "Any moment, you said?"
    G "Any moment."
    call hide_character("neutral")
    call display_character_left("angry")
    S "Well, I will not be made to wait like some fool!  Get their ambassador on the line.  I demand an audience immediately!"
    G "No need, [miperson].  Here he is now."
    show AH happy at right
    AH "Ooo-wee! Just got done hunting some space goose.  Now, what's this 'urgent' business you been hollering about?"
    menu:
        "Rage at him for being late.":
            call AH_rage
        "Explain problems with [l_title].":
            call AH_rational
        "Let the dreams decide.":
            $dream_count += 1
            $num = renpy.random.randint(0, 1)
            if num > 0.5:
                call AH_rage
            else:
                call AH_rational
    return
        
label AH_rage:
    S "Space goose?  SPACE GOOSE?"
    S "You made me, the ruler of Dreamion, wait thirty minutes for space goose?  Do you have any idea of the gravity of this situation you uncultured buffoon!"
    hide AH happy
    show AH angry at right
    AH "Now hold up, little gally!  I ain't come here for you ta' be cond-sendin' me, ya'hear?  Ain't nobody speaks like dat to da Mastahs a' Space!"
    S "Masters of Space, ha!  You're the only ones who call yourselves that.  The rest of us have more accurate names for you!"
    AH "Best watch where ya' step, boyo.  Don't make me go all Psycho on ya'!"
    menu:
        "Bring it!":
            call AH_war
        "Hold up.  Let's calm down.":
            call AH_zero
        "Let the dreams decide.":
            $dream_count += 1
            $num = renpy.random.randint(0, 1)
            if num > 0.5:
                call AH_zero
            else:
                call AH_war
    return
                
label AH_war:
    scene bg m_cc
    call dcl("angry")
    show AH angry at right
    S "I step where I like, boyo!  I'm the Ruler of Dreamion, and don't you forget it!"
    AH "Yeah, we'll see how long that lasts.  You've disrespected me for the last time!"
    hide AH angry
    "---You are now at war with the Masters of Space---"
    $mAH.toWar()
    return
    
label AH_zero:
    call hide_character("angry")
    call display_character_left("neutral")
    S "Wait, wait.  Look... Tempers are fairly heated at the moment.  How about we resume this converstaion at a later date?"
    AH "What coversation?"
    S "I need to make my way through your territory to find the Space Serum and save my love!"
    AH "Sounds like alotta yer problem.  Count me out."
    hide AH angry
    G "That could've ended more poorly.  Perhaps the Masters of Space are too rash to see reason, [miperson]?  In which case, war might be our only option"
    S "Perhaps Gaius, perhaps."
    G "Just remember, all you do is for the one you love.  There is no dishonor in that."
    S "True, and what is more true is that I cannot let her die to the Space Pox."
    G "No, [miperson].  Such as disaster must be prevented at all costs."
    "---End Diplomacy - your relationship with the Masters of Space has not changed---"
    return
    
label AH_rational:
    call hide_character("angry")
    call display_character_left("neutral")
    S "I wish you had gotten here sooner;  this is a dire matter indeed.  My love is sick with Space Pox, and I must get to Estelle to secure the Space Serum."
    hide AH happy
    show AH neutral at right
    AH "Okay, but I don't see what that's gotta do wit' me."
    S "I need to move my fleet towards Estelle."
    AH "Yeah, and...?"
    S "And the only way to Estelle is through your realm, Ser Hicks.  I require passage through the Masters' of Space part of the nebula."
    hide AH neutral
    show AH angry at right
    AH "Oh, I see how it is.  Only call on ol' Alfred Hicks when you need a favor, huh?  Well, no one enters Masters a' Space terriotry 'ceptin the Masters a' Space, ya' unnerstan' dat?"
    menu:
        "I know the history, but I still need your help!":
            call AH_please
        "More like Losers of Space!":
            call AH_insult
        "Let the dreams decide.":
            $dream_count += 1
            $num = renpy.random.randint(0, 1)
            if num > 0.5:
                call AH_insult
            else:
                call AH_please
    return
                
label AH_insult:
    call hide_character("neutral")
    call display_character_left("angry")
    S "This is why everyone calls you the Losers of Space! A bunch of no good, uncultured fools, ALL OF YOU!  How about I give you a taste of my DREAM BEAM, huh?  How about I blaze a path straight through your territory with or without your permission!?"
    AH "Oh, is that how it's gonna be, boyo!?  Well, you'll be regrettin' the day ya' picked a fight with the Masters a' Space!"
    hide AH angry
    "---You are now at war with the Masters of Space---"
    $mAH.toWar()
    return
    
label AH_please:
    S "I know the history, but I still need your help!  Please, you have to understand what I must do for love.  I can't just sit idle and let my love die!"
    AH "Hmph, you got quite the sob story, but rules is rules.  Masters a' Space territory is for Masters a' Space."
    hide AH angry
    $AH_relationship += 1
    "---End Diplomacy - your relationship with the Masters of Space has increased!---"
    return

label AH_lukewarm:
    G "Here comes Sir Hicks, [miperson].  From my accounts he seems rather chilly towards you.  I would tread carefully but be sure to stay strong and not back down.  They are less civilized after all."
    S "Don't worry Gaius.  I know how to handle him."
    show AH neutral at right
    AH "Alright boyo.  I ain't got a lot o' time fer the likes o' you, so let's make this quick."
    S "Now listen here. I don't mean to be-"
    AH "No, no.  I do the talking.  Either you give me [ship_count] scout ships, or we're done with negotiatin'.  I've had enough o' yer lip, so now I need yer ships."
    G "Sir, I don't know if our fleet has the ships to spare..."
    menu:
        "Give him the ships." if ship_count < shipScoutCount:
            call AH_yes_ships
        "No can do.":
            call AH_no_ships
        "Let the dreams decide.":
            $dream_count += 1
            $num = renpy.random.randint(0, 1)
            if num > 0.5:
                call AH_no_ships
            else:
                call AH_yes_ships
    return

label AH_yes_ships:
    $AH_relationship += 1
    S "Nonsense Gaius.  We always have ships to spare for our friends the Masters of Space.  In fact, happy to do it."
    AH "Yeah, I'm sure you is.  Look forward to future negotiations."
    hide AH neutral
    $shipScoutCount -= ship_count
    $ship_count += 1
    G "Alright sir, but I don't know how much longer this can go on."
    S "I know, Gaius.  I know, and if it comes to that, it's all for my love..."
    return

label AH_no_ships:
    if ship_count > shipScoutCount:
        S "But I do not currently have that number of ships available!"
        AH "Well, then make it happen soon, or we're done boyo."
        hide AH neutral
        G "Unfortunate [miperson].  Perhaps you ought to upgrade the production capacity for scout ships in your territories?"
        S "Perhaps Gaius.  Perhaps"
    else:
        call hide_character("neutral")
        call dcl("angry")
        S "This is outrageous!  This is blackmail!  This is beneath me!  How did you ever expect me to acquiesce to this request!?"
        hide AH neutral
        show AH angry at right
        AH "Hey!  You're lucky I even came to this gosh darned meeting!  Ain't like me to talk to such rude fools such as yerself.  Don't 'spect any favors from the Mastahs a' Space now, y'hear?  We want nothing ta do withyas!"
        hide AH angry
        S "Well fine!  That's just fine!  I will blaze a path straight through your small hillbilly kingdom!  I AM THE RULER OF DREAMION AND-!"
        G "He's gone [miperson].  Perhaps it's best we make war preparations?"
        call hide_character("angry")
        call dcl("neutral")
        S "Right, yes.  Let's get on that."
        "---You are now at war with the Masters of Space---"
        $mAH.toWar()
    return

label AH_progress:
    if repetitions == 0:
        call AH_event_1a
    elif repetitions > 7:
        call AH_time_out_war
    elif AH_relationship == 1:
        call AH_event_1b
    elif AH_relationship == 2:
        call AH_event_2
    elif AH_relationship == 3:
        show AH happy at right
        AH "Well, boyo, gotta say I'm happy ta see you."
        S "Is that so, Sir Hicks?"
        AH "Yep.  You done right by me; that much is fursure, and I mean ta do right by you."
        AH "I pronounce you, an honorary Master a' Space!"
        call hide_character("neutral")
        call dcl("happy")
        S "Why, this is great news!"
        S "Er, what does it mean, exactly?"
        AH "What does it mean?  What does it mean?"
        AH "It means my territory is your territory.  Feel free to go gallavantin' on through and save that pretty [l_title] o' yours!"
        S "Thank, Sir Hicks!  Truly thank you!"
        scene black
        with Dissolve(0.5)
        centered "---Congratulations!  You successfully allied with the Masters of Space!---"
        python:
            for i in territories:
                if i.owner == mAH:
                    i.owner = mPlayer
    return
    
label AH_time_out_war:
    scene bg m_cc
    show AH angry
    AH "I don't know what you're playing at [c_boygirl], but I ain't got time to sit 'round and watch you toy with me an' plot my demise.  Consider us enemies."
    scene black
    with Dissolve(0.5)
    centered "---You are now at war with the Masters of Space!---"
    $mAH.toWar()
    return
    
label AH_event_1a:
    G "Here comes Alfred Hicks now, [miperson].  Remember what happened last time.  It's important to be charming and persuasive but also to use small words."
    S "That's rather rude, Gaius."
    G "Sorry, [miperson].  I meant no disrespect. The Masters of Space are honorable people."
    S "I meant the notion that I'd have to be reminded to be charming. I mean, really."
    G "Yes, of course."
    show AH neutral at right
    AH "Alright, I've come ta yer little meeting like ya' asked, but you know how I feel about all this lover [c_boygirl] business."
    S "Yes, and we have called another meeting in order to try and change your mind on the subject."
    AH "Okay, and...?"
    menu:
        "And nothing.":
            call AH_nothing
        "You have to understand how important this is to me!":
            call AH_personal
        "How can I convince you?":
            call AH_what_do_YOU_want
        "Let the dreams decide.":
            $dream_count += 1
            $num = renpy.random.randint(0, 2)
            if num == 0:
                call AH_nothing
            elif num == 1:
                call AH_personal
            else:
                call AH_what_do_YOU_want
    return
    
label AH_nothing:
    S "And?"
    S "And?"
    call hide_character("neutral")
    call dcl("angry")
    S "And NOTHING, YOU IDIOT!  I am the ruler of Dreamion, and you need to show me appropriate respect!  I do not grovel!  I do not ask where I can and cannot go!  I go there, and the people worship me as I pass through!"
    hide AH neutral
    show AH angry at right
    AH "Oh is that so?  Well excuuuuuse me, your high holiness, but you ain't no Mastah a' Space, so I don't gotta listen to none a' this!"
    AH "You Dreamion punks and your pretty little [l_title] can all go die o' Space Pox for all I care!"
    S "Yeah?! Not before we blaze your little star system to ashes!"
    hide AH angry
    G "That went well, [miperson].  Shall we prepare for war?"
    S "At once."
    scene black
    with Dissolve(0.5)
    centered "---You are now at war with the Masters of Space---"
    $mAH.toWar()
    return
    
label AH_personal:
    S "You have to understand!  [l_capital_title] [l_name] is the love of my life! I cannot possibly sit by and watch [l_pronoun] die."
    S "I must do everything in my power in order to save [l_pronoun]."
    AH "Yeah, some sob story, is it?  Some true love nonsense?  Well, it's as I said before.  The Mastahs a' Space don't change years a' tradition for some snot nosed punk."
    S "But [l_pronoun]'ll die if you don't let me through!"
    AH "[l_cpronoun] ain't my concern, [c_boygirl].  I protect me and my own, and [l_name] ain't no Mastah a' Space last I checked."
    menu:
        "How can you be so heartless?":
            call AH_sob_story_MORE
        "What if [l_pronoun] became a Master of Space?":
            call AH_become_one
        "You bastard!":
            call AH_bastard
        "Let the dreams decide.":
            $dream_count += 1
            $num = renpy.random.randint(0, 2)
            if num == 0:
                call AH_become_one
            elif num == 1:
                call AH_so_story_MORE
            else:
                call AH_bastard
    return
    
label AH_sob_story_MORE:
    S "How can you just let [l_pronoun] die? Have you no compassion?"
    AH "Like I says, I look out for me and mine first. You of all people should understand that. Now if you'll excuse me, I got work to do."
    hide AH neutral
    S "Damn. Cold as ice."
    G "It's seeming more and more unlikely that he'll let us through, [miperson]. Perhaps we should increase production on shield ships? The Masters of Space are not technologically advanced enough to make EMPs, you know."
    S "Of course I know that, Gaius. I just need to save my [l_title]!"
    G "Yes, and by any means necessary.  I know."
    scene black
    with Dissolve(0.5)
    centered "---End Diplomacy - your relationship with the Masters of Space has not changed.---"
    return
    
label AH_become_one:
    S "Not a Master of Space, huh? Well, what if... what if...?"
    AH "Yeah?"
    S "What if [l_pronoun] were to become a Master of Space?"
    hide AH neutral
    show AH angry at right
    AH "Oh that's how you want to play it, huh? Insults!?"
    AH "You think you can just become a Master of Space?"
    AH "Master of Space is in yer blood or it's not, and it ain't in you stupid Dreamion dreamers!"
    S "I didn't mean any offense!  I just wanted-!"
    AH "It don't matter what ya' just wanted!  It matters what ya' got, and you got yerself a war, boyo!"
    S "Wait, I-!"
    hide AH angry
    S "Damn, that backfired."
    G "Perhaps for the best, [miperson].  Let's prepare for war."
    scene black
    with Dissolve(0.5)
    centered "---You are now at war with the Masters of Space---"
    $mAH.toWar()
    return
    
label AH_bastard:
    S "You bastard! [l_cpronoun]'s dying!"
    AH "..."
    hide AH
    scene black
    with Dissolve(0.5)
    centered "---You are now at war with the Masters of Space---"
    $mAH.toWar()
    return
    
label AH_what_do_YOU_want:
    S "Look, I realize that Dreamion is only a small section of Nebula Nine, but we're willing to do anything you need.  Anything at all.  Can't you think of something we could help you with, so that you could let us through your territory?"
    AH "Hmmm... maybe."
    S "Yeah?"
    AH "Alright, I'll grant you passage through my territories dependin' on one thing."
    S "And that is?"
    AH "See, I actually been havin' some problems with another Masters of Space family headed by the nefarious Randolph McCoy.  See, they thinks they have rights to my territories whereas them being MY territories, I thinks otherwise."
    S "I see."
    AH "So here's how it's gonna be. You drive the McCoys outta them territories, and I let you have passage through it. Deal?"
    call AH_event_1
    return
    
label AH_event_1b:
    G "Alfred Hicks is on his way, [miperson].  Prepare yourself and your courtesies if you truly wish to ally with such people."
    S "I am always courteous, Gaius."
    G "As you say, [miperson]."
    show AH neutral at right
    AH "You ready to take on the nefarious McCoy?"
    call AH_event_1
    return

label AH_event_2:
    G "Here comes Sir Hicks as expected."
    show AH happy at right
    AH "Ah, if it isn't ma' fav'rite non-Masters of Space!"
    S "Hello, Sir Hicks."
    AH "Let's get down ta' bus'ness, right?"
    AH "You ready to cotinue yer fine work against the nefarious, evil Randolph McCoy?"
    call AH_event_1
    return
    
label AH_event_1:
    menu:
        "Let's do it.":
            call AH_attack_McCoy
        "Gaius, what do you know about Randolph McCoy?":
            call AH_rMcCoy
        "Not now.":
            call AH_refusal
        "Let the dreams decide.":
            $dream_count += 1
            $num = renpy.random.randint(0, 2)
            if num == 0:
                call AH_attack_McCoy
            elif num == 1:
                call AH_rMcCoy
            else:
                call AH_refusal
    return
    
label AH_attack_McCoy:
    S "To battle we go!"
    AH "Atta boy!  Let's get that rapscallion!"
    $mMcCoy = Owner("m", "orange", [Battalion("fighter",14),Battalion("emp",9),Battalion("emp",12),Battalion("emp",5),Battalion("fighter",1)], "{color=#ffffff}")
    $enemy = mMcCoy
    call allocationRoutine
    if territory.owner != mPlayer:
        $territory.setOwner(mAH)
        scene bg m_cc
        call dcl("neutral")
        show AH neutral at right
        AH "Well, that's a damn shame.  A damn shame."
        AH "I know you tried, but... Well, that's a damn shame.  I'll be takin' my leave now."
        hide AH neutral
        S "That bastard watched my troops get slaughtered over HIS territory, and that's all he can say?!"
        G "This setback ought not to be forgiven, [miperson].  Be careful how you proceed from here.  Your love's life hangs in the balance"
        scene black
        with Dissolve(0.5)
        centered "---End diplomacy - your relationship with the Masters of Space has not changed---"
    else:
        scene bg m_cc
        call dcl("neutral")
        show AH happy at right
        AH "A glorious victory!  Well done boyo! And as promised, you get access to the territory."
        S "No problem.  It was my pleasure to put the nefarious McCoy back in his place."
        scene black
        with Dissolve(0.5)
        centered "---End Diplomacy - your relationship with The Masters of Space has improved!---"
        $AH_relationship += 1
    $repetitions += 1
    return
    
label AH_rMcCoy:
    S "I have never heard of this McCoy before, Sir Hicks."
    S "How exactly is he nefarious?"
    AH "Oh, he is the worst kinda people. You don't wanna hang around th' likes a' him."
    S "How so?"
    AH "He fought for the Space Brigade during the Masters of Space Civil War.  I'm sure you studied that in one o' yer fancy schools, but anyway..."
    AH "He's a right bandit, sure 'nough.  He's been parading 'round the Nebula like he owns th' place takin' what ain't his."
    AH "Attacked my brother Tom Hicks without so much as the drop of a hat in a field too."
    S "A hat in a field?  Interesting..."
    S "Gaius, what do you know about Randolph McCoy?"
    G "Although our scouting is extensive, [miperson], I cannot say that we have heard of any of these 'nefarious deeds' to which Sir Alfred Hicks alludes."
    hide AH neutral
    show AH angry at right
    AH "You callin' me a liar?  That's an insult ta' my honor, I'll have ya' know."
    G "Just relaying information, sir.  I meant no insult."
    AH "And what's that 'sposed t' mean?"
    S "He was just saying-"
    AH "Nah, I know what he was just sayin', and I'll have none of it!  Consider the deal off, and don't 'cha dare show yer face in my side of the Nebula, ya' hear?!"
    hide AH angry
    G "A very tempermental fellow, isn't he?  I guess it can't be helped, [miperson]."
    S "We go to war."
    scene black
    with Dissolve(0.5)
    centered "---You are now at war with the Masters of Space!---"
    $mAH.toWar()
    return
    
label AH_refusal:
    S "Sadly I don't think my army is in fighting shape at the moment, but you have my word that I will take care of this McCoy person for you."
    AH "Eh, just 'cause I didn't have fancy schoolin' like you did, don't mean I ain't got plenty o' words already. I'll have yer ships, not your words, and that's a fact."
    S "My army isn't ready!  You will have my aid soon enough, I swear it!"
    AH "Uh-huh, don't be condscendin' me boyo. I ain't got the time."
    AH "I'll see myself out."
    hide AH neutral
    S "Drat, he sure is difficult to please."
    G "As always, [miperson], the Masters of Space are more trouble than they are worth.  Perhaps another course of action will be more productive?"
    S "War?"
    G "It pains me to say it, but with your [l_title]'s life on the line, there is little choice in the matter."
    S "We'll have to see, Gaius."
    S "We'll have to see..."
    scene black
    with Dissolve(0.5)
    centered "---End Diplomacy - your relationship with the Masters of Space has decreased!---"
    $AH_relationship -= 1
    return
    