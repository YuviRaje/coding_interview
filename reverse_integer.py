
'''
123 -> 3 2 1

321
'''

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):

        result = 0
        is_neg = False
        if A < 0:
            is_neg = True
            A = A * -1

        while A :
            remainder = A % 10

            result = result*10 + remainder
            A = A / 10

        return result * -1 if is_neg else result






