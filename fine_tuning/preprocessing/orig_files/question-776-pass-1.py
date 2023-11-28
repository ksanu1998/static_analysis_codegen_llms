def truncMod(a, n):
    q = a // n
    return a - n * q


if __name__ == '__main__':
    a = 9
    b = 4
    print(a, "%", b, "=", truncMod(a, b))
    a = -9
    b = 4
    print(a, "%", b, "=", truncMod(a, b))
    a = 9
    b = -4
    print(a, "%", b, "=", truncMod(a, b))
    a = -9
    b = -4
    print(a, "%", b, "=", truncMod(a, b))
