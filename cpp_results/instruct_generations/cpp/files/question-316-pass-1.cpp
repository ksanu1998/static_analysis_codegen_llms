#include <bits/stdc++.h> 
 using namespace std ;
int countSubsets(int N) {
    int dp[N+1];
    dp[0] = 1;
    for (int i=1; i<=N; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[N];
}