#include <bits/stdc++.h> 
 using namespace std ;
 
long long NumberofWays ( int n ) {
    long long dp[n+1][n+1];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for(int i = 1; i <= n; i++) {
        for(int j = 0; j <= i; j++) {
            if(j > 0) {
                dp[i][j] += dp[i-1][j-1];
            }
            if(j < i) {
                dp[i][j] += dp[i-1][j];
            }
        }
    }
    return dp[n][n];
}