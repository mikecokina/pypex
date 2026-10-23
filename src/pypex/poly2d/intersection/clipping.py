"""Convex polygon clipping using unrounded binary64 coordinates."""
from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def _signed_double_area(vertices: NDArray[np.float64]) -> float:
    """Signed shoelace sum, translated to reduce cancellation."""
    if len(vertices) < 3:
        return 0.0
    local = vertices - vertices[0]
    return float(np.sum(local[:-1, 0] * local[1:, 1] - local[1:, 0] * local[:-1, 1]))


def intersection_area(subject: NDArray, clip: NDArray) -> float:
    """Return convex intersection area by Sutherland-Hodgman clipping.

    Both hulls must contain cyclically ordered convex vertices. Either winding
    is accepted. Boundary points are inside; no rounding or tolerance is used.
    Inputs are never modified. Arithmetic is float64 (Python floats in the
    clipping loop). This is not an exact geometric predicate implementation.
    """
    subject = np.asarray(subject, dtype=np.float64)
    clip = np.asarray(clip, dtype=np.float64)
    if len(subject) < 3 or len(clip) < 3:
        return 0.0

    # Use a common local origin for clipping and area calculation.
    origin = subject[0]
    subject = subject - origin
    clip = clip - origin
    winding = _signed_double_area(clip)
    if winding == 0.0:
        return 0.0
    orientation = 1.0 if winding > 0.0 else -1.0
    vertices = subject.tolist()
    ax, ay = clip[-1].tolist()
    for bx, by in clip.tolist():
        if len(vertices) < 3:
            return 0.0
        dx, dy = bx - ax, by - ay
        output = []
        sx, sy = vertices[-1]
        start_side = orientation * (dx * (sy - ay) - dy * (sx - ax))
        for ex, ey in vertices:
            end_side = orientation * (dx * (ey - ay) - dy * (ex - ax))
            if (start_side < 0.0 < end_side) or (end_side < 0.0 < start_side):
                # Strictly opposite signs guarantee a nonzero denominator.
                # Boundary endpoints are emitted once by the inside rule below
                # (the start endpoint belongs to the previous cyclic edge).
                # Parallel/collinear segments never enter this branch.
                t = start_side / (start_side - end_side)
                output.append([sx + t * (ex - sx), sy + t * (ey - sy)])
            if end_side >= 0.0:
                output.append([ex, ey])
            sx, sy, start_side = ex, ey, end_side
        vertices = output
        ax, ay = bx, by

    return abs(_signed_double_area(np.asarray(vertices, dtype=np.float64))) * 0.5
