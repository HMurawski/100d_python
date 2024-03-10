from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce()
    # detect collision with right paddle
        if ball.distance(paddle_r) < 50 and ball.xcor() > 340 or ball.distance(paddle_l) < 50 and ball.xcor() < -340:
            ball.bounce_x()

    # detect misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()


screen.exitonclick()
