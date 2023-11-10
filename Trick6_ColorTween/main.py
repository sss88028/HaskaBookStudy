import copy
import turtle
from typing import List
import time
import color_base
import numpy as np


def tween_value(current: List[float], target: List[float], rate: float, minimum: float) -> List[float]:
    res = []
    for curr, tgt in zip(current, target):
        diff = tgt - curr
        delta = diff * rate
        if abs(delta) < minimum:
            if abs(diff) <= minimum:
                res.append(tgt)
            else:
                delta = np.sign(delta) * minimum
                res.append(curr + delta)
        else:
            res.append(curr + delta)

    return res


t = turtle.Turtle()

deltaTime = 1000
width, height = 200, 200

start_color = color_base.Color()
cur_color = copy.deepcopy(start_color)

target_color = color_base.Color()
target_color.r = 100 / 255
target_color.g = 200 / 255
target_color.b = 200 / 255


def update_colors():
    t.color(cur_color.rgb)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

    t.penup()
    t.forward(width + 50)
    t.pendown()

    t.color(cur_color.rgb)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

    turtle.update()


update_colors()
turtle.mainloop()
