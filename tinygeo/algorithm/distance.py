##
# this module implement some algorithms of distance with two geometry.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
from tinygeo import Point, Segment, Straight, Line, Polygon


# Distance of Point and Point
def _distance_point_to_point(p1, p2):
    return p1.distance(p2)


# Distance of Point and Straight
def _distance_point_to_straight(p, st):
    numerator = st.A * p.x + st.B * p.y + st.C
    denominator = math.sqrt(st.A**2 + st.B**2)
    return abs(numerator / denominator)


# TODO more geometry


# API: Distance of two geometry
def Distance(g1, g2):
    if isinstance(g1, Point) and isinstance(g2, Point):
        return _distance_point_to_point(g1, g2)
    elif isinstance(g1, Point) and isinstance(g2, Straight):
        return _distance_point_to_straight(g1, g2)
    elif isinstance(g1, Straight) and isinstance(g2, Point):
        return _distance_point_to_straight(g2, g1)
    # TODO elif
    else:
        raise TypeError
