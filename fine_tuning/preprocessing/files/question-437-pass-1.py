MAX = 1000
dp = [[-1 for i in range(MAX)]for i in range(MAX)]


def minSizeRec(arr, low, high, k):if low > high:
        return 0
    if dp[low][high]!= -1:
        return dp[low][high]
    if k == 0:
        return minSizeRec(arr, low + 1, high, k)
    min_size = float('inf')
    for i in range(low, high + 1):
        min_size = min(min_size, 1 + minSizeRec(arr, low, i - 1, k - 1) + minSizeRec(arr, i + 1, high, k))
    dp[low][high] = min_size
    return min_size


def minSize(arr, k):
    return minSizeRec(arr, 0, len(arr) - 1, k)


# Test case 1:
arr = [1, 2, 3, 4, 5]
k = 2
print(minSize(arr, k))
# Test case 2:
arr = [1, 2, 3, 4, 5, 6]
k = 3
print(minSize(arr, k))
# Test case 3:
arr = [1, 2, 3, 4, 5, 6, 7]
k = 4
print(minSize(arr, k))
# Test case 4:
arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 5
print(minSize(arr, k))
# Test case 5:
arr = [1, 2, 3, 4
