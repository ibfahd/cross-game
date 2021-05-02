from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def cross(self):        
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def win(self):
        return self.ycor() >= FINISH_LINE_Y

    def recross(self):
        self.goto(STARTING_POSITION)