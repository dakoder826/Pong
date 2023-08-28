from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

turtle = Turtle()
ball = Ball()

screen = Screen()
screen.tracer(0)
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

l_score = Score((-100, 200))
r_score = Score((100, 200))

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddles
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # when player right player misses(left player scores)
    if ball.xcor() > 410:
        l_score.add_score()
        ball.reset()
    # when player left player misses(right player scores)
    elif ball.xcor() < -410:
        r_score.add_score()
        ball.reset()

    # when a player wins
    if l_score.score == 6:
        time.sleep(0.5)
        l_score.left_won()
        game_is_on = False

    elif r_score.score == 6:
        time.sleep(0.5)
        r_score.right_won()
        game_is_on = False

screen.exitonclick()
