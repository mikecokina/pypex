import unittest
from pypex.base import shape


class BaseTestCase(unittest.TestCase):
    def test_polygon_validity_check_valid(self):
        valid_hull = [[0, 0], [1, 0], [0.5, 1]]
        self.assertTrue(shape.Shape2D.polygon_validity_check(valid_hull, _raise=False))

    def test_polygon_validity_check_invalid(self):
        invalid_hull = [[0, 0], [1], [0.5, 1]]
        self.assertFalse(shape.Shape2D.polygon_validity_check(invalid_hull, _raise=False))
        invalid_hull = [[0.5, 1]]
        self.assertFalse(shape.Shape2D.polygon_validity_check(invalid_hull, _raise=False))
        invalid_hull = [0.5, 1]
        self.assertFalse(shape.Shape2D.polygon_validity_check(invalid_hull, _raise=False))
