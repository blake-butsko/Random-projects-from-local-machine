# Blake Butsko 11/31/2021

import turtle
import math
sc = turtle.Screen()

# turtle.color("black", "red")
# turtle.begin_fill()
# turtle.circle(80)
# turtle.end_fill()

# I think black is the assumed color unless specified


# # # # # # # # # # # using arrow keys
# turtle.goto(100,100)

# def f():
#     turtle.forward(50)
# def l():
#     turtle.left(90)
# def r():
#     turtle.right(90)
# def b():
#     turtle.forward(-50)
# def g():turtle.pendown()
# def h():turtle.penup()

# sc.onkey(f,'w')
# sc.onkey(l,'a')
# sc.onkey(b,'s')
# sc.onkey(r,'d')
# sc.onkey(g, 'g')
# sc.listen(h, 'h')

# turtle.Screen().exitonclick()

# turtle.goto(100,100)

def proj_graphic(x_distance, height, angle=45):
    turtle.goto(100,0)
    turtle.goto(-100,0)
    turtle.setheading(0)
    turtle.left(angle)
    turtle.forward(math.sqrt( (x_distance/2)*height   ))
    turtle.right(angle*2)
    turtle.forward(math.sqrt( (x_distance/2)*height ))
    # turtle.goto(x_distance/2,height)
    # turtle.goto(x_distance/2,0)

proj_graphic(100,50)

turtle.Screen().exitonclick()