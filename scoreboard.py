from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.level=1
        self.write(f"Level : {self.level}" , FONT)

    def levelup(self):
        self.level += 1
        self.clear()
        self.goto(-280, 280)
        self.write(f"Level : {self.level}", FONT)
    
    def gameover(self):
        self.goto(-50, 0)
        self.write("GAME OVER", FONT)
