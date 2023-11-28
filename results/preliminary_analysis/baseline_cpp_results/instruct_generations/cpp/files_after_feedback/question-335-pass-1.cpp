#include <bits/stdc++.h>
using namespace std;
const int MOD = 1000000007;
int number_of_ways(const int arr[], int n, int k) {
    int dp[k+1];
    dp[0] = 1;
    for(int i=1; i<=k; i++) {
        for(int j=0; j<n; j++) {
            if(arr[j] >= i) {
                dp[i] = (dp[i] + dp[i-arr[j]]) % MOD;
            }
        }
    }
    return dp[k];
}