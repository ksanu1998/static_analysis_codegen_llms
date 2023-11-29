#include <bits/stdc++.h>
using namespace std;
int maxSum(int tri[n][3], int n) {
    int dp[n][3];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            dp[i][j] = tri[i][j];
        }
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                if (j!= k) {
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + tri[i][j]);
                }
            }
        }
    }
    int max_sum = 0;
    for (int i = 0; i < 3; i++) {
        max_sum = max(max_sum, dp[n - 1][i]);
    }
    return max_sum;
}