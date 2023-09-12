from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level=1
        with open("highest level.txt","r") as data :
            self.highest_level = int(data.read())
        self.pencolor("white")
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f" LEVEL:{self.level}",font=('Courrier', 20, 'normal'),align='center',)
        self.goto(160,260)
        self.write(f" HIGHEST LEVEL:{self.highest_level}", font=('Courrier', 20, 'normal'), align='center', )
    def increase_level(self):
        self.level+=1
        self.update_level()

    def game_over(self):
            self.goto(0, 0)
            if self.level>self.highest_level:
                self.highest_level=self.level
                with open("highest level.txt","w") as data:
                    data.write(f"{self.highest_level}")
                self.update_level()
            self.goto((100,0))
            self.write("GAME OVER", align="center", font=("Courrier", 40, "normal"))