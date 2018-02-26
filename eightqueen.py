# coding=utf8
"""
八皇后问题是一个古老的问题，于1848年由一位国际象棋棋手提出：
在8×8格的国际象棋上摆放八个皇后，使其不能互相攻击，即任意两个皇后都不能处于同一行、同一列或同一斜线上，如何求解？
---
ideas:
1. 尝试所有的, 直到找到满足条件的
2. 只尝试可能的
3. 排除不可能的, 剩下的就是可能的
"""
from time import sleep
import copy


class Point:
    """
    point on panel
    ---
    x: x-axis
    y: y-axis
    v: value of the point; 0_not used, 1_used, -1_not usable
    """

    def __init__(self, x=None, y=None, v=0):
        self.x = x
        self.y = y
        self.v = v

    def __repr__(self):
        # return f"({self.x},{self.y})"
        return f"({self.x},{self.y},{self.v})"

    def __str__(self):
        # return f"({self.x},{self.y},{self.v})"
        return f"({self.x},{self.y})"


class Panel:
    """
    panel represents chessboard
    """

    def __init__(self, x_range, y_range):
        self.x_range = x_range
        self.y_range = y_range
        self.points = init_panel(x_range, y_range)

    def __repr__(self):
        res = "["
        for p in self.points:
            if p.x == 0:
                res += '\n'
            res += str(p)
        res += ']'
        return res


def in_col(p1, p2):
    """
    n1和n2是否垂直共线
    """
    return p1.x == p2.x


def in_row(p1, p2):
    """
    n1,n2是否水平共线
    """
    return p1.y == p2.y


def in_diagonal(p1, p2):
    """
    n1,n2是否对角共线
    """
    return abs(p2.y - p1.y) == abs(p2.x - p1.x)


def init_panel(x_range, y_range):
    panel = []
    for y in range(y_range):
        for x in range(x_range):
            panel.append(Point(x, y, 0))
    return panel


def label_impossible(p, panel):
    """
    给定一点n(x,y), 标出棋盘panel上不可能的坐标
    """
    for pp in filter(lambda pp: pp.v == 0, panel.points):
        if in_row(p, pp) or in_col(p, pp) or in_diagonal(p, pp):
            pp.v = -1


def later_terminate(row):
    res = True
    for pprev in rt_next[row + 1:]:
        if pprev.x < (x_range - 1):
            res = False
            break
    return res


def select_point_in_row(panel, row):
    """
    select a point in a row, range:(start,end) 
    """
    # get start
    start = row * x_range
    if row == (y_range - 1):
        start += rt_next[row].x + 1
    elif later_terminate(row):
        start += rt_next[row].x + 1
        for r in range(row + 1, y_range):
            if row == (panel.x_range - 1):
                rt_next[row + 1] = Point(-1, row + 1)
            else:
                rt_next[row + 1] = Point(0, row + 1)
    else:
        start += rt_next[row].x
    # get end
    end = (row + 1) * panel.x_range
    # select
    # print("select from", panel.points[start:end])
    for p in panel.points[start:end]:
        if p.v == 0:
            p.v = 1
            label_impossible(p, panel)
            return p


def select_2nd_point_in_row(panel, row):
    """
    select a point in a row, range:(start,end)
    """
    # get start
    start = row * x_range
    if row == (y_range - 1):
        start += rt_next[row].x + 1
    elif later_terminate(row):
        start += rt_next[row].x + 1
        for r in range(row + 1, y_range):
            if row == (panel.x_range - 1):
                rt_next[row + 1] = Point(-1, row + 1)
            else:
                rt_next[row + 1] = Point(0, row + 1)
    else:
        start += rt_next[row].x
    # get end
    end = (row + 1) * panel.x_range
    # select
    # print("*select from", panel.points[start:end])
    first = True
    for p in panel.points[start:end]:
        if p.v == 0:
            if first:
                first = False
                continue
            p.v = 1
            return p


def give_rt_next(row_end):
    for r in range(row_end, 0, -1):
        # panel_tmp = copy.deepcopy(panel)
        clear_label(rt_next[r], panel)
        p = select_2nd_point_in_row(panel, r)
        # print("*return", str(p))
        if p is None:
            rt_next[r] = Point(0, r)
            continue
        rt_next[r] = p
        return
    # print("not find other route")


def clear_label(p, panel):
    # print("*clear %s in %s" % (p, panel))
    for pp in panel.points:
        if in_row(p, pp) or in_col(p, pp) or in_diagonal(p, pp):
            pp.v = 0
    for pp in filter(lambda pp: pp.v == 1, panel.points):
        for ppp in panel.points:
            if (ppp.x == pp.x) and (ppp.y == pp.y):
                continue
            if in_row(pp, ppp) or in_col(pp, ppp) or in_diagonal(pp, ppp):
                ppp.v = -1
    # print("*clear get", panel)


if __name__ == "__main__":
    # route
    rt = []
    x_range = 8
    y_range = 8
    # previous rt
    rt_next = [Point(0, i) for i in range(8)]
    while len(rt) < 8:
        rt = []
        panel = Panel(x_range, y_range)
        print("-route tip:", rt_next)
        for r in range(8):
            p = select_point_in_row(panel, r)
            # print("return", str(p))
            if p is None:
                print("not complete:", rt)
                give_rt_next(r - 1)
                # sleep(1)
                break
            else:
                rt.append(p)
                rt_next[r] = p
    print("***result", rt)
