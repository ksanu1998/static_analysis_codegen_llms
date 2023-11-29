#include <bits/stdc++.h>
using namespace std;
int MinOfCubedDP(int k) {
    int dp[k + 1];
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= k; i++) {
        dp[i] = min(dp[i - 1] + 1, dp[i - 2] + 2);
    }
    return dp[k];
}