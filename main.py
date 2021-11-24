from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(270)

#Declare variables for humidity, and maybe
#for temeprature
humidness = sense.get_humidity()

#Declare colors:
#Example: red=(255,0,0)
#
#Astro Pi Uses only RGB colors and
#will only read defined ones

#Colors stuff (don't touch pls)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,233,0)

#More colors but for pixel art
y=(255,255,0)
y_2=(255,200,0)
y_3=(255,150,0)
g=(10,155,30)
b=(0,0,0)
cy=(50,240,235)
gr=(125,125,125)
w=(255,255,255)

#Art time :D
dry=[cy, cy, cy, cy, cy, y, y, y,
     cy, cy, cy, cy, cy, cy, y, y,
     cy, g, g, cy, cy, y, cy, y,
     cy, g, g, g, cy, cy, cy, cy,
     g, g, g, cy, cy, gr, gr, cy,
     cy, g, g, cy, cy, gr, gr, cy,
     y_2, y_2, y_3, y_3, y_3, y_3, y_2, y_2,
     y, y, y_2, y_2, y, y, y_3, y_3
     ]

wet=[cy, cy, cy, cy, cy, cy, cy, cy,
     cy, w, w, w, w, w, w, cy,
     w, w, w, w, w, w, w, w,
     w, w, w, w, w, w, w, w,
     cy, cy, blue, cy, cy, cy, blue, cy,
     blue, cy, cy, cy, blue, cy, cy, cy,
     cy, cy, cy, cy, cy, cy, cy, blue,
     cy, blue, cy, cy, blue, cy, cy, cy
     ]

#The gift
rp=(214,0,121)
rp2=(255,0,65)
rg=(3, 150, 50)
rg2=(0,225,50)

raspberry=[w, rg, rg, w, w, rg, rg, w,
           w, rg2, rg2, rg2, rg2, rg2, rg2, w,
           w, w, rp, rp2, rp2, rp, w, w,
           w, rp, rp2, rp, rp, rp2, rp, w,
           w, rp2, rp, rp2, rp2, rp, rp2, w,
           w, rp, rp2, rp, rp, rp2, rp, w,
           w, rp2, rp, rp2, rp2, rp, rp2, w,
           w, w, rp2, rp, rp, rp2, w, w
           ]

sense.show_message("My name should be Alan Turing", scroll_speed=0.025, text_colour=green, back_colour=rp)
sleep(1)
if humidness < 40:
  sense.show_message("It is quite dry right?", scroll_speed=0.025, text_colour=blue, back_colour=y_3)
  sleep(1)
  sense.set_pixels(dry)
  sleep(1)
  sense.show_message("Good luck Space Astronauts!", scroll_speed=0.025, text_colour=cy, back_colour=blue)
  sense.set_pixels(raspberry)
else:
  sense.show_message("It sure is humid here huh...", scroll_speed=0.025, text_colour=yellow, back_colour=blue)
  sleep(1)
  sense.set_pixels(wet)
  sleep(1)
  sense.show_message("Good luck Space Astronauts!", scroll_speed=0.025, text_colour=cy, back_colour=blue)
  sense.set_pixels(raspberry)
