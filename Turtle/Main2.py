import turtle

turtle.Screen().bgcolor("Blue")
turtle.Screen().setup(300, 400)

polygon = turtle.Turtle()
polygon.color("white")
polygon.width(3)

num_sides = 5
side_length = 100
angle = 144

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
