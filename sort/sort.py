"""
	参考文章url:https://www.imooc.com/article/288482
"""

def select_sort(arr):
	"""选择排序，从开头元素的后面选择一个比开头元素小的数，找到后和开头元素交换"""
	arr_len = len(arr)
	for i in range(arr_len-1):
		min_index = i
		for j in range(i+1,arr_len):
			if(arr[min_index]>arr[j]):
				min_index = j
		arr[i], arr[min_index] = arr[min_index], arr[i]		
	return arr
	
def insert_sort(arr):
	"""插入排序，
		1. 将序列分成已排序和未排序两部分，
		2. 每次从未排序序列中选择一个，找到合适的位置，插入到已排序序列中
	"""
	arr_len = len(arr)
	for i in range(1,arr_len):
		for j in range(i,0,-1):
			if(arr[j]<arr[j-1]):
				arr[j],arr[j-1] = arr[j-1],arr[j]
	return arr

if __name__ == "__main__":
	arr = [1,0,5,3,7,4,-3,100]
	#print(select_sort(arr))
	print(insert_sort(arr))
