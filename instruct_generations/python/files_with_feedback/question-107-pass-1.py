def convertToTernary(N):
    if N == 0:
        return "0"
    elif N % 3 == 1:
        return "1" + convertToTernary(N // 3)
    else:
        return "2" + convertToTernary(N // 3)
