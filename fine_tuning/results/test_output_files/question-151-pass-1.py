def nCr(n, r):
    if (r > n - r):
        r = n - r
    if (r == 0):
        return 1
    if (n == 1):
        return 1
    if (n == r):
        return 1
    if (n == 2 and r == 2):
        return 2
    if (n == 3 and r == 3):
        return 3
    if (n == 4 and r == 4):
        return 5
    if (n == 5 and r == 5):
        return 10
    if (n == 6 and r == 6):
        return 15
    if (n == 7 and r == 7):
        return 21
    if (n == 8 and r == 8):
        return 35
    if (n == 9 and r == 9):
        return 76
    if (n == 10 and r == 10):
        return 165
    if (n == 11 and r == 11):
        return 306
    if (n == 12 and r == 12):
        return 512
    if (n == 13 and r == 13):
        return 924
    if (n == 14 and r == 14):
        return 1760
    if (n == 15 and r == 15):
        return 3286
    if (n == 16 and r == 16):
        return 6303
    if (n == 17 and r == 17):
        return 12400
    if (n == 18 and r == 18):
        return 246
