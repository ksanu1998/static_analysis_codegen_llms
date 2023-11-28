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


def Partition (arr, n, k):
    prefix = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        prefix [i] = prefix [i - 1] + arr [i]
    LOGS = 20
    ans = 0
    for i in range(LOGS, -1, -1):
        if (checkpossible (ans | (1 << i ), arr , prefix , n , k )):
            ans = ans | (1 << i)
    return ans
arr = [0 , 1 , 2 , 7 , 10 , 23 ,21 ,6 ,8 ,7 ,3 ]
k = 2
n = len(arr) - 1
print(Partition (arr, n, k))
