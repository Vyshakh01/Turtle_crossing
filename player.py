from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.reset()
        self.setheading(90)
    def move_up(self):
        self.forward(15)

    def move_down(self):
        self.backward(15)
    def reset(self):
        self.goto(0, -280)



