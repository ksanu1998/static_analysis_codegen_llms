import random
a, b = None, None


def Partition(arr, l, r):
    lst = arr[r]
    i = l
    j = l
    while (j < r):
        if (arr[j] < lst):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def randomPartition(arr, l, r):
    n = r - l + 1
    pivot = random .randrange(1, 100) % n
    arr[l + pivot], arr[r] = arr[r], arr[l + pivot]
    return Partition(arr, l, r)


def MedianUtil(arr, l, r, k, a1, b1):
    global a, b
    if (l <= r):
        partitionIndex = randomPartition(arr, l, r)
        if (partitionIndex == k):
            b = arr[partitionIndex]
            if (a1 != -1):
                return
        elif (partitionIndex == k - 1):
            a = arr[partitionIndex]
            if (b1 != -1):
                return
        if (partitionIndex >= k):
            return MedianUtil(arr, l, partitionIndex - 1, k, a, b)
        else:
            return MedianUtil(arr, partitionIndex + 1, r, k, a, b)
    return


def findMedian(arr, n):
    global a
    global b
    a = -1
    b = -1
    if (n % 2 == 1):
        MedianUtil(arr, 0, n - 1, n // 2, a, b)
        ans = b
    else:
        MedianUtil(arr, 0, n - 1, n // 2, a, b)
        ans = (a + b) // 2
    print("Median = ", ans)


arr = [12, 3, 5, 7, 4, 19, 26]
n = len(arr)
findMedian(arr, n)
