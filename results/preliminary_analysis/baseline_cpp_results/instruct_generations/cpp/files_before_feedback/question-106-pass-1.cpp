#include <bits/stdc++.h> 
 using namespace std ;
 const int mod = 1000000007 ;
int countSubsets(int a[], int n) {
    int dp[n+1][3];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    dp[0][1] = 1;
    dp[0][2] = 1;

    for(int i=1; i<=n; i++) {
        for(int j=0; j<3; j++) {
            if(j == 0) {
                dp[i][j] = (dp[i-1][j] + dp[i-1][1] + dp[i-1][2]) % mod;
            } else if(j == 1) {
                dp[i][j] = (dp[i-1][j] + dp[i-1][0]) % mod;
            } else {
                dp[i][j] = (dp[i-1][j] + dp[i-1][1]) % mod;
            }
        }
    }

    int ans = 0;
    for(int i=0; i<3; i++) {
        ans = (ans + dp[n][i]) % mod;
    }

    return ans;
}