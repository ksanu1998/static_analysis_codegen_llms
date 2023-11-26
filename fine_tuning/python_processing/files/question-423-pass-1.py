arr = [100, 1000, 100, 1000, 1]
sum = [-1] * 10000


def maxSumWO3Consec(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    if n == 2:
        return max(arr[0], arr[1])

    if n == 3:
        return max(arr[0], arr[1], arr[2])

    for i in range(n):
        if i > 0 and i < n-1:
            if sum[i-1]!= -1:
                sum[i] = max(sum[i-1], arr[i] + sum[i-2])
            else:
                sum[i] = arr[i] + sum[i-1]
        else:
            sum[i] = arr[i]

    return sum[n-1]
