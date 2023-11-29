def printSmallest(a, n):
    for i in range(a, n):
        if i % 3 == 0:
            return i
    return -1