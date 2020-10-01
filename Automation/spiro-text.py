import turtle

make = turtle.Pen()
turtle.bgcolor('mistyrose') #You can change the bg to your fav color
colors = ["red", "orange", "yellow", "green", "blue", "purple", "gray", "brown", "aqua", "sea green"]
your_name = turtle.textinput("Waiting for your Input :) ", "Enter Something or it will return nothing :D")
sides = int(turtle.numinput("Add your Color Sides", "How Many Color Sides Do You Want (1-10)", 5, 1, 10))

for x in range(100):
    make.pencolor(colors[x%sides%10])
    make.penup()
    make.forward(x*4)
    make.pendown()
    make.write(your_name, font=("Times", int( (x*2 + 4) /4), "bold")) #You can add your custom fonts here..!
    make.left(360/sides+2)
