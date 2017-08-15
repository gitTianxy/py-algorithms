# encoding=utf-8
"""
Binary-Search demo
ref: http://blog.csdn.net/shichaosong/article/details/8861246
-------------------------------------
I. 应用场景
不经常变动而查找频繁的有序列表.

II. 算法思想
...

III. 算法步骤
0. [init] 序列排序
1. [loop] 确定整个查找区间的中间位置: mid=(left+right)/2
2. [loop] 将待查关键字值与中间位置的关键字值进行比较
    a. 若相等，则查找成功;
    b. 若大于，则在后（右）半个区域继续进行折半查找;
    c. 若小于，则在前（左）半个区域继续进行折半查找
3. [end] 获取结果: 要么查找成功， 要么查找失败。

IV. 优缺点及注意事项
1. 优点
比较次数少，查找速度快，平均性能好
2. 缺点
要求待查表为有序表，且插入删除困难。
"""

if __name__ == '__main__':
    pass
