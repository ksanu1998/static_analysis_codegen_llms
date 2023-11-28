def isSumEqual(ar, n):
    if (ar[0] == 0):
        return 0
    if (ar[n - 1] == 0):
        return 1
    if (ar[n - 1] < ar[0]):
        return 0
    if (ar[n - 1] == ar[0]):
        return 1
    if (ar[n - 1] > ar[0]):
        return 2


if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 10
    print(isSumEqual(ar, n))
