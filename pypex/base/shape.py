import numpy as np
from abc import ABCMeta, abstractmethod
from collections import Iterable
from numpy import array


class Shape2D(metaclass=ABCMeta):
    def __init__(self, hull):
        self.polygon_validity_check(hull=hull, _raise=True)
        self._hull = np.array(hull)
        self.x, self.y = 0, 1

    def __str__(self):
        return "Poly ({}): [{}]".format(len(self.hull), ", ".join([str(v) for v in self.hull]))

    def __repr__(self):
        return "Poly ({}): [{}]".format(len(self.hull), ", ".join([str(v) for v in self.hull]))

    @property
    def hull(self):
        return self._hull

    @hull.setter
    def hull(self, hull):
        self._hull = hull

    @abstractmethod
    def intersects(self, shape):
        pass

    @abstractmethod
    def intersection(self, shape):
        pass

    def sort_clockwise(self, inplace=False):
        center = np.sum(self.hull, axis=0) / self.hull.shape[0]
        x, y = self.hull.T[self.x] - center[self.x], self.hull.T[self.y] - center[self.y]
        atan2 = np.arctan2(y, x)
        arr1inds = atan2.argsort()[::-1][:len(atan2)]
        hull = self.hull[arr1inds[::-1]]
        if inplace:
            self.hull = hull
        return hull

    @staticmethod
    def validity_check(hull, length, _raise=True):
        length_test = (len(hull) == length) if length in [3, 2] else (len(hull) > length)
        try:
            if length_test & (isinstance(hull, (Iterable, array))) & np.all(np.array([len(v) == 2 for v in hull])):
                return True
        except TypeError:
            pass
        if _raise:
            raise ValueError("invalid 2D polygon shape")
        return False

    @classmethod
    def polygon_validity_check(cls, hull, _raise=True):
        return cls.validity_check(hull, 1, _raise)
