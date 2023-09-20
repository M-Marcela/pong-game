from turtle import Screen
from gamescreen import GameScreen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

window = Screen()
window.bgcolor("black")
window.setup(width=800, height=600)
window.title("Pong")
window.tracer(0)

play_field = GameScreen()

r_paddle = Paddle(x=350, y=0)
l_paddle = Paddle(x=-350, y=0)
ball = Ball()
score = Scoreboard()

window.listen()
window.onkey(r_paddle.up, "Up")
window.onkey(r_paddle.down, "Down")
window.onkey(l_paddle.up, "w")
window.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    window.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detetct L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
