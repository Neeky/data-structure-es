#!/usr/bin/env python3

"""
冒泡排序
"""

from typing import List

def bubble_sort(lst:List):
    """
    1. 从前往后依次比较两个无线，大的元素往后移动
    2. 现次重复步骤 1 这样第二大的元素也可以迁移到最后面
    3. 重复 n -1 次就能完成元素的排查
    """
    length = len(lst)
    if length <= 1:
        return 
    
    """
    对于一个长度为 n 的数组每从头到尾比较一趟就能把当前的“极大值”放到对应的位置，所以只要比较 n - 趟就能完成
    """
    trips = length - 1
    for i in range(trips):
        """
        对于每一趟的比较操作都是从索引为 0 的位置开始的，对于有 n 个元素的数据只要比较 n - 1 次就能比较出这一趟的“极大值”
        之前比较过的就没有必要再比较了，所以一趟比较也只要比较 n - i - 1 次
        """
        for j in range(length - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def main():
    lst = []
    bubble_sort(lst)
    print(lst)

    lst = [0]
    bubble_sort(lst)
    print(lst)

    lst = [0, -1]
    bubble_sort(lst)
    print(lst)

    lst = [1, 2, 5, 0]
    bubble_sort(lst)
    print(lst)

    lst = [1, 0, 8, 0]
    bubble_sort(lst)
    print(lst)



if __name__ == "__main__":
    main()
