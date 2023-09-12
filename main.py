import turtle
from player import Player
import time
from car import Car
from scoreboard import Scoreboard
screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.title("TURTLE CROSSING")
screen.bgcolor("black")
screen.tracer(0)
player=Player()
is_game_on=True
screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")
car = Car()
level=Scoreboard()


while is_game_on:

    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move()


    if player.ycor()>280:
        player.reset()
        car.increase_speed()
        level.increase_level()
    for new_car in car.all_cars:
        if new_car.distance(player)<20:
            #player.reset()
            level.game_over()
            is_game_on=False

screen.exitonclick()
