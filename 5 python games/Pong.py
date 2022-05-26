# 08/09/2021 11:34pm 6-7/10 intoxication
# Change header when you put it in your portfolio if you don't then then to the empolyer that is seeing this I've moved on to bigger and better things and no longer have time to read my own comments c'est la vie
# "Learn Python by Building Five Games - Full Course" https://www.youtube.com/watch?v=XGf2GcyHPhc

# Built on turtle module (basic graphics)
# "for beginers so not using obj orienting prog not really using classes except as it relates to the turtle"
# old school programming

import turtle
import winsound
import sys

# creation of window/screen (lil window where the game shows up)
wn = turtle.Screen()
wn.title('A Pong Without Ping')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0) # stops window from updating (have to manually update), speeds up game

# Score
score_a = 0
score_b = 0

# Paddle A (left)
paddle_a = turtle.Turtle()  #Turtle object (class of turle inherits it's methods, properties, and such)
paddle_a.speed(0) #speed of animation (sets speed to max possible)
paddle_a.shape('square') #Built in shape (delfault 20 by 20 pixels)
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=7, stretch_len=1) #factor of 5 and 1 (5*20,1*20)
paddle_a.penup() #Don't draw while moving (you know this part)
paddle_a.goto(-350,0) #start at (also know this)

# Paddle B (Right)
paddle_b = turtle.Turtle()  
paddle_b.speed(0) 
paddle_b.shape('square') 
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=7, stretch_len=1) 
paddle_b.penup() 
paddle_b.goto(350,0) #Test program at each stage (obviously)

# Ball
ball = turtle.Turtle()  
ball.speed(0) 
ball.shape('square') 
ball.color('white')
ball.penup()
ball.goto(0,0) #Test program at each stage (obviously)
ball.dx = 0.1 #dx means delta x might want to mess with so it looks good
ball.dy = -0.1 #everytime the ball moves it moves by 2 pixels

# Pen (Scoring)
pen = turtle.Turtle()
pen.speed
pen.color('White')
pen.penup()
pen.hideturtle() #Don't want to see it just the text it will write
pen.goto(0,260)
pen.write('Player A: 0  Player B: 0', align = 'center', font = ('courier',24,'bold'))

# Functions (move paddles up and down)
def paddle_a_up():
    y = paddle_a.ycor() #ycor is a method from the turtle module that returns the y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #ycor is a method from the turtle module that returns the y coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #ycor is a method from the turtle module that returns the y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #ycor is a method from the turtle module that returns the y coordinate
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, 'w') #on pressing w call the paddle up function
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up') #Capitalize!!
wn.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    # everytime the loop runs it updates the screen
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) #everytime it goes through the loop it updates the x position by 2
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)  #asynchronous
    elif ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0) #could change to -390 and have a continous ball
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(score_a,score_b), align = 'center', font = ('courier',24,'bold'))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    elif ball.xcor()<-390:
        ball.goto(0,0) 
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(score_a,score_b), align = 'center', font = ('courier',24,'bold'))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # Paddle and ball collisons
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1 
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)