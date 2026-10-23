Pypex documentation
===================

Pypex provides operations on convex 2D polygons, line segments and points.

Installation
------------

Install the latest published version::

    python -m pip install pypex

To install the development version, run this from the repository root::

    python -m pip install .

Intersection areas
------------------

Choose the area algorithm with the public enum::

    from pypex import IntersectionAreaMethod, Polygon

    a = Polygon([[0, 0], [2, 0], [2, 2], [0, 2]])
    b = Polygon([[1, 0.5], [3, 0.5], [3, 2.5], [1, 2.5]])

    a.intersection_area(b)  # 1.5; defaults to SUTHERLAND_HODGMAN
    a.intersection_area(b, method=IntersectionAreaMethod.LEGACY)  # 1.5

See :meth:`pypex.poly2d.polygon.Polygon.intersection_area` for the method
contract and :class:`pypex.poly2d.intersection.enums.IntersectionAreaMethod`
for the supported choices.

API reference
-------------

.. toctree::
   :maxdepth: 4

   api_docs/modules

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
