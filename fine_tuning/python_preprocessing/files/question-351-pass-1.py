def maxSum(arr, k, n):
    if k > n:
        return 0
    if k == 1:
        return arr[0]
    if k == n:
        return max(arr)
    return max(arr[i] + maxSum(arr[i+1:], k-1, n-i-1), maxSum(arr, k, n-1))
