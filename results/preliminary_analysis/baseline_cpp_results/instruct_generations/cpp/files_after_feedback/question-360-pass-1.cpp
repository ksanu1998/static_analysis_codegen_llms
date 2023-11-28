#include <bits/stdc++.h>
using namespace std;
#define N 3
int maxPathSum(int tri[N][N]) {
    int dp[N][N];
    for (int i = 0; i < N; i++) {
        dp[i][0] = tri[i][0];
    }
    for (int i = 1; i < N; i++) {
        for (int j = 1; j < N; j++) {
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + tri[i][j];
        }
    }
    int maxSum = dp[N - 1][N - 1];
    for (int i = 0; i < N; i++) {
        maxSum = max(maxSum, dp[N - 1][i]);
    }
    return maxSum;
}
int main() {
    int tri[N][N] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    cout << maxPathSum(tri) << endl;
    return 0;
}