"""Analytic and numerical regression cases for convex intersection areas."""
import unittest
from unittest.mock import patch

import numpy as np

from pypex import IntersectionAreaMethod, Polygon


SQUARE = np.array([[0., 0.], [2., 0.], [2., 2.], [0., 2.]])
METHODS = tuple(IntersectionAreaMethod)


class IntersectionAreaTestCase(unittest.TestCase):
    def check_area(self, a, b, expected, methods=METHODS, rtol=1e-9, atol=1e-10):
        a, b = Polygon(a), Polygon(b)
        before = (a.hull.copy(), b.hull.copy())
        for method in methods:
            with self.subTest(method=method, expected=expected):
                forward = a.intersection_area(b, method=method)
                reverse = b.intersection_area(a, method=method)
                self.assertIsInstance(forward, float)
                self.assertTrue(np.isfinite(forward))
                self.assertGreaterEqual(forward, 0.0)
                np.testing.assert_allclose([forward, reverse], expected, rtol=rtol, atol=atol)
                self.assertLessEqual(forward, min(a.surface_area(), b.surface_area()) + atol)
        np.testing.assert_array_equal(a.hull, before[0])
        np.testing.assert_array_equal(b.hull, before[1])

    def test_analytic_configurations(self):
        cases = [
            (SQUARE + [3, 0], 0.),  # disjoint
            (SQUARE, 4.),  # identical/coincident edges
            (SQUARE * .5 + .5, 1.),  # full containment in both directions
            (SQUARE + [1, .5], 1.5),  # partial overlap
            (SQUARE + [2, 0], 0.),  # edge touching
            (SQUARE + [2, 2], 0.),  # vertex touching
            (SQUARE + [1, 0], 2.),  # partially coincident edges
            ([[0, 0], [1, 0], [2, 0], [2, 2], [0, 2]], 4.),  # collinear vertices
            ([[0, 0], [4, 0], [0, 4]], 4.),  # triangle against quadrilateral
            ([[-1, 1], [1, -1], [3, 1], [1, 3]], 4.),  # coincident vertices
        ]
        for other, area in cases:
            self.check_area(SQUARE, other, area)
        # A square with a corner cut off; intersect with x+y <= 2 triangle.
        pentagon = [[0, 0], [2, 0], [2, 1], [1, 2], [0, 2]]
        self.check_area(pentagon, [[0, 0], [2, 0], [0, 2]], 2.)
        self.check_area([[0, 0], [2, 0], [0, 2]], [[0, 0], [2, 0], [2, 2]], 1.)

    def test_orderings_and_windings(self):
        for order in ([0, 1, 2, 3], [3, 2, 1, 0], [2, 0, 3, 1]):
            self.check_area(SQUARE[order], (SQUARE + [1, .5])[order], 1.5)
        # Constructor normalizes ordering; explicitly exercise both cyclic
        # windings of the clipping implementation through the public method.
        for reverse_a in (False, True):
            for reverse_b in (False, True):
                a, b = Polygon(SQUARE), Polygon(SQUARE + [1, .5])
                if reverse_a:
                    a.hull = a.hull[::-1]
                if reverse_b:
                    b.hull = b.hull[::-1]
                self.assertAlmostEqual(a.intersection_area(b), 1.5)

    def test_transformations(self):
        for angle in (0., .37, 1.7):
            rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
            for scale in (.1, 1., 100.):
                for offset in ([0., 0.], [13., -27.]):
                    a = SQUARE @ rotation.T * scale + offset
                    b = (SQUARE + [1., .5]) @ rotation.T * scale + offset
                    self.check_area(a, b, 1.5 * scale**2, atol=2e-8)

    def test_small_intersections_without_rounding(self):
        for width in (1e-6, 1e-9, 2.**-40):
            shift = 2. - width
            expected = 2. * (2. - shift)  # area of the represented float64 inputs
            self.check_area(SQUARE, SQUARE + [shift, 0.], expected,
                            methods=(IntersectionAreaMethod.SUTHERLAND_HODGMAN,), rtol=1e-12, atol=0.)
        tiny = SQUARE * 1e-8
        self.check_area(tiny, tiny + [1e-8, 0.], 2e-16,
                        methods=(IntersectionAreaMethod.SUTHERLAND_HODGMAN,), rtol=1e-14, atol=0.)

    def test_nearly_parallel_edges(self):
        # Clipping y >= delta*x from the unit square removes a triangle
        # of area delta/2. The lower clip edge is almost horizontal.
        for delta in (1e-8, 1e-12):
            clip = [[0, 0], [1, delta], [1, 2], [0, 2]]
            self.check_area(SQUARE * .5, clip, 1. - delta / 2,
                            methods=(IntersectionAreaMethod.SUTHERLAND_HODGMAN,), rtol=0., atol=2e-16)

    def test_float64_promotion(self):
        # int64 edge products would overflow; float32 shoelace products
        # would overflow at this scale. The clipping method promotes both.
        for dtype in (np.int64, np.float32):
            a = Polygon(np.array(SQUARE * 1e20 if dtype == np.float32 else SQUARE * 1e10,
                                 dtype=dtype))
            length = float(a.hull[:, 0].max())
            np.testing.assert_allclose(a.intersection_area(a), length**2, rtol=1e-14)

    def test_legacy_nearly_parallel_rounding(self):
        square = Polygon(SQUARE * .5)
        clip = Polygon([[0., 0.], [1., 1e-12], [1., 2.], [0., 2.]])
        self.assertEqual(square.intersection_area(clip, IntersectionAreaMethod.LEGACY), 1.)
        np.testing.assert_allclose(square.intersection_area(clip), 1. - 5e-13,
                                   rtol=0., atol=2e-16)

    def test_large_translation(self):
        a = Polygon(SQUARE + 1e12)
        b = Polygon(SQUARE + [1, .5] + 1e12)
        self.assertEqual(a.intersection_area(b), 1.5)
        self.assertEqual(b.intersection_area(a), 1.5)

    def test_legacy_rounding_discrepancy(self):
        # Default legacy rounding to ten decimals collapses this thin strip.
        a, b = Polygon(SQUARE), Polygon(SQUARE + [2. - 2.**-40, 0.])
        self.assertGreater(a.intersection_area(b), 0.)
        self.assertEqual(a.intersection_area(b, method=IntersectionAreaMethod.LEGACY), 0.)

    def test_legacy_small_scale_discrepancy(self):
        # Edge determinants are below the legacy fixed 1e-10 parallel threshold.
        a, b = Polygon(SQUARE * 1e-8), Polygon(SQUARE * 1e-8 + [1e-8, 0.])
        np.testing.assert_allclose(a.intersection_area(b), 2e-16, rtol=1e-14, atol=0.)
        self.assertEqual(a.intersection_area(b, IntersectionAreaMethod.LEGACY), 0.)

    def test_zero_area_hulls(self):
        flat = Polygon([[0., 0.], [1., 0.], [2., 0.]])
        square = Polygon(SQUARE)
        self.assertEqual(flat.intersection_area(square), 0.)
        self.assertEqual(square.intersection_area(flat), 0.)

    def test_regular_polygons_and_invariants(self):
        rng = np.random.default_rng(42)
        for count_a, count_b in ((3, 7), (5, 11), (16, 9), (30, 32)):
            def regular(count):
                angles = np.linspace(0., 2 * np.pi, count, endpoint=False)
                return np.column_stack((np.cos(angles), np.sin(angles)))
            for _ in range(8):
                a = Polygon(regular(count_a))
                b = Polygon(regular(count_b) + rng.uniform(-1., 1., 2))
                results = []
                for method in METHODS:
                    area = a.intersection_area(b, method)
                    reverse = b.intersection_area(a, method)
                    self.assertTrue(np.isfinite(area))
                    self.assertGreaterEqual(area, 0.)
                    self.assertLessEqual(area, min(a.surface_area(), b.surface_area()) + 1e-9)
                    np.testing.assert_allclose(area, reverse, rtol=1e-9, atol=1e-9)
                    results.append(area)
                np.testing.assert_allclose(*results, rtol=1e-9, atol=1e-9)

    def test_enum_and_string_compatibility(self):
        a, b = Polygon(SQUARE), Polygon(SQUARE + 1.)
        for method in IntersectionAreaMethod:
            with self.subTest(method=method):
                self.assertEqual(IntersectionAreaMethod(method.value), method)
                self.assertEqual(a.intersection_area(b, method),
                                 a.intersection_area(b, method.value))
        self.assertEqual(IntersectionAreaMethod.SUTHERLAND_HODGMAN.value, 'sutherland_hodgman')
        self.assertEqual(IntersectionAreaMethod.LEGACY.value, 'legacy')

    def test_dispatch_and_independence(self):
        a, b = Polygon(SQUARE), Polygon(SQUARE + 1.)
        with patch.object(Polygon, 'intersection', side_effect=AssertionError('legacy called')):
            self.assertEqual(a.intersection_area(b), 1.)
        result = a.intersection(b)
        self.assertEqual(a.intersection_area(b, IntersectionAreaMethod.LEGACY), float(result.surface_area()))
        for method in ('unknown', '', 'Sutherland_Hodgman', None):
            with self.assertRaises(ValueError):
                a.intersection_area(b, method)
