def maxSum(n):
    if (n == 1):
        return 1
    else:
        return int((n * (n - 1) / 2) - 1 + n / 2)


n = 3
print(maxSum(n))
