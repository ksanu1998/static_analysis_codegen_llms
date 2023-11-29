def findPrimes(arr, n):
    for (i in range(2, n + 1)):
        if (arr[i] == 0):
            print(i, end=" ")
    return


if __name__ == "__main__":
    arr = [1, 0, 1, 0, 1, 1, 0, 0, 1, 1]
    n = 10
    findPrimes(arr, n)
