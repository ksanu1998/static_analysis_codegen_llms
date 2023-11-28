#include <bits/stdc++.h> 
 using namespace std ;
int subsetXOR(int arr[], int n, int K) {
    int dp[n+1][K+1];
    memset(dp, 0, sizeof(dp));
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=K; j++) {
            if(arr[i-1] <= j) {
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j];
            } else {
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    return dp[n][K];
}