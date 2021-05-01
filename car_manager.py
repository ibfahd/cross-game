from turtle import Turtle
from random import choice, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.penup()
        self.goto(320, randrange(-260,280, 20))
    
    def go(self):
        self.goto(self.xcor() - MOVE_INCREMENT, self.ycor())

