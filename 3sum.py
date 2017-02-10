'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers.

Assume that there will only be one solution

Example: 
given array S = {-1 2 1 -4}, 
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)

min(a + b + c - k) 
'''


def three_sum(arr, target):

	arr.sort()
	result = float('inf')

	for i, each in enumerate(arr):
		result = min(result, two_sum(arr, target - each), i)

	return result


def two_sum(arr, target, a_index):

	i = 0
	j = len(arr) - 1
	result = float('inf')

	while i != j:
		if i == a_index:
			i += 1
		elif j == a_index:
			j -= 1
		else:
			temp = arr[i] + arr[j] - target

			if temp > 0:
				j -= 1
			else:
				i += 1











