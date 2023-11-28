def printTheArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
    print()


def generateAllBinaryStrings(n, arr, i):
    if i == n:
        printTheArray(arr, n)
        return
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)


if __name__ == "__main__":
    n = 4
    arr = [None] * n
    generateAllBinaryStrings(n, arr, 0)
