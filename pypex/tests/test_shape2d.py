import numpy as np
import unittest

from numpy.testing import assert_array_equal
from pypex.poly2d.polygon import Polygon

parray = np.array([[0.5, 1.5], [0, 0], [1, 0], [0, 1], [1, 1]])


class Shape2DTestCase(unittest.TestCase):
    __parray__ = np.array([[0.5, 1.5], [0, 0], [1, 0], [0, 1], [1, 1]])

    def setUp(self):
        self.poly = Polygon(hull=self.__parray__)

    def test_sort_clockwise(self):
        expected = [[0, 0], [1, 0], [1, 1], [0.5, 1.5], [0, 1]]
        obtained = self.poly.sort_clockwise()
        assert_array_equal(expected, obtained)



