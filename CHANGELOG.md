# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## 0.3.0

### Added

- Added type annotations and docstrings across the package.
- Added `pypex.base.types` with shared type aliases.
- Added `Shape2D.__hash__`.
- Added `sat` unit tests and regression tests for parallel and collinear segments.
- Added support for Python 3.13 and 3.14.

### Changed

- Renamed the `in_touch` parameter to `touch_is_separated` with the opposite meaning: `True` now treats touching as separated. `Line.intersects()` and `Line.intersection()` default to `touch_is_separated=True`, matching the previous `in_touch=False`; the other functions default to `False`.
- Made optional parameters keyword-only, including `touch_is_separated`, `tol`, `round_tol`, `inplace`, `_full` and `_validity`.
- Renamed the collinear segment description from `OVERLAP` to `COLINEAR`.
- Dropped support for Python 3.10 and older; supported versions are 3.11 to 3.14.
- Raised the minimum NumPy to 1.23.2 (2.3.2 on Python 3.14) and matplotlib to 3.6.0 (3.10.6 on Python 3.14).

### Fixed

- Corrected vectorized parallel-segment distance in `intersections()`: the denominator was `sqrt(a1^2 + sqrt(b1^2))` instead of `sqrt(a1^2 + b1^2)`; it now uses `np.hypot(a1, b1)`.
- Corrected collinear segment overlap detection in `separating_axis_theorem_line_adapt()`: projected intervals are now ordered, so segments with opposite directions are detected as overlapping.
- Replaced 2D `np.cross`, which is unsupported in NumPy 2.5, in `point._line_side()`.

## 0.2.2 - 2025-02-12

### Changed

- Updated Python compatibility through Python 3.12.

## 0.2.1 - 2021-10-27

### Changed

- Updated the NumPy version.

## 0.2.0 - 2020-11-01

### Added

- Added `inerpolygon` to find polygons whose points are the centers of the original polygon's edges.
- Added a line parametrization method.

### Changed

- Added support for transposing `Shape2D` (`.T`) to simplify interaction with raw points.

## 0.1.0

### Added

- Added 2D `Polygon`, `Line`, and `Point` implementations.
- Added the 2D separating axis theorem (SAT) algorithm.
- Added line and polygon intersection implementations.
