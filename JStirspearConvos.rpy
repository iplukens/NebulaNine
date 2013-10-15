image JS neutral = "j_bust_neutral.png"
image JS happy = "j_bust_happy.png"
image JS angry = "j_bust_angry.png"
image bg e_cc = "e_CC_bg.png"

init:
    $ JS_relationship = 2
    $ JS_progress = 0
    $ JS_suspicion = False
    $ JS_weak = False

label JS_event:
    $JS_Timeout += 1
    define JS = Character(_("James Stirspear"), color="#ff0000")
    scene bg e_cc
    if JS_first == False and not mJS.atWar:
        call dcl("angry")
        $JS_first = True
        show JS happy at right
        call JS_first_meeting
    else:
        if JS_relationship < 3:
            call dcl("angry")
        else:
            call dcl("neutral")
        show JS happy at right
        call JS_diplomacy
    return

label JS_first_meeting:
    S "Hello, James."
    JS "Ah, [c_name]! It's been a long time since I've seen you around. Why all the guards?"
    S "If you recall, we were never the best of friends."
    JS "Why don't you just let bygones be bygones?"
    menu:
        "Try to make pleasant conversation.":
            call JS_nice
        "Just get this over with.":
            call JS_help
        "Tell him what you really think.":
            call JS_rude
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 3)
            if num < 0:
                call JS_nice
            elif num < 1:
                call JS_help
            else:
                call JS_rude
    return

label JS_nice:
    call dcl("neutral")
    S "Oh, I have no problem letting bygones be bygones.  The Space Academy is behind me now, and I have bigger issues now than our adolescent squabbles."
    JS "Bigger issues, hmmm?  So I've heard."
    S "So you know about [l_name]?"
    JS "Please, [c_name].  You don't become the king of the Nebula unless you pay a little attention to your underlings."
    S "No one calls you the king of the Nebula."
    JS "Their mistake."
    menu:
        "Ignore his arrogance.":
            call JS_help
        "Take this guy down a peg.":
            call JS_outrage
        "Assert your dominance.":
            call JS_strong
        "Let the dreams decide.":
            $dream_count += 1
            $ num = renpy.random.randint(0, 3)
            if num < 0:
                call JS_help
            elif num < 1:
                call JS_outrage
            else:
                call JS_strong
    return

label JS_outrage:
    S "King? King of the Nebula? Are you high off space rocks?"
    JS "ROCK AND ROLL, YOU KNOW ME!"
    S "What?!"
    JS "YEAH! WOOOOOO!"
    S "James, this is absolutely ridiculous!"
    call JS_war
    return

label JS_strong:
    $ JS_relationship -= 1
    S "No, your mistake.  I control more of Nebula Nine than any other leader, including both of your neighbors. You'd best respect me and my wishes."
    JS "And I meant to congratulate you on that.  You've had quite the conquest - I'm sure you plan to take my territories now, right?"
    S "That's not what I meant."
    JS "But that's what you implied."
    S "Not at all."
    JS "Oh, really? Then suppose I don't give you the Space Serum that you require.  What then, [c_name]?"
    S "How did you know-?"
    JS "Answer the question."
    menu:
        "Then I'll pry it from your cold, dead fingers.":
            call JS_take_it
        "You wouldn't do that.":
            call JS_empathy
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 2)
            if num < 1:
                call JS_take_it
            else:
                call JS_empathy
    return

label JS_empathy:
    $ JS_relationship += 1
    S "You wouldn't do that.  You loved [l_pronoun2] as much as I did once!"
    JS "That may be true, but perhaps the slight [l_pronoun] gave me years ago of choosing a fool like you over me has hardened my heart."
    S "Perhaps that is possible, but I don't believe it's true."
    JS "Believe what you want.  Estelle's ports remain closed."
    call JS_help
    return

label JS_take_it:
    S "Then I suppose I would simply crush you with my army and take the serum by force."
    JS "For some reason, that's what I thought you'd say."
    S "I know you're responsible for what happened, James, and I'm going to make you pay."
    JS "You foolishness pains me, but I can see you've made up your mind."
    call JS_war
    return

