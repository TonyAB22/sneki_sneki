# Sneki_Sneki Game

import turtle
import curses 
import time 
import random 

# Initializing Screen
win = turtle.Screen()
win.title("Sneki's Game") #screen title
win.bgcolor("purple") #background color
win.setup(w=500,h=500) #window width, height
win.tracer(0) #turn off screen updates

# Keyboard Bindings
win.keypad(True) #enable keypad
win.listen()
win.onkeypress(go_up, "w") #bindings for up
win.onkeypress(go_down, "s") #bindings for down
win.onkeypress(go_right, "d") #bindings for right
win.onkeypress(go_left, "a") #bindings for left

# Display Score Values
pen = turtle.Turtle()
pen.speed(0) 
pen.shape("square") #score shape
pen.color("white") #score color 
pen.penup() #score path
pen.hideturtle() #hide path
pen.goto (0, 160) #position
pen.write("Score: 0 High Score: {}".format(high_score), align ="center", font=("Garamond", 21, "bold")) #score display
score = 0 #default scoring 
high_score = 0

# Snake Head Values
head = turtle.Turtle() #snake 
head.speed (0) #snake movement
head.shape("square") #snake shape 
head.color("white") #snake color
head.penup() #path taken by snake
head.goto(0,100) #snake position
head.direction = "stop" #snake direction 

# Snake Food Values 
food = turtle.Turtle()
food.speed (0)
food.shape("circle")
food.color("black")
food.penup(0) #path taken by food
food.goto(0,100)

# Initialize Startup Food and Snake Coordinates
snake = [[0,0], [0,0], [0,0] #input values for snake
food = [0,0] #input values for food

#Increase the Score
score = score+5
if score > high_score: 
    high_score = score

#Rest Score 



# Misc. Codes Haha
from curses. import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
window.keypad(True) #enable keypad
curses.curs_set(0)

win = tintinoo
whyarewehere = "just to sufffer"
HAHAHHAAHA

x = 3
