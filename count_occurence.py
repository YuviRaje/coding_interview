# coding=utf-8
'''
Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0

**Example : **
Given [5, 7, 7, 8, 8, 10] and target value 8,
return 2.

PROBLEM APPROACH :

For complete solution, look at the hint.
'''


def get_left_start(arr, key):

    start = 0
    end = len(arr) - 1
    result = - 1


    while start <= end:

        mid = (start + end)/2

        if arr[mid] == key:
            result = mid
            end = mid - 1

        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return result


def get_right_end(arr, key):

    start = 0
    end = len(arr) - 1
    result = - 1

    while start <= end:

        mid = (start + end) /2

        if arr[mid] == key:
            result = mid
            start = mid + 1

        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return result

def get_freq(arr, key):

    left_index = get_left_start(arr, key)
    right_index = get_right_end(arr, key)
    if left_index == -1:
        return - 1
    else:
        return right_index - left_index + 1

arr = [5, 7, 7, 8, 8, 10]

print get_freq(arr, 8)