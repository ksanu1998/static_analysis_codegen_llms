#include <bits/stdc++.h>
using namespace std;
const int n = 3;
int minFallingPathSum(int (&A)[n][n]) {
    int dp[n][n];
    for (int i = 0; i < n; i++) {
        dp[i][0] = A[i][0];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + A[i][j];
        }
    }
    int minSum = dp[n - 1][n - 1];
    for (int i = 0; i < n; i++) {
        minSum = min(minSum, dp[n - 1][i]);
    }
    return minSum;
}