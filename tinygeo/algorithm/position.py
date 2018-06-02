##
# this module implement some algorithms of positional relation with two geometry.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tinygeo import Point, Segment, Straight, Line, Polygon
from tinygeo.constant import POSITION_TYPE, MATH

def _position_point_to_point(p1, p2):
    if p1 == p2:
        return POSITION_TYPE.INTERSECT
    else:
        return POSITION_TYPE.DEPACH

def _position_point_to_segment(p, sg):
    raise NotImplementedError

def _position_point_to_straight(p, st):
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
    raise NotImplementedError

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
    # TODO elsif
    else:
        raise TypeError
