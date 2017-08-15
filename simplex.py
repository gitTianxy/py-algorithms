# encoding=utf-8
"""
Simplex Algorithm demo
ref: https://www.hrwhisper.me/introduction-to-simplex-algorithm/
----------------------------------
I. 应用场景
求解线性规划问题.

II. 算法思想
...

III. 算法步骤
1. [init] <初始化>找到一个初始的基本可行解
2. [loop] 不断的进行旋转（pivot）操作
3. [end] 重复2, 直到结果不能改进为止

IV. 注意事项
1. 初始化操作
    绝大多数情况下，初始解就是基本可行解，但是也有例外: 对于'初始解不是基本可行解'的情形, 需要进行初始化操作，
判断其是否有解并返回一个基本可行解
2. 退化(Degeneracy)
    在旋转的过程中，可能会存在保持目标值不变的情况，这种现象称为退化。退化可能会导致循环(cycling)的情况，
这是使得单纯形算法不会终止的唯一原因。
    处理退化的方法有两种: 1) 适用Bland规则; 2)加入随机扰动
"""
import numpy as np


class Simplex(object):
    def __init__(self, obj, max_mode=False):  # default is solve min LP, if want to solve max lp,should * -1
        self.mat, self.max_mode = np.array([[0] + obj]) * (-1 if max_mode else 1), max_mode

    def add_constraint(self, a, b):
        self.mat = np.vstack([self.mat, [b] + a])

    def _simplex(self, mat, B, m, n):
        while mat[0, 1:].min() < 0:
            col = np.where(mat[0, 1:] < 0)[0][0] + 1  # use Bland's method to avoid degeneracy. use mat[0].argmin() ok?
            row = np.array([mat[i][0] / mat[i][col] if mat[i][col] > 0 else 0x7fffffff for i in
                            range(1, mat.shape[0])]).argmin() + 1  # find the theta index
            if mat[row][col] <= 0: return None  # the theta is ∞, the problem is unbounded
            self._pivot(mat, B, row, col)
        return mat[0][0] * (1 if self.max_mode else -1), {B[i]: mat[i, 0] for i in range(1, m) if B[i] < n}

    def _pivot(self, mat, B, row, col):
        mat[row] /= mat[row][col]
        ids = np.arange(mat.shape[0]) != row
        mat[ids] -= mat[row] * mat[ids, col:col + 1]  # for each i!= row do: mat[i]= mat[i] - mat[row] * mat[i][col]
        B[row] = col

    def solve(self):
        """
        返回结果格式为: (goal-expression value, {nonzero-variance-idx: variance-value})
        """
        m, n = self.mat.shape  # m - 1 is the number slack variables we should add
        temp, B = np.vstack([np.zeros((1, m - 1)), np.eye(m - 1)]), list(range(n - 1, n + m - 1))  # add diagonal array
        mat = self.mat = np.hstack([self.mat, temp])  # combine them!
        if mat[1:, 0].min() < 0:  # is the initial basic solution feasible?
            row = mat[1:, 0].argmin() + 1  # find the index of min b
            temp, mat[0] = np.copy(mat[0]), 0  # set first row value to zero, and store the previous value
            mat = np.hstack([mat, np.array([1] + [-1] * (m - 1)).reshape((-1, 1))])
            self._pivot(mat, B, row, mat.shape[1] - 1)
            if self._simplex(mat, B, m, n)[0] != 0: return None  # the problem has no answer

            if mat.shape[1] - 1 in B:  # if the x0 in B, we should pivot it.
                self._pivot(mat, B, B.index(mat.shape[1] - 1), np.where(mat[0, 1:] != 0)[0][0] + 1)
            self.mat = np.vstack([temp, mat[1:, :-1]])  # recover the first line
            for i, x in enumerate(B[1:]):
                self.mat[0] -= self.mat[0, x] * self.mat[i + 1]
        return self._simplex(self.mat, B, m, n)


if __name__ == "__main__":
    """
    e.g.
       minimize -x1 - 14x2 - 6x3
       st
        x1 + x2 + x3 <=4
        x1 <= 2
        x3 <= 3
        3x2 + x3 <= 6
        x1 ,x2 ,x3 >= 0
       answer :-32
    """
    t = Simplex([-1, -14, -6])
    t.add_constraint([1, 1, 1], 4)
    t.add_constraint([1, 0, 0], 2)
    t.add_constraint([0, 0, 1], 3)
    t.add_constraint([0, 3, 1], 6)
    print(t.solve())
    print '----------------'
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
    t = Simplex([8, 11, 6, 4], max_mode=True)
    t.add_constraint([5, 7, 4, 3], 14)
    t.add_constraint([1, 0, 0, 0], 1)
    t.add_constraint([0, 1, 0, 0], 1)
    t.add_constraint([0, 0, 1, 0], 1)
    t.add_constraint([0, 0, 0, 1], 1)
    print(t.solve())