label JS_rude:
    $ JS_relationship -= 1
    S "As if you let bygones be bygones.  You never got over me getting [l_name]'s hand in the end, did you?"
    JS "I don't know what you're trying to insinuate there, [c_name].  I hold no hatred for you, and in fact, consider you a dear friend."
    JS "Now, did you want something from me, or did you come here just to dredge up old grudges?"
    menu:
        "I'm just trying to save [l_name].":
            call JS_help
        "I wasn't finished yet.":
            call JS_rude_2
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 2)
            if num < 1:
                call JS_help
            else:
                call JS_rude_2
    return

label JS_rude_2:
    $ JS_relationship -= 1
    S "Old grudges?  How about new felonies?"
    JS "Excuse me, [c_name]?"
    S "You poisoned [l_name]!  I know you did!  They were Estellian ships that took her away!"
    JS "You know, that really hurts. I thought you would have grown up a bit since our school days, but you're just as hot-headed as ever."
    S "And you're just as treacherous and heartless!"
    JS "Look, you're clearly trying to pick a fight, and I know I can't dissuade you from something once you've set your mind to it."
    S "You made the decision yourself, the day you decided to poison [l_name]!"
    call JS_war
    return

label JS_help:
    S "Look, I just want to save my [l_title] [l_name]. [l_cpronoun]'s terribly ill with Space Pox, and I'm not sure how long [l_pronoun] has to live without the Serum."
    JS "Sorry to hear it! I remember [l_name] from the Academy days. I always thought [l_pronoun] was kinda cute. Sorry I didn't show up to the wedding, by the way, but I do have a territory to run."
    S "You weren't invited."
    JS "Ah, but I've never been above a little wedding crashing."
    menu:
        "But are you above assassination and kidnapping...?":
            call JS_suspicious
        "We would've shot you on sight.":
            call JS_shoot
        "I crashed a wedding once.":
            call JS_anecdote
    return

label JS_anecdote:
    S "You know, I remember when your cousin, Terrence Shakesglaive, got married.  It was quite a party."
    JS "You were invited to that?"
    S "Not exactly. I snuck in inside the cake and popped out during the reception. Your aunt had a heart attack, if I remember correctly."
    JS "What are you talking about?"
    S "Your cousin Terrence's wedding.  There was an open bar.  I must have had about six jack and cokes before we even popped the champagne."
    JS "Are you trying to confuse me, [c_name]? You should know it won't work. I like to play two or three steps ahead."
    S "I could tell that from the way you danced at the wedding."
    hide JS
    show JS angry at right
    pause(0.5)
    show JS happy at right
    JS "Good one, [c_name].  I've always had two left feet.  Of course, I have two right ones as well."
    S "Anyway, it's always nice to catch up, James.  Quick question though."
    JS "Yes?"
    S "You have any Space Serum lying around?"
    JS "Not a drop."
    S "This whole situation seems a bit fishy."
    call JS_suspicious
    return

label JS_shoot:
    $ JS_relationship += 1
    S "I would've dream beamed you on sight."
    JS "Sounds like quite the slumber party."
    S "I wasn't joking."
    JS "I was simply hoping to keep it light.  You know how we Estellians have such weak backs."
    S "Huh?"
    JS "Quick as ever, eh [c_name]?"
    menu:
        "No, that was just stupid.":
            call JS_ugh
        "Why did you start talking about your back?":
            call JS_confused
        "Let's move on...":
            call JS_suspicious
    return

