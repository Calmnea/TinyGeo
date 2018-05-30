from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math

_PRECISION = 1.0e-9
_isZero = lambda x: abs(x) < _PRECISION

def _distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)



if __name__ == '__main__':
    assert(_isZero(1.1 - 1.1)) 
    assert(_distance(1, 2, 2, 2) == 1)