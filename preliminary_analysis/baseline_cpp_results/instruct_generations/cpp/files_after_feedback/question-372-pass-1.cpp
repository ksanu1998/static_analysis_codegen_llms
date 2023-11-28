#include <bits/stdc++.h>
using namespace std;
#define N 100
const int n = 3, m = 4;
int maxPlus(int arr[n][m]) {
    int dp[n][m];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i == 0 && j == 0) {
                dp[i][j] = arr[i][j];
            } else if (i == 0) {
                dp[i][j] = dp[i][j - 1] + arr[i][j];
            } else if (j == 0) {
                dp[i][j] = dp[i - 1][j] + arr[i][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + arr[i][j];
            }
        }
    }
    return dp[n - 1][m - 1];
}