label JS_ugh:
    $ JS_relationship += 1
    S "Apparently Estellians have weak backs, and an even weaker grasp on humour."
    JS "Fair enough - although I was hoping we wouldn't resort to insults on our first meeting in so many years."
    S "I'm sorry, but didn't you just imply that I was thick?"
    JS "But aren't you?"
    S "Not in the head."
    JS "I jest, [c_name]. I jest. You are, as ever, my equal.  Now, what are you here about?"
    S "I told you, my [l_title]."
    JS "Ah, yes, well, I'll have to give that whole issue another look. But for now, it seems my martini has run dry - and not in the way I like."
    JS "I bid you farewell."
    S "Wait, but-"
    hide JS
    S "Damn. Guess I'll have to wait another cycle."
    G "Time permitting.  Your love grows more ill every day."
    scene black
    with Dissolve(0.5)
    centered "Your relationship with Estelle has improved!"
    return

label JS_confused:
    $ JS_relationship -= 1
    S "What? Why are you talking about your back?  What does that have to do with anything?"
    JS "..."
    S "James, what's going on?  You better watch your back if you don't tell me what's going on!"
    JS "You're serious?"
    S "Yes!"
    JS "I was simply joking that if I did not keep the conversation light, it would be heavy, and heavy things would be a problem for someone with a weak back."
    S "That doesn't make any sense.  Conversations can't hurt people's backs!"
    JS "You're sharp as ever, I'm afraid.  Remind me to call you back here if I ever need a new paper weight or to hammer in a nail."
    menu:
        "I will not stand for these insults!":
            call JS_war
        "Fair enough.":
            call JS_me_dumb
    return

label JS_me_dumb:
    S "Fair enough."
    JS "I must be off.  I think I could use a few dozen more martinis before your presence becomes tolerable again."
    scene black
    with Dissolve(0.5)
    centered "Your relationship with Estelle has decreased!"
    return

label JS_suspicious:
    $ JS_suspicion = True
    S "It's rather unusual for a citizen of Dreamion to contract an Estellian disease, don't you think? Especially a rare sickness for which you hold the only cure."
    JS "I know what you're trying to imply, and I'm quite insulted."
    JS "If I were trying to assassinate your darling [l_title], I would have been a good deal subtler. Despite what you may think, it is not my usual practice to go around starting quarrels."
    S "That's not how I remember it. You were always tormenting me in school."
    JS "\"Tormenting\" is such a strong word. I like to think of it as‚ \"building character.\""
    S "You switched my cocoa with space goose poo. Twice!"
    JS "We were kids! And come on, in hindsight, don't you think it was rather amusing?"
    S "For you and your group of friends, maybe. Pranks like that made my life miserable!"
    JS "Alright, alright, calm down. No need to bring up these old grudges."
    menu:
        "Sorry, I overreacted.":
            call JS_apology
        "I will not!":
            call JS_rude_2
        "Let the dreams decide.":
            $ dream_count += 1
            $ num = renpy.random.randint(0, 2)
            if num < 1:
                call JS_apology
            else:
                call JS_rude_2
    return

label JS_apology:
    $JS_relationship += 1
    S "I'm sorry. I shouldn't get so upset."
    JS "No, it's understandable. I was a real brat, years ago."
    S "It's really my fault. There's no evidence that [l_name]'s sickness was due to your interference, and it would be quicker to get to the Serum with your cooperation."
    JS "I'm glad you're starting to see reason. I'm not sure I can trust you yet, but I might help you. I really was rather fond of [l_name], anyway."
    JS "We'll have to see."
    scene black
    with Dissolve(0.5)
    centered "Your relationship with Estelle has improved!"
    return

label JS_diplomacy:
    menu:
        "Offer ships.":
            call JS_offer
        "Talk.":
            $JS_progress += 1
            if JS_progress == 1:
                call JS_talk_one
            elif JS_progress == 2:
                call JS_talk_two
            elif JS_progress == 3:
                call JS_talk_three
            return
        "Insult.":
            call JS_insult_rand
            return
    return
        
