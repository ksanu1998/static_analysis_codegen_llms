def product(x):
    if x < 10:
        return x
    else:
        return x % 10 * product(x // 10)
