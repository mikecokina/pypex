import numpy as np

from pypex.base.conf import ROUND_PRECISION as PRECISION


def _line_side(p1, p2, a, b):
    """
    Idea is described in ``
    Help to determine, whether both point of line p lie on the same side of line ab or not.

    :param p1: numpy.array; firs point of line p
    :param p2: numpy.array; second point of line p
    :param a: numpy.array; first point of line p'
    :param b: numpy.array; second point of line p'
    :return: float
    """
    p1, p2, a, b = np.array(p1), np.array(p2), np.array(a), np.array(b)
    cp1 = np.cross(b - a, p1 - a)
    cp2 = np.cross(b - a, p2 - a)
    return np.dot(cp1, cp2)


# /* Check whether p1 and p2 lie on the same side of line ab */
# todo: reconsider to use edge definition instead of single point in arguments
def same_side(p1, p2, a, b):
    """
    Idea is described in ``
    Determine, whether both point of line p lie on the same side of line ab or not.

    :param p1: numpy.array; firs point of line p
    :param p2: numpy.array; second point of line p
    :param a: numpy.array; first point of line p'
    :param b: numpy.array; second point of line p'
    :return: float
    """
    # todo: add possibility to deside whther on edge point is inside or outside
    return True if _line_side(p1, p2, a, b) >= 0 else False


def is_point_in_polygon(point, polygon):
    """

    :param point: pypex.poly2d.point.Point
    :param polygon: pypex.poly2d.polygon.Polygon
    :return:
    """
    polygon = polygon.sort_clockwise(inplace=False)
    point = np.array([point.x, point.y])
    result = True

    for i in range(-2, len(polygon)-2):
        latest = same_side(point, polygon[i], polygon[i+1], polygon[i+2])
        result &= latest
    return result


class _Point(object):
    def __init__(self, i, x, y):
        self.i = i
        self.x = x
        self.y = y

    def __key(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return (other.x == self.x) & (other.y == self.y)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point [{}, {}]".format(self.x, self.y)

    def __repr__(self):
        return "Point [{}, {}]".format(self.x, self.y)

    def __eq__(self, other):
        return (other.x == self.x) & (other.y == self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    @staticmethod
    def set(points, tol=PRECISION):
        _points = [_Point(i, round(point.x, tol), round(point.y, tol)) for i, point in enumerate(points)]
        indices = [_point.i for _point in set(_points)]
        return np.array(points)[indices]

    def is_inside_polygon(self, polygon):
        return is_point_in_polygon(self, polygon)

    def to_list(self):
        return [self.x, self.y]

    def to_array(self):
        return np.array(self.to_list())
