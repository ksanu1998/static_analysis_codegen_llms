#include <bits/stdc++.h> 
 using namespace std ;
int findMinimumCost(int n, int x, int y) {
    int dp[n+1];
    dp[0] = 0;
    for (int i=1; i<=n; i++) {
        dp[i] = INT_MAX;
        for (int j=1; j<=i; j++) {
            int cost = dp[i-j] + abs(x-j) + abs(y-j);
            dp[i] = min(dp[i], cost);
        }
    }
    return dp[n];
}