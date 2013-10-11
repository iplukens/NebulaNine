###Define classes and other nice objects here so we can call them in the game
init python:
    
    class Laser(object):
        def __init__(self, x, y, dx , function=None):
            self.transform = Transform(child="laser.png", xanchor=0.5, yanchor=0.5, function=function)
            self.x = x + 80
            self.y = y + 35
            self.dx = dx
            self.dy = 0

    def laser_update(pilot, st, at):
        global last_time
        # The pilot is the first ball in our list, and he's the one
        # that gets last_time updated.
        if last_time is None:
            dt = 0
        else:
            dt = st - last_time

        last_time = st

        # Basic movement, and bouncing off the walls.
        for i in lasers:

            i.x += i.dx * dt
            i.y += 0


        # Update the transforms.
        for i in lasers:

            # This is the code that deals with Ren'Py to update the
            # various transforms. Note that we use absolute coordinates
            # to position ourselves with subpixel accuracy.
            i.transform.xpos = absolute(i.x)
            i.transform.ypos = absolute(i.y)
            i.transform.update()

        return 0
        
    ### check if owner has an adjacent territory to the player
    def owner_is_adjacent(owner):
        for i in adjacents:
            if territories[i].owner == owner:
                return True
        return False
    
    class Battalion:
        def __init__(self, type, count):
            self.type = type
            self.count = count      

    class stat_list(object):
        def __init__(self, attack, speed, initiative, defense, special, name):
            self.attack = attack
            self.speed = speed
            self.initiative = initiative
            self.defense = defense
            self.special = special
            self.name = name
    scout = stat_list(3, 1, 1, 1, "none", "_scout_ship")
    fighter = stat_list(5, 2, 3, 2, "none", "_fighter")
    generator = stat_list(2, 4, 2, 5, "Shield", "_row_shield_ship")
    dgenerator = stat_list(1, 4, 2, 5, "All-shield", "_shield_ship")
    emp = stat_list(3, 3, 4, 4, "EMP", "_emp_ship")
    command = stat_list(3, 3, 3, 3, "DREAM-BEAM", "_cc")

