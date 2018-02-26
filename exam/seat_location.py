# encoding=utf-8
"""
LEVEL:
    advanced
PROBLEM:
    假设有一个男生和女生分别有15人的班级，要求排出一个6×5的座次, 使其满足任意一人周围都是异性或者墙. 求满足条件的方案的个数.
"""

if __name__ == '__main__':
    num = 15
    multi = 1
    for i in range(1, num+1):
        multi *= i
    result = multi*multi*2
    print 'result:', result
