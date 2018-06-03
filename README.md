# TinyGeo

***轻量级Python几何图形库***

该工具包目标用于快速实现平面空间下的小型建模和几何计算，封装了常用的几何算法，包括几何元素的属性计算，位置空间判断、平滑及抽吸等。

## 安装
...

## 快速开始
``` python
from tinygeo import Point, Segment, Polygon
from tinygeo.algorithm import Distance, PosRelation

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

```