MOD = 1000000007


def number_of_ways(arr, n, k):
    if (k == 1):
        return 1
    dp = [-1] * (k + 1)
    for i in range(n):
        dp[arr[i]] = 0
    dp[0] = 1
    dp[1] = 1 if (dp[1] == -1)else dp[1]
    for i in range(2, k + 1):
        if (dp[i] == 0):
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= MOD
    return dp[k]


if __name__ == "__main__":
    arr = [3]
    n = len(arr)
    k = 6
    print(number_of_ways(arr, n, k))
