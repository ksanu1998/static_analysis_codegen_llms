#include <bits/stdc++.h> 
 using namespace std ;
int maxSum(int* arr, int k, int n) {
    int dp[n+1][k+1];
    for (int i=0; i<=n; i++) {
        for (int j=0; j<=k; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + arr[i-1]);
            }
        }
    }
    return dp[n][k];
}