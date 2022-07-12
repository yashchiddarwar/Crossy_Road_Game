from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed_car = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(300, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.speed_car)

    def increase_speed(self):
        self.speed_car = self.speed_car + MOVE_INCREMENT



