import turtle

turtle.Screen().bgcolor("Red")
turtle.Screen().setup(300, 400)

polygon = turtle.Turtle()
polygon.color("Black")
polygon.width(3)

num_sides = 10
side_length = 70
angle = 360 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
