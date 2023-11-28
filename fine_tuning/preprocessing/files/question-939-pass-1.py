def msbPos(n):
    if n == 0:
        return 0
    i = 0
    while n > 0:
        n >>= 1
        i += 1
    return i - 1
