#include <bits/stdc++.h> 
 using namespace std ;
int countWays(int arr[], int m, int N) {
    int dp[N+1];
    dp[0] = 1;
    for(int i=1; i<=N; i++) {
        for(int j=0; j<m; j++) {
            if(arr[j] <= i) {
                dp[i] += dp[i-arr[j]];
            }
        }
    }
    return dp[N];
}