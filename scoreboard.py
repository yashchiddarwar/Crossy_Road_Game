from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.score_display()

    def score_display(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(270, 270)
        self.write(f"{self.score}",False, "center", FONT)

    def score_update(self):
        self.score += 1
        self.score_display()

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", False, "center", FONT)


