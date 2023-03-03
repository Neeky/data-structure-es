#!/usr/bin/env python3

"""
选择排序

首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完成。
"""

from typing import List


def select_sort(lst:List):
    """
    第一次从未排序的列表(整个列表)里找出最小的元素，并把它保存在 lst[0] 处
    第二次从未排序的列表(除第一个之后的所有元素)里找出最小的元素，并把它保存在 lst[1] 处
    """
    length = len(lst)
    if length <= 1:
        return
    
    # 执行到这里说明至少有两个元素
    """
    只要将“最小的” n - 1 个元素排好序之后整个列表就有序了
    """
    for i in range(length - 1):
        """
        假设 i 是最小元素的下标，将其它保存到临时变量 minx 中
        """
        minx = i
        """
        从 minx 之后往后找，如果它的值大于 lst[minx] 就更新 minx 的值
        """
        for j in range(minx + 1, length):
            if lst[minx] > lst[j]:
                minx = j
        # 如果 minx 和 i 不一样，说明 minx 对应的值比较 i 对应的值小，这个时候我们要交换两个数
        if minx != i:
            lst[i], lst[minx] = lst[minx], lst[i]

def main():
    lst = []
    select_sort(lst)
    print(lst)

    lst = [0]
    select_sort(lst)
    print(lst)

    lst = [0, -1]
    select_sort(lst)
    print(lst)

    lst = [1, 2, 5, 0]
    select_sort(lst)
    print(lst)

    lst = [1, 0, 8, 0]
    select_sort(lst)
    print(lst)



if __name__ == "__main__":
    main()
