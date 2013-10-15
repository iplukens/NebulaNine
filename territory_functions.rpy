init python:
    def get_attacked_territory(owner):
        for i in territories:
            if i.owner == owner:
                for x in i.adjacents:
                    if territories[x].owner == mPlayer:
                        global territory
                        territory = territories[x]

    def highlight_territory():
        for i in range (0, 18):
            if territories[i] == territory:
                star_name_hover = "system" + str(i-1) + "_owned_yellow.png"
                ui.imagebutton(star_name_hover, star_name_hover, xpos=territories[i].x0, ypos=territories[i].y0)
    def gaius_conquer():
        for i in territories:
            if i.owner != mPlayer:
                i.setOwner(mG)
    def has_territories(owner):
        for i in territories:
            if i.owner == owner:
                return True
        return False

label set_recruitment:
    $recruitUntrainedCount = 0
    $recruitScoutCount = 0
    $recruitFighterCount = 0
    $recruitGeneratorCount = 0
    $recruitDGeneratorCount = 0
    $recruitEMPCount = 0
    python:
        for x in territories:
            if x.owner == mPlayer:
                recruitUntrainedCount += x.units_per_turn.untrained
                recruitScoutCount += x.units_per_turn.scout
                recruitFighterCount += x.units_per_turn.fighter
                recruitGeneratorCount += x.units_per_turn.generator
                recruitDGeneratorCount += x.units_per_turn.dGenerator
                recruitEMPCount += x.units_per_turn.emp


label set_adjacents:
    $adjacents = []
    python:
        for t in territories:
            t.setNotAdjacent()
        for x in territories:
            if x.owner == mPlayer:
                for y in x.adjacents:
                    adjacents.append(y)
                    territories[y].setIsAdjacent()
    return
    
label set_production:
    python:
        for t in territories:
            t.setNotUpgraded()
    return

label takeOver:
    $territory.setOwner(winner)
    return

label take_all_AH:
    python:
        for t in territories:
            if t.owner == mAH:
                t.setOwner(mPlayer)
    return