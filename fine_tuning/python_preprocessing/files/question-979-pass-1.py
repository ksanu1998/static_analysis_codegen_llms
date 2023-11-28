def power(x, y, p):
    if y == 0:
        return 1
    else:
        return (x * power(x, y-1, p)) % p
