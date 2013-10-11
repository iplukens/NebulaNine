init:
    $ c_name = "S"
    define S = DynamicCharacter("c_name", color="FFFFFF")
    $ l_name = "L"
    define L = DynamicCharacter("l_name", color="ff1493")

label tutorial:
    scene bg d_cc
    show gaius neutral
    G "Ah, you're awake. You seem a bit woozy. I am Gaius Escariot, and as always, I remain your humble servant. I apologize for waking you so early from your sleep, but there are urgent matters requiring your attention. However, before we begin..."
    call screen character_select
    $bGender = _return
    if bGender == "male":
        $ c_name = "Sigfried"
        $ c_pronoun = "he"
        $ c_cpronoun = "He"
        $ c_pronoun2 = "him"
        $ c_cpronoun2 = "Him"
        $ c_pronoun_possessive = "his"
        $ c_cpronoun_possessive = "His"
        $ c_title = "prince"
        $ capital_title = "Prince"
        $ miperson = "milord"
        $ c_boygirl = "boy"
    else:
        $ c_name = "Sophia"
        $ c_pronoun = "she"
        $ c_cpronoun = "She"
        $ c_pronoun2 = "her"
        $ c_cpronoun2 = "Her"
        $ c_pronoun_possessive = "her"
        $ c_cpronoun_possessive = "Her"
        $ c_title = "princess"
        $ capital_title = "Princess"
        $ miperson = "milady"
        $ c_boygirl = "girl"
    scene bg d_cc
    show gaius neutral
    call dcl("neutral")
    G "Right, of course.  I should really write that down so this doesn't keep happening."
    G "And you, how's your memory? I could give you a quick reminder of who you are, if that might help fill in the gaps."
    menu:
        "Yes, please.":
            call tutorial_recap
        "No thanks.":
            call advance_tutorial
    return

label tutorial_recap:
    S "That would be wise.  I seem to be slightly out of sorts as well."
    G "Yes, of course, [miperson].  You are the [capital_title] of Dreamion, a kingdom consisting of two star systems at the tail end of Nebula Nine."
    G "Like all leaders of Dreamion, every so often you enter into a sleep-like trance, and you allow your dreams to make decisions for you."
    G "Now, Nebula Nine, despite the relative splendor we live in, is an awfully divided place. In the cycles since you entered your dream-state, relations between the territories have become even more tense."
    G "The Nebula is divided into five factions. The first is Dreamion, as you know.  Our neighbors are the Masters of Space, identified by their orange colors. They are led by the coarse and, dare I say, uncultured Alfred Hicks."
    G "Further on in the Nebula's star systems are the Nebulists and the Bureau of Transformers, or BoT, if you prefer."
    G "Corvida Corax leads the cyan-clad Nebulists. They worship the Nebula, which is exactly as crazy as it sounds, but be wary, as they don't take kindly to non-believers."
    G "ROBBIT leads the BoTs, if you can call it leadership at all. I can't say I know very much about him, as he's rarely been seen. From our reports, he's a very odd and unpredictable green robot."
    G "Furthest from Dreamion lies the red kingdom of Estelle, home of the notorious James Stirspear."
    G "Remember him, [miperson]?  He tormented you constantly when you two were at the Space Academy together.  I would recommend that you approach any negotiations with him cautiously; word is he's become a ruthless and treacherous leader."
    S "Thank you, Gaius. Your knowledge is ever useful."
    call advance_tutorial
    return

label advance_tutorial:
    G "Now, for the reason you have been awakened early from your dreams…"
    G "A terrible thing has happened."
    S "What's wrong?"
    G "Your lover was kidnapped while you slumbered."
    menu:
        "Where is my princess?!":
            call a_female
        "Where is my prince?!":
            call a_male
        "Let the dreams decide.":
            $dream_count += 1
            $num = renpy.random.randint(0, 1)
            if num > 0.5:
                call a_male
            else:
                call a_female
    S "What happened? Where is [l_name]?!?"
    G "Fortunately, we were able to rescue [l_pronoun2] quickly. However, several days after [l_pronoun_possessive] return, [l_pronoun] became seriously ill."
    G "Our doctors finally traced the source. I'm afraid it's Space Pox, my liege."
    S "Space Pox?"
    G "A rare and deadly Estellian disease, for which there is but one cure: the Space Serum. The few existing samples are kept on the Estellian homeworld, located in the very furthest star system from Dreamion."
    S "We must set off for Estelle at once!"
    G "I understand the need for haste, [miperson], but to reach Estelle you must pass through the territories that lie between. I fear that they will not welcome Dreamion's armies willingly…"
    S "But we must try!"
    G "I agree. The troops have been assembled; they await your command. I wish you luck in your quest, for the very future of Dreamion may depend on the outcome..."
    return

label a_male:
    $aGender = "male"
    $a_cGender = "Male"
    $ l_name = "Pendragon"
    $ l_pronoun = "he"
    $ l_cpronoun = "He"
    $ l_pronoun2 = "him"
    $ l_cpronoun2 = "Him"
    $ l_pronoun_possessive = "his"
    $ l_cpronoun_possessive = "His"
    $ l_title = "prince"
    $ l_capital_title = "Prince"
    return

label a_female:
    $aGender = "female"
    $a_cGender = "Female"
    $ l_name = "Persephone"
    $ l_pronoun = "she"
    $ l_cpronoun = "She"
    $ l_pronoun2 = "her"
    $ l_cpronoun2 = "Her"
    $ l_pronoun_possessive = "her"
    $ l_cpronoun_possessive = "Her"
    $ l_title = "princess"
    $ l_capital_title = "Princess"
    return