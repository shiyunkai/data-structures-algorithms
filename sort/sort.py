"""
	�ο�����url:https://www.imooc.com/article/288482
"""

def select_sort(arr):
	"""ѡ�����򣬴ӿ�ͷԪ�صĺ���ѡ��һ���ȿ�ͷԪ��С�������ҵ���Ϳ�ͷԪ�ؽ���"""
	arr_len = len(arr)
	for i in range(arr_len-1):
		min_index = i
		for j in range(i+1,arr_len):
			if(arr[min_index]>arr[j]):
				min_index = j
		arr[i], arr[min_index] = arr[min_index], arr[i]		
	return arr
	
def insert_sort(arr):
	"""��������
		1. �����зֳ��������δ���������֣�
		2. ÿ�δ�δ����������ѡ��һ�����ҵ����ʵ�λ�ã����뵽������������
	"""

if __name__ == "__main__":
	arr = [1,0,5,3,7,4,-3,100]
	print(select_sort(arr))
