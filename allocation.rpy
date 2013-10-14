###NOTE: I still need to draw icons for selected ship on the right part of screen
# Also need to highlight stuff on the left part of screen

screen allocation_image:
    imagemap:
        auto "allocation_%s.png"

        hotspot (266, 278, 24, 24) action Return("sub1")
        hotspot (266, 308, 24, 24) action Return("sub10")
        hotspot (381, 278, 24, 24) action Return("add1")
        hotspot (381, 308, 24, 24) action Return("add10")
        
        
        ###To select ships
        hotspot (68,88,150,34) action Return("fighter")
        hotspot (68,163,150,34) action Return("generator")
        hotspot (68,238,150,34) action Return("scout")
        hotspot (68,322,150,34) action Return("dgenerator")
        hotspot (68,400,150,34) action Return("emp")
        hotspot (68,480,150,34) action Return("command")
        
        ###Highlight Selection
        if aUnitType == "scout":
            imagebutton:
                idle "a_scout.png"
                hover "a_scout.png"
                xpos 70
                ypos 245
            imagebutton:
                idle "d_scout_ship.png"
                hover "d_scout_ship.png"
                xpos 280
                ypos 150
        if aUnitType == "fighter":
            imagebutton:
                idle "a_fighter.png"
                hover "a_fighter.png"
                xpos 70
                ypos 91
            imagebutton:
                idle "d_fighter.png"
                hover "d_fighter.png"
                xpos 280
                ypos 150
        if aUnitType == "command":
            imagebutton:
                idle "a_command.png"
                hover "a_command.png"
                xpos 70
                ypos 484
            imagebutton:
                idle "d_cc.png"
                hover "d_cc.png"
                xpos 280
                ypos 130
        if aUnitType == "generator":
            imagebutton:
                idle "a_row_shield.png"
                hover "a_row_shield.png"
                xpos 70
                ypos 166
            imagebutton:
                idle "d_row_shield_ship.png"
                hover "d_row_shield_ship.png"
                xpos 280
                ypos 150
        if aUnitType == "dgenerator":
            imagebutton:
                idle "a_shield.png"
                hover "a_shield.png"
                xpos 70
                ypos 325     
            imagebutton:
                idle "d_shield_ship.png"
                hover "d_shield_ship.png"
                xpos 280
                ypos 150
        if aUnitType == "emp":
            imagebutton:
                idle "a_emp.png"
                hover "a_emp.png"
                xpos 70
                ypos 403
            imagebutton:
                idle "d_emp_ship.png"
                hover "d_emp_ship.png"
                xpos 280
                ypos 150
                
        hotspot (580,10,160,35) action Return("confirm")
        hotspot (750,10,35, 35) action Return("help")
        
        text "[aUnitCount]" xoffset 305 yoffset 290
        
        $deployableCommand = shipCommandCount - deployedCommandCount
        text "[deployableCommand]" xoffset 105 yoffset 522 size 16
        
        $deployableGenerator = shipGeneratorCount - deployedGeneratorCount
        text "[deployableGenerator]" xoffset 105 yoffset 205 size 16
        
        $deployableFighter = shipFighterCount - deployedFighterCount
        text "[deployableFighter]" xoffset 105 yoffset 128 size 16
        
        $deployableScout = shipScoutCount - deployedScoutCount
        text "[deployableScout]" xoffset 105 yoffset 282 size 16
        
        $deployableDGenerator = shipDGeneratorCount - deployedDGeneratorCount
        text "[deployableDGenerator]" xoffset 105 yoffset 362 size 16
        
        $deployableEMP = shipEMPCount - deployedEMPCount
        text "[deployableEMP]" xoffset 105 yoffset 442 size 16
        
        ###Draw stuff to screen based on conditions
        if aFullArmy[0].type != "None":
            if aFullArmy[0].type == "fighter":
                imagebutton:
                    idle "d_fighter.png"
                    hover "d_fighter.png"
                    xpos 475
                    ypos 110
            if aFullArmy[0].type == "generator":
                imagebutton:
                    idle "d_row_shield_ship.png"
                    hover "d_row_shield_ship.png"
                    xpos 475
                    ypos 110
            if aFullArmy[0].type == "dgenerator":
                imagebutton:
                    idle "d_shield_ship.png"
                    hover "d_shield_ship.png"
                    xpos 475
                    ypos 110
            if aFullArmy[0].type == "emp":
                imagebutton:
                    idle "d_emp_ship.png"
                    hover "d_emp_ship.png"
                    xpos 475
                    ypos 110
            if aFullArmy[0].type == "scout":
                imagebutton:
                    idle "d_scout_ship.png"
                    hover "d_scout_ship.png"
                    xpos 475
                    ypos 110
            if aFullArmy[0].type == "command":
                imagebutton:
                    idle "d_cc.png"
                    hover "d_cc.png"
                    xpos 475
                    ypos 110
            text "[aFullArmy[0].count]" xoffset 490 yoffset 197 size 16
            imagebutton:
                idle "cancel.png"
                hover "cancelh.png"
                xpos 490
                ypos 225
                action Return("cancel1")
        else:
            hotspot (470,105,101,85) action Return("slot1")
        
        
        if aFullArmy[1].type != "None":
            if aFullArmy[1].type == "fighter":
                imagebutton:
                    idle "d_fighter.png"
                    hover "d_fighter.png"
                    xpos 475
                    ypos 260
            if aFullArmy[1].type == "generator":
                imagebutton:
                    idle "d_row_shield_ship.png"
                    hover "d_row_shield_ship.png"
                    xpos 475
                    ypos 260
            if aFullArmy[1].type == "dgenerator":
                imagebutton:
                    idle "d_shield_ship.png"
                    hover "d_shield_ship.png"
                    xpos 475
                    ypos 260
            if aFullArmy[1].type == "emp":
                imagebutton:
                    idle "d_emp_ship.png"
                    hover "d_emp_ship.png"
                    xpos 475
                    ypos 260
            if aFullArmy[1].type == "scout":
                imagebutton:
                    idle "d_scout_ship.png"
                    hover "d_scout_ship.png"
                    xpos 475
                    ypos 260
            if aFullArmy[1].type == "command":
                imagebutton:
                    idle "d_cc.png"
                    hover "d_cc.png"
                    xpos 475
                    ypos 260
            text "[aFullArmy[1].count]" xoffset 490 yoffset 347 size 16
            imagebutton:
                idle "cancel.png"
                hover "cancelh.png"
                xpos 490
                ypos 370
                action Return("cancel2")
        else:
            hotspot (470,255,101,85) action Return("slot2")
            
        if aFullArmy[2].type != "None":
            text "[aFullArmy[2].count]" xoffset 490 yoffset 495 size 16
            if aFullArmy[2].type == "fighter":
                imagebutton:
                    idle "d_fighter.png"
                    hover "d_fighter.png"
                    xpos 475
                    ypos 410
            if aFullArmy[2].type == "generator":
                imagebutton:
                    idle "d_row_shield_ship.png"
                    hover "d_row_shield_ship.png"
                    xpos 475
                    ypos 410
            if aFullArmy[2].type == "dgenerator":
                imagebutton:
                    idle "d_shield_ship.png"
                    hover "d_shield_ship.png"
                    xpos 475
                    ypos 410
            if aFullArmy[2].type == "emp":
                imagebutton:
                    idle "d_emp_ship.png"
                    hover "d_emp_ship.png"
                    xpos 475
                    ypos 410
            if aFullArmy[2].type == "scout":
                imagebutton:
                    idle "d_scout_ship.png"
                    hover "d_scout_ship.png"
                    xpos 475
                    ypos 410
            if aFullArmy[2].type == "command":
                imagebutton:
                    idle "d_cc.png"
                    hover "d_cc.png"
                    xpos 475
                    ypos 410
            imagebutton:
                idle "cancel.png"
                hover "cancelh.png"
                xpos 490
                ypos 518
                action Return("cancel3")
        else:
            hotspot (470,400,101,85) action Return("slot3")
            
        if aFullArmy[3].type != "None":
            if aFullArmy[3].type == "fighter":
                imagebutton:
                    idle "d_fighter.png"
                    hover "d_fighter.png"
                    xpos 610
                    ypos 180
            if aFullArmy[3].type == "generator":
                imagebutton:
                    idle "d_row_shield_ship.png"
                    hover "d_row_shield_ship.png"
                    xpos 610
                    ypos 180
            if aFullArmy[3].type == "dgenerator":
                imagebutton:
                    idle "d_shield_ship.png"
                    hover "d_shield_ship.png"
                    xpos 610
                    ypos 180
            if aFullArmy[3].type == "emp":
                imagebutton:
                    idle "d_emp_ship.png"
                    hover "d_emp_ship.png"
                    xpos 610
                    ypos 180
            if aFullArmy[3].type == "scout":
                imagebutton:
                    idle "d_scout_ship.png"
                    hover "d_scout_ship.png"
                    xpos 610
                    ypos 180
            if aFullArmy[3].type == "command":
                imagebutton:
                    idle "d_cc.png"
                    hover "d_cc.png"
                    xpos 610
                    ypos 180
            text "[aFullArmy[3].count]" xoffset 630 yoffset 272 size 16
            imagebutton:
                idle "cancel.png"
                hover "cancelh.png"
                xpos 630
                ypos 300
                action Return("cancel4")
        else:
            hotspot (610,180,100,85) action Return("slot4")
            
        if aFullArmy[4].type != "None":
            text "[aFullArmy[4].count]" xoffset 630 yoffset 422 size 16
            if aFullArmy[4].type == "fighter":
                imagebutton:
                    idle "d_fighter.png"
                    hover "d_fighter.png"
                    xpos 610
                    ypos 330
            if aFullArmy[4].type == "generator":
                imagebutton:
                    idle "d_row_shield_ship.png"
                    hover "d_row_shield_ship.png"
                    xpos 610
                    ypos 330
            if aFullArmy[4].type == "dgenerator":
                imagebutton:
                    idle "d_shield_ship.png"
                    hover "d_shield_ship.png"
                    xpos 610
                    ypos 330
            if aFullArmy[4].type == "emp":
                imagebutton:
                    idle "d_emp_ship.png"
                    hover "d_emp_ship.png"
                    xpos 610
                    ypos 330
            if aFullArmy[4].type == "scout":
                imagebutton:
                    idle "d_scout_ship.png"
                    hover "d_scout_ship.png"
                    xpos 610
                    ypos 330
            if aFullArmy[4].type == "command":
                imagebutton:
                    idle "d_cc.png"
                    hover "d_cc.png"
                    xpos 610
                    ypos 330
            imagebutton:
                idle "cancel.png"
                hover "cancelh.png"
                xpos 630
                ypos 450
                action Return("cancel5")
        else:
            hotspot (610,325,100,85) action Return("slot5")
            

    


