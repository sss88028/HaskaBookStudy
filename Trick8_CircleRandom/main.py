import turtle
import random

import getrandompoints
import time
from coloredshape import Circle
from color_base import Color


def draw_points(points_getter: getrandompoints.GetRandomPoints, color: Color):
    start_time = time.time()
    points = points_getter.get_points(2000)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
    for p in points:
        c = Circle(x=p[0], y=p[1], radius=2, color=color)
        c.draw()


screen = turtle.Screen()
screen.tracer(0)
screen.listen()
r = min(screen.window_width(), screen.window_height()) / 2

seed_value = 100
# seed_value = int(time.time())
random.seed(seed_value)

red_color = Color([1, 0, 0])
blue_color = Color([0, 0, 1])

random_0 = getrandompoints.RectangleRandomPoints(radius=r / 2, x=r / 2, y=r / 2)
draw_points(random_0, red_color)

random_1 = getrandompoints.PolarRandomPoints(radius=r / 2, x=-r / 2, y=r / 2)
draw_points(random_1, blue_color)

random_2 = getrandompoints.BetterPolorRandomPoints()
draw_points(random_2, blue_color)

screen.exitonclick()
