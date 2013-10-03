label territory_upgrade(territory):
    call screen territory_menu
    $result = _return
    if result != "exit":
        show gaius neutral at right
        $territory.setUpgraded()
    if result == "3un":
        $territory.units_per_turn.untrained_add(territory.upgrade_num.untrained)
        $recruitUntrainedCount += territory.upgrade_num.untrained
        G "A wise decision.  I will increase the recruitment on this star."
    elif result == "2s":
        $territory.units_per_turn.scout_add(territory.upgrade_num.scout)
        $recruitScoutCount += territory.upgrade_num.scout
        G "A wise decision.  Scouting production of this territory shall go up accordingly."
    elif result == "2f":
        $territory.units_per_turn.fighter_add(territory.upgrade_num.fighter)
        $recruitFighterCount += territory.upgrade_num.fighter
        G "A wise decision.  More fighters will make our enenmies tremble."
    elif result == "1r":
        $territory.units_per_turn.generator_add(territory.upgrade_num.generator)
        $recruitGeneratorCount += territory.upgrade_num.generator
        G "A wise decision.  I will work towards increasing the facilities for training row shield ships."
    elif result == "1a":
        $territory.units_per_turn.dGenerator_add(territory.upgrade_num.dGenerator)
        $recruitDGeneratorCount += territory.upgrade_num.dGenerator
        G "A wise decision.  I will make sure production allows for more shield ships."
    elif result == "1e":
        $territory.units_per_turn.emp_add(territory.upgrade_num.emp)
        $recruitEMPCount += territory.upgrade_num.emp
        G "A wise decision.  I will up the manufacture of emp devices."
    return

screen territory_menu:
    add "space_nebula_ground.png" xalign 0 yalign 0
    if territory.upgraded:
        add "production_per_turn.png" at Position(xpos=0, xanchor=0, ypos=120, yanchor=0)
        text "[territory.units_per_turn.untrained]" xpos 42 ypos 240
        text "[territory.units_per_turn.scout]" xpos 172 ypos 240
        text "[territory.units_per_turn.fighter]" xpos 302 ypos 240
        text "[territory.units_per_turn.generator]" xpos 432 ypos 240
        text "[territory.units_per_turn.dGenerator]" xpos 562 ypos 240
        text "[territory.units_per_turn.emp]" xpos 692 ypos 240
        textbutton "Cancel" xpos 0.43 ypos 440 action Return("exit")
    else:
        add "production_per_turn.png" at Position(xpos=0, xanchor=0, ypos=0, yanchor=0)
        text "[territory.units_per_turn.untrained]" xpos 42 ypos 120
        text "[territory.units_per_turn.scout]" xpos 172 ypos 120
        text "[territory.units_per_turn.fighter]" xpos 302 ypos 120
        text "[territory.units_per_turn.generator]" xpos 432 ypos 120
        text "[territory.units_per_turn.dGenerator]" xpos 562 ypos 120
        text "[territory.units_per_turn.emp]" xpos 692 ypos 120
        if territory.upgrade_num.untrained != 0:
            textbutton "+[territory.upgrade_num.untrained] untrained per turn" xpos 200 ypos 200 action Return("3un")
        if territory.upgrade_num.scout != 0:
            textbutton "+[territory.upgrade_num.scout] scouts per turn" xpos 200 ypos 240 action Return("2s")
        if territory.upgrade_num.fighter != 0:
            textbutton "+[territory.upgrade_num.fighter] fighters per turn" xpos 200 ypos 280 action Return("2f")
        if territory.upgrade_num.generator != 0:
            textbutton "+[territory.upgrade_num.generator] row shields per turn" xpos 200 ypos 320 action Return("1r")
        if territory.upgrade_num.dGenerator != 0:
            textbutton "+[territory.upgrade_num.dGenerator] all shields per turn" xpos 200 ypos 360 action Return("1a")
        if territory.upgrade_num.emp != 0:
            textbutton "+[territory.upgrade_num.emp] emps per turn" xpos 200 ypos 400 action Return("1e")
        textbutton "Cancel" xpos 200 ypos 440 action Return("exit")