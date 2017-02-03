
import heapq

def running_median(arr):

	max_heap_left = []
	min_heap_right = []

	for each in arr:

		if len(max_heap_left) == 0 or each < max_heap_left[0]:
			heapq.heappush(max_heap_left, each * -1)

		else:
			heapq.heappush(min_heap_right, each)


		if abs(len(max_heap_left) - len(min_heap_right)):
			if len(max_heap_left) > len(min_heap_right):
				popped_number = max_heap_left[0] * -1
				heapq.heappop(max_heap_left)
				heapq.heappush(min_heap_right, popped_number )
			else:
				popped_number = min_heap_right[0] 
				heapq.heappop(min_heap_right)
				heapq.heappush(max_heap_left, popped_number * -1)

	if len(max_heap_left) == len(min_heap_right):
		return (max_heap_left[0] * -1 + min_heap_right[0])/2.0
	else:
		if len(max_heap_left) > len(min_heap_right):
			return max_heap_left[0] * -1
		else:
			return min_heap_right[0]	

arr  = [1,2,3,4,5]

print running_median(arr)	
arr = [1,2,3,4,5,6]
print running_median(arr)	
