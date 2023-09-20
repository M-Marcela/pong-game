from turtle import Turtle

ALIGHMENT = "center"
FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
        
    def update_score(self):
        self.goto(x=-70, y=220)
        self.write(self.l_score, align=ALIGHMENT, font=FONT)
        self.goto(x=70, y=220)
        self.write(self.r_score, align=ALIGHMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()
