from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from tinygeo import Point, Segment, Polygon
from tinygeo import MBR, GetMBR
from tinygeo.algorithm import Distance, PosRelation
from tinygeo.display import GeoViewer

p1 = Point(1, 1)
p2 = Point(2, 1)
p3 = Point(2, 2)
p4 = Point(1, 2)
s1 = Segment(p1, p2)
poly1 = Polygon([p1, p2, p3, p4])

print(s1.length, s1.slope)
# output: 1.0 0.0

print(poly1.perimeter, poly1.area)
# output: 4.0 1.0

print(Distance(p3, s1.toStraight()))
# output: 1.0

print(PosRelation(p1, p2))
# output: depach

mbr = GetMBR(s1)
print(mbr)

viewer = GeoViewer()
viewer.draw(p1)
viewer.draw(p2)
viewer.draw(s1, color='red')
viewer.draw(poly1)
viewer.show()