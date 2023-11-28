#include <bits/stdc++.h> 
 #define MAX  256 
 using namespace std ;
int numberofways(string A, string B, int N, int M) {
    int dp[N + 1][M + 1];
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            if (A[i - 1] == B[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[N][M];
}