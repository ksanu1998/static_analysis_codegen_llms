def NumberOfRectangles(n, m):
    if (n < 1 or m < 1):
        return 0
    if (n == 1 and m == 1):
        return 1
    if (n == 1):
        return m
    if (m == 1):
        return n
    return (n * (n - 1) / 2 * m + NumberOfRectangles(n - 2, m));


if __name__ == "__main__":
    n = 3
    m = 3
    print(NumberOfRectangles(n, m))
