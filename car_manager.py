from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.x = 300
        self.y = random.choice(range(-250, 250))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(self.x, self.y)
        self.color(random.choice(COLORS))
        self.speed(self.car_speed)
        self.setheading(180)

    def move_car(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.y)


