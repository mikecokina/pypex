from pypex import Line


def main():
    line1 = Line([[0.0, 0.0], [1.1, 1.1]])
    line2 = Line([[0.0, 1.0], [1.0, 0.0]])

    intersects = line1.intersects(line2)
    print("{} is in intersection with {}: {}".format(line1, line2, intersects))

    intersection = line1.intersection(line2)
    print("{} intersects {} in {}\n".format(line1, line2, intersection))

    full = line1.intersects(line2, _full=True)
    print("full info of intersection of {} and {}\n"
          "     defined infinite lines intersects: {}\n"
          "     defined segments intersects: {}\n"
          "     defined segments intersects in {}\n"
          "     defined segments distance {}\n"
          "     defined segments description {}\n"
          "".format(line1, line2, full[0], full[1], full[2], full[3], full[4]))


    try:
        import matplotlib as mpl
        from matplotlib import pyplot as plt

        # mpl rcParams
        params = {'legend.fontsize': 8, 'legend.handlelength': 0.5, "font.size": 8}
        mpl.rcParams.update(params)

        colors, markers = ["r", "b"], ["x", "o"]
        for idx, line in enumerate([line1, line2]):
            for point in line.to_array():
                plt.scatter(point[0], point[1], s=50, c=colors[idx], marker=markers[idx])
            plt.plot(line.to_array().T[0], line.to_array().T[1], c=colors[idx])
        plt.show()
    except ImportError:
        pass

    line1 = Line([[0.0, 0.0], [1.1, 1.1]])
    line2 = Line([[0.0, 1.0], [1.1, 2.1]])
    full = line1.intersects(line2, _full=True)
    print("full info of intersection of {} and {}\n"
          "     defined infinite lines intersects: {}\n"
          "     defined segments intersects: {}\n"
          "     defined segments intersects in {}\n"
          "     defined segments distance {}\n"
          "     defined segments description {}\n"
          "".format(line1, line2, full[0], full[1], full[2], full[3], full[4]))

    try:
        import matplotlib as mpl
        from matplotlib import pyplot as plt

        # mpl rcParams
        params = {'legend.fontsize': 8, 'legend.handlelength': 0.5, "font.size": 8}
        mpl.rcParams.update(params)

        colors, markers = ["r", "b"], ["x", "o"]
        for idx, line in enumerate([line1, line2]):
            for point in line.to_array():
                plt.scatter(point[0], point[1], s=50, c=colors[idx], marker=markers[idx])
            plt.plot(line.to_array().T[0], line.to_array().T[1], c=colors[idx])
        plt.show()
    except ImportError:
        pass

    line1 = Line([[0.0, 0.0], [1.1, 1.1]])
    line2 = Line([[0.0, 0.0], [2.1, 2.1]])
    full = line1.intersects(line2, _full=True)
    print("full info of intersection of {} and {}\n"
          "     defined infinite lines intersects: {}\n"
          "     defined segments intersects: {}\n"
          "     defined segments intersects in {}\n"
          "     defined segments distance {}\n"
          "     defined segments description {}\n"
          "".format(line1, line2, full[0], full[1], full[2], full[3], full[4]))

    try:
        import matplotlib as mpl
        from matplotlib import pyplot as plt

        # mpl rcParams
        params = {'legend.fontsize': 8, 'legend.handlelength': 0.5, "font.size": 8}
        mpl.rcParams.update(params)

        colors, markers = ["r", "b"], ["x", "o"]
        for idx, line in enumerate([line1, line2]):
            for point in line.to_array():
                plt.scatter(point[0], point[1], s=50, c=colors[idx], marker=markers[idx], zorder=80 if idx == 0 else 50)
            plt.plot(line.to_array().T[0], line.to_array().T[1], c=colors[idx])
        plt.show()
    except ImportError:
        pass

    line1 = Line([[0.0, 0.0], [1.1, 1.1]])
    line2 = Line([[1.2, 1.2], [2.1, 2.1]])
    full = line1.intersects(line2, _full=True)
    print("full info of intersection of {} and {}\n"
          "     defined infinite lines intersects: {}\n"
          "     defined segments intersects: {}\n"
          "     defined segments intersects in {}\n"
          "     defined segments distance {}\n"
          "     defined segments description {}\n"
          "".format(line1, line2, full[0], full[1], full[2], full[3], full[4]))

    try:
        import matplotlib as mpl
        from matplotlib import pyplot as plt

        # mpl rcParams
        params = {'legend.fontsize': 8, 'legend.handlelength': 0.5, "font.size": 8}
        mpl.rcParams.update(params)

        colors, markers = ["r", "b"], ["x", "o"]
        for idx, line in enumerate([line1, line2]):
            for point in line.to_array():
                plt.scatter(point[0], point[1], s=50, c=colors[idx], marker=markers[idx], zorder=80 if idx == 0 else 50)
            plt.plot(line.to_array().T[0], line.to_array().T[1], c=colors[idx])
        plt.show()
    except ImportError:
        pass


if __name__ == "__main__":
    main()
