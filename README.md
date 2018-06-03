# TinyGeo

*快速、便捷的轻量级Python几何图形库*

## 特性
- 可快速实现平面空间下的小型几何建模
- 快速调用调用常用的几何属性计算，位置空间判断、平滑以及抽吸等算法
- 方便的可视化操作（需matplotlib支持）
- 支持数据持久化(todo)

## 安装
(todo)

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