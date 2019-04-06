from pypex.base import shape
from pypex.poly2d.intersection import sat


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
