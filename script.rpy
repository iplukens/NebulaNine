image bg space_nebula = "space_nebula_ground.png"
image bg space = "space_1.png"
image bg d_cc = "d_CC_bg.png"

# main character
### call dcl(mood) to show the right character
image mcharacter neutral = "sm_bust_neutral.png"
image mcharacter angry = "sm_bust_angry.png"
image mcharacter happy = "sm_bust_happy.png"
image fcharacter neutral = "sf_bust_neutral.png"
image fcharacter angry = "sf_bust_angry.png"
image fcharacter happy = "sf_bust_happy.png"

# love interest character
### call dll(mood) to show the right character
### call say_l(text) to have the right character name say stuff
image mlove neutral = "pm_bust_neutral.png"
image mlove angry = "pm_bust_angry.png"
image mlove happy = "pm_bust_happy.png"
image flove neutral = "pf_bust_neutral.png"
image flove angry = "pf_bust_angry.png"
image flove happy = "pf_bust_happy.png"

# Gaius Escariot
define G = Character(_("Gaius Escariot"), color="#ffcccc")
image gaius neutral = "g_bust_neutral.png"
image gaius angry = "g_bust_angry.png"
image gaius happy = "g_bust_happy.png"

init python:
    hicks_timeout = 0
    kill_count = 0
    JS_Timeout = 5
    AH_conquered = False
    RB_conquered = False
    CC_conquered = False
    debug = 1 ### gets some cool options
    class Owner(object):
        def __init__(self, name, color, army, color_code, atWar=False):
            self.army = army
            self.name = name
            self.color = color
            self.color_code = color_code
            self.atWar = atWar
            self.defeated = 0
        def toWar(self):
            self.atWar = True
        def makePeace(self):
            self.atWar = False
        def allied(self):
            self.defeated = 1
        def conquered(self):
            self.defeated = 2
    
    class UPT(object):
        def __init__(self, untrained, scout, fighter, generator, dGenerator, emp, defense = None):
            self.untrained = untrained
            self.scout = scout
            self.fighter = fighter
            self.generator = generator
            self.dGenerator = dGenerator
            self.emp = emp
            self.defense = defense
        def untrained_add(self, int):
            self.untrained += int
        def scout_add(self, int):
            self.scout += int
        def fighter_add(self, int):
            self.fighter += int
        def generator_add(self, int):
            self.generator += int
        def dGenerator_add(self, int):
            self.dGenerator += int
        def emp_add(self, int):
            self.emp += int
    
    class Territory(object):
        def __init__(self, owner, units_per_turn, upgrade_numbers, x0, y0, adjacents):
            self.owner = owner
            self.units_per_turn = units_per_turn
            self.upgrade_num = upgrade_numbers
            self.x0 = x0
            self.y0 = y0
            self.adjacents = adjacents
            self.isAdjacent = False
            self.upgraded = False
        def setIsAdjacent(self):
            self.isAdjacent = True
        def setNotAdjacent(self):
            self.isAdjacent = False
        def setUpgraded(self):
            self.upgraded = True
        def setNotUpgraded(self):
            self.upgraded = False
        def setOwner(self, owner):
            self.owner = owner

    cycles = "cycle"

# You can place the script of your game in this file.
    
