# import turtle

# t = turtle.Turtle()
# t.forward(100)
# t.right(90)
# t.forward(100)
# turtle.done()

# import turtle

# screen = turtle.Screen()
# screen.bgcolor("blue")
# screen.setup(width=600, height=400)
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("darkgreen")
# t.forward(150)
# screen.exitonclick()

# import turtle

# t = turtle.Turtle()
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# turtle.done()

# import turtle

# t = turtle.Turtle()
# for i in range(2):
#     t.forward(150)
#     t.right(90)
#     t.forward(80)
#     t.right(90)
# turtle.done()

# import turtle
# t = turtle.Turtle()
# for i in range(3):
#     t.forward(120)
#     t.right(120)
# turtle.done()

# import turtle
# t = turtle.Turtle()
# t.circle(60)
# turtle.done()

# import turtle

# t = turtle.Turtle()
# for i in range(5):
#     t.forward(150)
#     t.right(144)
# turtle.done()

import turtle
t = turtle.Turtle()
t.forward(50)
t.left(45)
t.forward(30)
print("Position:", t.position())
print("Heading:", t.heading())
print("Is pen down?", t.isdown())
print("Distance from origin:", t.distance(0,0))
turtle.done()