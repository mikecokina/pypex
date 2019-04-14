from pypex.poly2d import line


def main():
    line1 = line.Line([[0.0, 0.0], [1.1, 1.1]])
    line2 = line.Line([[0.0, 1.0], [1.0, 0.0]])

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

    line1 = line.Line([[0.0, 0.0], [1.1, 1.1]])
    line2 = line.Line([[0.0, 1.0], [1.1, 2.1]])
    full = line1.intersects(line2, _full=True)
    print("full info of intersection of {} and {}\n"
          "     defined infinite lines intersects: {}\n"
          "     defined segments intersects: {}\n"
          "     defined segments intersects in {}\n"
          "     defined segments distance {}\n"
          "     defined segments description {}\n"
          "".format(line1, line2, full[0], full[1], full[2], full[3], full[4]))

    line1 = line.Line([[0.0, 0.0], [1.1, 1.1]])
    line2 = line.Line([[0.0, 0.0], [2.1, 2.1]])
    full = line1.intersects(line2, _full=True)
    print("full info of intersection of {} and {}\n"
          "     defined infinite lines intersects: {}\n"
          "     defined segments intersects: {}\n"
          "     defined segments intersects in {}\n"
          "     defined segments distance {}\n"
          "     defined segments description {}\n"
          "".format(line1, line2, full[0], full[1], full[2], full[3], full[4]))

    line1 = line.Line([[0.0, 0.0], [1.1, 1.1]])
    line2 = line.Line([[1.2, 1.2], [2.1, 2.1]])
    full = line1.intersects(line2, _full=True)
    print("full info of intersection of {} and {}\n"
          "     defined infinite lines intersects: {}\n"
          "     defined segments intersects: {}\n"
          "     defined segments intersects in {}\n"
          "     defined segments distance {}\n"
          "     defined segments description {}\n"
          "".format(line1, line2, full[0], full[1], full[2], full[3], full[4]))


if __name__ == "__main__":
    main()
