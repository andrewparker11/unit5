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
        color = white
    elif num == 2:
        color = black
    elif num == 3:
        color = red
    elif num == 4:
        color = yellow
    elif num == 5:
        color = orange
    elif num == 6:
        color = green
    elif num == 7:
        color = lightBlue
    elif num == 8:
        color = blue
    elif num == 9:
        color = purple
    else:
        color = darkPink
        
    rectangle = RectangleAsset(970,500,blackOutline,color)
    Sprite(rectangle,(25,15))

App().listenMouseEvent('click',mouseClick)
App().run()