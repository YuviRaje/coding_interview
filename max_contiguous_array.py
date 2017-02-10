
def max_contiguous_array(arr, start_index, end_index):
	if start_index == end_index:
		return arr[start_index]
	elif start_index > end_index:
		return float('-inf')
	else:
		mid = (start_index + end_index) /2 

		left_subarray_max_sum = max_contiguous_array(arr, start_index, mid - 1)
		right_subarray_max_sum = max_contiguous_array(arr, mid + 1,end_index)

		current_sum = current_subarray_sum(arr, start_index, mid, end_index)

		return max(left_subarray_max_sum, right_subarray_max_sum, current_sum)


def current_subarray_sum(arr, left_index, mid, right_index):

	i = mid 
	j = mid + 1
	current_sum = 0
	left_max_sum = float('-inf')
	right_max_sum = float('-inf')
	while i >= left_index:
		current_sum += arr[i]

		left_max_sum = max(left_max_sum, current_sum)
		i -= 1
	current_sum = 0
	while j <= right_index:
		current_sum += arr[j]

		right_max_sum = max(right_max_sum, current_sum)
		j += 1

	return left_max_sum + right_max_sum 


arr = [-2,1,-3,4,-1,2,1,-5,4]

print max_contiguous_array(arr, 0, len(arr) -1)

