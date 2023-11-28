def Max_Sum(arr1, arr2, n):
    dp = [[0 for i in range(2)]for j in range(n)]
    for i in range(n):
        if (i == 0):
            dp[i][0] = arr1[i]
            dp[i][1] = arr2[i]
            continue
        else:
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + arr1[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + arr2[i])
    return max(dp[n - 1][0], dp[n - 1][1])


if __name__ == '__main__':
    arr1 = [9, 3, 5, 7, 3]
    arr2 = [5, 8, 1, 4, 5]
    n = len(arr1)
    print(Max_Sum(arr1, arr2, n))
