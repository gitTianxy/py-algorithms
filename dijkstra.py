# encoding=utf-8
"""
Dijkstra algorithm demo
-------------------------
I. 应用场景
1. 带'非负'权值的图(之所以有非负的要求,是为了保证靠后获得的路径长度总是大于已有的路径长度)
2. 用于求指定顶点start到其余'所有'顶点最短路径

II. 数据结构
1. 点集区分U/S:
    S: 已经有路径的点集
    U: 还无路径的点集
2. 最短路径集:
    记录起点start到S中个点的最短路径及其权值

III. 算法步骤
0. init: S(empty list), U(all node), shortest_path(empty list), all_path(start_node_path), curr_node=start_node
1. get shortest_path from 'all_path' of which the tail-node not included in 'S'.
2. add 'tail-node' into 'S', while rm it from 'U'; and add the path into 'shortest_path'.
3. curr_node='tail-node' and get new_path based on curr_node; add new_path into 'all_path'
4. if U is empty: terminate; else: jump to step '1'

IV. 算法复杂度
1. 时间复杂度: ...
2. 空间复杂度: ...
"""

# 有向图
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

paths = []

s = []
v = list(range(0, 6))
start = 0


def dijkstra(start):
    global links
    global paths
    global s
    global v
    all_path = []
    start_node_path = dict(path=[start, start], weight=0)
    all_path.append(start_node_path)
    while len(v) > 0:
        shortest_path = None
        all_path.sort(key=lambda p: p['weight'])
        for p in all_path:
            if s.__contains__(p['path'][len(p['path']) - 1]):
                continue
            shortest_path = p
            break
        if shortest_path is None:
            break
        tail_node = shortest_path['path'][len(shortest_path['path']) - 1]
        s.append(tail_node)
        v.remove(tail_node)
        paths.append(shortest_path)
        new_paths = get_new_paths(shortest_path)
        all_path.extend(new_paths)
    print paths


def get_new_paths(curr_path):
    global links
    global start
    new_paths = []
    curr_tail = curr_path['path'][len(curr_path['path']) - 1]
    for l in links:
        if l['start'] == curr_tail:
            if curr_tail == start:
                path = [l['start'], l['to']]
                weight = l['w']
            else:
                path = list(curr_path['path'])
                path.append(l['to'])
                weight = curr_path['weight'] + l['w']
            new_paths.append(dict(path=path, weight=weight))
    return new_paths


if __name__ == "__main__":
    dijkstra(start=0)
