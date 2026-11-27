# def fizz_buz(n):
#     for i in range(1,n+1):
#         if i % 15 == 0:
#             print("fizzBuzz")
#         elif i % 3 == 0:
#             print("fizz")
#         elif i % 5 == 0:
#             print("buzz")
#         else:
#             print(i)
# fizz_buz(16)
# ******************************************************************************
# def digit_sum(n):
#     total = 0
#     while n > 0:
#         print(n)
#         total = total + n % 10
#         n=n//10
#     return total
# sonuc = digit_sum(1234)
# print(sonuc)
# *******************************************************************************
# def alternate_case(s):
#     result = ""
#     for i in range(len(s)):
#         if i % 2 == 0:
#             result = result + s[i].upper()
#         else:
#             result = result + s[i].lower()
#     return result
# print(alternate_case("hello world"))
# *********************************************************************************
# import turtle
#
# def drawPolygon(t ,sides,lenght):
#     for i in range(sides):
#         t.forward(lenght)
#         t.left(360 /sides)
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.pensize(3)
# colors = ["red","yellow","blue"]
#
# for i in range(3):
#     t.penup()
#     t.goto(-150+i*120,-30)
#     t.pendown()
#     t.color(colors[i])
#     drawPolygon(t,3+i,60)
# wn.exitonclick()
# **********************************************************************************
# import turtle
# def filledSquares(t,size,color):
#     t.fillcolor(color)
#     t.begin_fill()
#     for i in range (4):
#         t.forward(size)
#         t.left(90)
#     t.end_fill()
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# for i in range(5):
#     t.penup()
#     t.goto(-165+i*70,-25)
#     t.pendown()
#     if i % 2 == 0:
#         filledSquares(t,30,"red")
#     else:
#         filledSquares(t,30,"blue")
#
#
#
# wn.exitonclick()
#*********************************************************************
# import turtle
#
#
# def drawSquare(t,size):
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
# t = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t.pensize(3)
# for i in range(12):
#     drawSquare(t,80)
#     t.left(30)
#
# wn.exitonclick()
#*********************************************************************
import turtle


def drawSquare(t,size,filled):
    if filled :
        t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    if filled :
        t.end_fill()
wn = turtle.Screen()
wn.bgcolor("lightgreen")
t = turtle.Turtle()
size = 40
for row in range(6):
    for col in range(6):
        t.penup()
        t.goto(-120+col*size,-120+row*size)
        t.pendown()
        drawSquare(t,size,(row +col)%2 == 0)
wn.exitonclick()