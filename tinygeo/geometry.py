from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
from copy import deepcopy
from tinygeo.constant import MATH, isZero

_isNum = lambda x: isinstance(x, (int, float))


class Point(object):
    def __init__(self, x, y):
        if not (_isNum(x) and _isNum(y)):
            raise TypeError
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not _isNum(value):
            raise TypeError
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not _isNum(value):
            raise TypeError
        self._y = value

    def __repr__(self):
        return "Point(%s, %s)" % (self._x, self._y)

    def __eq__(self, other):
        return isZero(self._x - other.x) and isZero(self._y - other.y)

    def __add__(self, other):
        return Point(self._x + other.x, self._y + other.y)

    def __sub__(self, other):
        return Point(self._x - other.x, self._y - other.y)

    def __mul__(self, n):
        return Point(n * self._x, n * self._y)

    def distance(self, other):
        return math.sqrt((self._x - other.x)**2 + (self._y - other.y)**2)


class Straight(object):
    ''' form of expression: Ax + By + C = 0 '''

    def __init__(self, A, B, C):
        if not (_isNum(A) and _isNum(B) and _isNum(C)):
            raise TypeError
        if isZero(A) and isZero(B):
            raise ValueError
        self._A = A
        self._B = B
        self._C = C
        self._slope = None
        self._modify = True

    # TODO setter A, B, C
    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        if not _isNum(value):
            raise TypeError
        if isZero(self._B) and isZero(value):
            raise ValueError
        self._A = value
        self._modify = True

    @property
    def B(self):
        return self._B

    @B.setter
    def B(self, value):
        if not _isNum(value):
            raise TypeError
        if isZero(self._A) and isZero(value):
            raise ValueError
        self._B = value
        self._modify = True

    @property
    def C(self):
        return self._C

    @C.setter
    def C(self, value):
        if not _isNum(value):
            raise TypeError
        self._C = value
        self._modify = True

    @property
    def slope(self):
        if self._modify:
            if isZero(self._B):
                self._slope = MATH.NaN
            else:
                self._slope = -self._A / self._B
        return self._slope

    def toSegment(self, x1, x2):
        if isZero(self._B):
            y1, y2 = x1, x2
            _x = -(self._C / self._A)
            return Segment(Point(_x, y1), Point(_x, y2))
        else:
            p1 = Point(x1, -(self._A * x1 + self._C) / self._B)
            p2 = Point(x2, -(self._A * x2 + self._C) / self._B)
            return Segment(p1, p2)


class Segment(object):
    def __init__(self, p1, p2):
        if not (isinstance(p1, Point) and isinstance(p2, Point)):
            raise TypeError
        self._p1 = deepcopy(p1)
        self._p2 = deepcopy(p2)
        self._length = 0.
        self._slope = None
        self._modify_l = True  # modify flag for length
        self._modify_s = True  # modify flag for slope

    @property
    def length(self):
        if self._modify_l:
            self._length = self._p1.distance(self._p2)
            self._modify_l = False
        return self._length

    @property
    def p1(self):
        return self._p1

    @p1.setter
    def p1(self, p):
        if not isinstance(p, Point):
            raise TypeError
        self._p1 = p
        self._modify()

    @property
    def p2(self):
        return self._p2

    @p2.setter
    def p2(self, p):
        if not isinstance(p, Point):
            raise TypeError
        self._p2 = p
        self._modify()

    @property
    def slope(self):
        if self._modify_s:
            if isZero(self._p1.x - self._p2.x):
                self._slope = None
            else:
                self._slope = math.atan(
                    ((self._p2.y - self._p1.y) / (self._p2.x - self._p1.x)))
            self._modify_s = False
        return self._slope

    def toStraight(self):
        A = self._p2.y - self._p1.y
        B = self._p1.x - self._p2.x
        C = self._p1.y * self._p2.x - self._p1.x * self._p2.y
        return Straight(A, B, C)

    def __repr__(self):
        return "Segment[%s, %s]" % (self._p1, self._p2)

    def _modify(self):
        self._modify_l = True
        self._modify_s = True


class Line(object):
    def __init__(self, points):
        if not isinstance(points, list):
            raise TypeError
        if len(points) < 2:
            raise ValueError('Points size less than 2.')
        self._points = points[:]
        self._length = 0.
        self._modify = True

    @property
    def points(self):
        return self._points

    @property
    def length(self):
        if self._modify:
            rev = 0
            for p1, p2 in zip(self._points[:-1], self._points[1:]):
                rev += p1.distance(p2)
            self._length = rev
            self._modify = False
        return self._length

    def toSegments(self):
        return [
            Segment(*item) for item in zip(self._points[:-1], self._points[1:])
        ]

    def size(self):
        return len(self._points)

    def __repr__(self):
        if len(self._points) > 3:
            txt = "%s, %s, ..., %s" % \
            (self._points[0], self._points[1], self._points[-1])
        else:
            txt = ', '.join([str(p) for p in self._points])
        return "Line[%s; size: %d]" % (txt, len(self._points))


class Polygon(object):
    def __init__(self, points):
        if not isinstance(points, list):
            raise TypeError
        if len(points) < 2:
            raise ValueError('Points size less than 2.')
        self._points = points[:]
        self._perimeter = 0.
        self._area = 0.
        self._modify_p = True  # modify flag for perimeter
        self._modify_a = True  # modify flag for area

    def size(self):
        return len(self._points)

    @property
    def points(self):
        return self._points

    @property
    def perimeter(self):
        if self._modify_p:
            rev = 0.
            for p1, p2 in zip(self._points,
                              self._points[1:] + [self._points[0]]):
                rev += p1.distance(p2)
            self._perimeter = rev
            self._modify_p = False
        return self._perimeter

    def length(self):
        return self.perimeter

    @property
    def area(self):
        if self._modify_a:
            rev = 0.
            for p1, p2 in zip(self._points,
                              self._points[1:] + [self._points[0]]):
                rev += (p1.x * p2.y - p1.y * p2.x)
            self._area = abs(rev) * 0.5
            self._modify_a = False
        return self._area

    def toSegments(self):
        # TODO
        raise NotImplementedError

    def __repr__(self):
        if len(self._points) > 3:
            txt = "%s, %s, ..., %s" % \
            (self._points[0], self._points[1], self._points[-1])
        else:
            txt = ', '.join([str(p) for p in self._points])
        return "Polygon[%s; size: %d]" % (txt, len(self._points))


if __name__ == "__main__":
    import math

    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(5, 6)
    p4 = Point(7, 8)
    p5 = Point(0, 0)
    p6 = Point(1, 0)
    p7 = Point(1, 1)
    p8 = Point(0, 1)
    s1 = Segment(p1, p2)
    s2 = Segment(p2, p3)
    l1 = Line([p1, p2, p3])
    l2 = Line([p1, p2, p3, p4])
    poly1 = Polygon([p5, p6, p7, p8])
    poly2 = Polygon([p5, p6, p7, p8, p5])
    assert (str(p1) == 'Point(1, 2)')
    assert (str(p1 + p2) == 'Point(4, 6)')
    assert (str(p1 - p2) == 'Point(-2, -2)')
    assert (str(p1 * 2) == 'Point(2, 4)')
    assert (isZero(s1.length - math.sqrt(8)))
    assert (isZero(l1.length - math.sqrt(8) * 2))
    assert (l1.size() == 3)
    assert (l2.toSegments()[0].length == s1.length)
    assert (poly1.perimeter == 4)
    assert (poly2.length() == 4)
    assert (poly1.area == 1)
    assert (poly2.area == 1)
    print(l1)
    print(l2)
    print(poly1)
    print(poly2)