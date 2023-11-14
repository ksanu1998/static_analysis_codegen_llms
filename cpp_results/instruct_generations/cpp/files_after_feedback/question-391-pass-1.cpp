#include <bits/stdc++.h>
using namespace std;
int minimalSteps(const string& s, int n) {
    int dp[n+1];
    dp[0] = 0;
    for (int i=1; i<=n; i++) {
        dp[i] = INT_MAX;
        for (int j=0; j<i; j++) {
            if (s[j] == s[i-1]) {
                dp[i] = min(dp[i], dp[j] + 1);
            }
        }
        dp[i] = min(dp[i], dp[i-1] + 1);
    }
    return dp[n];
}