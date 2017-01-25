


def sqrt(number):

    low = 1
    high = number - 1

    while low <= high:

        mid  = (low + high) /2

        if mid * mid == number:
            return  mid

        elif mid * mid > number:
            high = mid - 1
        else:
            low = mid + 1

    return low - 1

print sqrt(15)

