#include <bits/stdc++.h>
using namespace std;
int CountWays(int N, int M) {
    // Initialize the dp array
    int dp[N][M];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            dp[i][j] = -1;
        }
    }
    // Initialize the first row and column
    dp[0][0] = 1;
    for (int i = 1; i < N; i++) {
        dp[i][0] = 1;
    }
    for (int j = 1; j < M; j++) {
        dp[0][j] = 1;
    }
    // Fill the rest of the dp array
    for (int i = 1; i < N; i++) {
        for (int j = 1; j < M; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    // Return the last element of the dp array
    return dp[N - 1][M - 1];
}