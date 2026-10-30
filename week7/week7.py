# -----------------1----------------------
# def sumTo(n):
#     total = n*(n+1)/2
#     return total
# print(sumTo(10))
# n=int(input("enter the number"))
# print(sumTo(n))
# -----------------2-----------------------
# import turtle
# def drawStar(t,n,size):
#     angle =180-180/n
#     for i in range(n):
#         t.forward(size)
#         t.right(angle)
# wn = turtle.Screen()
# alex = turtle.Turtle()
# alex.pensize(3)
# drawStar(alex,11,100)
# wn.exitonclick()
# -----------------3------------------------
# def sumTo(n):
#     total = 0
#     for i in range(1,n+1):
#         total = total + i
#     return total
# sum = sumTo(10)
# print(sum)
# -----------------4-------------------------
# import math
# def mySqrt(x):
#     guess=x/2
#     for i in range(20):
#         guess=(1/2)*(guess+x/guess)
#     return guess
# n=int(input("enter the number"))
# print(mySqrt(n))
# print(math.sqrt(n))
# ------------------5-------------------------
# import turtle
# def drawSprite(someturtle,legs,lenght):
#     angle = 360.0/legs
#     for i in range(legs):
#         someturtle.forward(lenght)
#         someturtle.backward(lenght)
#         someturtle.left(angle)
# def drawFancySquare(t,size):
#     for corner in range(4):
#         drawSprite(t,8,20)
#         t.forward(size)
#         t.left(90)
# t=turtle.Turtle()
# t.pensize(3)
# wn=turtle.Screen()
# wn.bgcolor("lightgreen")
# drawFancySquare(t,100)
# wn.exitonclick()
# ----------------------6-----------------------------
# import turtle
# def drawTip(t,size):
#     t.begin_fill()
#     t.left(90)
#     t.forward(size/2)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size/2)
#     t.right(90)
#     t.end_fill()
# def drawSpriteWithTips(t,legs,length):
#     angle = 360/legs
#     for i in range(legs):
#         t.forward(length)
#         drawTip(t,10)
#         t.backward(length)
#         t.left(angle)
# def fancySquare(t,size):
#     for corner in range(4):
#         drawSpriteWithTips(t,8,20)
#         t.forward(size)
#         t.left(90)
# t=turtle.Turtle()
# wn=turtle.Screen()
# wn.bgcolor("green")
# t.color("black")
# t.pensize(2)
# fancySquare(t,100)
# wn.exitonclick()
# ---------------------7-----------------------------
# n=int(input("enter a number"))
# def checkSign(n):
#     if n>0:
#         return "positive"
#     elif n<0:
#         return "negative"
#     else:
#         return "zero"
# num_list = [-7,0,15]
# for num in num_list:
#     print(checkSign(num))
# ---------------------8----------------------------------
import  turtle

def drawBar(t,height,gap):
    t.penup()
    t.left(90)
    t.forward(height+gap)
    t.write("  "+str(height))
    t.backward(height+gap)
    t.right(90)
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
def barChart(data):
    maxHeight = max(data)
    numBars = len(data)
    border = 10
    gap = (maxHeight+border)/25
    wn=turtle.Screen()
    wn.bgcolor("green")
    right=40*numBars+border
    top=maxHeight+4*border
    wn.setworldcoordinates(-border,-border,right,top)
    t=turtle.Turtle()
    t.color("blue")
    t.fillcolor("red")
    t.pensize(3)
    for height in (data):
        drawBar(t,height,gap)
    wn.exitonclick()
data=[100,200,300,400,500,600]
barChart(data)