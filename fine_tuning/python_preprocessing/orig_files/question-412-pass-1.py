def lis(arr, n):
    result = 0
    lis = [0 for i in range(n)]
    for i in range(n):
        lis[i] = 1
    for i in range(1, n):
        for j in range(i):
            if (arr[i] > arr[j] and lis[i] < lis[j] + 1):
                lis[i] = lis[j] + 1
    for i in range(n):
        if (result < lis[i]):
            result = lis[i]
    return result


def minimumNumberOfDeletions(arr, n):
    len = lis(arr, n)
    return (n - len)


arr = [30, 40, 2, 5, 1, 7, 45, 50, 8]
n = len(arr)
print("Minimum number of deletions = ", minimumNumberOfDeletions(arr, n))
