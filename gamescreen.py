from turtle import Turtle

class GameScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.create_border()
        self.center_line()


    def create_border(self):
        self.speed(0)
        self.goto(-400, -300)
        self.hideturtle()
        self.color("white")
        self.goto(-400, 300)
        self.goto(400, 300)
        self.goto(400, -300)
        self.goto(-400, -300)

    def center_line(self):
        self.penup()
        self.goto(x=0, y=300)
        self.pensize(5)
        self.setheading(270)
        self.fd(10)
        self.pendown()
        for _ in range(15):
            self.fd(20)
            self.penup()
            self.fd(20)
            self.pendown()
        
