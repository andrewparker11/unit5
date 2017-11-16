#Andrew Parker
#11/16/17
#betterColorWindow.py - improves color change window

from ggame import *
from random import randint
randint (0,1)

Colors = [Color(0xFFFFFF,1), Color(0x000000,1), Color(0xFF0000,1), Color(0xFFFF00,1),Color(0xFFA500,1), Color(0x00FF00,1), Color(0x00FFFF,1), Color(0x0000FF,1), Color(0x7F00FF,1), Color(0xFF007F,1)] 
#white = black = red =  yellow = orange = green =  lightBlue =  blue =  purple =  darkPink =  

blackOutline = LineStyle(1,black) #pixels, color

def mouseClick(event):
    num = randint(1,10)
    if num == 1:
        color = colors[0]
    elif num == 2:
        color = colors[1]
    elif num == 3:
        color = colors[2]
    elif num == 4:
        color = colors[3]
    elif num == 5:
        color = colors[4]
    elif num == 6:
        color = colors[5]
    elif num == 7:
        color = colors[6]
    elif num == 8:
        color = colors[7]
    elif num == 9:
        color = colors[8]
    else:
        color = darkPink
        
    rectangle = RectangleAsset(970,500,blackOutline,color)
    Sprite(rectangle,(25,15))

App().listenMouseEvent('click',mouseClick)
App().run()