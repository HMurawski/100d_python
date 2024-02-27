from turtle import Turtle, Screen, penup, pendown
import random


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("pink")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()


#drawing different shapes

# def draw_triangle():
#     timmy_the_turtle.color(random.random(), random.random(), random.random())
#     for _ in range(3):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(120)

# def draw_square():
#     timmy_the_turtle.color(random.random(), random.random(), random.random())
#     for _ in range(4):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(90)

# def draw_hexagon():
#     timmy_the_turtle.color(random.random(), random.random(), random.random())
#     for _ in range(6):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(60)

# def draw_heptagon():
#     timmy_the_turtle.color(random.random(), random.random(), random.random())
#     for _ in range(7):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(51)

# def draw_octagon():
#     timmy_the_turtle.color(random.random(), random.random(), random.random())
#     for _ in range(8):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(45)

# def draw_nonagon():
#     timmy_the_turtle.color(random.random(), random.random(), random.random())
#     for _ in range(9):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(40)

# def draw_decagon():
#     timmy_the_turtle.color(random.random(), random.random(), random.random())
#     for _ in range(10):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(36)



# def draw_shapes():
#     draw_triangle()
#     draw_square()
#     draw_hexagon()
#     draw_heptagon()
#     draw_octagon()
#     draw_nonagon()
#     draw_decagon()

# draw_shapes()

def draw_polygon(sides):
    angle = 360 / sides

    for _ in range(sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)
        


def draw_shapes():
    for sides in range(3,11):
        timmy_the_turtle.color(random.random(), random.random(), random.random())
        draw_polygon(sides)
        

draw_shapes()




screen = Screen()
screen.exitonclick()



# 360 / 3 = 120
# 360 / 4 = 90
# 360 / 5 = 72
# 360 / 6 = 60
# 360 / 7 = 51
# 360 / 8 = 45
# 360 / 9 = 40
# 360 / 10 = 36