# for i in range(100):
#     print("We like Python's turtles!")
# months = ["january", "february", "march", "april", "may", "june","july","september","october","november","december"]
# for month in months:
#     print("One of the months of the year is",month)
# numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for i in numbers:
#     print(i,"squared is",i**2)
# import turtle
#
# t = turtle.Turtle()
# screen = turtle.Screen()
# t.penup()
# t.goto(-350,0)
# t.pendown()
#
# for i in range(3):
#     t.forward(100)
#     t.left(120)
#
#
# t.penup()
# t.goto(-200,0)
# t.pendown()
# for i in range(4):
#     t.forward(100)
#     t.left(90)
#
# t.penup()
# t.goto(0,0)
# t.pendown()
# for i in range(6):
#     t.forward(100)
#     t.left(60)
#
# t.penup()
# t.goto(300,0)
# t.pendown()
# for i in range(8):
#     t.forward(100)
#     t.left(45)
import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(5)

t.stamp()
t.penup()

for i in range(12):
    t.forward(125)
    t.pendown()
    t.forward(15)
    t.penup()
    t.forward(25)
    t.stamp()
    t.backward(165)
    t.left(30)


screen.exitonclick()