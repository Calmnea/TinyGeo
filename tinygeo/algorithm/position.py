##
# this module implement some algorithms of positional relation with two geometry.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tinygeo import Point, Segment, Straight, Line, Polygon
from tinygeo import MBR, GetMBR
from tinygeo.constant import POSITION_TYPE, MATH, isZero
from .distance import Distance


# the cross of two 2D vector not real exist
# this is just to compute the topology of the vector
def _cross_vec(vec1, vec2):
    return vec1.x * vec2.y - vec2.x * vec1.y


def _position_mbr_to_mbr(m1, m2):
    if (m1.top() < m2.bottom() or m1.bottom() > m2.top()
            or m1.left() > m2.right() or m1.right() < m2.left()):
        return POSITION_TYPE.DEPACH
    if m1.contain(m2):
        return POSITION_TYPE.CONTAIN
    if m1.contain(m2):
        return POSITION_TYPE.BE_CONTAINED
    return POSITION_TYPE.INTERSECT


def _position_point_to_point(p1, p2):
    if p1 == p2:
        return POSITION_TYPE.OVERLAP
    else:
        return POSITION_TYPE.DEPACH


def _position_point_to_straight(p, st):
    raise NotImplementedError


def _position_point_to_segment(p, sg):
    raise NotImplementedError


def _position_point_to_polygon(p, poly):
    raise NotImplementedError


def _position_segment_to_polygon(sg, poly):
    raise NotImplementedError


def _position_segment_to_segment(sg1, sg2):
    raise NotImplementedError


def _position_segment_to_straight(sg, st):
    raise NotImplementedError


def _position_straight_to_straight(st1, st2):
    if st1.B == 0 and st2.B == 0:
        if st1.A * st2.C == st1.C * st2.A:
            return POSITION_TYPE.OVERLAP
        else:
            return POSITION_TYPE.DEPACH
    elif st1.B != 0 and st2.B != 0:
        if st1.A * st2.B == st1.B * st2.A:
            if st1.C * st2.B == st1.B * st2.C:
                return POSITION_TYPE.OVERLAP
            else:
                return POSITION_TYPE.DEPACH
        else:
            return POSITION_TYPE.INTERSECT
    else:
        return POSITION_TYPE.INTERSECT


def _position_straight_to_polygon(st, poly):
    raise NotImplementedError


def _position_polygon_to_polygon(poly1, poly2):
    raise NotImplementedError


# API
def PosRelation(geo1, geo2):
    if isinstance(geo1, Point) and isinstance(geo2, Point):
        return _position_point_to_point(geo1, geo2)
    elif isinstance(geo1, Point) and isinstance(geo2, Segment):
        return _position_point_to_segment(geo1, geo2)
    elif isinstance(geo1, Segment) and isinstance(geo2, Point):
        return _position_point_to_segment(geo2, geo1)
    elif isinstance(geo1, Point) and isinstance(geo2, Polygon):
        return _position_point_to_polygon(geo1, geo2)
    elif isinstance(geo1, Polygon) and isinstance(geo2, Point):
        return _position_point_to_polygon(geo2, geo1)
    elif isinstance(geo1, Segment) and isinstance(geo2, Segment):
        return _position_segment_to_segment(geo1, geo2)
    elif isinstance(geo1, Segment) and isinstance(geo2, Polygon):
        return _position_segment_to_polygon(geo1, geo2)
    elif isinstance(geo1, Polygon) and isinstance(geo2, Segment):
        return _position_segment_to_polygon(geo2, geo1)
    elif isinstance(geo1, Segment) and isinstance(geo2, Straight):
        return _position_segment_to_straight(geo1, geo2)
    elif isinstance(geo1, Straight) and isinstance(geo2, Segment):
        return _position_segment_to_straight(geo2, geo1)
    elif isinstance(geo1, Straight) and isinstance(geo2, Straight):
        return _position_straight_to_straight(geo1, geo2)
    elif isinstance(geo1, Straight) and isinstance(geo2, Polygon):
        return _position_straight_to_polygon(geo1, geo2)
    elif isinstance(geo1, Polygon) and isinstance(geo2, Straight):
        return _position_straight_to_polygon(geo2, geo1)
    elif isinstance(geo1, Polygon) and isinstance(geo2, Polygon):
        return _position_polygon_to_polygon(geo1, geo2)
    else:
        raise TypeError
