from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from copy import deepcopy
from tinygeo import Point, Segment, Straight, Line, Polygon, MBR, GetMBR


class GeoViewer(object):
    def __init__(self, size=None):
        self.plt = plt
        self.figure, self.ax = self.plt.subplots()
        self._mbr = None

    def _update_mbr(self, geo):
        mbr = GetMBR(geo)
        if not self._mbr:
            self._mbr = deepcopy(mbr)
        else:
            self._mbr.expand(mbr)

    def _draw_point(self, p, color, linewidth, style):
        self.ax.scatter(p.x, p.y, c=color, linewidths=linewidth, marker=style)
        self._update_mbr(p)

    def _draw_segment(self, sg, color, linewidth, style):
        xs = [sg.p1.x, sg.p2.x]
        ys = [sg.p1.y, sg.p2.y]
        self.ax.add_line(
            Line2D(xs, ys, color=color, linewidth=linewidth, linestyle=style))
        self._update_mbr(sg)

    def _draw_straight(self, st, color, linewidth, style):
        raise NotImplementedError

    def _draw_line(self, l, color, linewidth, style):
        xs = [p.x for p in l.points]
        ys = [p.y for p in l.points]
        self.ax.add_line(
            Line2D(xs, ys, color=color, linewidth=linewidth, linestyle=style))
        self._update_mbr(l)

    def _draw_polygon(self, poly, color, linewidth, style):
        xs = [p.x for p in poly.points + [poly.points[0]]]
        ys = [p.y for p in poly.points + [poly.points[0]]]
        self.ax.add_line(
            Line2D(xs, ys, color=color, linewidth=linewidth, linestyle=style))
        self._update_mbr(poly)

    def draw(self, geo, color=None, linewidth=None, style=None):
        if isinstance(geo, Point):
            self._draw_point(geo, color, linewidth, style)
        elif isinstance(geo, Segment):
            self._draw_segment(geo, color, linewidth, style)
        elif isinstance(geo, Line):
            self._draw_line(geo, color, linewidth, style)
        elif isinstance(geo, Straight):
            self._draw_straight(geo, color, linewidth, style)
        elif isinstance(geo, Polygon):
            self._draw_polygon(geo, color, linewidth, style)
        else:
            raise TypeError

    def show(self, buffer=1):
        self.ax.set_xlim(
            left=self._mbr.left() - buffer, right=self._mbr.right() + buffer)
        self.ax.set_ylim(
            bottom=self._mbr.bottom() - buffer, top=self._mbr.top() + buffer)
        self.plt.show()
