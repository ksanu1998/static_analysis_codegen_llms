import sys


def maxSubArraySum(a, n, k, i):
    if (i == 0):
        maxSum = 0
        for (i = 0; i < n; i++)
            maxSum += a[i]
        return maxSum

    if (i == n):
        return 0

    maxSum = maxSubArraySum(a, n, k, i + 1)
    if (i + k < n):
        maxSum = max(maxSum,
                     a[i] + maxSubArraySum(a, n, k, i + k + 1))
    return maxSum


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    n = len(a)
    k = 2
    print(maxSubArraySum(a, n, k, 0))
