import numpy as np
from pypex.poly2d import polygon


def main():
    poly1 = polygon.Polygon([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    poly2 = polygon.Polygon([[0.5, 0.3], [0.0, -1.0], [1.0, -1.0]])

    print("Polygon with hull defined by {} \n is automaticaly sorted to clokwise corners as {}\n"
          "".format([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], poly1.hull))

    try:
        import matplotlib
        import matplotlib.pyplot as plt
        from matplotlib.patches import Polygon as polyg
        from matplotlib.collections import PatchCollection

        # mpl rcParams
        params = {'legend.fontsize': 8, 'legend.handlelength': 0.5, "font.size": 8}
        matplotlib.rcParams.update(params)

        fig, ax = plt.subplots()
        patches = [polyg(poly1.hull, True), polyg(poly2.hull, True)]
        p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)
        colors = 100 * np.random.rand(len(patches))
        p.set_array(np.array(colors))
        ax.add_collection(p)
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.show()
    except ImportError:
        pass

    print("\n {} has following edges".format(poly1))
    for edge in poly1.edges():
        print("edge {}".format(edge))
    print("\n")

    intersects = poly1.intersects(poly2)
    print("{} intersects {}: {}".format(poly1, poly2, intersects))

    intersection = poly1.intersection(poly2)
    print("Intersection of {} and {} is following polygon: \n"
          "     {}".format(poly1, poly2, intersection))

    try:
        import matplotlib
        import matplotlib.pyplot as plt
        from matplotlib.patches import Polygon as polyg
        from matplotlib.collections import PatchCollection

        # mpl rcParams
        params = {'legend.fontsize': 8, 'legend.handlelength': 0.5, "font.size": 8}
        matplotlib.rcParams.update(params)

        fig, ax = plt.subplots()
        patches = [polyg(poly1.hull, True), polyg(poly2.hull, True)]
        p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4, edgecolors="k")
        colors = 100 * np.random.rand(len(patches))
        p.set_array(np.array(colors))
        ax.add_collection(p)
        plt.scatter(intersection.hull.T[0], intersection.hull.T[1])
        plt.xlim(-0.5, 1.5)
        plt.ylim(-1.5, 1.5)
        plt.show()
    except ImportError:
        pass

    # inpolygon
    _polygon = np.array([[0.0, 0.0], [0.3, 0.0], [0.4, 1.1], [0.1, 0.5]])
    poly = polygon.Polygon(_polygon)
    inpolygon = poly.inpolygon()

    try:
        import matplotlib
        import matplotlib.pyplot as plt
        from matplotlib.patches import Polygon as polyg
        from matplotlib.collections import PatchCollection

        # mpl rcParams
        params = {'legend.fontsize': 8, 'legend.handlelength': 0.5, "font.size": 8}
        matplotlib.rcParams.update(params)

        fig, ax = plt.subplots()
        patches = [polyg(poly.hull, True), polyg(inpolygon.hull, True)]
        p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4, edgecolors="k")
        colors = 100 * np.random.rand(len(patches))
        p.set_array(np.array(colors))
        ax.add_collection(p)
        plt.xlim(-0.25, 0.6)
        plt.ylim(-0.25, 1.2)
        plt.show()

    except ImportError:
        pass


if __name__ == "__main__":
    main()
