#include <bits/stdc++.h>
using namespace std;
int longest_subseq(int n, int k, const string& s) {
    int dp[n + 1][k + 1];
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            if (s[i - 1] - s[i - j] <= k) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + 1);
            }
        }
    }
    return dp[n][k];
}