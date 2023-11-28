def Golomb(n):
    if n == 1:
        return 1
    else:
        return (Golomb(n-1) + 1) * 2
