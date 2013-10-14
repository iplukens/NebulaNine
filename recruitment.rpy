image bg recruit = "recruitment_ground.png"

screen recruitment_image:
    imagemap:
        auto "recruitment_%s.png" 

        hotspot (627, 223, 23, 23) action Return("sub10S")
        hotspot (627, 193, 23, 23) action Return("sub1S")
        hotspot (741, 223, 23, 23) action Return("add10S")
        hotspot (741, 193, 30, 23) action Return("add1S")
        
        hotspot (243, 193, 23, 23) action Return("sub1F")
        hotspot (243, 223, 23, 23) action Return("sub10F")
        hotspot (357, 223, 23, 23) action Return("add10F")
        hotspot (357, 193, 23, 23) action Return("add1F")
        
        hotspot (435, 223, 23, 23) action Return("sub10G")
        hotspot (435, 193, 23, 23) action Return("sub1G")
        hotspot (550, 223, 23, 23) action Return("add10G")
        hotspot (550, 193, 23, 23) action Return("add1G")

        hotspot (339, 445, 23, 23) action Return("sub1DG")
        hotspot (339, 475, 23, 23) action Return("sub10DG")
        hotspot (454, 445, 23, 23) action Return("add1DG")
        hotspot (454, 475, 23, 23) action Return("add10DG")
        
        hotspot (532, 445, 23, 23) action Return("sub1E")
        hotspot (532, 475, 23, 23) action Return("sub10E")
        hotspot (646, 445, 23, 23) action Return("add1E")
        hotspot (646, 475, 23, 23) action Return("add10E")
        
        
        hotspot (585, 10, 155, 35) action Return("exit")
        hotspot (420, 10, 155, 35) action Return("confirmRecruit")
        hotspot (750, 10, 35, 35) action Return ("helpScreen")
        
        text "[rTempUntrained]" xoffset 157 yoffset 15 
        
        
        #This is the text that displays for shield generators, cannot display things that evaluate for reasons i dont understand
        text "[rTempGeneratorCount]" xoffset 475 yoffset 210 size 14
        text "/" xoffset 500 yoffset 210 size 14
        $rcanGDep = recruitGeneratorCount - recruitedGenerator
        text "[rcanGDep]" xoffset 510 yoffset 210 size 14
        

        text "[rTempFighterCount]" xoffset 283 yoffset 210 size 14
        text "/" xoffset 308 yoffset 210 size 14
        $rcanFDep = recruitFighterCount - recruitedFighter
        text "[rcanFDep]" xoffset 318 yoffset 210 size 14
        
        
        text "[rTempScoutCount]" xoffset 667 yoffset 210  size 14
        text "/" xoffset 692 yoffset 210 size 14
        $rcanSDep = recruitScoutCount - recruitedScout
        text "[rcanSDep]" xoffset 702 yoffset 210 size 14


        ###Bottom Row stuff
        text "[rTempDGeneratorCount]" xoffset 379 yoffset 462 size 14
        text "/" xoffset 404 yoffset 462 size 14
        $rcanDGDep = recruitDGeneratorCount - recruitedDGenerator
        text "[rcanDGDep]" xoffset 414 yoffset 462 size 14

        text "[rTempEMPCount]" xoffset 572 yoffset 462 size 14
        text "/" xoffset 597 yoffset 462 size 14
        $rcanEDep = recruitEMPCount - recruitedEMP
        text "[rcanEDep]" xoffset 607 yoffset 462 size 14

label recruitmentRoutine:
    $rRecruiting = True
    $rTempUntrained = shipUntrainedCount
    $rTempScoutCount = 0
    $rTempFighterCount = 0
    $rTempGeneratorCount = 0
    $rTempDGeneratorCount = 0
    $rTempEMPCount = 0
    
    if tutorial_recruitment:
        scene bg recruit
        G "Use this screen to up your troop count."
        G "Every turn, your star systems allow you to train a certain number of troops of each ship type, but remember, you cannot train more ships than you have available troops!"
        $tutorial_recruitment = False
    
    while(rRecruiting):
        window hide None
        call screen recruitment_image
        call recruitAction pass (_return)
        window show None
    return
    
