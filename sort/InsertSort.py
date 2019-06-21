"""
插入排序
把n个待排序的元素看成为一个有序表和一个无序表。开始时有序表中只包含1个元素，
无序表中包含有n-1个元素，
排序过程中每次从无序表中取出第一个元素，
将它插入到有序表中的适当位置，使之成为新的有序表，重复n-1次可完成排序过程。
"""


def insert_sort(lis):
    lis_len = len(lis)
    for i in range(1, lis_len):  # 执行n-1次
        for j in range(i, 0, -1):
            if lis[j - 1] > lis[j]:
                lis[j - 1], lis[j] = lis[j], lis[j - 1]
    return lis


if __name__ == "__main__":
    lis = insert_sort([100, 20, 30, 15, 88, 14, 8, 90, 120])
    print(lis)
