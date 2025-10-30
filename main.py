from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong")
screen.listen()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')

screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 350 or ball.ycor() < -350:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect ball position otu of the screen
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()