|Travis build|  |GitHub version|  |Licence GPLv2| |Python version| |OS|

.. |Travis build| image:: https://travis-ci.org/mikecokina/pypex.svg?branch=dev
    :target: https://travis-ci.org/mikecokina/pypex

.. |GitHub version| image:: https://img.shields.io/badge/version-0.2.1-yellow.svg
   :target: https://github.com/Naereen/StrapDown.js

.. |Python version| image:: https://img.shields.io/badge/python-3.6|3.7|3.8|3.9-orange.svg
   :target: https://github.com/Naereen/StrapDown.js

.. |Licence GPLv2| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/Naereen/StrapDown.js

.. |OS| image:: https://img.shields.io/badge/os-Linux|Windows|macOS-magenta.svg
   :target: https://github.com/Naereen/StrapDown.js

.. _example_scripts: https://github.com/mikecokina/elisa/tree/master/scripts/analytics

Pypex
=====

**Pypex** is python library created for purpose of easier interactions with 2D convex polygons and lines.
It gives you a strong and simple tool if you need determine properties such as surface areas of polygons
defined by points, find if two lopygons intersects each other or determine polygon in which other two defined
polygons intersects.

Examples
--------

In this sections are shown several examples of `pypex` usage.

Point vs Polygon interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**[In]**

