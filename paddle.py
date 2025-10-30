from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, paddle_coordinates):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed('fastest')
        self.shape("square")
        self.color("white")
        self.goto(paddle_coordinates)
        self.speed(3)

    def move_up(self):
        if self.xcor() == 350:
            self.goto(350, 320)
        else:
            self.goto(-350, 320)
        self.speed(3)

    def move_down(self):
        if self.xcor() == 350:
            self.goto(350, -320)
        else:
            self.goto(-350, -320)
        self.speed(3)