### BATTLE CLASSES -- SO MANY !!! ---
    class unit:
        def __init__(self, position, type, count, initiative, owner):
            self.position = position
            self.type = type
            self.count = count
            self.initiative = initiative
            self.owner = owner
            self.defending = False
            self.shield = 0
        def setDefending(self, input):
            self.defending = input
        def kill(self, number):
            if (number == 0):
                number = 1
            temp = self.shield
            self.shield -= number
            if (self.shield < 0):
                number -= temp
                self.shield = 0
            else:
                number = 0
            if (number >= self.count):
                number = self.count
                if self.type == command:
                    global shipCommandCount
                    shipCommandCount = 0
            if(self.owner == mPlayer):
                if self.type == scout:
                    global shipScoutCount
                    global deployedScoutCount
                    shipScoutCount -= number
                    deployedScoutCount -= number
                if self.type == fighter:
                    global shipFighterCount
                    global deployedFighterCount
                    shipFighterCount -= number
                    deployedFighterCount -= number
                if self.type == generator:
                    global shipGeneratorCount
                    global deployedGeneratorCount
                    shipGeneratorCount -= number
                    deployedGeneratorCount -= number
                if self.type == dgenerator:
                    global shipDGeneratorCount
                    global deployedDGeneratorCount
                    shipDGeneratorCount -= number
                    deployedDGeneratorCount -= number
                if self.type == emp:
                    global shipEMPCount
                    global deployedEMPCount
                    shipEMPCount -= number
                    deployedEMPCount -= number
            else:
                kill_count += number
            self.count -= number

    def remove_dead_units():
        length = len(unit_queue)
        i = 0
        while(i < length):
            if unit_queue[i].count == 0:
                unit_queue.pop(i)
                length = len(unit_queue)
            i += 1
        return
        # bubble SORT WOOOOO
    def sort_units():
        swapped = True
        while(swapped):
            swapped = False
            for i in range(0, len(unit_queue) - 1):
                if unit_queue[i].initiative > unit_queue[i + 1].initiative:
                    temp = unit_queue[i]
                    unit_queue[i] = unit_queue[i+1]
                    unit_queue[i+1] = temp
                    swapped = True
        return

    def draw_queue():
        queue_string = unit_queue[0].owner.color_code + unit_queue[0].type.name + "{/color}"
        for i in range(1, len(unit_queue)):
            queue_string += ", " + unit_queue[i].owner.color_code + unit_queue[i].type.name + "{/color}"
        ui.text(queue_string, xoffset=10, yoffset=30)
        return
        
    def draw_ships():
        for i in range(0, len(unit_queue)):
            ship_name =  unit_queue[i].owner.name + unit_queue[i].type.name + ".png"
            pos = unit_queue[i].position
            count = str(unit_queue[i].count)
            shield = "{color=#00f}" + str(unit_queue[i].shield) + "{/color}"
            if pos < 3:
                if i == 0:
                    ui.imagebutton("active_unit_indicator.png", "active_unit_indicator.png", xpos=675, ypos=330+(pos*90))
                ui.imagebutton(ship_name, ship_name, xpos=675, ypos=330+(pos*90))
                ui.text(count, xoffset=675+80, yoffset=330+(pos*90)+55)
                ui.text(shield, xoffset=675+80, yoffset=330+(pos*90))
            elif pos < 5:
                if i == 0:
                    ui.imagebutton("active_unit_indicator.png", "active_unit_indicator.png", xpos=510, ypos=395+((pos-3)*90))
                ui.imagebutton(ship_name, ship_name, xpos=510, ypos=395+((pos-3)*90))
                ui.text(count, xoffset=510+80, yoffset=395+((pos-3)*90)+55)
                ui.text(shield, xoffset=510+80, yoffset=395+((pos-3)*90))
            elif pos < 8:
                if i == 0:
                    ui.imagebutton("active_unit_indicator.png", "active_unit_indicator.png", xpos=60, ypos=330+((pos - 5)*90))
                ui.imagebutton(ship_name, ship_name, xpos=60, ypos=330+((pos - 5)*90))
                ui.text(count, xoffset=60+80, yoffset=330+((pos-5)*90)+55)
                ui.text(shield, xoffset=60+80, yoffset=330+((pos-5)*90))
            else:
                if i == 0:
                    ui.imagebutton("active_unit_indicator.png", "active_unit_indicator.png", xpos=225, ypos=395+((pos-8)*90))
                ui.imagebutton(ship_name, ship_name, xpos=225, ypos=395+((pos-8)*90))
                ui.text(count, xoffset=225+80, yoffset=395+((pos-8)*90)+55)
                ui.text(shield, xoffset=225+80, yoffset=395+((pos-8)*90))
        return
    def draw_battle_hotspots():
        for i in range(0, len(unit_queue)):
            button_ground = "unit_button_ground.png"
            button_hover = "unit_button_hover.png"
            pos = unit_queue[i].position
            if pos < 3:
                ui.imagebutton(button_ground, button_hover, xpos=675, ypos=330+(pos*90), clicked=ui.returns(pos))
            elif pos < 5:
                ui.imagebutton(button_ground, button_hover, xpos=510, ypos=395+((pos-3)*90), clicked=ui.returns(pos))
        return

#### positions for the ai actions
#elif pos < 8:
#ui.imagebutton(button_ground, button_hover, xpos=60, ypos=330+((pos - 5)*90), clicked=ui.returns(pos))
#else:
#ui.imagebutton(button_ground, button_hover, xpos=225, ypos=395+((pos-8)*90), clicked=ui.returns(pos))

