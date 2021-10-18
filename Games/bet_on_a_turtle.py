from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make a Bet",
    prompt="Which turtle will win the race? Enter a color:\n (red, orange, yellow, green, blue, purple)",
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y_axis = 150

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_axis)
    y_axis -= 60
    turtles.append(tim)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for tim in turtles:
        tim.forward(random.randint(0, 10))  # randint includes both 0 and 10
        if (
            tim.xcor() > 230
        ):  # turtle is 40 * 40 size so it would have entirely crossed for 250 so make it 40/2 =20->250-20
            print(f"{tim.pencolor()} won !")  # color shows pencolor and fillcolor
            if user_bet == tim.pencolor():
                print("You won!")
            else:
                print("You lost ...")
            is_race_on = False

screen.exitonclick()
