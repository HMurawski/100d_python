from turtle import Turtle, Screen, penup, pendown
import random


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("pink")
timmy_the_turtle.speed("fastest")


def draw_spirograph(size_of_the_gap):
    for _ in range(int(360 / size_of_the_gap)):
        timmy_the_turtle.color(random.random(), random.random(), random.random())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_the_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