label allocationRoutine:
    play music "battle.mp3"
    $aAllocation = True
    $aUnitCount = 0
    $aUnitType = "fighter"
    $aDeploy = False
    $aSelectedSlot = 1
    $aFullArmy = [Battalion("None",0),Battalion("None",0),Battalion("None",0),Battalion("None",0),Battalion("None",0)]
    while(aAllocation):
        window hide None
        call screen allocation_image
        call allocationAction pass (_return)
        if(aDeploy):
            call deployBattalion
            $aDeploy = False
        window show None
    call battle_routine
    play music "theme.mp3"
    return
    
label allocationAction(input):
    if input == "confirm":
        $aAllocation = False
        
    elif input == "add10":
        $aUnitCount += 10
    elif input == "add1":
        $aUnitCount += 1
    elif input == "sub10":
        if aUnitCount - 10 < 0:
            $aUnitCount -= aUnitCount
        else: 
            $aUnitCount -= 10
    elif input == "sub1" and aUnitCount > 0:
        $aUnitCount -= 1
    ###Do we want to be able to deploy untrained?
    elif input == "fighter":
        $aUnitType = "fighter"
    elif input == "scout":
        $aUnitType = "scout"
    elif input == "generator":
        $aUnitType = "generator"
    elif input == "dgenerator":
        $aUnitType = "dgenerator"
    elif input == "emp":
        $aUnitType = "emp"
    elif input == "command":
        $aUnitType = "command"
    elif input == "slot1":
        $selectedSlot = 0
        $aDeploy = True
    elif input == "slot2":
        $selectedSlot = 1
        $aDeploy = True
    elif input == "slot3":
        $selectedSlot = 2
        $aDeploy = True
    elif input == "slot4":
        $selectedSlot = 3
        $aDeploy = True
    elif input == "slot5":
        $selectedSlot = 4
        $aDeploy = True
    elif input == "cancel1":
        call cancelBattalion pass (0)
    elif input == "cancel2":
        call cancelBattalion pass (1)
    elif input == "cancel3":
        call cancelBattalion pass (2)
    elif input == "cancel4":
        call cancelBattalion pass (3)
    elif input == "cancel5":
        call cancelBattalion pass (4)
    elif input == "confirm":
        $aAllocation = False
    elif input == "help":
        call screen helpScreen
    return
    
