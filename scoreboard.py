from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = open('data.txt').read()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def paste_highscore(self):
        high_score = int(self.highscore)
        if self.score > high_score:
            open('data.txt', mode='w').write(str(self.score))
        else:
            pass



    def update_scoreboard(self):
        self.clear()
        self.paste_highscore()
        self.write(f"Score: {self.score} Highscore: {self.highscore}",  align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
    #def game_over(self):
       # self.goto(0, 0)
       # self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