#### LOOK OVER THIS - should shield ships also get shields?
    def up_shields():
        if unit_queue[0].type == generator:
            for i in unit_queue:
                if i.owner == unit_queue[0].owner:
                    if unit_queue[0].position < 3 and i.position < 3:
                        i.shield += unit_queue[0].count / 2
                    elif unit_queue[0].position < 5 and i.position < 5:
                        i.shield += unit_queue[0].count / 2
                    elif unit_queue[0].position < 8 and i.position < 8:
                        i.shield += unit_queue[0].count / 2
                    else:
                        i.shield += unit_queue[0].count / 2
        else:
            for i in unit_queue:
                if i.owner == unit_queue[0].owner:
                    i.shield += unit_queue[0].count / 3

    def get_dead_attack(attacker, defendee):
        if defendee.defending:
            d_attack_val = ((defendee.type.attack + defendee.type.defense) / 2) * defendee.count * 1.5 / 2
        else:
            d_attack_val = ((defendee.type.attack + defendee.type.defense) / 2) * defendee.count / 2
        dead_attack = d_attack_val / (attacker.type.defense * 2)
        return dead_attack

    def get_dead_defense(attacker, defendee):
        if defendee.defending:
            dead_defense = (attacker.type.attack * attacker.count) / (defendee.type.defense * 2)
        else:
            dead_defense = (attacker.type.attack * attacker.count) / defendee.type.defense
        if defendee.position < 3 or (defendee.position > 4 and defendee < 8):
            dead_defense = dead_defense * .5
        return dead_defense

    def attack_them(attacker, defendee):
        dead_attack = get_dead_attack(attacker, defendee)
        dead_defense = get_dead_defense(attacker, defendee)
        attacker.kill(int(dead_attack))
        defendee.kill(int(dead_defense))
        draw_attack_animation(attacker, defendee)

    def check_shields():
        result = False
        for i in unit_queue:
            if i.owner == mPlayer:
                if i.shield > 0:
                    result = True
                    break
        return result

    def cpu_attack():
        best_attack = 0
        defendee = 0
        for i in unit_queue:
            if i.owner == mPlayer:
                new_attack = get_dead_attack(unit_queue[0], i)
                if new_attack > best_attack:
                    best_attack = new_attack
                    defendee = i
        if best_attack == 0:
            unit_queue[0].setDefending(True)
        else:
            attack_them(unit_queue[0], defendee)
        return

    def find_guy(position):
        for i in range (0, len(unit_queue)):
            if unit_queue[i].position == position:
                return i
        return -1
            
    def dream_beam(guy):
        ship_name = "d_cc.png"
        ui.imagebutton(ship_name, ship_name, xpos=20, ypos=100)
        guy.count = 0
        
    def wipeShields():
        for i in range (0, len(unit_queue)):
            if unit_queue[i].owner != unit_queue[0].owner:
                unit_queue[i].shields = 0
            
    def check_counts():
        global enemy_count
        global player_count
        enemy_count = 0
        player_count = 0
        for i in unit_queue:
            if i.owner == mPlayer:
                player_count += i.count
            else:
                enemy_count += i.count
        return
        
    def draw_attack_animation(attacker,defender):
    
    #Sets the offset we will draw at, this way player is always on the left
        if attacker.owner != mPlayer:
            xAttackerOffset = 520
            xDefenderOffset = 25
        else:
            xAttackerOffset = 25
            xDefenderOffset = 520
    
    #Sets up the ship count we will use, only exception is Command Center is always 1
        if attacker.type.name == "command":
            attackShips = 1
        else :
            attackShips = 1 + attacker.count/10
    
        if defender.type.name == "command":
            defendShips = 1
        else :
            defendShips = 1 + defender.count/10
    
        ship_name =  attacker.owner.name + attacker.type.name + ".png"
        
        global last_time
        last_time = None
        global lasers
        lasers = [Laser(0, 900, 1000, function=laser_update)]
        for i in range (0 , attackShips):
            xcoord = renpy.random.randint(0, 280)
            ycoord = renpy.random.randint(60, 300)
            
            if attacker.owner == mPlayer:
                lasers.append(Laser(xAttackerOffset + xcoord, ycoord, 1000))
            else:
                lasers.append(Laser(xAttackerOffset + xcoord, ycoord, -1000))
                
            ui.imagebutton(ship_name, ship_name, xpos=xAttackerOffset + xcoord, ypos=ycoord)
        ship_name =  defender.owner.name + defender.type.name + ".png"
        for i in range (0 , defendShips):
            xcoord = renpy.random.randint(0, 280)
            ycoord = renpy.random.randint(60, 300)
            ui.imagebutton(ship_name, ship_name, xpos=xDefenderOffset + xcoord, ypos=ycoord)
            
        for i, b in enumerate(lasers):
            renpy.show("lasers%d" % i, what=b.transform)
        return
