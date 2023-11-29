def findNthDigit(p, q, N):
    if N < 1:
        return -1
    if p < q:
        return -1
    if N == 1:
        return p % q
    else:
        return findNthDigit(p // q, q, N - 1)
