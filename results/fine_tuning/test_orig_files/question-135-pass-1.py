def findNthDigit(p, q, N):

def findNthDigit(p, q, N):
    n = p
    for i in range(N-1):
        n = n // q
    return str(n)[-1]
