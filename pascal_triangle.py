# coding=utf-8
'''
Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
'''

def pascal_triangle(numRows):
    pascal = [[1]]
    for i in range(1,numRows):
        pascal.append([])
        for j in range(i+1):
            result = pascal[i-1][j-1] if i-1 >= 0 and j-1 >=0 and j-1 <= i - 1 else 0
            result += pascal[i-1][j] if i-1 >= 0 and j >=0 and j <= i - 1 else 0
            pascal[i].append(result)

    return pascal


print pascal_triangle(5)


