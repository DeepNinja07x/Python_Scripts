"""
Single Player Pong Game
By @someshnarwade
"""

# TODO Add Blocks
# TODO Add Block Collision
# TODO Randomize block colors
# TODO Add ScoreBoard
# TODO Add player lives
# TODO Add Levels

import os
import turtle
from random import choice

wn = turtle.Screen()
wn.title("Solo Pong by Somesh Narwade")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")  # 20 x 20
paddle.color("white")
paddle.shapesize(stretch_wid=0.5, stretch_len=5)  # 10 x 100
paddle.penup()
paddle.goto(0, -280)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

colors = ["red", "blue", "green", "yellow", "purple", "violet"]
# Bricks
bricks = []
xcor = -390
y = 0
for y in range(0, 100, 20):
    for i in range(40):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")  # 20 x 20
        brick.color(choice(colors))
        brick.penup()
        brick.goto(xcor + i * 20, 100 + y)
        bricks.append(brick)

score = 0
life = 3
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
lives = "$ " * life
pen.write(
    f"Score: {score} Lives = {lives}", align="center", font=("Courier", 24, "normal")
)


# Functions
def paddle_left():
    """paddle movement"""
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)


def paddle_right():
    """paddle movement"""
    x = paddle.xcor()
    x += 20
    paddle.setx(x)


# Keyboard Bindings
wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")


# Main Game Loop
loop = True
while loop:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Exit Conditions
    if not life:
        loop = False
        print("Game Over!")

    if len(bricks) == 0:
        print("You Win!")
        loop = False

    # Border Checking
    if ball.ycor() < -290:  # bottom collision
        ball.goto(0, 0)
        ball.dy *= -1
        os.system("aplay --quiet sounds/fail.wav&")
        life -= 1
        lives = "$ " * life
        pen.clear()
        pen.write(
            f"Score: {score} Lives: {lives}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay --quiet sounds/bounce.wav&")

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        os.system("aplay --quiet sounds/bounce.wav&")

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        os.system("aplay --quiet sounds/bounce.wav&")

    # Collision
    if -280 < ball.ycor() < -270 and (paddle.xcor() - 50) < ball.xcor() < (
        paddle.xcor() + 50
    ):
        ball.sety(-270)
        ball.dy *= -1
        os.system("aplay --quiet sounds/bounce.wav&")

    for brick in bricks:
        if (brick.ycor() - 10) <= ball.ycor() <= (brick.ycor() + 10) and (
            brick.xcor() - 10
        ) <= ball.xcor() <= (brick.xcor() + 10):
            os.system("aplay --quiet sounds/bounce.wav&")
            brick.hideturtle()
            ball.dx *= -1
            ball.dy *= -1
            bricks.remove(brick)
            score += 1
            pen.clear()
            pen.write(
                f"Score: {score} Lives: {lives}",
                align="center",
                font=("Courier", 24, "normal"),
            )
