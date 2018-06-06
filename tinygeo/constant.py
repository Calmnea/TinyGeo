##
# define a const class which contain some constant objects.

import math

class _const:
    class ConstError(TypeError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        self.__dict__[name] = value

MATH = _const()
MATH.NaN = 'NaN'
MATH.PRECISION = 1.0e-9
MATH.PI = math.pi

POSITION_TYPE = _const()
POSITION_TYPE.INTERSECT = 'intersect'
POSITION_TYPE.CONTAIN = 'contain'
POSITION_TYPE.DEPACH = 'depach'
POSITION_TYPE.PARALLEL = 'parallel'
POSITION_TYPE.OVERLAP = 'overlap'
POSITION_TYPE.BE_CONTAINED = 'be-contained'

isZero = lambda x: abs(x) < MATH.PRECISION