###NOTE: I still need to draw icons for selected ship on the right part of screen
# Also need to highlight stuff on the left part of screen

screen allocation_image:
    imagemap:
        auto "allocation_%s.png"

        hotspot (228, 278, 24, 24) action Return("sub1")
        hotspot (228, 308, 24, 24) action Return("sub10")
        hotspot (343, 278, 24, 24) action Return("add1")
        hotspot (343, 308, 24, 24) action Return("add10")
        
        
        ###To select ships
        hotspot (28,88,150,34) action Return("fighter")
        hotspot (28,163,150,34) action Return("generator")
        hotspot (28,238,150,34) action Return("scout")
        hotspot (28,322,150,34) action Return("dgenerator")
        hotspot (28,400,150,34) action Return("emp")
        hotspot (28,480,150,34) action Return("command")
        
        ###Highlight Selection
        if aUnitType == "scout":
            imagebutton:
                idle "a_scout.png"
                hover "a_scout.png"
                xpos 33
                ypos 245
            imagebutton:
                idle "d_scout_ship.png"
                hover "d_scout_ship.png"
                xpos 225
                ypos 150
        if aUnitType == "fighter":
            imagebutton:
                idle "a_fighter.png"
                hover "a_fighter.png"
                xpos 33
                ypos 91
            imagebutton:
                idle "d_fighter.png"
                hover "d_fighter.png"
                xpos 225
                ypos 150
        if aUnitType == "command":
            imagebutton:
                idle "a_command.png"
                hover "a_command.png"
                xpos 33
                ypos 484
            imagebutton:
                idle "d_cc.png"
                hover "d_cc.png"
                xpos 225
                ypos 130
        if aUnitType == "generator":
            imagebutton:
                idle "a_row_shield.png"
                hover "a_row_shield.png"
                xpos 33
                ypos 166
            imagebutton:
                idle "d_row_shield_ship.png"
                hover "d_row_shield_ship.png"
                xpos 225
                ypos 150
        if aUnitType == "dgenerator":
            imagebutton:
                idle "a_shield.png"
                hover "a_shield.png"
                xpos 33
                ypos 325     
            imagebutton:
                idle "d_shield_ship.png"
                hover "d_shield_ship.png"
                xpos 225
                ypos 150
        if aUnitType == "emp":
            imagebutton:
                idle "a_emp.png"
                hover "a_emp.png"
                xpos 33
                ypos 403
            imagebutton:
                idle "d_emp_ship.png"
                hover "d_emp_ship.png"
                xpos 225
                ypos 150
                
        hotspot (580,10,160,35) action Return("confirm")
        hotspot (750,10,35, 35) action Return("help")
        
        text "[aUnitCount]" xoffset 265 yoffset 290
        
        $deployableCommand = shipCommandCount - deployedCommandCount
        text "[deployableCommand]" xoffset 75 yoffset 522 size 16
        
        $deployableGenerator = shipGeneratorCount - deployedGeneratorCount
        text "[deployableGenerator]" xoffset 75 yoffset 205 size 16
        
        $deployableFighter = shipFighterCount - deployedFighterCount
        text "[deployableFighter]" xoffset 75 yoffset 128 size 16
        
        $deployableScout = shipScoutCount - deployedScoutCount
        text "[deployableScout]" xoffset 75 yoffset 282 size 16
        
        $deployableDGenerator = shipDGeneratorCount - deployedDGeneratorCount
        text "[deployableDGenerator]" xoffset 75 yoffset 362 size 16
        
        $deployableEMP = shipEMPCount - deployedEMPCount
        text "[deployableEMP]" xoffset 75 yoffset 442 size 16
        
        ###Draw stuff to screen based on conditions
        if aFullArmy[0].type != "None":
            if aFullArmy[0].type == "fighter":
                imagebutton:
                    idle "d_fighter.png"
                    hover "d_fighter.png"
                    xpos 440
                    ypos 80
            if aFullArmy[0].type == "generator":
                imagebutton:
                    idle "d_row_shield_ship.png"
                    hover "d_row_shield_ship.png"
                    xpos 440
                    ypos 80
            if aFullArmy[0].type == "dgenerator":
                imagebutton:
                    idle "d_shield_ship.png"
                    hover "d_shield_ship.png"
                    xpos 440
                    ypos 80
            if aFullArmy[0].type == "emp":
                imagebutton:
                    idle "d_emp_ship.png"
                    hover "d_emp_ship.png"
                    xpos 440
                    ypos 80
            if aFullArmy[0].type == "scout":
                imagebutton:
                    idle "d_scout_ship.png"
                    hover "d_scout_ship.png"
                    xpos 440
                    ypos 80
            if aFullArmy[0].type == "command":
                imagebutton:
                    idle "d_cc.png"
                    hover "d_cc.png"
                    xpos 440
                    ypos 80
            text "[aFullArmy[0].count]" xoffset 460 yoffset 187 size 16
            imagebutton:
                idle "cancel.png"
                hover "cancelh.png"
                xpos 460
                ypos 215
                action Return("cancel1")
        else:
            hotspot (430,75,140,100) action Return("slot1")
        
        
        if aFullArmy[1].type != "None":
            if aFullArmy[1].type == "fighter":
                imagebutton:
                    idle "d_fighter.png"
                    hover "d_fighter.png"
                    xpos 440
                    ypos 250
            if aFullArmy[1].type == "generator":
                imagebutton:
                    idle "d_row_shield_ship.png"
                    hover "d_row_shield_ship.png"
                    xpos 440
                    ypos 250
            if aFullArmy[1].type == "dgenerator":
                imagebutton:
                    idle "d_shield_ship.png"
                    hover "d_shield_ship.png"
                    xpos 440
                    ypos 250
            if aFullArmy[1].type == "emp":
                imagebutton:
                    idle "d_emp_ship.png"
                    hover "d_emp_ship.png"
                    xpos 440
                    ypos 250
            if aFullArmy[1].type == "scout":
                imagebutton:
                    idle "d_scout_ship.png"
                    hover "d_scout_ship.png"
                    xpos 440
                    ypos 250
            if aFullArmy[1].type == "command":
                imagebutton:
                    idle "d_cc.png"
                    hover "d_cc.png"
                    xpos 440
                    ypos 250
            text "[aFullArmy[1].count]" xoffset 460 yoffset 357 size 16
            imagebutton:
                idle "cancel.png"
                hover "cancelh.png"
                xpos 460
                ypos 385
                action Return("cancel2")
        else:
            hotspot (430,245,140,100) action Return("slot2")
            
        if aFullArmy[2].type != "None":
            text "[aFullArmy[2].count]" xoffset 460 yoffset 527 size 16
            if aFullArmy[2].type == "fighter":
                imagebutton:
                    idle "d_fighter.png"
                    hover "d_fighter.png"
                    xpos 440
                    ypos 420
            if aFullArmy[2].type == "generator":
                imagebutton:
                    idle "d_row_shield_ship.png"
                    hover "d_row_shield_ship.png"
                    xpos 440
                    ypos 420
            if aFullArmy[2].type == "dgenerator":
                imagebutton:
                    idle "d_shield_ship.png"
                    hover "d_shield_ship.png"
                    xpos 440
                    ypos 420
            if aFullArmy[2].type == "emp":
                imagebutton:
                    idle "d_emp_ship.png"
                    hover "d_emp_ship.png"
                    xpos 440
                    ypos 420
            if aFullArmy[2].type == "scout":
                imagebutton:
                    idle "d_scout_ship.png"
                    hover "d_scout_ship.png"
                    xpos 440
                    ypos 420
            if aFullArmy[2].type == "command":
                imagebutton:
                    idle "d_cc.png"
                    hover "d_cc.png"
                    xpos 440
                    ypos 420
            imagebutton:
                idle "cancel.png"
                hover "cancelh.png"
                xpos 460
                ypos 455
                action Return("cancel3")
        else:
            hotspot (430,415,140,100) action Return("slot3")
            
        if aFullArmy[3].type != "None":
            if aFullArmy[3].type == "fighter":
                imagebutton:
                    idle "d_fighter.png"
                    hover "d_fighter.png"
                    xpos 610
                    ypos 165
            if aFullArmy[3].type == "generator":
                imagebutton:
                    idle "d_row_shield_ship.png"
                    hover "d_row_shield_ship.png"
                    xpos 610
                    ypos 165
            if aFullArmy[3].type == "dgenerator":
                imagebutton:
                    idle "d_shield_ship.png"
                    hover "d_shield_ship.png"
                    xpos 610
                    ypos 165
            if aFullArmy[3].type == "emp":
                imagebutton:
                    idle "d_emp_ship.png"
                    hover "d_emp_ship.png"
                    xpos 610
                    ypos 165
            if aFullArmy[3].type == "scout":
                imagebutton:
                    idle "d_scout_ship.png"
                    hover "d_scout_ship.png"
                    xpos 610
                    ypos 165
            if aFullArmy[3].type == "command":
                imagebutton:
                    idle "d_cc.png"
                    hover "d_cc.png"
                    xpos 610
                    ypos 165
            text "[aFullArmy[3].count]" xoffset 630 yoffset 272 size 16
            imagebutton:
                idle "cancel.png"
                hover "cancelh.png"
                xpos 630
                ypos 300
                action Return("cancel4")
        else:
            hotspot (600,160,140,100) action Return("slot4")
            
        if aFullArmy[4].type != "None":
            text "[aFullArmy[4].count]" xoffset 630 yoffset 437 size 16
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
                ypos 465
                action Return("cancel5")
        else:
            hotspot (600,325,140,100) action Return("slot5")
            

    


label allocationRoutine:
    
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
        call helpScreen
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