label recruitAction(input):
    if input == "exit":
        $rRecruiting = False
    elif input == "helpScreen":
        call screen helpScreen
    elif input == "confirmRecruit":
        $rRecruiting = False
        $shipUntrainedCount = rTempUntrained
        $shipScoutCount += rTempScoutCount
        $shipFighterCount += rTempFighterCount
        $shipGeneratorCount += rTempGeneratorCount
        $shipDGeneratorCount += rTempDGeneratorCount
        $shipEMPCount += rTempEMPCount
        $recruitScoutCount -= rTempScoutCount
        $recruitFighterCount -= rTempFighterCount
        $recruitGeneratorCount -= rTempGeneratorCount
        $recruitDGeneratorCount -= rTempDGeneratorCount
        $recruitEMPCount -= rTempEMPCount
    elif input == "add10S":
        call addTroop pass (10, "scout")
    elif input == "add1S":
        call addTroop pass (1, "scout")
    elif input == "sub10S":
        call addTroop pass (-10, "scout")
    elif input == "sub1S":
        call addTroop pass (-1, "scout")
        
    elif input == "add10F":
        call addTroop pass (10, "fighter")
    elif input == "add1F":
        call addTroop pass (1, "fighter")
    elif input == "sub10F":
        call addTroop pass (-10, "fighter")
    elif input == "sub1F":
        call addTroop pass (-1, "fighter")
        
    elif input == "add10G":
        call addTroop pass (10, "generator")
    elif input == "add1G":
        call addTroop pass (1, "generator")
    elif input == "sub10G":
        call addTroop pass (-10, "generator")
    elif input == "sub1G":
        call addTroop pass (-1, "generator")
        
    elif input == "add10DG":
        call addTroop pass (10, "dGenerator")
    elif input == "add1DG":
        call addTroop pass (1, "dGenerator")
    elif input == "sub10DG":
        call addTroop pass (-10, "dGenerator")
    elif input == "sub1DG":
        call addTroop pass (-1, "dGenerator")   
    
    elif input == "add10E":
        call addTroop pass (10, "emp")
    elif input == "add1E":
        call addTroop pass (1, "emp")
    elif input == "sub10E":
        call addTroop pass (-10, "emp")
    elif input == "sub1E":
        call addTroop pass (-1, "emp")  
    return
    
label addTroop(number, type):
    
    
    if rTempUntrained < number:
        $number = rTempUntrained

    if type == "scout":
        if rTempScoutCount + number > recruitScoutCount:
            $number = recruitScoutCount - rTempScoutCount
        if rTempScoutCount + number < 0:
            $number = -rTempScoutCount
        $rTempScoutCount += number
        $rTempUntrained -= number
        
        
    elif type == "fighter":
        if rTempFighterCount + number > recruitFighterCount:
            $number = recruitFighterCount - rTempFighterCount
        if rTempFighterCount + number < 0:
            $number = -rTempFighterCount
        $rTempFighterCount += number
        $rTempUntrained -= number
        
        
    elif type == "generator":
        if rTempGeneratorCount + number > recruitGeneratorCount:
            $number = recruitGeneratorCount - rTempGeneratorCount
        if rTempGeneratorCount + number < 0:
            $number = -rTempGeneratorCount
        $rTempGeneratorCount += number
        $rTempUntrained -= number
        
        
    elif type == "dGenerator":
        if rTempDGeneratorCount + number > recruitDGeneratorCount:
            $number = recruitDGeneratorCount - rTempDGeneratorCount
        if rTempDGeneratorCount + number < 0:
            $number = -rTempDGeneratorCount
        $rTempDGeneratorCount += number
        $rTempUntrained -= number
        
        
    elif type == "emp":
        if rTempEMPCount + number > recruitEMPCount:
            $number = recruitEMPCount - rTempEMPCount
        if rTempEMPCount + number < 0:
            $number = -rTempEMPCount
        $rTempEMPCount += number
        $rTempUntrained -= number
        
    return
