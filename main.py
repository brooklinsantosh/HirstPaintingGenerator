from src.color_palette import Extractor
from turtle import Turtle, Screen, colormode
import random


cp = Extractor()
cp.extract("images/image.jpg",30)


colormode(255)
tim = Turtle()
screen = Screen()

screen.setup(350,350)

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setposition(-130,-130)
tim.setheading(0)

rows = 10
cols = 10

for c in range(rows):
    for _ in range(cols):
        tim.dot(20, random.choice(cp.COLORS))
        tim.forward(30)
    tim.setheading(90)
    tim.forward(30)
    tim.setheading(180)
    tim.forward(cols*30)
    tim.setheading(0)

screen.exitonclick()