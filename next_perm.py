'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

def next_perm(number):

    for i in range(len(number) - 1, 1, -1):
        if number[i-1]< number[i]:
            just_greater_number_index = get_just_greater_number(number,i)

            number[i-1],number[just_greater_number_index] = number[just_greater_number_index], number[i-1]

            return number[:i] + number[i:].sort()