.. code-block:: python

    from pypex import Polygon, Point

    point = Point(0.3, 0.3)
    polygon = Polygon([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    # You can also use .contains_point() in case of Polygon instance.
    in_poly = point.is_inside_polygon(polygon)
    print(f"{point} is inside polygon: {in_poly}")

**[Out]**::

    Point [0.3, 0.3] is inside polygon: True


.. image:: ./docs/source/_static/pnt_vs_poly.svg
  :width: 50%
  :alt: pnt_vs_poly.svg
  :align: center


Point properties
~~~~~~~~~~~~~~~~

**[In]**

.. code-block:: python

    from pypex import Polygon, Point

    point = Point(0.3, 0.3)
    pnt_array = point.to_array()
    print(f"Point as numpy array {pnt_array}")

**[Out]**::

    Point as numpy array [0.3 0.3]

**[In]**

.. code-block:: python

    pnt_list = point.to_list()
    print(f"Point as python list {pnt_list}")

**[Out]**::

    Point as python list [0.3, 0.3]

**[In]**

.. code-block:: python

    points = [Point(0.3456111, 0.3123), Point(0.3456, 0.3123)]
    set_tol3 = Point.set(points, round_tol=3)
    print(f"Points {points} define following set with tolerance 3: {set_tol3}"))

**[Out]**::

    Points [Point [0.3456111, 0.3123], Point [0.3456, 0.3123]] define following set with tolerance 3: [Point [0.3456111, 0.3123]]


**[In]**

.. code-block:: python

    set_tol9 = Point.set(points, round_tol=9)
    print("Points {points} define following set with tolerance 9: {set_tol9}")

**[Out]**::

    Points [Point [0.3456111, 0.3123], Point [0.3456, 0.3123]] define following set with tolerance 9: [Point [0.3456111, 0.3123] Point [0.3456, 0.3123]]


Line vs Line interaction
~~~~~~~~~~~~~~~~~~~~~~~~

**[In]**

.. code-block:: python

    line1 = Line([[0.0, 0.0], [1.1, 1.1]])
    line2 = Line([[0.0, 1.0], [1.0, 0.0]])

    intersects = line1.intersects(line2)
    print(f"{line1} is in intersection with {line2}: {intersects}")

**[Out]**::

    Line: [[0. 0.], [1.1 1.1]] is in intersection with Line: [[0. 1.], [1. 0.]]: True


**[In]**

.. code-block:: python

    intersection = line1.intersection(line2)
    print(f"{line1} intersects {line2} in {intersection}")

**[Out]**::

    Line: [[0. 0.], [1.1 1.1]] intersects Line: [[0. 1.], [1. 0.]] in Point [0.5, 0.5]

**[In]**

.. code-block:: python

    # full output
    full = line1.intersects(line2, _full=True)
    print("full info of intersection of {} and {}\n"
          "     defined infinite lines intersects: {}\n"
          "     defined segments intersects: {}\n"
          "     defined segments intersects in {}\n"
          "     defined segments distance {}\n"
          "     defined segments description {}\n"
          "".format(line1, line2, full[0], full[1], full[2], full[3], full[4]))

**[Out]**::

    full info of intersection of Line: [[0. 0.], [1.1 1.1]] and Line: [[0. 1.], [1. 0.]]
        defined infinite lines intersects: True
        defined segments intersects: True
        defined segments intersects in Point [0.5, 0.5]
        defined segments distance nan
        defined segments description INTERSECT

.. image:: ./docs/source/_static/ln_vs_ln_00.svg
  :width: 50%
  :alt: ln_vs_ln_00.svg
  :align: center

**[In]**

.. code-block:: python

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

**[Out]**::

    full info of intersection of Line: [[0. 0.], [1.1 1.1]] and Line: [[0. 1.], [1.1 2.1]]
        defined infinite lines intersects: False
        defined segments intersects: False
        defined segments intersects in nan
        defined segments distance 0.7071067811865476
        defined segments description PARALLEL

.. image:: ./docs/source/_static/ln_vs_ln_01.svg
  :width: 50%
  :alt: ln_vs_ln_01.svg
  :align: center

**[In]**

.. code-block:: python

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

**[Out]**::

    full info of intersection of Line: [[0. 0.], [1.1 1.1]] and Line: [[0. 0.], [2.1 2.1]]
        defined infinite lines intersects: True
        defined segments intersects: True
        defined segments intersects in nan
        defined segments distance 0.0
        defined segments description OVERLAP

.. image:: ./docs/source/_static/ln_vs_ln_02.svg
  :width: 50%
  :alt: ln_vs_ln_02.svg
  :align: center

**[In]**

.. code-block:: python

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

**[Out]**::

    full info of intersection of Line: [[0. 0.], [1.1 1.1]] and Line: [[1.2 1.2], [2.1 2.1]]
        defined infinite lines intersects: True
        defined segments intersects: False
        defined segments intersects in nan
        defined segments distance 0.0
        defined segments description OVERLAP

.. image:: ./docs/source/_static/ln_vs_ln_03.svg
  :width: 50%
  :alt: ln_vs_ln_03.svg
  :align: center

Polygon vs polygon interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**[In]**

.. code-block:: python

    import numpy as np
    from pypex.poly2d import polygon

    poly1 = polygon.Polygon([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    poly2 = polygon.Polygon([[0.5, 0.3], [0.0, -1.0], [1.0, -1.0]])

    print("Polygon with hull defined by {} \n is automaticaly sorted to clokwise corners as {}\n"
          "".format([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], poly1.hull))



**[Out]**::

    Polygon with hull defined by [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
    is automaticaly sorted to clokwise corners as [[0. 0.] [1. 0.] [1. 1.] [0. 1.]]


**[In]**

.. code-block:: python

    print(f"\n {poly1} has following edges")
    for edge in poly1.edges():
        print(f"edge {edge}")

**[Out]**::

    Poly (4): [[0. 0.], [1. 0.], [1. 1.], [0. 1.]] has following edges
    edge [[0. 1.] [0. 0.]]
    edge [[0. 0.] [1. 0.]]
    edge [[1. 0.] [1. 1.]]
    edge [[1. 1.] [0. 1.]]

**[In]**

.. code-block:: python

    intersects = poly1.intersects(poly2)
    print(f"{poly1} intersects {poly2}: {intersects}")

**[Out]**::

    Poly (4): [[0. 0.], [1. 0.], [1. 1.], [0. 1.]] intersects Poly (3): [[ 0. -1.], [ 1. -1.], [0.5 0.3]]: True


**[In]**

.. code-block:: python

    intersection = poly1.intersection(poly2)
    print(f"Intersection of {poly1} and {poly2} is following polygon: \n"
          f"{intersection}")

**[Out]**::

    Intersection of Poly (4): [[0. 0.], [1. 0.], [1. 1.], [0. 1.]] and Poly (3): [[ 0. -1.], [ 1. -1.], [0.5 0.3]] is following polygon:
    Poly (3): [[0.38461538 0.        ], [0.61538462 0.        ], [0.5 0.3]]


.. image:: ./docs/source/_static/poly_vs_poly.svg
  :width: 50%
  :alt: poly_vs_poly.svg
  :align: center


**[In]**

.. code-block:: python

    _polygon = np.array([[0.0, 0.0], [0.3, 0.0], [0.4, 1.1], [0.1, 0.5]])
    poly = polygon.Polygon(_polygon)
    inpolygon = poly.inpolygon()

.. image:: ./docs/source/_static/inpolygon.svg
  :width: 50%
  :alt: inpolygon.svg
  :align: center

Projections
~~~~~~~~~~~

**[In]**

.. code-block:: python

    import numpy as np
    from pypex import projection

    point = np.array([0.3, 0.4])
    x_like_vector = np.array([1.0,  1.0])
    # vector which define `x` axis of new system
    new_x_like_vector = x_like_vector / np.linalg.norm(x_like_vector)
    # perpendicular to `new_x_like_vector` which define y axis of new system
    new_y_like_vector = [-new_x_like_vector[1], new_x_like_vector[0]]
    projected_point = projection.cartesian_to_vectors_defined(tn=new_x_like_vector, nn=new_y_like_vector, vector=point)

    print(f'Point {point} projected to new system as {projected_point}')

**[Out]**::

    Point [0.3 0.4] projected to new system as [0.49497475 0.07071068]

.. image:: ./docs/source/_static/projection_00.svg
  :width: 50%
  :alt: projection_00.svg
  :align: center

**[In]**

.. code-block:: python

    # direction vector
    to_vector = np.array([0.3, 1.2])
    # vector which will be ptojected to direction vetor
    vector = np.array([1.0, 1.0])
    # vector projected to direction vector
    projected_vector = projection.projection(vector, to_vector)
    print(f"Vector {vector} projected to vector {to_vector} as {projected_vector}")

**[Out]**::

    Vector [1. 1.] projected to vector [0.3 1.2] as [0.29411765 1.17647059]

.. image:: ./docs/source/_static/projection_01.svg
  :width: 50%
  :alt: projection_01.svg
  :align: center