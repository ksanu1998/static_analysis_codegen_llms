def findNDigitNums(n):
    out = []
    findNDigitNumsUtil(n, out, 0, 0, 0)
    return out
