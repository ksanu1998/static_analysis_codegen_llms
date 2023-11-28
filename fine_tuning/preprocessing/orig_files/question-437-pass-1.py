MAX = 1000
dp = [[-1 for i in range(MAX)]for i in range(MAX)]


def minSizeRec(arr, low, high, k):
    if dp[low][high] != -1:
        return dp[low][high]
    if (high - low + 1) < 3:
        return (high - low + 1)
    res = 1 + minSizeRec(arr, low + 1, high, k)
    for i in range(low + 1, high):
        for j in range(i + 1, high + 1):
            if (
                arr[i] == (
                    arr[low] +
                    k) and arr[j] == (
                    arr[low] +
                    2 *
                    k) and minSizeRec(
                    arr,
                    low +
                    1,
                    i -
                    1,
                    k) == 0 and minSizeRec(
                    arr,
                    i +
                    1,
                    j -
                    1,
                    k) == 0):
                res = min(res, minSizeRec(arr, j + 1, high, k))
    dp[low][high] = res
    return res


def minSize(arr, n, k):
    dp = [[-1 for i in range(MAX)]for i in range(MAX)]
    return minSizeRec(arr, 0, n - 1, k)


if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6, 4]
    n = len(arr)
    k = 1
    print(minSize(arr, n, k))
