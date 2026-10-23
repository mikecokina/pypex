# Intersection area benchmark and numerical behavior

Run separately from unit tests, from the repository root:

```sh
PYTHONPATH=src python benchmarks/intersection_area.py --number 2000 --repeat 5
```

The script preconstructs polygons, warms up each method and reports the median
per-call time over five repeats. The ratio is legacy time divided by clipping
time. These measurements include the full public area method, including polygon
construction inside the legacy intersection implementation. They exclude input
polygon construction. Results depend on hardware, vertex count and geometry;
Python clipping loops need not remain faster for very large hulls.

Example measured in this workspace on x86_64, Python 3.13.14, NumPy 2.5.4:

| Case                            | Sutherland-Hodgman (µs) | Legacy (µs) | Legacy / SH |
|---------------------------------|------------------------:|------------:|------------:|
| Triangle / triangle             |                    9.27 |      130.81 |      14.11x |
| Triangle / convex (16 vertices) |                   17.22 |      121.45 |       7.05x |
| Convex (16) / convex (24)       |                   45.75 |      160.46 |       3.51x |
| Disjoint (16 / 24)              |                    6.42 |      103.46 |      16.12x |
| Nearly coincident (16 / 16)     |                   32.55 |      165.44 |       5.08x |

## Investigated numerical differences

Let `S = [[0, 0], [2, 0], [2, 2], [0, 2]]`. The following areas are
analytically known from rectangular intersections; legacy is not used as the
reference answer.

| Input hulls                        | Analytic area |       Sutherland-Hodgman |        Legacy |
|------------------------------------|--------------:|-------------------------:|--------------:|
| `S`, `S + [2 - 2**-40, 0]`         |      `2**-39` | `1.8189894035458565e-12` |         `0.0` |
| `S * 1e-8`, `S * 1e-8 + [1e-8, 0]` |       `2e-16` | `2.0000000000000002e-16` |         `0.0` |
| `S + 1e12`, `S + [1, 0.5] + 1e12`  |         `1.5` |                    `1.5` | `134217728.0` |

The first case collapses when legacy rounds candidate intersection vertices to
ten decimal places. In the second, edge determinants fall below the existing
absolute `1e-10` parallel threshold, so needed crossing points are omitted.
The third loses area precision when legacy `surface_area()` subtracts products
of large absolute coordinates. These existing behaviors are preserved.

For the unit square clipped by `[[0, 0], [1, delta], [1, 2], [0, 2]]`,
the exact area is `1 - delta/2`. At `delta=1e-12`, clipping returns
`0.9999999999995` while legacy returns `1.0`: rounding removes the slope.

The new method uses signed cross products for half-plane classification and
interpolates only when the classifications differ. A parallel or collinear
segment cannot require division in exact arithmetic; boundary endpoints are
emitted directly. Shoelace evaluation uses a local origin to reduce cancellation.
No epsilon, vertex rounding, or upper-bound clamping is applied.

Both methods assume convex polygons. Binary64 predicates can still misclassify
nearly collinear geometry due to cancellation, and the two argument orders can
differ by floating-point roundoff. Input precision already lost under translation
cannot be recovered. Extreme magnitudes can overflow products or underflow tiny
areas. This implementation does not provide exact predicates or arbitrary precision.

The unit tests cover analytic areas, both argument orders, cyclic winding and
constructor orderings, coincident/collinear edges, tiny overlaps, near-parallel
edges, transformations, nonmutation and deterministic regular-polygon comparisons.
Legacy agreement is checked on ordinary configurations; the explicit small-scale
regressions record deviations rather than adopting legacy results as truth.
