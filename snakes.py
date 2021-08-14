# Sneki_Sneki Game

import turtle
import curses 
import time 
import random 

# Initializing Screen
win = turtle.Screen()
win.title("Sneki's Game") #screen title
win.bgcolor("violet") #background color
win.setup(w=500,h=500) #window width, height
win.tracer(0) #turn off screen updates

# Keyboard Bindings
win.keypad(True) #enable keypad
win.listen()
win.onkeypress(go_up, "w") #bindings for up
win.onkeypress(go_down, "s") #bindings for down
win.onkeypress(go_right, "d") #bindings for right
win.onkeypress(go_left, "a") #bindings for left

#Initiate Values
key = KEY_RIGHT #wala ko kasabot ngano key right
score = 0 #default scoring

# Snake Head Values
head = turtle.Turtle()
head.speed (0) #snake speed
head.shape("square") #snake shape 
head.color("black") #snake color
head.penup()
head.goto(0,100)
head.direction = "stop"

# Snake Food Values 
food = turtle.Turtle()
food.speed (0)
food.shape("triangle")
food.color("blue")
food.penup(0)
food.goto(0,100)

# Initialize Startup Food and Snake Coordinates
snake = [[0,0], [0,0], [0,0] #input values for snake
food = [0,0]


# Misc. Codes Haha
from curses. import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
window.keypad(True) #enable keypad
curses.curs_set(0)

win = tintinoo
whyarewehere = "just to sufffer"
HAHAHHAAHA

x = 3