# The game starts here.
label start:
    play music "theme.mp3"
    call saveInit
    #tutorial shit goes here
    $gameOn = True
    call tutorial
    while(gameOn):
        $playerTurn = True
        $action_available = True
        call incomeStep
        call potentialEvents
        call set_production
        call set_recruitment
        call recruited_zeroed
        if tutorial_map_intro:
            call map_intro
        while(playerTurn):
            call end_game
            call set_adjacents
            call check_defeated
            window hide None
            call screen map_image
            $index = _return
            if index == "end":
                $playerTurn = False
            elif index == "recruitmentRoutine":
                call recruitmentRoutine
            else:
                $territory = territories[index]
                if territory.isAdjacent:
                    scene bg space_nebula
                    call add_stars
                    call dcl("neutral")
                    if territory.owner.name == "d":
                        call territory_upgrade(territory)
                    else:
                        if territory.owner.atWar:
                            menu:
                                "Attack!":
                                    $enemy = territory.owner
                                    call allocationRoutine
                                "Make peace offering." if territory.owner == mCC and CC_negotiation_possible:
                                    if action_available:
                                        $action_available = False
                                        call CC_start
                                    else:
                                        scene bg d_cc
                                        call dcl("neutral")
                                        show gaius neutral at right
                                        G "You can only negotiate once per star cycle, [miperson]. Although, you can declare war at any time..."
                                "Cancel":
                                    call add_stars
                                    S "Maybe some other time..."
                                "Take territory" if debug == 1:
                                    $territory.setOwner(mPlayer)
                        else:
                            menu:
                                "Enter negotiations":
                                    if not action_available:
                                        scene bg d_cc
                                        call dcl("neutral")
                                        show gaius neutral at right
                                        G "You can only negotiate once per star cycle, [miperson].  Although, you can declare war at any time..."
                                    else:
                                        $action_available = False
                                        if territory.owner.name == "m":
                                            call AH_event
                                        elif territory.owner.name == "b":
                                            call RB_event
                                        elif territory.owner.name == "n":
                                            call CC_start
                                        elif territory.owner.name == "e":
                                            call JS_event
                                "Declare war!":
                                    $territory.owner.toWar()
                                    if territory.owner.name == "m":
                                        call AH_war
                                    elif territory.owner.name == "b":
                                        call RB_war
                                    elif territory.owner.name == "n":
                                        call CC_declare_war
                                    elif territory.owner.name == "e":
                                        call JS_war
                                "Cancel":
                                    call add_stars
                                    S "Maybe some other time..."
                                "Take territory" if debug == 1:
                                    $territory.setOwner(mPlayer)
        call cpuActions     
    
label map_intro:
    scene bg space_nebula
    call add_stars
    G "So this is the map of Nebula Nine, [miperson].  Over in the lower left are our territories, the white star system of Dreamion."
    $territory = territories[0]
    $highlight_territory()
    $renpy.pause(0.2)
    $territory = territories[1]
    $highlight_territory()
    $renpy.pause(0.2)
    G "From here, we can interact with our own star systems or with any stars that are adjacent to our own."
    G "If we go to our territory, we can improve the number of troops we can get and train each turn."
    G "Then we can train them using the training button in the top left."
    G "Then, of course, if you try adjacent territories of other factions-"
    $territory = territories[2]
    $highlight_territory()
    $renpy.pause(0.5)
    G "You can interact with such exciting people as the Masters of Space."
    $tutorial_map_intro = False
    return

label potentialEvents:
    if hicks_timeout > 2 and not mAH.atWar and owner_is_adjacent(mAH):
        call AH_time_out_war
    
    ###check various flags to display something at the start of a turn 
    elif CCTurnsTilWar <= 0 and not mCC.atWar and owner_is_adjacent(mCC):
        call CC_TimeLimitWar
    elif CC_relationship <= 0 and not mCC.atWar and owner_is_adjacent(mCC):
        call CC_war
    elif CC_blasphemy_count >= 3 and not mCC.atWar  and owner_is_adjacent(mCC):
        $CC_negotiation_possible = False
        call CC_war
    
    elif RBTurnsTilWar < 0 and RBWarSeen == False and RB_relationship != 4 and owner_is_adjacent(mRB):
        call RB_TimeLimitWar
        $RBWarSeen = True
    elif RBTurnsSinceMet > 1 and RBEventOne == False:
        call RB_1A_Item
        $RBEventOne = True
    elif RBTurnsSinceMet > 3 and RBEventTwo == False and RBWarSeen == False:
        call RB_2A_Item
        $RBEventTwo = True
    elif RBTurnsSinceMet > 5 and RB_relationship >= 1 and RBEventThree == False and RBWarSeen == False:
        call RB_3A_Item
        $RBEventThree = True
    elif RBTurnsSinceMet > 7 and RB_relationship >= 2 and territories[5].owner == mPlayer and RBEventFour == False and RBWarSeen == False:
        call RB_4A_Item
        $RBEventFour = True
    elif JS_Timeout == 0 and not mJS.atWar and owner_is_adjacent(mJS):
        call JS_timeout_war
    return

