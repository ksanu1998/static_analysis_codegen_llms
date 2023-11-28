def maxSum(n):
    if n < 1:
        return 0
    else:
        return max(n, maxSum(n-1) + abs(n-1))
