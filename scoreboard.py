from turtle import  Turtle



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 280)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"score = {self.score} ", False, align="center")

    def scoreincrease(self):
        self.score += 1
        self.clear()
        self.write(f"score = {self.score} ", False, align="center")

    def gameover(self):
            self.goto(0,0)
            self.write("Game Over ", False, align="center")