label JS_insult_rand:
    call dcl("angry")
    $ num = renpy.random.randint(0, 5)
    $ war_stuff_JS = False
    $ JS_relationship -= 1
    if JS_relationship == 0:
        $ war_stuff_JS = True
        call JS_war
    elif num < 1:
        S "You know, you have too many arms.  Who even has that many arms?  No one.  It's stupid.  You're stupid."
        JS "Thank you, [c_name].  I'll be sure to keep that in mind.  Anything else?"
        S "Uh... you suck."
        JS "See you later, [c_name]."
    elif num < 2:
        S "You call that a martini?  I could drink you under the table with both hands tied behind my back!"
        JS "That expression really doesn't translate well.  I have four arms, you know?"
        S "Yeah, that doesn't change the fact that I can drink more than you!"
        JS "Well said, [c_name].  For some reason I don't see these negotiations going terribly well.  I think I shall take my leave."
        hide JS
        S "Hey!  Come back!  I need to show you how much I can drink!"
    elif num < 3:
        S "Hey, James.  You know [l_name] never loved you, right?"
        JS "That's quite alright.  I hear she's going to die from Space Pox soon anyway."
        S "..."
        S "Did you seriously just say that?"
        JS "Yes, I believe I did."
        $ war_stuff_JS = True
        call JS_war
    elif num < 4:
        S "James?  More like LAMES!"
        JS "Well played.  I'll be sure to make fun of your name as soon as I bother learning it."
        S "You know my name!"
        JS "I can't say I do.  Stan?  Eric John?"
        JS "Anyway, I'll see you later Steve."
    else:
        S "You're dumb, you know that?"
        JS "I know a lot of things, but that seemed to have slipped my mind."
        S "Well, now you know unless you don't because you're too dumb."
        JS "Bye, [c_name].  The conversation has been stimulating as always."
    if not war_stuff_JS:
        scene black
        with Dissolve(0.5)
        centered "---End diplomacy - your relationship with Estelle has decreased!---"
    return

label JS_offer:
    S "Alright, James.  I know what you're after.  How much of my fleet do you need?  100 ships? 200? 1000?"
    JS "I have no need of your charity, [c_name]. How about a trade though?"
    S "What kind of trade?"
    JS "I give you the Space Serum, and you give me your [l_title]."
    S "What?!"
    JS "You heard me."
    S "That's not going to happen."
    JS "I can't convince you?  How about I throw in some of that cocoa I know you love so much."
    menu:
        "Enough of this guy.":
            call JS_war
        "Just leave.":
            S "Look, James, I don't have time for this. My love's life hangs in the balance."
            JS "Didn't you hear me? I just offered to save [c_pronoun]. But I suppose pride is a cruel mistress, eh [c_name]?"
            hide JS
            S "..."
            scene black
            with Dissolve(0.5)
            centered "End Diplomacy"
    return

label JS_war:
    scene bg e_cc
    call dcl("angry")
    show JS happy at right
    if JS_progress >= 1:
        S "I've had enough of your stalling!"
    S "We were never close, James, but going after [l_name] was the last straw. There's no chance of peace between us - not now, not ever!"
    JS "If you feel that way, I suppose that's how it's going to be."
    scene black
    with Dissolve(0.5)
    centered "You are now at war with Estelle"
    $mJS.toWar()
    return
    
label JS_talk_one:
    call dcl("neutral")
    JS "Ah, [c_name].  Lovely see you again."
    S "Hello again, James."
    JS "So nice of you to stop by again so soon.  You look positively dreamy today, if I say so myself."
    S "Very funny, James, but I don't exactly have time for pleasantries."
    JS "You never have time for pleasantries."
    S "..."
    JS "You were saying?"
    if not JS_suspicion:
        S "There's just one thing that has been bothering me.  The ships of the rebels who captured my [l_title]... They were Estellian build."
        JS "Interesting."
        S "Well, what do you make of it?"
        JS "Like I said. It's perplexing."
        JS "What are you trying to get at?"
        menu:
            "I'm getting at your throat.":
                call JS_war
            "Shouldn't you know where your own ships are?":
                call JS_weak_leader
            "Nothing.":
                call JS_nothing
            "Let the dreams decide.":
                call JS_weak_leader
    else:
        S "I'm here about the ships involved in [l_name]'s kidnapping.  Obviously Estellian build."
        JS "If you say so."
        S "I do, as does Gaius."
        JS "Gaius says a lot of things - perhaps you should trust more in your own judgement."
        call JS_weak_leader
    return
    
