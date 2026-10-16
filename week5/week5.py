# import random
#
# for i in range(10):
#     print(random.random())
# import random
#
# for i in range(10):
#     print(random.randint(25,35))
# import math
#
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c= math.sqrt(a**2 + b**2)
# c = math.hypot(a,b)
# print(c)
# import math
#
# def areaOfCircle(radius):
#     return  math.pi * (radius ** 2)
# print(areaOfCircle(5))
# import turtle
#
# def drawStart(t,side):
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
# tess = turtle.Turtle()
# sc = turtle.Screen()
# tess.color("red")
# drawStart(tess,100)
#
#
#
#
# sc.exitonclick()
import turtle
def drawSquare(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)
# tess = turtle.Turtle()
# sc = turtle.Screen()
#
# tess.color("pink")
# sc.bgcolor("green")
# tess.pensize(4)
# for i in range(5):
#     drawSquare(tess, 20)
#     tess.penup()
#     tess.forward(40)
#     tess.pendown()
# sc.exitonclick()

# import turtle
#
# screen = turtle.Screen()
# tess = turtle.Turtle()
# screen.bgcolor("lightgreen")
# tess.color("blue")
# tess.pensize(3)
#
# for i in range(20 ,120 ,20):
#     drawSquare(tess, i)
#     tess.penup()
#     tess.backward(10)
#     tess.right(90)
#     tess.forward(10)
#     tess.left(90)
#     tess.pendown()
#
#
#
# screen.exitonclick()