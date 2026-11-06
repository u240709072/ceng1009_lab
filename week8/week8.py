# def getGrade(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
# marks=[95,90,89.9,80,79.9,70,45,59.5,30]
# for mark in marks:
#     print("your grade is ",getGrade(mark))
# mark = float(input("enter your mark: "))
# print("your grade is ",getGrade(mark))
# -------------------------------------------1-----------------------------------------
# import turtle
# def chooseColor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
# def drawBar(t,height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height+gap)
#     t.write(" "+str(height))
#     t.backward(height+gap)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
# def barChart(data):
#     maxHeight = max(data)
#     numBars = len(data)
#     border = 10
#     gap = (maxHeight + border) / 25
#     wn = turtle.Screen()
#     wn.bgcolor("green")
#     right = 40 * numBars + border
#     top = maxHeight + 4 * border
#     wn.setworldcoordinates(-border, -border, right, top)
#     t = turtle.Turtle()
#     t.color("blue")
#     t.pensize(3)
#     for height in (data):
#         drawBar(t, height, gap)
#     wn.exitonclick()
# data=[100,200,300,400,500,600]
# barChart(data)
# ----------------------------------------------2-------------------------------------------------
# import turtle
# def chooseColor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "hotpink"
# def drawBar(t,height,gap):
#     if height >= 0:
#         labelY = height + gap
#     else:
#         labelY= gap
#     t.penup()
#     t.left(90)
#     t.forward(labelY)
#     t.write(" "+str(height))
#     t.backward(labelY)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
# def barChart(data):
#     maxHeight = max(data)
#     minHeight = min(data)
#     border = 10
#     bottom = min(minHeight,0)-border
#     numBars = len(data)
#     gap = (maxHeight + border) / 25
#     wn = turtle.Screen()
#     wn.bgcolor("green")
#     right = 40 * numBars + border
#     top = maxHeight + 4 * border
#     wn.setworldcoordinates(-border, bottom, right, top)
#     t = turtle.Turtle()
#     t.color("blue")
#     t.pensize(3)
#     for height in (data):
#         drawBar(t, height, gap)
#     wn.exitonclick()
# data=[100,-200,300,-400,500,600]
# barChart(data)
# -----------------------------------------3----------------------------------------------------
import math


def findHypot(side1,side2):
    hypot = (side1**2+side2**2) ** 0.5
    return hypot
def calcWithMath(side1,side2):
    hypot = math.hypot(side1,side2)
    return hypot
print(findHypot(3,4))
print(calcWithMath(3,4))