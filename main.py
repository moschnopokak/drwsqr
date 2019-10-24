import turtle
import math

class Triangle(object):
    def __init__(self,x,y,side,color,angle):
        self.color = color
        self.x = x
        self.y = y
        self.side = side
        self.angle = angle

    def draw(self):
        turtle.up()
        turtle.color(self.color)
        turtle.right(self.angle)
        turtle.goto(self.x, self.y)
        turtle.down()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        turtle.forward(self.side)
        turtle.left(120)
        turtle.forward(self.side)
        turtle.left(120)
        turtle.forward(self.side)
        turtle.left(120)
        turtle.end_fill()
        turtle.hideturtle()

def sheet():
    tri1 = Triangle(90, 90, 100, 'green', 0)
    tri1.draw()
    tri2 = Triangle(90, 90, 100, 'blue', 60)
    tri2.draw()
    tri3 = Triangle(90, 90, 100, 'orange', 60)
    tri3.draw()
    tri4 = Triangle(90, 90, 100, 'magenta', 60)
    tri4.draw()
    tri5 = Triangle(90, 90, 100, 'red', 60)
    tri5.draw()
    tri6 = Triangle(90, 90, 100, 'cyan', 60)
    tri6.draw()


def piss():
    tri1 = Triangle(0, 0, 100, 'green', 0)
    tri1.draw()
    tri2 = Triangle(0, 0, 100, 'maroon', 60)
    tri2.draw()
    tri4 = Triangle(0, 0, 100, 'blue', 150)
    tri4.draw()
    tri3 = Triangle(100, 0, 100, 'lime', 180)
    tri3.draw()
    tri3 = Triangle(50, -1 * math.sqrt(7500), 100, 'purple', 90)
    tri3.draw()
    tri3 = Triangle(50, math.sqrt(7500), 100, 'navy', 180)
    tri3.draw()


def fisher():
    tri1 = Triangle(0, 0, 100, 'gray', 0)
    tri1.draw()
    tri2 = Triangle(-100, 0, 100, 'gray', 0)
    tri2.draw()
    tri4 = Triangle(-50, math.sqrt(7500), 100, 'gray', 0)
    tri4.draw()
    tri3 = Triangle(-50, math.sqrt(7500), 100, 'black', 60)
    tri3.draw()


def lichinus():
    tri1 = Triangle(0, 0, 100, 'cyan', 210)
    tri1.draw()
    tri2 = Triangle(0, 0, 100, 'teal', 180)
    tri2.draw()
    tri3 = Triangle(-1 * math.sqrt(7500), 50, 2 * math.sqrt(7500), 'navy', -30)
    tri3.draw()
    tri3 = Triangle(-1 * math.sqrt(7500), -50, 2 * math.sqrt(7500), 'yellow', 60)
    tri3.draw()


i = int(input("Мы подготовили 4 фигуры за один вечер, так что испытайте свою удачу и напишите любое число от одного до четырех: "))
if i == 1:
    sheet()
if i == 2:
    piss()
if i == 3:
    fisher()
if i == 4:
    lichinus()
