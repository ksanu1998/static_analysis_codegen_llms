def countPaths(m, n):
    if m == 1 and n == 1:
        return 1
    elif m == 1 or n == 1:
        return 1
    else:
        return countPaths(m-1, n) + countPaths(m, n-1)
