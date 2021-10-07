import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280
cars = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move_forward, "Up")

current_level = 1
sleep = 0.1
increment = 1
game_is_on = True
while game_is_on:
    if scoreboard.level > current_level:
        sleep *= 0.6
        current_level += 1
    time.sleep(sleep)
    screen.update()
    if increment == 1:
        car_manager = CarManager()
        cars.append(car_manager)
    increment += 1
    if increment > 6:
        increment = 1
    for car in list(cars):
        if car.xcor() < -300:
            cars.remove(car)
        car.move_car()
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() == FINISH_LINE_Y:
        scoreboard.level += 1
        scoreboard.update_scoreboard()
        player.reset_pos()

screen.exitonclick()