import tingbot
from tingbot import *
import json, urllib

def default():
    screen.image('img/default.png')
    screen.text('Press a button to test', font_size=12, color='green')

default()

@left_button.up
@right_button.up
@midleft_button.up
@midright_button.up
def button_off():
    default()

button_pressed_text = '%s pressed'

@left_button.down
def button_left():
    screen.image('img/button_left.png')
    screen.text(button_pressed_text % ('Left'), font_size=12, color='green')
@right_button.down
def button_right():
    screen.image('img/button_right.png')
    screen.text(button_pressed_text % ('Right'), font_size=12, color='green')
@midleft_button.down
def button_middleleft():
    screen.image('img/button_midleft.png')
    screen.text(button_pressed_text % ('Middle left'), font_size=12, color='green')
@midright_button.down
def button_middleright():
    screen.image('img/button_midright.png')
    screen.text(button_pressed_text % ('Middle right'), font_size=12, color='green')

@touch()
def touch_screen(xy, action):
    screen.image('img/screen_touch.png')
    screen.text('Screen touched', font_size=12, color='green', xy=(160,70), align='top')
    if 'up' == action:
        default()


tingbot.run()
