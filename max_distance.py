'''
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2
for the pair (3, 4)

'''


def max_dist(arr):

    lmin = []
    min_number = arr[0]

    for each in arr:
        min_number = min(min_number, each)
        lmin.append(min_number)

    rmax = [None]*len(arr)
    max_number = arr[-1]

    for i in range(len(arr)-1, -1, -1):
        max_number = max(max_number, arr[i])
        rmax[i] = max_number

    i = 0
    j = 0
    result = -1
    while i < len(arr) and j < len(arr):
        if lmin[i] > rmax[j]:
            i += 1
        else:
            result = max(result, (j - i))
            j +=1

    return result if result!=0 else -1




print max_dist([4,3,2,1])