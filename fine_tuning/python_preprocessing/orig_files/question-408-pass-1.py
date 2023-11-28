def maxSumWithK(a, n, k):
    maxSum = [0 for i in range(n)]
    maxSum[0] = a[0]
    curr_max = a[0]
    for i in range(1, n):
        curr_max = max(a[i], curr_max + a[i])
        maxSum[i] = curr_max
    sum = 0
    for i in range(k):
        sum += a[i]
    result = sum
    for i in range(k, n):
        sum = sum + a[i] - a[i - k]
        result = max(result, sum)
        result = max(result, sum + maxSum[i - k])
    return result


a = [1, 2, 3, -10, -3]
k = 4
n = len(a)
print(maxSumWithK(a, n, k))