label deployBattalion:
    
    call handleHousekeeping
    if aUnitCount > 0:
        $aFullArmy[selectedSlot] = Battalion(aUnitType, aUnitCount)
        $aUnitCount = 0
    return
    
label cancelBattalion(battalionNumber):
    if aFullArmy[battalionNumber].type == "fighter":
        $deployedFighterCount -= aFullArmy[battalionNumber].count
    elif aFullArmy[battalionNumber].type == "scout":
        $deployedScoutCount -= aFullArmy[battalionNumber].count
    elif aFullArmy[battalionNumber].type == "generator":
        $deployedGeneratorCount -= aFullArmy[battalionNumber].count
    elif aFullArmy[battalionNumber].type == "dgenerator":
        $deployedDGeneratorCount -= aFullArmy[battalionNumber].count
    elif aFullArmy[battalionNumber].type == "emp":
        $deployedEMPCount -= aFullArmy[battalionNumber].count
    elif aFullArmy[battalionNumber].type == "command":
        $deployedCommandCount -= aFullArmy[battalionNumber].count
        
    $aFullArmy[battalionNumber] = Battalion("None", 0)
    return

label handleHousekeeping:
    if aUnitType == "fighter":
        if aUnitCount > shipFighterCount - deployedFighterCount:
            $aUnitCount = shipFighterCount - deployedFighterCount
        $deployedFighterCount += aUnitCount
    if aUnitType == "emp":
        if aUnitCount > shipEMPCount - deployedEMPCount:
            $aUnitCount = shipEMPCount - deployedEMPCount
        $deployedEMPCount += aUnitCount
    if aUnitType == "scout":
        if aUnitCount > shipScoutCount - deployedScoutCount:
            $aUnitCount = shipScoutCount - deployedScoutCount
        $deployedScoutCount += aUnitCount
    if aUnitType == "command":
        if aUnitCount > shipCommandCount - deployedCommandCount:
            $aUnitCount = shipCommandCount - deployedCommandCount
        $deployedCommandCount += aUnitCount
    if aUnitType == "generator":
        if aUnitCount > shipGeneratorCount - deployedGeneratorCount:
            $aUnitCount = shipGeneratorCount - deployedGeneratorCount
        $deployedGeneratorCount += aUnitCount
    if aUnitType == "dgenerator":
        if aUnitCount > shipDGeneratorCount - deployedDGeneratorCount:
            $aUnitCount = shipDGeneratorCount - deployedDGeneratorCount
        $deployedDGeneratorCount += aUnitCount
    return