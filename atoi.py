def atoi( A):
    index = 0

    while A[index] == ' ':
        index += 1
    start = index

    if A[start] == '+' or A[start] == '-':
        start += 1
    index = start
    while index < len(A) and ord(A[index]) - ord('0') >= 0 and ord(A[index]) - ord('0') <= 9:
        index += 1

    end = index - 1

    return int(A[start:end + 1])


print atoi(' +7')