#include <bits/stdc++.h>
using namespace std;
int totalWays(int N, int M, int X) {
    int dp[N+1][M+1];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for(int i=1; i<=N; i++) {
        for(int j=1; j<=M; j++) {
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
            if(j >= X) {
                dp[i][j] -= dp[i-1][j-X];
            }
        }
    }
    return dp[N][M];
}