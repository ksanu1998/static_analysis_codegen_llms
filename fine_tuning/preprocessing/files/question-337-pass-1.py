'NEW_LINEdefcheckpossible(mask,arr,prefix,n,k):NEW_LINE'
 dp = [[0 for i in range(k + 1)]for i in range(n + 1)]
  dp[0][0] = 1
   for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(i - 1, -1, -1):
                if (dp[l][j - 1] and (((prefix[i] - prefix[l]) & mask) == mask)):
                    dp[i][j] = 1
                    break
    return dp[n][k]


def partition(arr, n, k):
    # Initialize the mask with all 1s
    mask = (1 << 31) - 1

    # Calculate the prefix sum of the array
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    # Call the check possible function
    return check_possible(mask, arr, prefix, n, k)
