
def merge_sort(arr, l, r):
	if l < r:
		mid = (l + r) /2 

		merge_sort(arr, l, mid)
		merge_sort(arr,mid + 1, r)
		merge(arr, l, mid, r)


def merge(arr, l, m, r):
	temp = []

	i = l
	j = m+1
	index = l

	while i <=m and j <= r:
		if arr[i] < arr[j]:
			temp.append(arr[i])
			i += 1
		else:
			temp.append(arr[j])
			j += 1
		index += 1

	temp.extend(arr[i:m+1])
	temp.extend(arr[j:r+1])

	arr[l:r + 1] = temp	

arr = [5,6,2,1,0]

merge_sort(arr, 0, len(arr) - 1)
print arr 

