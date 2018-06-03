##
# this module implement MBR(Minimum Bounding Rectangle) of geometry.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from copy import deepcopy
from tinygeo.geometry import Point, Segment, Line, Polygon


# MBR only save two Point Object: LeftLower(LL), RightUpper(RU)
class MBR(object):
    def __init__(self, ll, ru):
        if not (isinstance(ll, Point) and isinstance(ru, Point)):
            raise TypeError
        if ll.x <= ru.x and ll.y <= ru.y:
            self._ll = deepcopy(ll)
            self._ru = deepcopy(ru)
        else:
            raise ValueError

    @property
    def ll(self):
        return self._ll

    @ll.setter
    def ll(self, p):
        if not isinstance(p, Point):
            raise TypeError
        if p.x > self._ru.x or p.y > self._ru.y:
            raise ValueError
        self._ll = p

    @property
    def ru(self):
        return self._ru

    @ru.setter
    def ru(self, p):
        if not isinstance(p, Point):
            raise TypeError
        if p.x < self._ll.x or p.y < self._ll.y:
            raise ValueError
        self._ru = p

    def top(self):
        return self._ru.y

    def bottom(self):
        return self._ll.y

    def left(self):
        return self._ll.x

    def right(self):
        return self._ru.x

    def toPolygon(self):
        lu = Point(self._ll.x, self._ru.y)  # LeftUpper Point
        rl = Point(self._ru.x, self._ll.y)  # RightLower Point
        return Polygon([self._ll, lu, self._ru, rl])

    # expend MBR with a Point
    def add_point(self, p):
        if not isinstance(p, Point):
            raise TypeError
        if p.x < self._ll.x:
            self._ll.x = p.x
        if p.x > self._ru.x:
            self._ru.x = p.x
        if p.y < self._ll.y:
            self._ll.y = p.y
        if p.y > self._ru.y:
            self._ru.y = p.y

    def __repr__(self):
        return "MBR(%s, %s, %s, %s)" % (self._ll.x, self._ll.y, self._ru.x,
                                        self._ru.y)


def _get_mbr_point(p):
    return MBR(p, p)


def _get_mbr_segment(sg):
    mbr = MBR(sg.p1, sg.p1)
    mbr.add_point(sg.p2)
    return mbr


def _get_mbr_points(geo):
    mbr = MBR(geo.points[0], geo.points[0])
    for p in geo.points[1:]:
        mbr.add_point(p)
    return mbr


# API: Get MBR by Point/Segment/Line/Polygon
def GetMBR(geo):
    if isinstance(geo, Point):
        return _get_mbr_point(geo)
    elif isinstance(geo, Segment):
        return _get_mbr_segment(geo)
    elif isinstance(geo, (Line, Polygon)):
        return _get_mbr_points(geo)
    else:
        raise TypeError
