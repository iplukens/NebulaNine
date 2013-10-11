image bg battle = "battle_ground.png"

label battle_routine:
    $unit_queue = []
    call battle_init
    while(battle_on):
        window hide None
        scene bg battle
        $draw_queue()
        $draw_ships()
        $remove_dead_units()
        $sort_units()
        $unit_queue[0].setDefending(False)
        if unit_queue[0].owner == mPlayer:
            call player_battle
        else:
            pause (1.0)
            call ai_battle
        $unit_queue[0].initiative += unit_queue[0].type.speed
        call update_battle
    call battle_end
    window show None
    return
    
screen battle_input:
    imagemap:
        auto "battle_%s.png"
        $draw_queue()
        $draw_ships()
        textbutton "Attack!" xpos 330 ypos 60 action Return("attack")
        textbutton "Defend!" xpos 330 ypos 125 action Return("defend")
        if unit_queue[0].type.special != "none":
            textbutton "[unit_queue[0].type.special]!" xpos 330 ypos 190 action Return("special")
        textbutton "Surrender!" xpos 330 ypos 155 action Return("surrender")
    
screen draw_ships_clickable:
    imagemap:
        auto "battle_%s.png"
        $draw_queue()
        $draw_ships()
        $draw_battle_hotspots()

label ai_battle:
    if unit_queue[0].type == emp:
        if check_shields():
            $wipeShields()
            play sound "emp.mp3"
        else:
            $cpu_attack()
    elif unit_queue[0].type == fighter or unit_queue[0].type == scout:
        $cpu_attack()
        play sound "laser.wav"
        with hpunch
    else:
        $num = renpy.random.randint(0, 1)
        if num > 0.25:
            $up_shields()
        else:
            $cpu_attack()
    return

label player_battle:
    call screen battle_input
    $b_result = _return
    if b_result == "attack":
        call attack_routine
    elif b_result == "defend":
        $unit_queue[0].setDefending(True)
    elif b_result == "special":
        call special_routine
    else:
            call surrender
    return

label attack_routine:
    call screen draw_ships_clickable
    $position_index = _return
    $attack_them(unit_queue[0], unit_queue[find_guy(position_index)])
    $ renpy.play('laser.wav')
    with hpunch
    pause(1.0)
    return

label special_routine:
    if unit_queue[0].type == command:
        $beamed = True
        call screen draw_ships_clickable
        $position_index = _return
        $dream_beam(unit_queue[find_guy(position_index)])
        show dreambeam
        pause(1.0)
    if unit_queue[0].type == emp:
        $wipeShields()
        play sound "emp.mp3"
    if unit_queue[0].type == generator or unit_queue[0].type == dgenerator:
        $up_shields()
    return

label surrender:
    G "We must retreat, [miperson]."
    $battle_on = False
    $territory.setOwner(enemy)
    return

label battle_end:
    play music "theme.mp3"
    return

label update_battle:
    $check_counts()
    if shipCommandCount == 0:
        G "SIR...SIR...SIRRRRRRR!"
        call game_over
    if enemy_count == 0 or player_count == 0:
        $battle_on = False
    if enemy_count == 0 and player_count == 0:
        G "This contest has reached an impasse, [miperson]."
    elif player_count == 0:
        G "We have been defeated, [miperson]!"
        $territory.setOwner(enemy)
    elif enemy_count == 0:
        G "A glorious victory, [miperson!]"
        $territory.setOwner(mPlayer)
    return

label battle_init:
    $enemy_count = 0
    $player_count = 0
    $beamed = False
    $battle_on = True
    $enemy_army = enemy.army
    python:
        for i in range(0, len(enemy_army)):
            if (enemy_army[i].type == "scout"):
                unit_queue.append(unit(i, scout, enemy_army[i].count + turnCount, scout.initiative, enemy))
            if (enemy_army[i].type == "fighter"):
                unit_queue.append(unit(i, fighter, enemy_army[i].count + turnCount, fighter.initiative, enemy))
            if (enemy_army[i].type == "generator"):
                unit_queue.append(unit(i, generator, enemy_army[i].count + turnCount, generator.initiative, enemy))
            if (enemy_army[i].type == "dgenerator"):
                unit_queue.append(unit(i, dgenerator, enemy_army[i].count + turnCount, dgenerator.initiative, enemy))
            if (enemy_army[i].type == "emp"):
                unit_queue.append(unit(i, emp, enemy_army[i].count + turnCount, emp.initiative, enemy))
        for i in range(0, len(aFullArmy)):
            if (aFullArmy[i].type == "scout"):
                unit_queue.append(unit(i + 5, scout, aFullArmy[i].count, scout.initiative, mPlayer))
            if (aFullArmy[i].type == "fighter"):
                unit_queue.append(unit(i + 5, fighter, aFullArmy[i].count, fighter.initiative, mPlayer))
            if (aFullArmy[i].type == "generator"):
                unit_queue.append(unit(i + 5, generator, aFullArmy[i].count, generator.initiative, mPlayer))
            if (aFullArmy[i].type == "dgenerator"):
                unit_queue.append(unit(i + 5, dgenerator, aFullArmy[i].count, dgenerator.initiative, mPlayer))
            if (aFullArmy[i].type == "emp"):
                unit_queue.append(unit(i + 5, emp, aFullArmy[i].count, emp.initiative, mPlayer))
            if (aFullArmy[i].type == "command"):
                unit_queue.append(unit(i + 5, command, (aFullArmy[i].count + 4) * turnCount, command.initiative, mPlayer))
    return