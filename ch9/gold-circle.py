import turtle
t = turtle.Turtle()

def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

mycircle(0.9, 0.75, 0)