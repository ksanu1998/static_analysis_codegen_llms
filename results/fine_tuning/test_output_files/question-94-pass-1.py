def findNthNumber(N):
    if (N == 1):
        print(1)
        return
    n = 1
    while (N > n):
        n = n * 10 + 9
        n = n / 10
    n = n * 10 + 9
    n = n / 10
    print(n)


if __name__ == "__main__":
    N = 1
    findNthNumber(N)
