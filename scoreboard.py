
from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.increase()

    def update_scoreboard(self):
        """set the scoreboard"""
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase(self):
        """Increase the score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)
