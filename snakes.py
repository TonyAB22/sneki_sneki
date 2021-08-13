import curses

curses.initscr()
win = curses.newwin(20, 60, 0, 0)
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
curses.initscr() #initialize screen
window = curses.newwin(30, 60, 0, 0) #create new window H=30, W=60
window.keypad(True) #enable keypad
curses.noecho() #turn off automatic echoing of keys to the screen
curses.curs_set(0)
window.nodelay(True) #do not wait for the user input
#for games
