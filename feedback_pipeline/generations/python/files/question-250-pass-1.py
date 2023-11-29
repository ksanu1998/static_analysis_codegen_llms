def getHermiteNumber(n):
    if n == 1:
        return 0
    else:
        return (2*n-1)*getHermiteNumber(n-1) + 1