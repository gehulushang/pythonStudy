import turtle

import time

'''

t = turtle.Pen()

for x in range(360):
    t.forward(x)
    t.left(59)
'''
turtle.width(8)
turtle.color("blue")
turtle.circle(50)

turtle.penup()
turtle.goto(120,0)

turtle.pendown()
turtle.color("red")
turtle.circle(50)

turtle.penup()
turtle.goto(240,0)

turtle.pendown()
turtle.color("green")
turtle.circle(50)

turtle.penup()
turtle.goto(60,-50)

turtle.pendown()
turtle.color("yellow")
turtle.circle(50)


turtle.penup()
turtle.goto(180,-50)

turtle.pendown()
turtle.color("black")
turtle.circle(50)


time.sleep( 5 )