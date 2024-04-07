import turtle as t

SEGEMTNTS_START_POSITON = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
Up = 90
Down = 270
Right = 0
Left = 180
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head =  self.segments[0]

    def create_snake(self):
        for position in SEGEMTNTS_START_POSITON:
            self.add_segment(position)

    def add_segment(self,position):
        tim = t.Turtle("square")
        tim.color("green")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def Up(self):
        if self.head.heading() != Down:
            self.head.setheading(90)

    def Down(self):
        if self.head.heading() != Up:
            self.head.setheading(270)

    def Right(self):
        if self.head.heading() != Left:
            self.head.setheading(0)

    def Left(self):
        if self.head.heading() != Right:
            self.head.setheading(180)

