'''
Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

    A -> 1

    B -> 2

    C -> 3

    ...

    Z -> 26

    AA -> 27

    AB -> 28
'''


def col_number(title):

    index = 0
    result = 0

    for i in range(len(title) -1, -1, -1):
        result += (26 ** index) * (ord(title[i]) - ord('A') + 1)
        index += 1

    return result


def col_title(number):
    result = []
    while number > 0:
        result.append( number % 26 )
        number = number / 26

    result.reverse()
    return result

print col_title(27)