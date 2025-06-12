
from turtle import Turtle
import random


class Food(Turtle):
    """Food class for snake game"""

    def __init__(self):
        super().__init__()
        self.shape("circle")  # food ship
        self.speed(0)
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")  # food colour
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
