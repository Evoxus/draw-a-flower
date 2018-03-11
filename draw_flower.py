import turtle

def draw_inner_square(some_turtle):
    sides = 4
    while sides >= 1:
        some_turtle.forward(30)
        some_turtle.right(90)
        sides -= 1

def draw_outer_square(some_turtle):
    sides = 4
    while sides >= 1:
        some_turtle.forward(50)
        some_turtle.right(90)
        sides -= 1

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("Blue")

    carl = turtle.Turtle()
    carl.color("White")
    carl.shape("turtle")
    carl.speed(10)

    carl.left(90)
    carl.forward(200)
    for i in range(1,73):
        draw_inner_square(carl)
        carl.right(5)

    for i in range(1,37):
        draw_outer_square(carl)
        carl.right(10)

    window.exitonclick()

draw_flower()
