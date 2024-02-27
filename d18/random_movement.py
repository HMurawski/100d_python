from turtle import Turtle, Screen, penup, pendown
import random


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("pink")
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")


directions = [0,90,180,270]


for _ in range(100):
    timmy_the_turtle.color(random.random(), random.random(), random.random())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))













screen = Screen()
screen.exitonclick()