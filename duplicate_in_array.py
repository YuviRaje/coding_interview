'''
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1
'''

def duplicate(arr):

    index = 0
    while index < len(arr):

        while arr[index] != index:
            value = arr[index]
            if arr[value] != value:
                arr[value], arr[index] = value, arr[value]
            else:
                return value
        index += 1


print duplicate([3, 0, 1, 4, 1])