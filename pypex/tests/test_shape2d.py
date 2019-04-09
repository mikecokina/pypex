import numpy as np
import unittest

from numpy.testing import assert_array_equal
from pypex.poly2d.polygon import Polygon
from pypex.poly2d.line import Line
from pypex.poly2d.intersection.sat import intersects

parray = np.array([[0.5, 1.5], [0, 0], [1, 0], [0, 1], [1, 1]])


class Shape2DTestCase(unittest.TestCase):
    __parray__ = np.array([[0.5, 1.5], [0, 0], [1, 0], [0, 1], [1, 1]])

    def setUp(self):
        self.poly = Polygon(hull=self.__parray__)

    def test_sort_clockwise(self):
        expected = [[0, 0], [1, 0], [1, 1], [0.5, 1.5], [0, 1]]
        obtained = self.poly.sort_clockwise()
        assert_array_equal(expected, obtained)

    def test_sat_intersection_negative_case(self):
        # not intersection example:
        faces = [[[0.0, 0.5],
                  [1.0, 0.5],
                  [0.0, 1.0]],
                 [[0.0, 0.0],
                  [1.0, 0.4],
                  [0.0, -.7]]]
        self.assertFalse(intersects(faces[0], faces[1], in_touch=True))
        self.assertFalse(intersects(faces[0], faces[1], in_touch=False))

        # not intersection example:
        faces = [[[0.0, 0.5],
                  [1.0, 0.5],
                  [0.0, 1.0]],
                 [[0.0, 0.0],
                  [1.0, 0.3],
                  [0.0, 0.3]]]
        self.assertFalse(intersects(faces[0], faces[1], in_touch=True))
        self.assertFalse(intersects(faces[0], faces[1], in_touch=False))

    def test_sat_intersection_positive_case(self):
        faces = [[[0.0, 0.5],
                  [1.0, 0.5],
                  [0.0, 1.0]],
                 [[0.0, 2.0],
                  [1.0, 0.5],
                  [0.0, 0.5]]]
        self.assertTrue(intersects(faces[0], faces[1], in_touch=True))
        self.assertTrue(intersects(faces[0], faces[1], in_touch=False))

        faces = [[[0.0, 0.0],
                  [2.0, 0.0],
                  [0.0, 2.0]],
                 [[-.9, -.9],
                  [-3., 3.5],
                  [9.5, 1.0]]]
        self.assertTrue(intersects(faces[0], faces[1], in_touch=True))
        self.assertTrue(intersects(faces[0], faces[1], in_touch=False))

        faces = [[[0.0, 0.5],
                  [1.0, 0.5],
                  [1.0, 1.0],
                  [0.0, 1.0]],
                 [[0.5, 0.5],
                  [4.0, 0.5],
                  [4.0, 3.0],
                  [0.5, 3.0]]]
        self.assertTrue(intersects(faces[0], faces[1], in_touch=True))
        self.assertTrue(intersects(faces[0], faces[1], in_touch=False))

        faces = [[[0.0, 0.5],
                  [1.0, 0.5],
                  [1.0, 1.0],
                  [0.0, 1.0]],
                 [[0.5, 0.5],
                  [4.0, 0.5],
                  [4.0, 3.0]]]
        self.assertTrue(intersects(faces[0], faces[1], in_touch=True))
        self.assertTrue(intersects(faces[0], faces[1], in_touch=False))

    def test_sat_intersection_onedge_case(self):
        faces = [[[0.0, 0.0],
                  [1.0, 0.0],
                  [0.0, 1.0]],
                 [[-1., 1.0],
                  [0.0, 1.0],
                  [0.0, 0.0]]]
        self.assertFalse(intersects(faces[0], faces[1], in_touch=False))
        self.assertTrue(intersects(faces[0], faces[1], in_touch=True))

    def test_sat_intersection_touch_case(self):
        faces = [[[0.0, 0.0],
                  [1.0, 0.0],
                  [0.0, 1.0]],
                 [[0.0, 0.0],
                  [-.1, -.5],
                  [-.5, -.5]]]

        self.assertFalse(intersects(faces[0], faces[1], in_touch=False))
        self.assertTrue(intersects(faces[0], faces[1], in_touch=True))

    def test_line_sat_intersect(self):
        line1 = np.array([[-1., -1.], [0.3, 0.3]])
        line2 = np.array([[0.2, 0.2], [1.3, 1.3]])
        self.assertTrue(intersects(line1, line2, in_touch=True))
        self.assertTrue(intersects(line1, line2, in_touch=False))

        line1 = np.array([[-1., -1.], [0.3, 0.3]])
        line2 = np.array([[0.3, 0.3], [1.3, 1.3]])
        self.assertTrue(intersects(line1, line2, in_touch=True))
        self.assertFalse(intersects(line1, line2, in_touch=False))

        line1 = np.array([[1., 1.], [1., 2.]])
        line2 = np.array([[1., 2.], [1., 13.]])
        self.assertTrue(intersects(line1, line2, in_touch=True))
        self.assertFalse(intersects(line1, line2, in_touch=False))

        line1 = np.array([[1., 1.], [3.1, 1.]])
        line2 = np.array([[3.2, 1.], [5., 1.]])
        self.assertFalse(intersects(line1, line2, in_touch=True))
        self.assertFalse(intersects(line1, line2, in_touch=False))
