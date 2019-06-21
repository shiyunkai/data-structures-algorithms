def bubble_sort1(list):
    """冒泡排序-方法1"""
    length = len(list)
    for i in range(0, length - 1):  # i:[0,len-2]
        for j in range(0, length - 1 - i):
            if list[j] > list[j + 1]:
                # 交换两个数
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def bubble_sort2(list):
    """冒泡排序-方法2"""
    list_len = len(list) - 1
    for i in range(list_len, 0, -1):  # 外层循环n-1次
        for j in range(i):
            if list[j] > list[j + 1]:
                # 交换两个数
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


if __name__ == "__main__":
    sort_list = bubble_sort2([54, 26, 93, 17, 77, 31, 44, 55, 20])
    print(sort_list)
