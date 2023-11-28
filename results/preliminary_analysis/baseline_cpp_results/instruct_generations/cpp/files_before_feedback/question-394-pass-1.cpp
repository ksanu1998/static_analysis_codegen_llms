#include <bits/stdc++.h> 
 using namespace std ;
 #define N  1000 
 long long arrangeBraces ( int n , int pos [ ] , int k ) {
[CPP]
long long arrangeBraces(int n, int pos[], int k) {
    long long dp[n + 1][k + 1];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            if (pos[i - 1] == j) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD;
            }
        }
    }
    return dp[n][k];
}