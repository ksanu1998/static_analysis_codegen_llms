def findNumber(n):
    for i in range(1, n+1):
        if len(str(i)) == n:
            return i
    return -1
