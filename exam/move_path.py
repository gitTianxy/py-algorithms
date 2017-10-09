# encoding=utf-8
"""
LEVEL:
    primary
PROBLEM:
    假设有一款不会反复清扫同一个地方的机器人，它只能前后左右移动。最初的位置用0 表示，其后的移动位置用数字表示。
求这个机器人移动12 次时，有多少种移动路径？
"""


def exists(rt, dot_x, dot_y):
    for dot in rt:
        if dot[0] == dot_x and dot[1] == dot_y:
            return True
    return False


if __name__ == '__main__':
    # w, h = 25, 25
    # dots = [[0 for x in range(w)] for y in range(h)]
    # dots[0][0] = 1
    routes = []
    rt = []
    rt.append((0, 0))
    routes.append(rt)
    step = 0
    while step < 12:
        print '--- current step: %s, routes size: %s' % (step, len(routes))
        new_routes = []
        for rt in routes:
            rt_end = rt[len(rt) - 1]
            # print 'current route: %s, route end: %s' % (rt, rt_end)
            # up
            up_x = rt_end[0]
            up_y = rt_end[1] + 1
            if not exists(rt, up_x, up_y):
                rt_up = list(rt)
                rt_up.append((up_x, up_y))
                new_routes.append(rt_up)
            # down
            down_x = rt_end[0]
            down_y = rt_end[1] - 1
            if not exists(rt, down_x, down_y):
                rt_down = list(rt)
                rt_down.append((down_x, down_y))
                new_routes.append(rt_down)
            # left
            left_x = rt_end[0] - 1
            left_y = rt_end[1]
            if not exists(rt, left_x, left_y):
                rt_left = list(rt)
                rt_left.append((left_x, left_y))
                new_routes.append(rt_left)
            # right
            right_x = rt_end[0] + 1
            right_y = rt_end[1]
            if not exists(rt, right_x, right_y):
                rt_right = list(rt)
                rt_right.append((right_x, right_y))
                new_routes.append(rt_right)
        routes = new_routes
        step += 1
    print '--- current step: %s, routes size: %s' % (step, len(routes))
    print 'possible route number:', len(routes)
