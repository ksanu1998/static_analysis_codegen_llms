#include <bits/stdc++.h> 
 using namespace std ;
int countWays(int N) {
    int dp[N + 1];
    dp[0] = 1;
    for (int i = 1; i <= N; i++) {
        dp[i] = 0;
        for (int j = 1; j <= i; j++) {
            dp[i] += dp[i - j];
        }
    }
    return dp[N];
}