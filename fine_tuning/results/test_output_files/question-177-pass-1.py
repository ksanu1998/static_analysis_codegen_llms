def makeAP(arr, n):
    if (n == 1):
        return
    for (i = 1; i < n; i++)
        if (arr[i] - arr[i - 1]!= 1):
            arr[i] = arr[i - 1] + 1
    for (i = n - 2; i >= 0; i--)
        if (arr[i] - arr[i + 1]!= 1):
            arr[i] = arr[i + 1] + 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)
    makeAP(arr, n)
    print("Array after making it an Arithmetic Progression")
    for (i = 0; i < n; i++)
        print(arr[i], end=" ")
