def printEqualModNumbers(arr, n):
    arr .sort()
    d = arr[n - 1] - arr[0]
    if (d == 0):
        print("Infinite solution")
        return
    v = []
    i = 1
    while (i * i <= d):
        if (d % i == 0):
            v .append(i)
            if (i != d / i):
                v .append(d / i)
        i += 1
    for i in range(len(v)):
        temp = arr[0] % v[i]
        j = 1
        while (j < n):
            if (arr[j] % v[i] != temp):
                break
            j += 1
        if (j == n):
            print(v[i], end=" ")


arr = [38, 6, 34]
printEqualModNumbers(arr, len(arr))
