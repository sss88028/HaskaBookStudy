import copy
import turtle
import time
from tween_color_set import TweenColor
from Utility.color_base import Color
from Utility.coloredshape import Circle
from Utility.update_manager import UpdateManager

delta_time = 1 / 30

start_color = Color([0, 0, 0])

target_color1 = Color([100 / 255, 200 / 255, 150 / 255])
target_color2 = Color([255 / 255, 0 / 255, 0 / 255])

circle1 = Circle(color=start_color, radius=75, x=-100)
tween_color1 = TweenColor(circle1, copy.deepcopy(start_color), target_color1)

circle2 = Circle(color=start_color, radius=75, x=100)
tween_color2 = TweenColor(circle2, copy.deepcopy(start_color), target_color2)

update_manager = UpdateManager()
update_manager.add(circle1)
update_manager.add(circle2)

screen = turtle.Screen()
screen.tracer(0)
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    update_manager.update(delta_time)
    time.sleep(delta_time)

    isEnd = tween_color1.tween_color(delta_time, 5, 0.05)
    isEnd = tween_color2.tween_color(delta_time, 5, 0.05) and isEnd
    if isEnd:
        tween_color1.swap_color()
        tween_color2.swap_color()

screen.exitonclick()