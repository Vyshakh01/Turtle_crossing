from turtle import Turtle
import random
colors=["red","yellow","green","blue","orange","purple"]
moving_distance=5
incremental_distance=10
class Car():

    def __init__(self):
        self.all_cars=[]
        self.moving_speed = moving_distance
        self.increase_speeddistance=incremental_distance


    def create_cars(self):
        if random.randint(1,6)==1 :
            car=Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=2)
            car.color(random.choice(colors))
            car.goto(290,random.randint(-275,275))
            car.setheading(180)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:

            car.forward(self.moving_speed)
    def increase_speed(self):
        self.moving_speed+=self.increase_speeddistance


