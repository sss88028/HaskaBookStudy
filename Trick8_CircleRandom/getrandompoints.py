from abc import ABC, abstractmethod
from typing import List, Tuple
import random
import math


class GetRandomPoints(ABC):
    def get_points(self, size: int) -> List[Tuple[float, float]]:
        pass


class RectangleRandomPoints(GetRandomPoints):
    def __init__(self, **kwargs):
        self._radius = kwargs.get('radius', 50)
        self._radius_sqrt = self._radius * self._radius
        self._x = kwargs.get('x', 0)
        self._y = kwargs.get('y', 0)

    def get_points(self, size: int) -> List[Tuple[float, float]]:
        res = []
        while len(res) < size:
            new_x = random.uniform(-1, 1) * self._radius
            new_y = random.uniform(-1, 1) * self._radius
            dis = new_x * new_x + new_y * new_y
            if dis > self._radius_sqrt:
                continue
            res.append((self._x + new_x, self._y + new_y))
        return res


class PolarRandomPoints(GetRandomPoints):
    def __init__(self, **kwargs):
        self._radius = kwargs.get('radius', 50)
        self._x = kwargs.get('x', 0)
        self._y = kwargs.get('y', 0)

    def get_points(self, size: int) -> List[Tuple[float, float]]:
        res = []
        while len(res) < size:
            length = random.random() * self._radius
            angle = random.random() * 2 * math.pi
            points = self.get_polor_point(length, angle)
            res.append((self._x + points[0], self._y + points[1]))

        return res

    def get_polor_point(self, length: float, angle: float):
        new_x = math.cos(angle) * length
        new_y = math.sin(angle) * length
        return [new_x, new_y]


class BetterPolorRandomPoints(PolarRandomPoints):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_points(self, size: int) -> List[Tuple[float, float]]:
        res = []
        while len(res) < size:
            length = math.sqrt(random.random()) * self._radius
            angle = random.random() * 2 * math.pi
            points = self.get_polor_point(length, angle)
            res.append((self._x + points[0], self._y + points[1]))

        return res
