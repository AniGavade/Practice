# Sort the values of first list using second list
# l1 = ["f", "l", "y", "r", "s", "j", "b", "c", "a"]
# l2 = [0,   1,   1,    0,   1,   2,   2,   0,   1]
# key1 = dict(zip(l1, l2))
# print(key1)
# l1.sort(key=key1.get)
# print(l1)

import turtle
ninja = turtle.Turtle()
ninja.speed(360)

for i in range(40):
    ninja.forward(100)
    # ninja.right(20)
    ninja.forward(100)
    ninja.forward(100)
    # ninja.right(20)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(6)

turtle.done()
