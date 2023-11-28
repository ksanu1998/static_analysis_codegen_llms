arr = [100, 1000, 100, 1000, 1]
sum = [-1] * 10000


def maxSumWO3Consec(n):
    if (sum[n] != -1):
        return sum[n]
    if (n == 0):
        sum[n] = 0
        return sum[n]
    if (n == 1):
        sum[n] = arr[0]
        return sum[n]
    if (n == 2):
        sum[n] = arr[1] + arr[0]
        return sum[n]
    sum[n] = max(max(maxSumWO3Consec(n - 1),
                     maxSumWO3Consec(n - 2) + arr[n]),
                 arr[n] + arr[n - 1] + maxSumWO3Consec(n - 3))
    return sum[n]


if __name__ == "__main__":
    n = len(arr)
    print(maxSumWO3Consec(n))
