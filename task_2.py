import turtle

def pythagoras_tree(t, order, size):
    if order == 0:
        return
    else:
        t.forward(size)
        size = size * 0.75
        x, y = t.position()
        heading = t.heading()
        t.left(45)
        pythagoras_tree(t, order - 1, size)
        t.teleport(x, y)
        t.setheading(heading)
        t.right(45)
        pythagoras_tree(t, order - 1, size)

def draw_pythagoras_tree(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, -500)
    t.left(90)
    t.pendown()

    pythagoras_tree(t, order, size)


    window.mainloop()

def parse_input(user_input: str) -> int:
    return int(user_input)

user_input = input("Enter recursion level: ")

draw_pythagoras_tree(parse_input(user_input))