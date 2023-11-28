def sum(x, n):
    if (n == 0):
        return 1
    y = sum(x, n - 1)
    y = (x * y) / (n + 1)
    return (y + sum(x, n))


if __name__ == "__main__":
    x = 2
    n = 5
    print(sum(x, n))
