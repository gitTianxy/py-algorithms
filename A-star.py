# encoding=utf-8
"""
A* algorithm demo
----------------------------
I. A*算法最为核心的部分，就在于它的一个估值函数的设计上：
    f(n)=g(n)+h(n)
其中:
    g(n): 表示从起始搜索点到当前点的代价
    h(n): 表示当前结点到目标结点的估值<难点和核心>
II. 数据结构
    1. OPEN(list): 放置当前节点的所有后继节点
    2. CLOSE(list): 放置已选取的node
III. A*算法流程
    0. 把起始点放入open表
    1. 如果OPEN表不为空，从表头取一个结点n，如果为空算法结束或失败
    2. n是目标解吗？是，找到一个解(继续寻找，或终止算法)
    3. 否, 将n的所有后继结点展开，如果不在CLOSE表中，就将它们放入OPEN表, 并把n放入CLOSE表
    4. 计算每一个后继结点的估价值f(n)，将OPEN表按f(x)升序排序
    5. 重复算法，回到1
"""
from enum import Enum


class AStarDemo:
    """
    爬棋盘: 求从起点到终点的最短路径
    """
    # 三种启发式估算h的方法
    heuristic_type = Enum('HeuristicType', ('Manhantan', 'Euclidean', 'Diagonal'))

    def __init__(self):
        print 'a star demo---------------------------'
        self.open_list = []
        self.close_list = []
        self.grids = []
        self.init_grids()
        self.get_path(start_x=1, start_y=2, dest_x=5, dest_y=1)
        for g in self.close_list:
            print g

    def init_grids(self):
        for h in range(0, 6):
            self.grids.append([0 for i in range(0, 7)])
        self.grids[1][1] = 1
        self.grids[1][3] = 1
        self.grids[2][3] = 1
        self.grids[3][3] = 1
        self.grids[4][3] = 1

    def get_path(self, start_x, start_y, dest_x, dest_y):
        self.start = AStarDemo.Grid(x=start_x, y=start_y)
        self.dest = AStarDemo.Grid(x=dest_x, y=dest_y)
        # 0. init open-list
        self.open_list.append(AStarDemo.Grid(x=start_x, y=start_y))
        # do algorithm
        while True:
            # 1. is exhausted
            if len(self.open_list) == 0:
                break
            curr = self.open_list[0]
            self.close_list.append(curr)
            self.open_list = []
            # 2. is dest grid
            if curr.x == dest_x and curr.y == dest_y:
                break
            # 3. get neighbors of current grid
            if curr.x - 1 > -1:
                left = AStarDemo.Grid(x=curr.x - 1, y=curr.y)
                if not self.close_list.__contains__(left) and self.grids[left.y][left.x] == 0:
                    self.open_list.append(left)
            if curr.x + 1 < len(self.grids[0]):
                right = AStarDemo.Grid(x=curr.x + 1, y=curr.y)
                if not self.close_list.__contains__(right) and self.grids[right.y][right.x] == 0:
                    self.open_list.append(right)
            if curr.y - 1 > -1:
                lower = AStarDemo.Grid(x=curr.x, y=curr.y - 1)
                if not self.close_list.__contains__(lower) and self.grids[lower.y][lower.x] == 0:
                    self.open_list.append(lower)
            if curr.y + 1 < len(self.grids):
                upper = AStarDemo.Grid(x=curr.x, y=curr.y + 1)
                if not self.close_list.__contains__(upper) and self.grids[upper.y][upper.x] == 0:
                    self.open_list.append(upper)
            # 4. calculate 'h' and do sort
            self.open_list.sort(key=self.h)

    def h(self, curr):
        return abs(curr.x - self.dest.x) + abs(curr.y - self.dest.y)

    class Grid:
        """
        网格点
        """

        def __init__(self, x=None, y=None):
            self.x = x
            self.y = y

        def __eq__(self, o):
            return self.x == o.x and self.y == o.y

        def __str__(self):
            return "x=%s, y=%s" % (self.x, self.y)


class AllPathDemo:
    """
    有向图中两个节点间的最小距离
    """
    links = [
        dict(start=0, to=2, w=10),
        dict(start=0, to=4, w=30),
        dict(start=0, to=5, w=100),

        dict(start=1, to=2, w=5),

        dict(start=2, to=3, w=50),

        dict(start=3, to=5, w=10),

        dict(start=4, to=3, w=20),
        dict(start=4, to=5, w=60),
    ]

    def __init__(self):
        print 'all path demo ---------------------------'
        self.all_path_strategy(start_n=0, dest_n=5)

    @staticmethod
    def all_path_strategy(start_n, dest_n):
        """
        在计算规模较小的情况下, 可以吧所有可能路径都列出来
        NOTE:
            1. path的数据结构
            2. 计算终点的判断: is_dest的设置
            3. all_path的计算: new_path的赋值
        """
        all_path = [dict(path=[start_n], weight=0)]
        is_dest = False
        while not is_dest:
            is_dest = True
            new_path = []
            for p in all_path:
                if p['path'][len(p['path']) - 1] == dest_n:
                    new_path.append(p)
                    continue
                for link in AllPathDemo.links:
                    if link['start'] == p['path'][len(p['path']) - 1]:
                        path = list(p['path'])
                        path.append(link['to'])
                        weight = p['weight'] + link['w']
                        new_path.append(dict(path=path, weight=weight))
                        is_dest = False
            all_path = new_path

        all_path.sort(key=lambda p: p['weight'])
        print 'all path:', all_path
        shortest_p = None
        if len(all_path) > 0:
            shortest_p = all_path[0]
        print 'shortest path:', shortest_p


if __name__ == '__main__':
    AllPathDemo()
    AStarDemo()
