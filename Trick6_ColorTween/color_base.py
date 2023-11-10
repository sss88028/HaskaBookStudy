from typing import List

class Color:

    def __init__(self):
        self._color_array = [0, 0, 0]

    @property
    def rgb(self):
        return self._color_array

    @rgb.setter
    def rgb(self, val : List[float]):
        if len(val) != 3:
            raise ValueError("RGB value must be a list of three elements")
        self.r = val[0]
        self.g = val[1]
        self.b = val[2]

    @property
    def r(self) -> float:
        return self._color_array[0]

    @r.setter
    def r(self, val):
        self._color_array[0] = max(min(val, 1), 0)

    @property
    def g(self) -> float:
        return self._color_array[1]

    @g.setter
    def g(self, value):
        self._color_array[1] = max(min(value, 1), 0)

    @property
    def b(self) -> float:
        return self._color_array[2]

    @b.setter
    def b(self, value):
        self._color_array[2] = max(min(value, 1), 0)

    def __str__(self):
        return f"[{self.r} {self.g} {self.b}]"