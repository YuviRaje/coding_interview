def add_one(number):
    index = len(number) - 1
    carry = 1
    while index >= 0:
        if index == 0:
            number[index] += carry
        else:
            result = number[index] + carry
            number[index] = result % 10
            carry = result / 10
        index -= 1

    return number

print add_one([1,2,3])
