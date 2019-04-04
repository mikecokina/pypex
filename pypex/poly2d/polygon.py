from pypex.base import shape


class Polygon(shape.Shape2D):
    def __init__(self, hull):
        super(Polygon, self).__init__(hull=hull)

    def is_convex(self):
        pass

    def intersects(self, poly):
        pass

    def intersection(self, poly):
        pass


class Line(shape.Shape2D):
    def intersects(self, line):
        pass

    def intersection(self, line):
        pass
