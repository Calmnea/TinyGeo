from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from utils import _isZero, _distance

_isNum = lambda x: isinstance(x, (int, float))
_isList = lambda l: isinstance(l, list)

class Point(object):
    def __init__(self, x, y):
        if not (_isNum(x) and _isNum(y)):
            raise TypeError
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __eq__(self, other):
        return _isZero(self.x - other.x) and _isZero(self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Point(n * self.x, n * self.y)
    
    def distance(self, other):
        return _distance(self.x, self.y, other.x, other.y)

class Segment(object):
    def __init__(self, p1, p2):
        if not (isinstance(p1, Point) and isinstance(p2, Point)):
            raise TypeError
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return p1.distance(p2)

    def __repr__(self):
        return "Segment[%s, %s]" % (self.p1, self.p2)

class Line(object):
    def __init__(self, points):
        if not _isList(points):
            raise TypeError
        self.points = points[:]

    def length(self):
        rev = 0
        for i in range(len(self.points) - 1):
            rev += self.points[i].distance(self.points[i+1])
        return rev

    def __repr__(self):
        if len(self.points) > 3:
            txt = "%s, %s, ..., %s" % \
            (self.points[0], self.points[1], self.points[-1])
        else:
            txt = ', '.join([str(p) for p in self.points])
        return "Line[%s; size: %d]" % (txt, len(self.points))


if __name__ == "__main__":
    import math

    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(5, 6)
    p4 = Point(7, 8)
    s1 = Segment(p1, p2)
    s2 = Segment(p2, p3)
    l1 = Line([p1, p2, p3])
    l2 = Line([p1, p2, p3, p4])
    assert(str(p1) == 'Point(1, 2)')
    assert(str(p1 + p2) == 'Point(4, 6)')
    assert(str(p1 - p2) == 'Point(-2, -2)')
    assert(str(p1 * 2) == 'Point(2, 4)')
    assert(_isZero(s1.length() - math.sqrt(8)))
    assert(_isZero(l1.length() - math.sqrt(8) * 2))
    print(l1)
    print(l2)