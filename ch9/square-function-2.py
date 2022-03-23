import turtle
t = turtle.Turtle()

def mysquare(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()

mysquare(50, True)
mysquare(150, False)
