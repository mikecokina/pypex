"""Standalone benchmark: PYTHONPATH=src python benchmarks/intersection_area.py."""
import argparse
import platform
import statistics
import timeit

import numpy as np

from pypex import IntersectionAreaMethod, Polygon


def regular(count: int) -> np.ndarray:
    angles = np.linspace(0., 2 * np.pi, count, endpoint=False)
    return np.column_stack((np.cos(angles), np.sin(angles)))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--number', type=int, default=2000, help='calls per timing repeat')
    parser.add_argument('--repeat', type=int, default=5)
    args = parser.parse_args()
    if args.number < 1 or args.repeat < 1:
        parser.error('--number and --repeat must be positive')
    cases = [
        ('triangle / triangle', regular(3), regular(3) + [.3, .2]),
        ('triangle / convex (16)', regular(3), regular(16) + [.3, .2]),
        ('convex (16) / convex (24)', regular(16), regular(24) + [.3, .2]),
        ('disjoint (16 / 24)', regular(16), regular(24) + [3., 0.]),
        ('nearly coincident (16 / 16)', regular(16), regular(16) + [1e-8, -1e-8]),
    ]
    print(f'Python {platform.python_version()}, NumPy {np.__version__}, {platform.machine()}')
    print(f'Median of {args.repeat} repeats of {args.number} calls; construction excluded.')
    print('| Case | Sutherland-Hodgman (µs) | Legacy (µs) | Legacy / SH |')
    print('| --- | ---: | ---: | ---: |')
    for name, vertices_a, vertices_b in cases:
        a, b = Polygon(vertices_a), Polygon(vertices_b)
        times = []
        for method in IntersectionAreaMethod:
            call = lambda: a.intersection_area(b, method=method)
            call()  # warm up
            samples = timeit.repeat(call, number=args.number, repeat=args.repeat)
            times.append(statistics.median(samples) / args.number * 1e6)
        print(f'| {name} | {times[0]:.2f} | {times[1]:.2f} | {times[1] / times[0]:.2f}x |')


if __name__ == '__main__':
    main()
