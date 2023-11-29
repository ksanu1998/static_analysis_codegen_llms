def printPair(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i + j == n) and (i * j == n):
                print(i, j)
                return
