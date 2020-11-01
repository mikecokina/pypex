from pypex import Point, Polygon


def main():
    point = Point(0.3, 0.3)
    polygon = Polygon([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    in_poly = point.is_inside_polygon(polygon)
    print("{} is inside polygon: {}".format(point, in_poly))

    try:
        import matplotlib as mpl
        from matplotlib import pyplot as plt
        from matplotlib.patches import Polygon as polyg
        from matplotlib.collections import PatchCollection

        # mpl rcParams
        params = {'legend.fontsize': 8, 'legend.handlelength': 0.5, "font.size": 8}
        mpl.rcParams.update(params)

        fig, ax = plt.subplots(nrows=1, ncols=1)
        patches = [polyg(polygon.hull, True), polyg(polygon.hull, True)]
        p = PatchCollection(patches, cmap=mpl.cm.jet, alpha=0.4, edgecolors="k", facecolors="g")
        # p.set_array(np.array([10, 0, 0, 0, 1]))
        ax.add_collection(p)
        ax.scatter(point.to_array().T[0], point.to_array().T[1], s=50, c="r", marker="x")

        plt.xlim(-0.2, 1.2)
        plt.ylim(-0.2, 1.2)
        plt.show()
    except ImportError:
        pass

    pnt_array = point.to_array()
    print("Point as numpy array {}".format(pnt_array))

    pnt_list = point.to_list()
    print("Point as python list {}".format(pnt_list))

    points = [Point(0.3456111, 0.3123), Point(0.3456, 0.3123)]
    set_tol3 = Point.set(points, round_tol=3)
    print("Points {} define following set with tolerance 3: {}".format(points, set_tol3))

    set_tol9 = Point.set(points, round_tol=9)
    print("Points {} define following set with tolerance 9: {}".format(points, set_tol9))


if __name__ == "__main__":
    main()
