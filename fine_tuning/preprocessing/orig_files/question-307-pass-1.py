def sum(x, y, n):
    sum1 = ((x ** 2) * (x ** (2 * n) - 1)) // (x ** 2 - 1)
    sum2 = (x * y * (x ** n * y ** n - 1)) // (x * y - 1)
    return (sum1 + sum2)


if __name__ == '__main__':
    x = 2
    y = 2
    n = 2
    print(sum(x, y, n))
