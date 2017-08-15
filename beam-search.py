# encoding=utf-8
"""
Beam Search demo
ref: http://jhave.org/algorithms/graphs/beamsearch/beamsearch.shtml
-------------------------------------
I. 应用场景
通常用在图的解空间比较大的情况下.

II. 算法思想
beam search算法为了减少搜索所占用的空间和时间，在每一步深度扩展的时候，剪掉一些质量比较差的结点，保留下一些质量较高的结点。
这样减少了空间消耗，并提高了时间效率，但缺点就是有可能存在潜在的最佳方案被丢弃，因此Beam Search算法是不完全的.

III. 数据结构
h:
    heuristic function, to estimate the cost to reach the goal from a given node.
BEAM:
    to store the nodes that are to be expanded in the next loop of the algorithm;
    similar to open-list in breadth-first search.
SET of successor nodes:
    all of the nodes connected to the nodes in the BEAM
B:
    beam width, which specifies the number of nodes that are stored at each level of the Breadth-First Search.
hash table:
    to store nodes that have been visited, similar to the closed list used in the Breadth-First Search.

IV. 算法步骤
1. [init] adds the starting node to the BEAM and the hash table
2. [loop] adds all of the nodes connected to the nodes in the BEAM to its SET of successor nodes
3. [loop] adds the B nodes with the best heuristic values from the SET to the BEAM and the hash table
4. [end] until the goal node is found, the hash table becomes full(BAD END),
    or the BEAM is empty after the main loop has completed(BAD END).

V. The choice of B has a large impact on Beam Search's performance
-- With the variation of B, the effectiveness of algorithm changes, and the search process may even terminated
without able to find the goal (as shown in 'IV'):
1. when B is relatively small
    the process is likely terminated with 'the BEAM(open)' is empty, which represents a dead end in search;
    even as a path is find, it is not likely the best one.
2. when B is relatively large
    it is more likely to find the best path, but the search process also more likely to be ended with
    'the hash table(close)' is full, which represents memory-exhausted),
-- conclusion:
1. set the B to a median level that can achieve result good enough while cost reasonable memory
2. while increasing B, also enlarge the scale of 'the hash-table(close)'
"""

start_node = None
goal_node = None

if __name__ == '__main__':
    pass
