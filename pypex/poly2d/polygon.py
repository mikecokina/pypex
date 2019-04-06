import numpy as np

from pypex.base import shape
from pypex.poly2d.intersection import sat


class Polygon(shape.Shape2D):
    """
    Convex Polygon
    """
    def __init__(self, hull):
        super(Polygon, self).__init__(hull=hull)

        # todo: it works just for convex polygons
        self.sort_clockwise(inplace=True)

    def intersects(self, poly):
        # todo: implement convexity test
        return sat.intersects(self.hull, poly.hull)

    def intersection(self, poly):
        pass


class Line(shape.Shape2D):
    def intersects(self, line):
        pass

    def intersection(self, line):
        pass
