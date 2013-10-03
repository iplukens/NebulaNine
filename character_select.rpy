image female = "sf_bust_neutral.png"
image male = "sm_bust_neutral.png"

screen character_select:
    imagemap:
        ground "space_1.png"
        imagebutton:
            idle "sf_bust_neutral.png"
            hover "sf_bust_happy.png"
            xpos 0
            ypos 100
            action Return("female")
        imagebutton:
            idle "sm_bust_neutral.png"
            hover "sm_bust_happy.png"
            xpos 550
            ypos 100
            action Return("male")
        imagebutton:
            idle "character_select_text.png"
            hover "character_select_text.png"
            xpos 240
            ypos 50

### shorthand function for display_character_left
label dcl(mood):
    call display_character_left(mood)
    return

### displays the correct main character gender
### input = their mood of either happy, neutral, or sad
label display_character_left(mood):
    if bGender == "male":
        if mood == "happy":
            show mcharacter happy at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
        if mood == "neutral":
            show mcharacter neutral at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
        if mood == "angry":
            show mcharacter angry at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
    else:
        if mood == "happy":
            show fcharacter happy at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
        if mood == "neutral":
            show fcharacter neutral at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
        if mood == "angry":
            show fcharacter angry at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
    return

# call display_love_character
label dll(mood):
    call display_love_left(mood)
    return

### displays the correct love interest character gender
### input = their mood of either happy, neutral, or sad
label display_love_left(mood):
    if aGender == "male":
        if mood == "happy":
            show mlove happy at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
        if mood == "neutral":
            show mlove neutral at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
        if mood == "angry":
            show mcharacter angry at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
    else:
        if mood == "happy":
            show flove happy at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
        if mood == "neutral":
            show flove neutral at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
        if mood == "angry":
            show flove angry at Position(xpos = 0, xanchor = 0, ypos = 1.0, yanchor = 500)
    return

### hides the correct gender model of the character depending on input
### input = their mood of either happy, neutral, or sad
label hide_character(mood):
    if bGender == "male":
        if mood == "happy":
            hide mcharacter happy
        if mood == "neutral":
            hide mcharacter neutral
        if mood == "angry":
            hide mcharacter angry
    else:
        if mood == "happy":
            hide fcharacter happy
        if mood == "neutral":
            hide fcharacter neutral
        if mood == "angry":
            hide fcharacter angry
    return