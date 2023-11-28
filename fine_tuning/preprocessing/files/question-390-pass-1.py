def findLength(string, n):
    count = 0
    for i in range(n):
        if string[i] == '0':
            count += 1
        else:
            count = 0
    return count
