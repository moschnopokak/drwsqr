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