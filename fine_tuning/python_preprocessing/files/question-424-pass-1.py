def maxSumPairWithDifferenceLessThanK(arr, N, k):
    max_sum = 0
    for i in range(N):
        for j in range(i+1, N):
            diff = abs(arr[i] - arr[j])
            if diff <= k:
                max_sum = max(max_sum, arr[i] + arr[j])
    return max_sum
