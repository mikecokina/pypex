from pypex.poly2d import point
from pypex.poly2d import polygon


def main():
    pnt = point.Point(0.3, 0.3)
    poly = polygon.Polygon([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    in_poly = pnt.is_inside_polygon(poly)
    print("{} is inside polygon: {}".format(pnt, in_poly))

    pnt_array = pnt.to_array()
    print("Point as numpy array {}".format(pnt_array))

    pnt_list = pnt.to_list()
    print("Point as python list {}".format(pnt_list))

    points = [point.Point(0.3456111, 0.3123), point.Point(0.3456, 0.3123)]
    set_tol3 = point.Point.set(points, round_tol=3)
    print("Points {} define following set with tolerance 3: {}".format(points, set_tol3))

    set_tol9 = point.Point.set(points, round_tol=9)
    print("Points {} define following set with tolerance 9: {}".format(points, set_tol9))


if __name__ == "__main__":
    main()
