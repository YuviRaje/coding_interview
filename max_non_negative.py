'''
A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
'''


def max_non_negative(arr):
    start_index = None
    current_sum = 0
    max_sum = float('-inf')

    for i,each in enumerate(arr):
        if each > 0 and start_index == None:
            start_index = i
            current_sum = each
        elif start_index!= None and each > 0:
            current_sum += each
        else:
            max_sum = max(max_sum, current_sum)
            current_sum = 0
            start_index = None

    return max_sum

print max_non_negative([1, 2, 5, -7, 2, 3])