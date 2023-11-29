#include <bits/stdc++.h> 
 using namespace std ;
int MinimumCost(int a[], int n, int x) {
    int dp[n+1][x+1];
    for (int i=0; i<=n; i++) {
        for (int j=0; j<=x; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            } else if (a[i-1] <= j) {
                dp[i][j] = min(dp[i-1][j-a[i-1]] + a[i-1], dp[i-1][j]);
            } else {
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    return dp[n][x];
}