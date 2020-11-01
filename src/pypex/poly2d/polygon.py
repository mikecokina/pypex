import numpy as np
import matplotlib.path as mpltpath

from pypex.base import shape
from pypex.poly2d.intersection import sat, linter
from pypex.poly2d.point import Point
from pypex.poly2d.point import is_point_in_polygon
from pypex.poly2d.line import Line
from pypex.base.conf import ROUND_PRECISION


class Polygon(shape.Shape2D):
    """
    Convex Polygon
    """
    def __init__(self, hull, **kwargs):
        super(Polygon, self).__init__(hull=hull, **kwargs)
        self.sort_clockwise(inplace=True)
        self.mplpath = mpltpath.Path(self.hull)

    def edges(self, as_line=False):
        """
        Provide method to iterate over edges in polygon.
        :param as_line: bool; if True, numpy.array representation of edge is transformed to pypex.poly2d.line.Line
        :return: numpy.array;
        """
        for i in range(-1, len(self.hull)-1, 1):
            edge = np.array([self.hull[i], self.hull[i+1]])
            if as_line:
                edge = Line(edge)
            yield edge

    def intersects(self, poly, in_touch=False, round_tol=ROUND_PRECISION):
        """
        Whether two polygons intersects.

        :param round_tol: int;
        :param poly: pypex.poly2d.polygon.Polygon;
        :param in_touch: bool;
        :return: bool;
        """
        return sat.intersects(self.hull, poly.hull, in_touch, round_tol)

    def intersection(self, poly, round_tol=ROUND_PRECISION):
        """
        Find intersection polygon created by clipping of one polygon by another.

        :param poly: pypex.poly2d.polygon.Polygon
        :param round_tol: int; round precision of decimal points to consider numbers as same
        :return: pypex.poly2d.polygon.Polygon
        """
        in_poly1 = poly.hull[self.mplpath.contains_points(poly.hull)]
        in_poly2 = self.hull[poly.mplpath.contains_points(self.hull)]
        intersection_poly = np.concatenate((in_poly1, in_poly2), axis=0)
        intersection_poly = np.array([Point(*point) for point in intersection_poly])

        _, intersection_segment, intr_ptx, _, msg, _ = linter.intersections(self.hull, poly.hull, in_touch=True)
        points_mask = np.logical_and(msg == b'INTERSECT', intersection_segment)
        intr_ptx = [Point(*point) for point in intr_ptx[points_mask]]
        intersection_poly = np.concatenate((intersection_poly, intr_ptx), axis=0)
        intersection_poly = Point.set(intersection_poly, round_tol=round_tol)
        return Polygon(intersection_poly, _validity=False) if len(intersection_poly) > 2 else None

    def to_array(self):
        return self.hull

    def contains_point(self, point):
        """
        Test wether point lie in polygon.

        :param point: pypex.poly2d.point.Point
        :return:
        """
        return is_point_in_polygon(point, self)

    contains_Point = contains_point

    def surface_area(self):
        """
        Compute surface area of given polygon instance.
        :return: float; surface area of given polygon
        """
        lines = linter.polygon_hull_to_edges(self.hull)
        return 0.5 * np.abs(np.sum(lines[:, 0, 0] * lines[:, 1, 1] - lines[:, 1, 0] * lines[:, 0, 1]))

    def inpolygon(self):
        """
        Find polygon which points are defind as center of each edge of original polygon.
        :return: pypex.poly2d.polygon.Polygon
        """
        _inpolygon = list()
        for edge in self.edges(as_line=True):
            parametrized = edge.parametrized()
            _inpolygon.append(parametrized(0.5))
        return Polygon(_inpolygon)
