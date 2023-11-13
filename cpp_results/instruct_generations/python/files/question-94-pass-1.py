def findNthNumber(N):
    n = 1
    while True:
        s = str(n)
        if len(s) == N:
            return n
        n += 1