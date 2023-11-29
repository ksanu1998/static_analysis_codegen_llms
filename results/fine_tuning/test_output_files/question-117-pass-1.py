def checkArray(a, b, n):
    if (n == 0):
        return 0
    if (a[0] == b[0]):
        return 0
    if (a[0] > b[0]):
        return -1
    if (a[n - 1] > b[n - 1]):
        return -1
    if (a[0] < b[0]):
        return 1
    if (a[n - 1] < b[n - 1]):
        return 1
    return 0


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    b = [1, 2, 3, 4, 5, 6]
    n = len(a)
    print(checkArray(a, b, n))
