from __future__ import annotations

from typing import TypeAlias

import numpy as np
from numpy.typing import NDArray

INT = int
FLOAT = float

Float: TypeAlias = float | np.float32 | np.float64 | np.floating
NP_BOOL_: TypeAlias = np.bool_
Shape2DType: TypeAlias = list | NDArray
