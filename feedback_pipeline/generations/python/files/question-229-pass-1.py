def getMinNum(a, b, c):
    if a % c == 0:
        return a
    else:
        for i in range(a, b+1):
            if i % c == 0:
                return i
        return -1