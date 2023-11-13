from abc import ABC, abstractmethod
from typing import List


class UpdateObject(ABC):
    def update(self, delta_time: float):
        pass


class UpdateManager(UpdateObject):
    def __init__(self):
        self._update_obj_list: List[UpdateObject] = []

    def add(self, obj: UpdateObject):
        self._update_obj_list.append(obj)

    def remove(self, obj: UpdateObject):
        self._update_obj_list.remove(obj)

    def update(self, delta_time: float):
        for obj in self._update_obj_list:
            obj.update(delta_time)