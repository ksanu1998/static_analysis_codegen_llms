def findNthDigit(p, q, N):
    if (N > p + q):
        print("N is greater than the sum of p and q")
        return
    if (N == 1):
        print(1)
        return
    if (N == p + q):
        print(0)
        return
    if (N > p):
        findNthDigit(p, q, N - p - 1)
    else:
        findNthDigit(p - 1, q, N)


if __name__ == "__main__":
    p = 1
    q = 2
    N = 3
    findNthDigit(p, q, N)
