#include <bits/stdc++.h>
using namespace std;
int subsetXOR(const int arr[], int n, int k) {
    int dp[n+1][k+1];
    memset(dp, 0, sizeof(dp));
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=k; j++) {
            if(arr[i-1] == j) {
                dp[i][j] = 1;
            } else {
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]];
            }
        }
    }
    return dp[n][k];
}