from coloredshape import Circle
from color_base import Color
import utility


class TweenColor:
    def __init__(self, circle: Circle, start_color: Color, target_color: Color):
        self._circle = circle
        self._color_set = [start_color, target_color]

    def tween_color(self, delta_time: float, rate: float, minimum: float):
        (c, isEnd) = utility.tween_value(self._circle.color.rgb, self._color_set[0].rgb, rate * delta_time, minimum)
        self._circle.color.rgb = c
        return isEnd

    def swap_color(self):
        self._color_set[0], self._color_set[1] = self._color_set[1], self._color_set[0]