label JS_nothing:
    S "It was nothing. Don't know what I was saying."
    JS "You know, that does make it terribly hard on the rest of us, [c_name]."
    S "Huh?"
    JS "If even you don't know what you're saying, what chance do I have?"
    S "Not a good one, I'd venture."
    JS "Precisely.  Now is there anything else?  I'm a busy man."
    S "Well, the Space Serum..."
    JS "This tiring subject again?  I have nothing more to say on it.  I'll leave you to your ruminations."
    scene black
    with Dissolve(0.5)
    centered "-End Diplomacy-"
    return
    
label JS_weak_leader:
    $ JS_relationship += 1
    $ JS_weak = True
    S "Well, the way I see it, a leader of a faction ought to know where all his ships are at all times."
    JS "That he should, and I do."
    S "So how did your ships get to Dreamion without your knowlege?"
    JS "They must not have been my ships, [c_name]."
    S "They had Estellian colors."
    JS "As much as I'd like to outlaw red paint from the Nebula, I do not possess that power. You flatter me too much."
    S "I was implying nothing of the sort, James.  Who would take the time to impersonate your fleet?  The Masters of Space? The Nebulists? That weird frog guy?  I think not."
    JS "True, I don't see the motivation either."
    S "So?"
    JS "So... nothing.  I have no answers for you, [c_name]."
    menu:
        "When will you have answers?":
            call JS_further
        "Like hell, you don't!":
            call JS_war
    return
    
label JS_further:
    $ JS_relationship += 1
    S "No answers?"
    JS "None."
    S "And the Space Pox?"
    JS "Quite peculiar as well."
    S "You're holding something back, James, and I'm going to find out what."
    JS "I have no idea what you mean, [c_name], but I'm afraid I have to go.  I have... certain matters to attend to."
    S "Fair enough, but you can be sure I'll be back next cycle."
    scene black
    with Dissolve(0.5)
    centered "- End Diplomacy -"
    return
    
    
label JS_talk_two:
    call dcl("neutral")
    if JS_weak:
        show JS neutral at right
        S "James, so nice to see you again."
        JS "Right, good to see you too."
        S "You don't look as happy as usual."
        JS "Estellian ships.  Red, right?"
        S "Yes..."
        JS "What other nation has red in it?"
        call dcl("happy")
        S "Masters of Space!  Orange is made from red and yellow!"
        JS "Brilliant, [c_name].  Clearly the Masters of Space were nefarious enough to set up this whole plot."
        JS "They framed me and sent you on a rampage across the Nebula because... why exactly?"
        S "I have no idea.  I'll talk to Gaius, and we'll sort this out!"
        JS "No, don't talk to Gaius."
        S "Dont?  Why?"
        JS "Because you're an idiot."
        call dcl("neutral")
        JS "What's the first color in the rainbow?"
        S "ROY G BIV.  Red."
        JS "And what nation has the rainbow for its colors?"
        S "Dreamion."
        JS "Right."
        if JS_relationship == 4:
            $territory.setOwner(mPlayer)
            JS "Here, I'm giving you control of this star system."
            S "What? Why?"
            JS "Just, put it to good use."
        JS "I'll see you later, [c_name]."
        hide JS
        S "Well... that was weird."
        scene black
        with Dissolve(0.5)
        centered "- End Diplomacy -"        
    else:
        S "James."
        JS "You again. Fantastic.  Just this morning I was thinking to myself, \"What I really need is a visit from Nebula Nine's resident idiot.\" I'm so glad you've turned up."
        menu:
            "Haha, such jokes!":
                call JS_such_jokes
            "What did you say!?":
                call JS_anger_at_jokes
            "Let the dreams decide.":
                call JS_such_jokes
    return
    
