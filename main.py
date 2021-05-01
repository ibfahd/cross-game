import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = []
cars.append(CarManager())

def stop():
    global game_is_on
    game_is_on = False

def cross():
    player.cross()

screen.listen()
screen.onkey(cross,"Up")
screen.onkey(stop,"x")

loop = 0
while game_is_on:
    time.sleep(0.1)
    for car in cars:
        car.go()
    screen.update()
    loop += 1
    if (loop == 6):
       cars.append(CarManager()) 
       loop = 0

