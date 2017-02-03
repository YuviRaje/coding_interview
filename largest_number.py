'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

def largest_number(arr):

    return ''.join(map(str,sorted(arr, cmp=compare)))

def compare(x,y):
    return  (int(str(y) + str(x))) - (int(str(x) + str(y)))

arr = [3, 30, 34, 5, 9]

print largest_number(arr)