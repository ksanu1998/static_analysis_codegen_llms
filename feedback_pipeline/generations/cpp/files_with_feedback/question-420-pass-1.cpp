#include <iostream>
using namespace std;
const int inf = 1000000000;
int minCost(const int a[], int n, int k) {
    int dp[n+1][k+1];
    for (int i=0; i<=n; i++) {
        for (int j=0; j<=k; j++) {
            dp[i][j] = inf;
        }
    }
    dp[0][0] = 0;
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=k; j++) {
            int cost = abs(a[i-1] - a[i]) * (j-1);
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + cost);
        }
    }
    return dp[n][k];
}