#include <bits/stdc++.h>
using namespace std;
int KnapSack(const int val[], const int wt[], int n, int W) {
    int dp[n+1][W+1];
    for (int i=0; i<=n; i++) {
        for (int j=0; j<=W; j++) {
            if (i==0 || j==0) {
                dp[i][j] = 0;
            } else if (wt[i-1] > j) {
                dp[i][j] = dp[i-1][j];
            } else {
                dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i-1][j-wt[i-1]]);
            }
        }
    }
    return dp[n][W];
}