screen map_image:
    imagemap:
        auto "space_nebula_%s.png"
        imagebutton:
            idle "available_troops.png"
            hover "available_troops.png"
            xpos 0
            ypos 10
        imagebutton:
            idle "training_button.png"
            hover "training_button_pressed.png"
            xpos 0
            ypos 55
            action Return("recruitmentRoutine")
        imagebutton:
            idle "end_turn.png"
            hover "end_turn_pressed.png"
            xpos 590
            ypos 560
            action Return("end")
        imagebutton:
            idle "available_ships.png"
            hover "available_ships.png"
            xpos 0
            ypos 100
        $undeployedScoutCount = shipScoutCount - deployedScoutCount
        $undeployedFighterCount = shipFighterCount - deployedFighterCount
        $undeployedGeneratorCount = shipGeneratorCount - deployedGeneratorCount
        $undeployedDGeneratorCount = shipDGeneratorCount - deployedDGeneratorCount
        $undeployedEMPCount = shipEMPCount - deployedEMPCount
        $undeployedCommandCount = shipCommandCount - deployedCommandCount
        text "[shipUntrainedCount]" xoffset 145 yoffset 15
        text "[undeployedScoutCount] / [shipScoutCount]" xoffset 130 yoffset 193
        text "[undeployedFighterCount] / [shipFighterCount]" xoffset 130 yoffset 233
        text "[undeployedGeneratorCount] / [shipGeneratorCount]" xoffset 130 yoffset 298
        text "[undeployedDGeneratorCount] / [shipDGeneratorCount]" xoffset 130 yoffset 340
        text "[undeployedEMPCount] / [shipEMPCount]" xoffset 130 yoffset 385
        text "[undeployedCommandCount] / 1" xoffset 130 yoffset 453
        if territories[0].isAdjacent:
            hotspot (320, 473, 61, 56) action Return(0)
        python:
            for i in range(1, 18):
                star_name = "system" + str(i-1) + "_owned_" + territories[i].owner.color + ".png"
                star_name_hover = "system" + str(i-1) + "_owned_yellow.png"
                if territories[i].isAdjacent:
                    ui.imagebutton(star_name, star_name_hover, xpos=territories[i].x0, ypos=territories[i].y0, clicked=ui.returns(i))
                else:
                    ui.imagebutton(star_name, star_name_hover, xpos=territories[i].x0, ypos=territories[i].y0)

label incomeStep:
    ###updates turn stuff increase troop count, turn count whatever else
    $turnCount += 1
    
    
    if RBTurnsSinceMet != -1:
        $RBTurnsSinceMet += 1    
        $RBTurnsTilWar -= 1
        
    $shipUntrainedCount += recruitUntrainedCount
    ####Deployed count the player has used this turn
    call deployed_equals_zero
    if turnCount >= 1:
        $ cycles = "cycles"
    if turnCount == 1:
        $ cycles = "cycle"
    scene bg d_cc
    call dcl("neutral")
    if gaius_takeover:
        "It has been [turnCount] [cycles] since [l_title] [l_name] has fallen ill.  [recruitUntrainedCount] untrained troops have joined Dreamion."
    else:
        show gaius neutral at right
        G "My [c_title], it has been [turnCount] [cycles] since [l_capital_title] [l_name] has fallen ill.  [recruitUntrainedCount] untrained troops have joined our cause. We await your command."
    return

label deployed_equals_zero:
    ####Deployed count the player has used this turn
    $deployedScoutCount = 0
    $deployedFighterCount = 0
    $deployedGeneratorCount = 0
    $deployedDGeneratorCount = 0
    $deployedEMPCount = 0
    $deployedCommandCount = 0
return

label recruited_zeroed:
    $recruitedScout = 0
    $recruitedFighter= 0
    $recruitedGenerator = 0
    $recruitedDGenerator = 0
    $recruitedEMP = 0
return

