def select_sort(lis):
    lis_len = len(lis) - 1
    for i in range(lis_len, 0, -1):  # n-1,n-2,n-3,...,1 循环n-1次
        # 最大元素的下标
        max_index = i
        # 找到未排序序列中最大元素的下标
        for j in range(i):
            if lis[j] > lis[max_index]:
                max_index = j
        # 将最大号元素和序列末尾元素进行交换，即将最大元素放到序列末尾
        if max_index is not i:
            lis[max_index], lis[i] = lis[i], lis[max_index]
    return lis


if __name__ == "__main__":
    lis = select_sort([33, 24, 1, 34, 50, 100, 200, 101, 77, 45, 46])
    print(lis)
