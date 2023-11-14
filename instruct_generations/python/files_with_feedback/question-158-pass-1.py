import sys



def maxSubArraySum(a, n, k, i):
    if i == n:
        return 0
    else:
        max_sum = max(maxSubArraySum(a, n, k, i+1), a[i] + maxSubArraySum(a, n, k, i+k))
        return max_sum
