def constructBinString(a, b, x):
    binary_string = ''
    while x > 0:
        binary_string = str(x % 2) + binary_string
        x //= 2
    return binary_string.zfill(a + b)
