import turtle

# -- setup --
wn=turtle.Screen()
wn.bgcolor("lightgreen")
tess=turtle.Turtle()
#--function--
def drawPolygon(someturtle ,someside,somesize):
    angle=360/someside
    for i in range(someside):
        someturtle.forward(somesize)
        someturtle.left(angle)

def drawSpiral(someturtle ,angle):
    size = 1
    for i in range(100):
        someturtle.forward(size)
        someturtle.right(angle)
        size += 1
def drawEquitriangle(someturtle ,somesize):
    drawPolygon(someturtle,3,somesize)
def drawStar(someturtle ,somesize):
    for i in range(5):
        someturtle.forward(somesize)
        someturtle.right(144)
def drawSprite(someturtle ,legs,lenght):
    angle = 360/legs
    for i in range(legs):
        someturtle.forward(lenght)
        someturtle.backward(lenght)
        someturtle.left(angle)
# --exercises--
# Exercise1
# tess.color("hotpink")
# drawPolygon(tess,8,50)
# Exercise2
# tess.color("blue")
# for i in range(20):
#     drawPolygon(tess,4,100)
#     tess.left(18)
#Exercise3
# tess.pencolor("blue")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawSpiral(tess,90)
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawSpiral(tess,89)
#Exercise4
#drawEquitriangle(tess,100)
#Exercise5
# tess.color("hotpink")
# tess.pensize(5)
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# for i in range(5):
#     drawStar(tess,100)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()
#Exercise6
# tess.pensize(5)
# drawSprite(tess,15,120)











# --finish--
wn.exitonclick()