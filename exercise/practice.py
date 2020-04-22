import time

"""
主要练习的是Python的排序算法，
主要包含冒泡排序、选择排序、
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

    # 选择排序
    def selection_sort(self):
        sort_list = self
        for i in range(len(sort_list) - 1):
            # 记录最小数的索引
            min_index = i
            for j in range(i + 1, len(sort_list)):
                if sort_list[j] < sort_list[min_index]:
                    min_index = j
                # i 不是最小数时，将 i 和最小数进行交换
                if i != min_index:
                    sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]
        return sort_list


array_list = [32, 54, 12, 90, 65, 34, 27, 1, 87, 74, 15]

# 对数组array_list进行冒泡排序，并输出排序后的数组
print(SortFunction.bubble_sort(array_list))

# 对数组array_list进行选择排序，并输出排序后的数组
print(SortFunction.selection_sort(array_list))
