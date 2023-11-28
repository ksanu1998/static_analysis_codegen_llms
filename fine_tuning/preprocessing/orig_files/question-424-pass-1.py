def maxSumPairWithDifferenceLessThanK(arr, N, k):
    maxSum = 0
    arr .sort()
    i = N - 1
    while (i > 0):
        if (arr[i] - arr[i - 1] < k):
            maxSum += arr[i]
            maxSum += arr[i - 1]
            i -= 1
        i -= 1
    return maxSum


arr = [3, 5, 10, 15, 17, 12, 9]
N = len(arr)
K = 4
print(maxSumPairWithDifferenceLessThanK(arr, N, K))
