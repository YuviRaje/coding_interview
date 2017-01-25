'''
N number of books are given.
The ith book has Pi number of pages.
You have to allocate books to M number of students so that maximum number of pages alloted to a student is minimum. A book will be allocated to exactly one student. Each student has to be allocated at least one book. Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.

NOTE: Return -1 if a valid assignment is not possible

Input:
 List of Books M number of students

Your function should return an integer corresponding to the minimum number.
'''


def allocate(arr, index, partition):

    if partition == 0:
        return sum(arr[index:])

    if index >= len(arr):
        return float('-inf')


    best_ans = float('inf')

    for i in range(index + 1, len(arr)):

        subarray = arr[index: i]

        max_sum_from_next_subarray = allocate(arr, i, partition - 1)

        current_max_sum = max(sum(subarray), max_sum_from_next_subarray)

        best_ans = min(best_ans, current_max_sum)

    return best_ans


