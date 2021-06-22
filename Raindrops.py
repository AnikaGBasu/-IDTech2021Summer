import turtle as t
import random


def canvas():
    # setting turtle up
    t.color("#24e6ed")
    t.speed(0)
    t.up()
    t.goto(-350, -300)
    t.begin_fill()
    # drawing square or canvas
    for i in range(2):
        t.forward(675)
        t.left(90)
        t.forward(435)
        t.left(90)
    t.end_fill()


def numRaindrops(num):
    if num == 0:
        print("We the turtles have finished your rain.")
    else:
        # random radius
        radius = random.randint(1, 10)
        radius1 = radius
        # random ripples
        ripples = 5
        t.up()
        # random position
        pos_x = random.randint(-400, 400)
        pos_y = random.randint(-400, 400)
        # turtle goes to position
        t.goto(pos_x, pos_y)
        t.down()
        # random color
        t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # turtle draws the circle
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

        while ripples > 0:
            radius = radius + radius1

            if (radius + pos_x > 400) or (radius + pos_x < -400) or (radius + pos_y > 400) or (radius + pos_y < -400):
                ripples = 0
                break
            else:
                while ripples > 0:
                    ripples -= 1

            t.color("black")
            t.circle(radius)
            ripples -= 1

            # recursion

            return numRaindrops(num - 1)


canvas()
numRaindrops(6)

t.done()