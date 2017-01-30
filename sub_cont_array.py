def max_sub_cont(arr):
    current_sum = 0
    current_max = 0


    for each in arr:
        current_sum += each

        if current_sum < 0:
            current_sum = 0

        current_max = max(current_max, current_sum)
    if current_max == 0:
        return max(arr)
    return current_max
print 'hello world'
