# 08/27/21 Blake Butsko snake using object oriented method and pygame, doing in the OOP methodology is not the fastest but we'll learn more

import math
import random
import pygame #may need to download module to computer  Did pip install pygame then had to update
import tkinter as tk   #GUI toolkit
from tkinter import messagebox

class cube(object): #(object) creates cube 'food' as object
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass
    def move(self, dirnx, dirny):
        pass
    def draw(self, surface, eyes =False):
        pass

class snake(object): #inherits/contains cube objects  - gonna have a list of cubes that make up the body
    body = []
    turns = {} #dictionary
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos) #cube at starting position
        self.body.append(self.head) #adds cube to list
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #always code this in first so you can actually exit
                pygame.quit()
            keys = pygame.key.get_pressed() #alternative to doing if up key pressed go up, if down key pressed go down, if ...... -> the function gives a dictionary or something of all keys and a 1 or 0 if they were pressed or not
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] # creates new key in dictionary to record where the key was pressed and where the rest of the cubes/body should turn and how the snake actually turned
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:   #uses elif so it doesn't take more than one command and takes the last key press
                    self.dirnx = 0
                    self.dirny = 1   #y axis in pygame is funky
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i,c in enumerate(self.body): #i-index,c-cube in the self.body array
            p = c.pos[:]  #The [:] creates a copy of the pos list as to not erase any past things
            if p in self.turns: #if position is in the turns list get the direction value and location 
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1: #-1 on last cube remove the turn
                    self.turns.pop(p)
        # else:
        #     if c.dirnx

    def reset(self, pos): 
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        pass

def draw_grid(w, rows, surface):
    size_btwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x += size_btwn
        y += size_btwn

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y)) #draws two lines every loop given (color, start, and end point) the first line is vertical the next is horizontal

def redraw_window(surface):
    global rows, width #using global you got the variables from the main argument
    surface.fill((0,0,0))
    draw_grid(width, rows, surface)
    pygame.display.update()

def random_snack(rows, items):
    pass

def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 500
    rows = 20 #has to devide 500 evenly if you set it to a smaller number it will be harder for the player due to the small space
    win = pygame.display.set_mode((width, width)) #creating display window -> using width as height
    s = snake((255,0,0), (10,10)) #filling __init__ instanciating a snake I think also 10,10 is the middle if rows is 20
    flag = True

    clock = pygame.time.Clock() #prevents game from running faster than ten frames a second (snake can only move less than ten spaces a second)

    while flag:
        pygame.time.delay(50) #pygame tick delays game by 50 milisecs so it doesn't run too fast 
        clock.tick(10) #lower this goes the slower the game is gonna run, opposite of delay value
        redraw_window(win)

    pass








main()
