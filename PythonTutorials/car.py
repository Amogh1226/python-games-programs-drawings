# import turtle
#
# car = turtle.Turtle()
#
# # Below code for drawing rectanglura upper body
# car.color('#2B2BF6')
# car.fillcolor('#2B2BF6')
# car.penup()
# car.goto(0, 0)
# car.pendown()
# car.begin_fill()
# car.forward(370)
# car.left(90)
# car.forward(50)
# car.left(90)
# car.forward(370)
# car.left(90)
# car.forward(50)
# car.end_fill()
#
# # Below code for drawing window and roof
# car.penup()
# car.goto(100, 50)
# car.pendown()
# car.setheading(45)
# car.forward(70)
# car.setheading(0)
# car.forward(100)
# car.setheading(-45)
# car.forward(70)
# car.setheading(90)
# car.penup()
# car.goto(200, 50)
# car.pendown()
# car.forward(49.50)
#
# # Below code for drawing two tyres
# car.penup()
# car.goto(100, -10)
# car.pendown()
# car.color('#000000')
# car.fillcolor('#000000')
# car.begin_fill()
# car.circle(20)
# car.end_fill()
# car.penup()
# car.goto(300, -10)
# car.pendown()
# car.color('#000000')
# car.fillcolor('#000000')
# car.begin_fill()
# car.circle(20)
# car.end_fill()
#
# car.hideturtle()
#
# t = turtle.Turtle()
# t.fillcolor('pink')
# t.begin_fill()
# for i in range(4):
#      t.forward(150)
#      t.right(-120)
#  t.end_fill()
#
# turtle.done()

# bob = turtle.Turtle()
# john = turtle.Turtle()
#
# def move_turtles(ammount):
#     for i in range(ammount // 10):
#         bob.forward(10)
#         john.forward(10)
#
# move_turtles(100)


import turtle

turtle.setworldcoordinates(0, -100, 100, 100)

bob = turtle.Turtle(shape="turtle")
bob.penup()
bob.sety(20)

john = turtle.Turtle(shape="turtle")
john.penup()
john.sety(-20)

def move_bob():
    bob.forward(1)
    if bob.xcor() < 90:
        turtle.ontimer(move_bob, 75)

def move_john():
    john.forward(2)
    if john.xcor() < 90:
        turtle.ontimer(move_john, 100)

move_bob()
move_john()

turtle.exitonclick()