label JS_such_jokes:
    $ JS_relationship += 1
    S "I don't see Alfred Hicks anywhere."
    JS "Ha!  Good one, [c_name].  There might be hope for you yet."
    S "Perhaps for me, but not for [l_name]. Not without the Serum."
    JS "Smooth transition. You're rather on point this cycle. I'm impressed."
    S "Enough schmoozing, please.  We have business at hand."
    JS "Despite your persistence, my answer has not changed.  I will allow no passage through my territory, and that is final."
    S "But what about just giving me the Space Serum."
    JS "I'm afraid I can't do that.  My hands are tied - all of them."
    S "What do you mean, your hands are tied?"
    JS "I wish I could tell you, [c_name], but it's not in my nature.  I will see you again shortly, I presume?"
    S "We're not done here!"
    JS "Actually we are.  If you'd excuse me."
    scene black
    with Dissolve(0.5)
    centered "- End Diplomacy -"
    return
    
label JS_anger_at_jokes:
    call dcl("angry")
    S "This sort of thing is intolerable!  How can you say that!?"
    S "I've done nothing but play along with your games this whole time!"
    call JS_war
    return
    
    
label JS_talk_three:
    show JS neutral at right
    $gaius_takeover = True
    if JS_relationship > 3:
        JS "[c_name], there's something you need to know. I fear I may have already delayed too long in telling you..."
        S "Is it about the Space Serum?"
        JS "Yes, something like that. You didn't bring Gaius along this time?"
        S "No - wait. Why does that matter?"
        JS "Because, Gaius is... he..."
        S "What, James?  What did Gaius do?"
        JS "He orchestrated the whole thing!  I wasn't going to tell you, but-"
        S "No! That doesn't make any sense. Gaius has been a loyal advisor - no, a loyal friend, since I was a child. Why would he do any of this?"
        JS "Because he knew. He and I both knew how powerful you would become. Your leadership and power in battle is unmatched."
        JS "If you'd only applied yourself in the Academy, you would have gotten top marks. Can't you see what's happening right under your nose?"
        S "You're still not making sense."
        JS "Your [l_name], your sweet [l_name], he knew if anything happened to [l_pronoun2], you would do anything to fix things - even if that meant conquering the entire nebula."
        S "But what does he have to gain from this?"
        JS "At the last moment he meant to betray you and take the Nebula for his own, but now, well, I fear..."
        S "What James?"
        JS "I fear this may be the last you'll see of me. Gaius had another plan - one I discovered far too late."
        JS "Gaius has been using Dreamion's power behind your back to spread his influence throughout the Nebula, and now, you have built him an undefeatable army."
        S "We'll see about that."
        JS "I have faith in you, [c_name].  One thing you must know though before I go."
        S "What is it, James?"
        JS "I... I love you."
        S "What?  Well, uh... James... I-"
        JS "Kidding, [c_name]. Kidding."
        JS "The Space Serum is in the capital of Estelle. The capital is the heart of this territory, and the source of her strength. Conquer that, and Gaius will fall.  I bid you farewell."
    else:
        JS "[c_name], good to see you."
        S "You look worried, James."
        JS "Some of my information has been... off lately."
        S "I suppose I'm fortunate to have Gaius. He tells me everything I need to know; his reports have never failed me."
        JS "Ironic, isn't it?"
        S "How so?"
        JS "Don't mind me. Anyhow, it's time for me to bid you farewell, [c_name]. I don't think you'll be seeing me again."
        S "Are you trying to make a joke?"
        JS "No, it was nothing; you'll see for yourself, soon enough."
    $RBWarSeen = True
    $gaius_conquer()
    scene black
    with Dissolve(0.5)
    show gaius angry
    G "Muhahahahahaha, the Nebula will tremble under my mighty fist!"
    hide Gaius
    centered "- Gaius has conquered the Nebula! -"
    return

label JS_timeout_war:
    scene bg e_cc
    show JS happy
    JS "Sorry, [c_name], but I don't think I'm going to sit here while you try you best to figure out how to defeat me.  No one has that kind of time."
    scene black
    with Dissolve(0.5)
    centered "--- You are now at war with Estelle ---"