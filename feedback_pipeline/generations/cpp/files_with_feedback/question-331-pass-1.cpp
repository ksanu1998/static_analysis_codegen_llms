#include <bits/stdc++.h>
using namespace std;
#define MAXI 50
int dp[MAXI][MAXI][MAXI * MAXI];
int n, m;
int minDifference(int x, int y, int k, vector<vector<int>> b, vector<vector<int>> c) {
    // Initialize the dp table
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            for (int l = 0; l <= k; l++) {
                dp[i][j][l] = INT_MAX;
            }
        }
    }
    // Initialize the base cases
    dp[0][0][0] = 0;
    for (int i = 1; i <= n; i++) {
        dp[i][0][0] = INT_MAX;
    }
    for (int j = 1; j <= m; j++) {
        dp[0][j][0] = INT_MAX;
    }
    // Fill in the dp table
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            for (int l = 1; l <= k; l++) {
                int minVal = INT_MAX;
                for (int m = 0; m < b[i][j]; m++) {
                    minVal = min(minVal, dp[i - 1][j][l - 1] + c[i][j][m]);
                }
                dp[i][j][l] = minVal;
            }
        }
    }
    // Find the minimum difference
    int minDiff = INT_MAX;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            for (int l = 0; l <= k; l++) {
                minDiff = min(minDiff, dp[i][j][l]);
            }
        }
    }
    return minDiff;
}