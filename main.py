import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.player_up, "Up")
num = 6
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if num % 6 == 0:
        car_manager.create_car()
    car_manager.car_move()
    num = num + 1
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.next_level()
        car_manager.increase_speed()
        scoreboard.score_update()





screen.exitonclick()
