from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.screensize(canvheight=600,canvwidth=800)
screen.bgcolor("black")
screen.title('PONG')
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
l_score=Scoreboard(-75, 310)
r_score = Scoreboard(75, 310)




screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 310 or ball.ycor() < -310:
        ball.bounce_y()

    # detect collision with right paddle

    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor()>340:
        l_score.scored()
        ball.start_right()

    if ball.xcor()<-340:
        r_score.scored()
        ball.start_left()







screen.exitonclick()