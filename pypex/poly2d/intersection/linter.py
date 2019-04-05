import numpy as np
from pypex.base.conf import PRECISION


def intersection(p1, p2, a, b):
    """
    defs:
          x1, y1 = p1 + u * (p2 - p1) = p1 + u * dp1
          x2, y2 = a + v * (b - a) = a + v * dp2
          dp1 = p2 - p1 = (p2_x - p1_x, p2_y - p1_y)
          dp2 = pt4 - pt3 = (pt4_x - pt3_x, pt4_y - pt3_y)

    intersection:
          x1, y1 = x2, y2
          p1 + u * dp1 = a + v * dp2

          in coo:
          p1_x + u * dp1_x = pt3_x + v * dp2_x
          p1_y + u * dp1_y = pt3_y + v * dp2_y

          variables: u, v
          solution:
          d = (dp1_x * dp2_y) - (dp1_y * dp2_x)
          u = (((p1_y - pt3_y) * dp2_x) - (dp2_y * (p1_x - pt3_x))) / d
          v = (((p1_y - pt3_y) * dp1_x) - (dp1_y * (p1_x - pt3_x))) / d

    :param p1: numpy.array; first point of first segment
    :param p2: numpy.array; second point of first segment
    :param a: numpy.array; first point of second segment
    :param b: numpy.array; second point of second segment
    :return: tuple
                  0: intersection_status:
                          False: parallel
                          True:  intersection
                  1: segment intersection:
                          False:     no intersection
                          True:      intersection between defined points
                          numpy.nan: uknown
                  2: intersection point x value if exists, if not numpy.nan
                  3: intersection point y value if exists, if not numpy.nan
                  4: distance if parallel
    """
    p1, p2, a, b = np.array(p1), np.array(p2), np.array(a), np.array(b)
    # first line
    dp1 = p2 - p1
    # second line
    dp2 = b - a
    # determinant
    matrix = np.array([dp1, dp2])
    d = np.linalg.det(matrix)

    # test if d < 1e-10
    # testing on zero, but precission should cause a problem
    if np.abs(d) < PRECISION:
        # test distance between lines
        # if general form is known (ax + by + c1 = 0 and ax + by + c2 = 0),
        # d = abs(c1 - c2) / sqrt(a**2 + b**2)
        # parametric equation in general:
        #   x, y = [p1_x, p1_y] + u * [T_x, T_y], where T is tangential vector defined as p2 - p1
        # N = (a, b) represent normal vector of line; a, b from general equation of line
        # N = [-Ty, Tx], can be obtained
        # general equation:
        #   -Ty * x + Tx * y + c = 0, then
        # c = Ty * p1_x - Tx * p1_y
        # finaly, general equation:
        #   -Ty * x + Tx * y + (Ty * p1_x - Tx * p1_y) = 0
        #
        #
        # a1, b1, c1 = -dp1_y, dp1_x, (dp1_y * pt1_x) - (dp1_x * pt1_y)
        # a2, b2, c2 = -dp2_y, dp2_x, (dp2_y * pt3_x) - (dp2_x * pt3_y)

        a1, b1, c1 = -dp1[1], dp1[0], np.linalg.det(np.array([p1, dp1]))
        a2, b2, c2 = -dp2[1], dp2[0], np.linalg.det(np.array([a, dp2]))

        # sign of y coefficient (b1, b2)
        # we want same sign at y
        sign1 = +1 if b1 >= 0 else -1
        sign2 = +1 if b2 >= 0 else -1
        c2 *= +1 if sign1 == sign2 else -1

        d = abs(c2 - c1) / (np.sqrt(a1 ** 2 + b1 ** 2))

        int_segment, msg = (True, "OVERLAPPING") if d == 0 else (False, "PARALLEL")
        return int_segment, np.nan, np.nan, np.nan, d, msg

    # +0 because of negative zero (-0.0 is incorrect) formatting on output
    u = (np.linalg.det([dp2, p1 - a]) / d) + 0.
    v = (np.linalg.det([dp1, p1 - a]) / d) + 0.

    int_x, int_y = p1[0] + (u * dp1[0]), p1[1] + (u * dp1[1])
    int_segment = True if 0.0 <= u <= 1.0 and 0.0 <= v <= 1.0 else False
    return True, int_segment, int_x, int_y, np.nan, "INTERSECTING"
