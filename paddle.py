from turtle import Turtle
MOVE = 30

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)
        self.color("white")

    def up(self):
        self.sety(self.ycor()+MOVE)

    def down(self):
        self.sety(self.ycor()-MOVE)
