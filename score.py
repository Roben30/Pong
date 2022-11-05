from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.wrote()

    def wrote(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align='center', font=('Arial', 40, 'normal'))

    def increase_l_score(self):
        self.l_score += 1
        self.wrote()

    def increase_r_score(self):
        self.r_score += 1
        self.wrote()