def power(x, y, p):
    if (y == 0):
        return 1
    if (y == 1):
        return (x % p)
    if (y == 2):
        return ((x * x) % p)
    if (y == 3):
        return ((x * x * x) % p)
    if (y == 4):
        return ((x * x) % p)
    if (y == 5):
        return ((x * x * x * x * x) % p)
    if (y == 6):
        return ((x * x * x * x) % p)
    if (y == 7):
        return ((x * x * x * x * x * x) % p)
    if (y == 8):
        return ((x * x * x) % p)
    if (y == 9):
        return ((x * x * x * x * x) % p)
    if (y == 10):
        return ((x * x * x * x * x * x * x) % p)
    if (y == 11):
        return ((x * x * x * x * x * x * x * x) % p)
    if (y == 12):
        return ((x * x * x * x * x) % p)
    if (y == 13):
        return ((x * x * x * x * x * x * x) % p)
    if (y == 14):
        return ((x * x * x * x * x * x * x * x) % p)
    if (y == 15):
        return ((x * x * x * x * x * x * x * x * x) % p)
    if (y == 16):
        return ((x * x * x * x *
