def convertToTernary(N):
    if (N == 0):
        return 0
    res = 0
    while (N > 0):
        res = (res * 10) + (N % 3)
        N //= 3
    return res


if __name__ == "__main__":
    N = 12
    print(convertToTernary(N))
