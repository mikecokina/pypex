import numpy as np

from pypex.base import shape
from pypex.poly2d.intersection import sat
from pypex.poly2d.point import Point
from pypex.poly2d.line import Line


class Polygon(shape.Shape2D):
    """
    Convex Polygon
    """
    def __init__(self, hull):
        super(Polygon, self).__init__(hull=hull)

        # todo: it works just for convex polygons
        self.sort_clockwise(inplace=True)

    def edges(self):
        for i in range(-1, len(self.hull)-1, 1):
            yield np.array([self.hull[i], self.hull[i+1]])

    def intersects(self, poly):
        # todo: implement convexity test
        return sat.intersects(self.hull, poly.hull)

    def intersection(self, poly):
        # initialise list for intersection polygon
        intersection_poly = list()

        # add  the corners of `self` which are inside poly
        poly1 = np.array([Point(x=corner[0], y=corner[1]) for corner in self.hull])
        poly2 = np.array([Point(x=corner[0], y=corner[1]) for corner in poly.hull])

        in_poly1 = poly2[[corner.is_inside_polygon(self) for corner in poly2]]
        in_poly2 = poly1[[corner.is_inside_polygon(poly) for corner in poly1]]
        intersection_poly = np.concatenate((in_poly1, in_poly2), axis=0)



        # find point of intersected edges
        i = 0
        for edge1 in self.edges():
            line1 = Line(edge1)
            for edge2 in poly.edges():
                i += 1
                line2 = Line(edge2)
                intersection = line1.intersects(line2, _full=True)
                print(intersection)

