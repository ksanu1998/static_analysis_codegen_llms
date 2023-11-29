def findNumUtil(res, a, aCount, b, bCount, n):

def findNumUtil(res, a, aCount, b, bCount, n):
    if aCount == 0 and bCount == 0:
        return res

    if aCount > 0:
        aCount -= 1
        res = res * 10 + a
    else:
        bCount -= 1
        res = res * 10 + b

    return findNumUtil(res, a, aCount, b, bCount, n)
