import numpy as np

from pypex.poly2d import polygon as poly


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


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[{}, {}]".format(self.x, self.y)

    def __repr__(self):
        return "[{}, {}]".format(self.x, self.y)

    def is_inside_polygon(self, polygon: poly.Polygon):
        return is_point_in_polygon(self, polygon)
