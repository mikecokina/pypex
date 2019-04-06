import unittest

from pypex.poly2d.polygon import Polygon
from pypex.poly2d import point


class BaseTestCase(unittest.TestCase):
    def test_is_point_in_polygon_positive(self):
        poly = Polygon([[0, 0], [1, 0], [1, 1], [0, 1]])
        p = point.Point(x=0.5, y=0.5)
        obtained = point.is_point_in_polygon(p, poly)
        self.assertTrue(obtained)

    def test_is_point_in_polygon_negative(self):
        poly = Polygon([[-1, -1], [1, 0], [1, 1], [0.5, 1.9], [1, 1]])
        p = point.Point(x=-10, y=10)
        obtained = point.is_point_in_polygon(p, poly)
        self.assertFalse(obtained)

    def test_is_point_in_polygon_onedge(self):
        poly = Polygon([[0, 0], [1, 0], [1, 1]])
        p = point.Point(x=0.5, y=0)
        obtained = point.is_point_in_polygon(p, poly)
        self.assertTrue(obtained)


class PointTestCase(unittest.TestCase):
    def test_is_inside_polygon_positive(self):
        poly = Polygon([[0, 0], [1, 0], [1, 1], [0, 1]])
        p = point.Point(x=0.5, y=0.5)
        self.assertTrue(p.is_inside_polygon(poly))
