'''
N number of books are given.
The ith book has Pi number of pages.
You have to allocate books to M number of students so that maximum number of pages alloted to a student is minimum. A book will be allocated to exactly one student. Each student has to be allocated at least one book. Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.

NOTE: Return -1 if a valid assignment is not possible

Input:
 List of Books M number of students

Your function should return an integer corresponding to the minimum number.
'''


def allocate(books, index, partition):

    if partition == 0:
        return sum(books[index:])

    best_result = float('inf')

    for i in range(index + 1, len(books)):

        sub_array = books[index: i]

        current_result = max(sum(sub_array), allocate(books, index, partition -1 ))

        best_result = min(best_result, current_result)


    return best_result