label cpuActions:
    if gaius_takeover:
        scene bg e_cc
        show gaius angry
        "Gaius is acting this cycle."
        $num = renpy.random.randint(0, 1)
        if num > 0.50:
            window hide None
            scene bg space_nebula
            call add_stars
            play sound "alert.mp3"
            hide G
            $get_attacked_territory(mG)
            $highlight_territory()
            $ renpy.pause(1.0)
            scene bg d_cc with dissolve
            call dcl("neutral")
            $enemy = mJS
            "Gaius has amassed an army, and Dreamion must defend itself!"
            call allocationRoutine
            $num = renpy.random.randint(0, 2)
            if num > 1:
                window hide None
                scene bg space_nebula
                call add_stars
                play sound "alert.mp3"
                hide G
                $get_attacked_territory(mG)
                $highlight_territory()
                $ renpy.pause(1.0)
                scene bg d_cc with dissolve
                call dcl("neutral")
                $enemy = mJS
                "Gaius has amassed an army, and Dreamion must defend itself!"
                call allocationRoutine
        hide G
    else:
        if owner_is_adjacent(mAH):
            $hicks_timeout += 1
            scene bg m_cc
            show AH neutral
            G "The Masters of Space are acting this cycle, [miperson]"
            if mAH.atWar:
                $num = renpy.random.randint(0, 1)
                if num > 0.25:
                    window hide None
                    scene bg space_nebula
                    hide AH
                    call add_stars
                    play sound "alert.mp3"
                    $ get_attacked_territory(mAH)
                    $ highlight_territory()
                    $ renpy.pause(1.0)
                    scene bg d_cc with dissolve
                    call dcl("neutral")
                    $enemy = mAH
                    show gaius neutral at right
                    G "[capital_title]!  We are under attack!"
                    G "The Masters of Space have amassed an army, and we must defend ourselves!"
                    S "Yes, Gaius.  I understand."
                    call allocationRoutine
            hide AH neutral
        call set_adjacents
        if owner_is_adjacent(mRB):
            if RBTurnsSinceMet == -1:
                $RBTurnsSinceMet = 0
            scene bg b_cc
            show RB neutral
            G "The BoTs are acting this cycle, [miperson]"
            if mRB.atWar:
                $num = renpy.random.randint(0, 1)
                if num > 0.25:
                    window hide None
                    scene bg space_nebula
                    call add_stars
                    play sound "alert.mp3"
                    hide RB
                    $get_attacked_territory(mRB)
                    $highlight_territory()
                    $ renpy.pause(1.0)
                    scene bg d_cc with dissolve
                    call dcl("neutral")
                    $enemy = mRB
                    show gaius neutral at right
                    G "[capital_title]!  We are under attack!"
                    G "The BoTs have amassed an army, and we must defend ourselves!"
                    S "Yes, Gaius.  I understand."
                    call allocationRoutine
            hide RB
        call set_adjacents
        if owner_is_adjacent(mCC):
            $CCTurnsTilWar -= 1
            scene bg n_cc
            show corvida
            G "The Nebulists are acting this cycle, [miperson]"
            if mCC.atWar:
                $num = renpy.random.randint(0, 1)
                if num > 0.5:
                    window hide None
                    scene bg space_nebula
                    call add_stars
                    play sound "alert.mp3"
                    hide corvida
                    $get_attacked_territory(mCC)
                    $highlight_territory()
                    $ renpy.pause(1.0)
                    scene bg d_cc with dissolve
                    call dcl("neutral")
                    $enemy = mCC
                    show gaius neutral at right
                    G "[capital_title]! The Nebulists are at our borders!"
                    G "You must defend Dreamion!"
                    S "Ready our troops! We will depart at once."
                    call allocationRoutine
            hide corvida
        call set_adjacents
        if owner_is_adjacent(mJS):
            if JS_Timeout > 0:
                $JS_Timeout -= 1
            scene bg e_cc
            show JS neutral
            G "Estelle is acting this cycle, [miperson]"
            if mJS.atWar:
                $num = renpy.random.randint(0, 1)
                if num > 0.25:
                    window hide None
                    scene bg space_nebula
                    call add_stars
                    play sound "alert.mp3"
                    hide JS
                    $get_attacked_territory(mJS)
                    $highlight_territory()
                    $ renpy.pause(1.0)
                    scene bg d_cc with dissolve
                    call dcl("neutral")
                    $enemy = mJS
                    show gaius neutral at right
                    G "[capital_title]!  We are under attack!"
                    G "Estelle has amassed an army, and we must defend ourselves!"
                    S "Yes, Gaius.  I understand."
                    call allocationRoutine
            hide JS
    return
    
label add_stars:
    python:
        for i in range(1, 18):
            star_name = "system" + str(i-1) + "_owned_" + territories[i].owner.color + ".png"
            star_name_hover = "system" + str(i-1) + "_owned_yellow.png"
            ui.imagebutton(star_name, star_name_hover, xpos=territories[i].x0, ypos=territories[i].y0)
    return

