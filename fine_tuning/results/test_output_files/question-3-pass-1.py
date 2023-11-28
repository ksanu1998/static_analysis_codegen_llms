def findNthNumber(N):
    if (N == 1):
        print(1)
        return
    n = 9
    while (N > 0):
        N = N - n
        n = n - 1
    print(n)


if __name__ == "__main__":
    N = 10
    findNthNumber(N)
