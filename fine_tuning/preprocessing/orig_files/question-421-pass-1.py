def countSubarray(arr, n, k):
    s = 0
    i = 0
    while (i < n):
        if (arr[i] > k):
            i = i + 1
            continue
        count = 0
        while (i < n and arr[i] <= k):
            i = i + 1
            count = count + 1
        s = s + ((count * (count + 1)) // 2)
    return (n * (n + 1) // 2 - s)


arr = [1, 2, 3]
k = 2
n = len(arr)
print(countSubarray(arr, n, k))