label saveInit:
    #Starts all our persistent state data
    #Should we like do stuff to denote globals so we dont overlap?
    #I was thinking this stuff is fine but subscreens should get a letter then variable name
    ##### Testing stuff
    $save = 0
    
    #####Variables We actually use at present
    $turnCount = 0
    $bPlayerUpgraded = False
    
    ####Ship counts the player has
    $shipUntrainedCount = 0
    $shipScoutCount = 30
    $shipFighterCount = 20
    $shipGeneratorCount = 10
    $shipDGeneratorCount = 0
    $shipEMPCount = 0
    $shipCommandCount = 1
    
    ####Production count the player has per turn
    $recruitUntrainedCount = 10
    $recruitScoutCount = 2
    $recruitFighterCount = 2
    $recruitGeneratorCount = 2
    $recruitDGeneratorCount = 0
    $recruitEMPCount = 0
    
    ####Deployed count the player has used this turn
    call deployed_equals_zero
    
    $mPlayer = Owner("d", "white", [Battalion("scout",2),Battalion("None",0),Battalion("None",0),Battalion("None",0),Battalion("None",0)], "{color=#ffffff}")
    $mAH = Owner("m", "orange", [Battalion("fighter",8),Battalion("emp",4),Battalion("emp",8),Battalion("emp",1),Battalion("None",0)], "{color=#ffa500}")
    $mCC = Owner("n", "cyan", [Battalion("generator",15),Battalion("scout", 15),Battalion("dgenerator",20),Battalion("emp", 25),Battalion("generator",15)], "{color=#5dd5d5}")
    $mRB = Owner("b", "green", [Battalion("fighter",20),Battalion("fighter",20),Battalion("emp",30),Battalion("dgenerator",10),Battalion("scout",14)], "{color=#00ff00}")
    $mJS = Owner("e", "red", [Battalion("generator",25),Battalion("fighter",25),Battalion("dgenerator",25),Battalion("emp", 40),Battalion("scout",40)], "{color=#ff0000}")
    $mG = Owner("e", "red", [Battalion("dgenerator", 30),Battalion("dgenerator", 30),Battalion("scout", 30),Battalion("scout", 30),Battalion("emp", 50)], "{color=#ff0000}")
    $mG.toWar()
    
    
    #  UPT(untrained, scout, fighter, generator, dGenerator, emp):

    $territories = [Territory(mPlayer, UPT(10, 4, 4, 4, 0, 0), UPT(5, 2, 2, 1, 0, 0), 320, 473, [0, 1]), Territory(mPlayer, UPT(5, 2, 2, 2, 0, 0), UPT(5, 2, 2, 2, 0, 2), 404, 483, [0, 1, 2]), Territory(mAH, UPT(5, 0, 1, 1, 0, 2), UPT(5, 0, 1, 1, 0, 2), 468, 458, [1, 2, 3]), Territory(mAH, UPT(5, 0, 1, 1, 0, 2), UPT(5, 0, 1, 1, 0, 2), 500, 391, [2, 3, 4, 5]), Territory(mAH, UPT(2, 1, 1, 1, 1, 1), UPT(2, 1, 1, 1, 1, 1), 572, 404, [3, 4, 9]), Territory(mCC, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 458, 344, [3, 5, 6]), Territory(mCC, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 420, 272, [5, 6, 7, 8]), Territory(mCC, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 369, 300, [7, 8]), Territory(mCC, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 375, 229, [6, 7, 8, 13]), Territory(mRB, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 575, 340, [4, 9, 10]), Territory(mRB, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 620, 279, [9, 10, 11]), Territory(mRB, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 567, 260, [10, 11, 12]), Territory(mRB, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 587, 206, [11, 12, 15]), Territory(mJS, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 365, 178, [8, 13, 14]), Territory(mJS, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 407, 150, [13, 14, 17]), Territory(mJS, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 541, 148, [12, 15, 16]), Territory(mJS, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 504, 105, [15, 16, 17]), Territory(mJS, UPT(5, 2, 2, 2, 2, 2), UPT(5, 2, 2, 2, 2, 2), 425, 83, [14, 16, 17])]
    
    ####Init all other flags There are goin to be so many jeebus glorious spaghetti code
    $dream_count = 0
    
    ### first meeting flags
    $AH_first = False
    $CC_first = False
    
    ###HICKS FLAGS
    $hicks_timeout = 0
    
    ###RIBBOT FLAGS
    $RB_first = False
    $RBTurnsSinceMet = -1
    $RBTurnsTilWar = 3
    $RBWarSeen = False
    $RBEventOne = False
    $RBEventTwo = False
    $RBEventThree = False
    $RBEventFour = False
    $RB_relationship = 0
    
    ###STIRSPEAR FLAGS
    $JS_Timeout = 3
    
    ### Gaius switch
    $gaius_takeover = False
    
    $kill_count = 0
    
    $JS_first = False
    return