def proizvolov(a, b, n):
    if (n == 0):
        print(a)
        return
    if (n == 1):
        print(b)
        return
    proizvolov(a, b, n - 1)
    proizvolov(a, b, n - 2)


if __name__ == "__main__":
    n = 4
    proizvolov(1, 2, n)
