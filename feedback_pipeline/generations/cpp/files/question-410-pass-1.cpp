#include <bits/stdc++.h> 
 using namespace std ;
 const int MAX = 300 ;
 int dp [ MAX ] [ MAX ] ;
int minimumSquares(int m, int n) {
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == j) {
                dp[i][j] = 1;
            } else if (i > j) {
                dp[i][j] = dp[i - j][j] + 1;
            } else {
                dp[i][j] = dp[i][j - i] + 1;
            }
        }
    }
    return dp[m][n];
}