import time

"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


class Solution:
    # 二维列表
    array_list = [[1, 4, 7],
                  [2, 5, 8],
                  [3, 6, 9],
                  [4, 7, 10]]

    def __init__(self):
        # 初始化方法
        pass

    def find_number(target, array):
        lists = []
        for i in range(len(array)):
            for j in array[i]:
                lists.append(j)
        if target in lists:
            return True
        else:
            return False


get_input = int(input("请输入数字："))
print(time.process_time_ns())
print(Solution.find_number(get_input, Solution.array_list))
print(time.process_time_ns())
