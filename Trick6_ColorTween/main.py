from turtle import Screen
import time
import color_base
import numpy as np

def tween_value(current: float, target: float, rate: float, minimum: float) -> float:
    diff = target - current
    delta = diff * rate
    if abs(delta) < minimum:
        if abs(diff) <= minimum:
            return target
        else:
            delta = np.sign(delta) * minimum

    return current + delta

screen = Screen()
screen.setup(width=600, height=600)

deltaTime = 1 / 30
cur_color = color_base.Color()

target_color = color_base.Color()
target_color.r = 100 / 255
target_color.g = 200 / 255
target_color.b = 200 / 255

screen.bgcolor(cur_color.r, cur_color.g, cur_color.b)
screen.title("Color")


while True:
    time.sleep(deltaTime)
    screen.bgcolor(cur_color.r, cur_color.g, cur_color.b)
    cur_color.r = tween_value(cur_color.r, target_color.r, 0.1, 0.02)
    cur_color.g = tween_value(cur_color.g, target_color.g, 0.1, 0.02)
    cur_color.b = tween_value(cur_color.b, target_color.b, 0.1, 0.02)
    screen.update()

screen.exitonclick()


