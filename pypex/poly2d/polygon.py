from pypex.base import shape
from pypex.poly2d import sat


class Polygon(shape.Shape2D):
    def __init__(self, hull):
        super(Polygon, self).__init__(hull=hull)

    def is_convex(self):
        pass

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
