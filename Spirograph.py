# Blake Butsko 5/31/2021
import turtle


# background color
turtle.bgcolor("black")

turtle.pensize(2)
# no animation for drawing (0) is the fastest speed
turtle.speed(0)

# making the circles to be displayed
for x in range(5):
    # iterates through the circle colors
    for colors in ['red','magenta','blue','cyan','green','yellow','white']:
        turtle.color(colors)
        turtle.circle(100)
        turtle.shape()
        turtle.left(10)

turtle.hideturtle()