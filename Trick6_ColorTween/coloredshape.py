import copy
from color_base import Color
from abc import ABC, abstractmethod
from update_manager import UpdateObject
import turtle


class ColoredShape(UpdateObject):
    def update(self, delta_time: float):
        pass


class Circle(ColoredShape):
    def __init__(self, **kwargs):
        super().__init__()
        temp_color = kwargs.get('color', Color([0, 0, 0]))
        self.color = copy.deepcopy(temp_color)
        self._t = turtle.Turtle()
        self._t.hideturtle()
        self._radius = kwargs.get('radius', 20)
        self._x = kwargs.get('x', 0)
        self._y = kwargs.get('y', 0)

    def draw(self):
        self._t.penup()
        self._t.goto(self._x, self._y - self._radius)
        self._t.pendown()
        self._t.color(self.color.r, self.color.g, self.color.b)
        self._t.begin_fill()
        self._t.circle(self._radius)
        self._t.end_fill()
        self._t.penup()

    def update(self, delta_time: float):
        self.draw()