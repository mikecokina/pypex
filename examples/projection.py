import numpy as np
from pypex import projection


def main():
    point = np.array([0.3, 0.4])
    x_like_vector = np.array([1.0,  1.0])
    # vector which define `x` axis of new system
    new_x_like_vector = x_like_vector / np.linalg.norm(x_like_vector)
    # perpendicular to `new_x_like_vector` which define y axis of new system
    new_y_like_vector = [-new_x_like_vector[1], new_x_like_vector[0]]
    projected_point = projection.cartesian_to_vectors_defined(tn=new_x_like_vector, nn=new_y_like_vector, vector=point)
    print('Point {} projected to new system as {}'.format(point, projected_point))

    try:
        import matplotlib as mpl
        from matplotlib import pyplot as plt

        # mpl rcParams
        params = {'legend.fontsize': 8, 'legend.handlelength': 0.5, "font.size": 8}
        mpl.rcParams.update(params)

        plt.scatter(point[0], point[1], c='r')
        plt.scatter(projected_point[0], projected_point[1], c='b')
        plt.plot([0.0, new_x_like_vector[0]], [0.0, new_x_like_vector[1]])
        plt.plot([0.0, new_y_like_vector[0]], [0.0, new_y_like_vector[1]])
        plt.axis('equal')
        plt.grid(True)
        plt.show()
    except ImportError:
        pass

    # direction vector
    to_vector = np.array([0.3, 1.2])
    # vector which will be ptojected to direction vetor
    vector = np.array([1.0, 1.0])
    # vector projected to direction vector
    projected_vector = projection.projection(vector, to_vector)
    print("Vector {} projected to vector {} as {}".format(vector, to_vector, projected_vector))

    try:
        import matplotlib as mpl
        from matplotlib import pyplot as plt

        # mpl rcParams
        params = {'legend.fontsize': 8, 'legend.handlelength': 0.5, "font.size": 8}
        mpl.rcParams.update(params)

        plt.plot([0.0, to_vector[0]], [0.0, to_vector[1]])
        plt.plot([0.0, vector[0]], [0.0, vector[1]])
        plt.scatter(projected_vector[0], projected_vector[1])
        plt.axis('equal')
        plt.show()
    except ImportError:
        pass


if __name__ == "__main__":
    main()
