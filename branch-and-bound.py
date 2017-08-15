# encoding=utf-8
"""
branch and bound demo
ref:
    http://blog.csdn.net/yinlili2010/article/details/39313035
    http://blog.sina.com.cn/s/blog_75156ace0101hhh9.html
------------------------------------
I. 应用场景
找出满足约束条件的一个解，或是在满足约束条件的最优解(在解集中找出使某一目标函数值达到极大或极小的解)。

II. 算法思想
首先确定目标值的上下界， 边搜索边减掉搜索树的某些枝， 提高搜索效率。
分支界定法在两个方面加速了算法的搜索效率:
    1. 在选择扩展节点时， 总是选择一个最小成本的节点， 尽可能早的进入最有可能成为最优解的分支
    2. 扩展节点的过程，舍弃导致不可行解或导致非最优解的子节点。

III. 算法步骤
0. [init] 定界: 求解定界条件
1. [loop] 从活节点列表中取出一个扩展节点
2. [loop] 获取当前扩展节点的所有孩子节点
3. [loop] 在产生的孩子节点中，剪掉那些不可能产生可行解（或最优解）的节点, 其余的加入活节点列表
4. [end] 如此循环，直到找到问题的可行解（或最优解）或者活结点表为空

IV. 注意事项
...
"""
from simplex import Simplex

# 活节点列表
live_nodes = []
# 目标表达式
goal_expr_val = None
# 定界条件
goal_expr_limit = None


def branch_and_bound():
    pass


def get_children():
    pass


def get_relaxation_solution(goal_expr, linear_equations, var_num):
    s = Simplex(goal_expr['mat'], max_mode=goal_expr['max_mode'])
    for eq in linear_equations:
        s.add_constraint(eq['mat'], eq['val'])
    res = s.solve()
    if res is None:
        return
    expr_val = res[0]
    for i in range(1, var_num+1):
        if res[1].get(i) is None:
            res[1][i] = 0
    return dict(expr_val=expr_val, var_vals=res[1])


if __name__ == '__main__':
    """
        e.g. 
            maximize 8x1 + 11x2 + 6x3 + 4x4
            st
                5x1 + 7x2 + 4x3 + 3x4 <= 14
                x1, x2, x3, x4 <=1
                x1, x2, x3, x4 >= 0
            answer:
                22; [1,1,0.5,0]
        """
    idx = 0
    print '------------- branching %s -----------------' % idx
    goal_expr = dict(mat=[8, 11, 6, 4], max_mode=True)
    linear_equations = [
        dict(mat=[5, 7, 4, 3], val=14),
        dict(mat=[1, 0, 0, 0], val=1),
        dict(mat=[0, 1, 0, 0], val=1),
        dict(mat=[0, 0, 1, 0], val=1),
        dict(mat=[0, 0, 0, 1], val=1),
    ]
    print get_relaxation_solution(goal_expr, linear_equations, var_num=4)
    idx += 1
    print '------------- branching %s -----------------' % idx
    # x3=0
    goal_expr = dict(mat=[8, 11, 6, 4], max_mode=True)
    linear_equations = [
        dict(mat=[5, 7, 4, 3], val=14),
        dict(mat=[1, 0, 0, 0], val=1),
        dict(mat=[0, 1, 0, 0], val=1),
        dict(mat=[0, 0, 1, 0], val=0),
        dict(mat=[0, 0, -1, 0], val=0),
        dict(mat=[0, 0, 0, 1], val=1),
    ]
    print get_relaxation_solution(goal_expr, linear_equations, var_num=4)
    # x3=1
    goal_expr = dict(mat=[8, 11, 6, 4], max_mode=True)
    linear_equations = [
        dict(mat=[5, 7, 4, 3], val=14),
        dict(mat=[1, 0, 0, 0], val=1),
        dict(mat=[0, 1, 0, 0], val=1),
        dict(mat=[0, 0, 1, 0], val=1),
        dict(mat=[0, 0, -1, 0], val=-1),
        dict(mat=[0, 0, 0, 1], val=1),
    ]
    print get_relaxation_solution(goal_expr, linear_equations, var_num=4)
    idx += 1
    print '------------- branching %s -----------------' % idx
    # x3=1,x2=0
    goal_expr = dict(mat=[8, 11, 6, 4], max_mode=True)
    linear_equations = [
        dict(mat=[5, 7, 4, 3], val=14),
        dict(mat=[1, 0, 0, 0], val=1),
        dict(mat=[0, 1, 0, 0], val=0),
        dict(mat=[0, -1, 0, 0], val=0),
        dict(mat=[0, 0, 1, 0], val=1),
        dict(mat=[0, 0, -1, 0], val=-1),
        dict(mat=[0, 0, 0, 1], val=1),
    ]
    print get_relaxation_solution(goal_expr, linear_equations, var_num=4)
    # x3=1,x2=1
    goal_expr = dict(mat=[8, 11, 6, 4], max_mode=True)
    linear_equations = [
        dict(mat=[5, 7, 4, 3], val=14),
        dict(mat=[1, 0, 0, 0], val=1),
        dict(mat=[0, 1, 0, 0], val=1),
        dict(mat=[0, -1, 0, 0], val=-1),
        dict(mat=[0, 0, 1, 0], val=1),
        dict(mat=[0, 0, -1, 0], val=-1),
        dict(mat=[0, 0, 0, 1], val=1),
    ]
    print get_relaxation_solution(goal_expr, linear_equations, var_num=4)
    idx += 1
    print '------------- branching %s -----------------' % idx
    # x3=1,x2=1,x1=0
    goal_expr = dict(mat=[8, 11, 6, 4], max_mode=True)
    linear_equations = [
        dict(mat=[5, 7, 4, 3], val=14),
        dict(mat=[1, 0, 0, 0], val=0),
        dict(mat=[-1, 0, 0, 0], val=0),
        dict(mat=[0, 1, 0, 0], val=1),
        dict(mat=[0, -1, 0, 0], val=-1),
        dict(mat=[0, 0, 1, 0], val=1),
        dict(mat=[0, 0, -1, 0], val=-1),
        dict(mat=[0, 0, 0, 1], val=1),
    ]
    print get_relaxation_solution(goal_expr, linear_equations, var_num=4)
    # x3=1,x2=1,x1=1
    goal_expr = dict(mat=[8, 11, 6, 4], max_mode=True)
    linear_equations = [
        dict(mat=[5, 7, 4, 3], val=14),
        dict(mat=[1, 0, 0, 0], val=1),
        dict(mat=[-1, 0, 0, 0], val=-1),
        dict(mat=[0, 1, 0, 0], val=1),
        dict(mat=[0, -1, 0, 0], val=-1),
        dict(mat=[0, 0, 1, 0], val=1),
        dict(mat=[0, 0, -1, 0], val=-1),
        dict(mat=[0, 0, 0, 1], val=1),
    ]
    print get_relaxation_solution(goal_expr, linear_equations, var_num=4)
    idx += 1
