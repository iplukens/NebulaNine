transform beam_animation:
    "dream_beam1.png"
    pause .15
    "dream_beam2.png"
    pause .15
    "dream_beam3.png"
    pause .15
    "dream_beam4.png"
    pause .15
    "dream_beam5.png"
    pause .15
    "dream_beam6.png"
    pause .15
    repeat

image dreambeam:
    contains beam_animation
    xpos 510
    ypos 155

image eyelasersright:
    contains beam_animation
    xpos 520
    ypos 190

image eyelasersleft:
    contains beam_animation
    xpos 470
    ypos 180
    
image robbitpunch:
    "r_bust_angry_eye.png"
    linear 1.0 xalign 0.4
    repeat
    
transform transpa:

    alpha 0.5