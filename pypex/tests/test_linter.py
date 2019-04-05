import unittest
import numpy as np

from pypex.poly2d.intersection import linter


class LinterTestCase(unittest.TestCase):
    def test_intersection_parallel(self):
        line1 = [np.array([0, 1]), np.array([1, 1])]
        line2 = [np.array([0, 0]), np.array([1, 0])]
        obtained = linter.intersection(line1[0], line1[1], line2[0], line2[1])
        expected = (False, np.nan, np.nan, np.nan, 1.0, 'PARALLEL')
        self.assertEqual(obtained, expected)

    def test_intersection_overlap(self):
        line1 = [np.array([0, 1]), np.array([1, 1])]
        obtained = linter.intersection(line1[0], line1[1], line1[0], line1[1])
        expected = (True, np.nan, np.nan, np.nan, 0.0, 'OVERLAPPING')
        self.assertEqual(obtained, expected)

    def test_intersection_intersect(self):
        line1 = [np.array([-1, 0]), np.array([1, 0])]
        line2 = [np.array([0, -1]), np.array([0, 1])]
        obtained = linter.intersection(line1[0], line1[1], line2[0], line2[1])
        expected = (True, True, 0.0, 0.0, np.nan, 'INTERSECTING')
        self.assertEqual(obtained, expected)
