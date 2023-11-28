#include <bits/stdc++.h>
using namespace std;
const int MOD = 1000000007;
int countWays(int n) {
    int dp[n + 1];
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    }
    return dp[n];
}