# encoding=utf-8
"""
Gradient Descent demo
ref:
    https://ctmakro.github.io/site/on_learning/gd.html
    http://www.cnblogs.com/ooon/p/4947688.html
------------------------
I. 适用场景
找到某个函数的极小值或者最小值。

II. 算法思想
取一个初始状态, 然后对参数向量θ中的每个分量θj迭代减去速率因子a* (dJ(θ)/dθj), 最后算式取值会收敛到目标值

III. 操作步骤

"""
import math


class DerivativeDescentDemo:
    """
    导数下降法
    --用于一元函数问题
    """

    def __init__(self):
        print 'derivative descent demo -------------------'
        x = 0.0
        for i in range(50):
            x = self.derivative_descent(x)
            print('x = {:6f}, error(x) = {:6f}'.format(x, self.error(x)))

    def error(self, x):
        return (self.__problem(x) - 0) ** 2

    def derivative_descent(self, x):
        delta = 0.00000001
        derivative = (self.error(x + delta) - self.error(x - delta)) / (delta * 2)
        alpha = 0.01
        x = x - derivative * alpha
        return x

    def __problem(self, x):
        return x ** 3 + 2 * x + math.e ** x - 3


class GradientDescentDemo:
    """
    梯度下降
    -- 用于多元函数
    """

    def __init__(self, start, step, round):
        self.start = start
        self.step = step
        self.round = round
        print 'gradient descent demo -------------------'
        x = [0.0, 0.0]
        for i in range(50):
            x = self.gradient_descent(x)
            print('x = {:6f},{:6f}, error(x) = {:6f}'.format(x[0], x[1], self.error(x)))

    def gradient_descent(self, x):
        delta = 0.00000001
        derivative_x0 = (self.error([x[0] + delta, x[1]]) - self.error([x[0] - delta, x[1]])) / (delta * 2)
        derivative_x1 = (self.error([x[0], x[1] + delta]) - self.error([x[0], x[1] - delta])) / (delta * 2)
        alpha = 0.01
        x[0] = x[0] - derivative_x0 * alpha
        x[1] = x[1] - derivative_x1 * alpha
        return [x[0], x[1]]

    def error(self, x):
        return (problem(x) - 0) ** 2


import numpy as np


class NumpyGradientDescentDemo:
    """
    gradient descent implemented in numpy
    """

    def __init__(self, start, step, round):
        self.start = start
        self.step = step
        self.round = round
        print 'numpy demo -------------------'
        x = np.array(self.start)
        for i in range(self.round):
            x = self.gradient_descent(x)
            print('x = {:6f},{:6f}, error(x) = {:6f}'.format(x[0], x[1], self.error(x)))

    def gradient_descent(self, x):
        delta = 0.00000001
        gradient = np.zeros(x.shape)  # 梯度矢量

        for i in range(len(gradient)):  # 逐个求取偏导数，放进梯度矢量
            deltavector = np.zeros(x.shape)
            deltavector[i] = delta
            gradient[i] = (self.error(x + deltavector) - self.error(x - deltavector)) / (delta * 2)

        alpha = self.step
        x = x - gradient * alpha
        return x

    def error(self, x):
        return (problem(x) - 0) ** 2


def problem(x):
    return x[0] ** 5 + math.e ** x[1] + x[0] ** 3 + x[0] + x[1] - 5


if __name__ == "__main__":
    DerivativeDescentDemo()
    GradientDescentDemo(start=[0.0, 0.0], step=0.01, round=50)
    NumpyGradientDescentDemo(start=[0.0, 0.0], step=0.01, round=50)
