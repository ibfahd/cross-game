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
        self.goto(320, randrange(-240,240, 20))
    
    def go(self):
        self.goto(self.xcor() - MOVE_INCREMENT, self.ycor())

    def position(self):
        return self.xcor()

    def crash(self, crossing_turtle):
        return self.distance(crossing_turtle)