import numpy as np

from pypex.base import shape
from pypex.poly2d.intersection import sat


class Polygon(shape.Shape2D):
    def __init__(self, hull):
        super(Polygon, self).__init__(hull=hull)

        # todo: it works just for convex polygons
        self.sort_clockwise(inplace=True)

    def is_convex(self):
        """
        For each consecutive pair of edges of the polygon (each triplet of points), compute
        the z-component of the cross product of the vectors defined by the edges pointing
        towards the points in increasing order. Take the cross product of these vectors:

        given p[k], p[k+1], p[k+2] each with coordinates x, y:
        dx1 = x[k+1]-x[k]
        dy1 = y[k+1]-y[k]
        dx2 = x[k+2]-x[k+1]
        dy2 = y[k+2]-y[k+1]
        zcrossproduct = dx1*dy2 - dy1*dx2

        The polygon is convex if the z-components of the cross products are either all positive
        or all negative. Otherwise the polygon is nonconvex.

        :return: bool
        """
        # todo: this method makes no sense here, 'till sort clokwise is not capable to sort non convex corners
        signs = list()
        for i in range(-2, len(self.hull) - 2):
            v1, v2 = self.hull[i] - self.hull[i+1], self.hull[i+1] - self.hull[i+2]
            d = np.linalg.det([v1, v2]) + 0.
            signs.append(True if d >= 0 else False)
        return np.all(signs)

    def intersects(self, poly):
        # todo: implement convexity test
        return sat.intersects(self.hull, poly.hull)

    def intersection(self, poly):
        pass


class Triangle(shape.Shape2D):
    def __init__(self, hull):
        self.triangle_validity_check(hull, _raise=True)
        super(Triangle, self).__init__(hull=hull)

    def intersection(self, triangle):
        pass

    def intersects(self, triangle):
        pass

    @staticmethod
    def is_convex():
        return True


class Line(shape.Shape2D):
    def intersects(self, line):
        pass

    def intersection(self, line):
        pass
