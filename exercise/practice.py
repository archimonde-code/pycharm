"""
主要练习的是Python的排序算法，
主要包含冒泡排序、选择排序
"""


class SortFunction:

    def __init__(self):
        # 初始化方法
        pass

    # 冒泡排序
    def bubble_sort(self):
        list_sort = self
        for i in range(1, len(list_sort)):
            for j in range(0, len(list_sort)-i):
                if list_sort[j] > list_sort[j + 1]:
                    list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]
        return list_sort


array_list = [32, 54, 12, 90, 65, 34, 27, 1, 87, 74, 15]
print(SortFunction.bubble_sort(array_list))