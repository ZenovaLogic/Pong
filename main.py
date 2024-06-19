from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Ah no way, it's Pong!")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

running = True
while running:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320
            or ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect right player miss
    if ball.xcor() > 380:
        score.left_player_score()
        score.update_score()
        ball.reset_position()

    # Detect left player miss
    if ball.xcor() < -380:
        score.right_player_score()
        score.update_score()
        ball.reset_position()

screen.exitonclick()
