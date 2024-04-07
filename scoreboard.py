from turtle import  Turtle



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/home/yacine/Documents/score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 280)
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"score = {self.score}  Higher score = { self.high_score}", False, align="center")


    def scoreincrease(self):
        self.score += 1
        self.clear()
        self.write(f"score = {self.score} ", False, align="center")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/home/yacine/Documents/score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
