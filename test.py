from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from tinygeo import Point, Segment
from tinygeo.algorithm import Distance, PosRelation

p1 = Point(1, 1)
p2 = Point(2, 1)
p3 = Point(3, 4)
s1 = Segment(p1, p2)

print(s1.length)
# output: 1.0

print(PosRelation(p1, p2))
# output: depach

print(Distance(p3, s1.toStraight()))
# output: 5.0