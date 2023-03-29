from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.screensize(canvheight=600,canvwidth=800)
screen.bgcolor("black")
screen.title('PONG')
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.move_up, 'Up')
screen.onkey(paddle.move_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()






















screen.exitonclick()