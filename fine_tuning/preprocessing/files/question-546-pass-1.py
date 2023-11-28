def minOperations(str, n):
    count = 0
    for i in range(n):
        if str[i] == '0':
            count += 1
    return count
