from pypex.poly2d import polygon as poly


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[{}, {}]".format(self.x, self.y)

    def __repr__(self):
        return "[{}, {}]".format(self.x, self.y)

    def is_inside_polygon(self, polygon: poly.Polygon):
        pass
