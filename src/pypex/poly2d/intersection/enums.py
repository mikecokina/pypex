"""Algorithm choices for polygon intersection areas."""
from enum import StrEnum


class IntersectionAreaMethod(StrEnum):
    """Supported algorithms for :meth:`~pypex.poly2d.polygon.Polygon.intersection_area`."""

    SUTHERLAND_HODGMAN = "sutherland_hodgman"
    LEGACY = "legacy"
