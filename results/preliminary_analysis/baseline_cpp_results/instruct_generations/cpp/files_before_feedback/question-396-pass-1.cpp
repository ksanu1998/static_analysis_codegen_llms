#include <cstring> 
 #include <iostream> 
 int static const DP_s = 9 ;
int getNumStrictMonotone(int len) {
    int dp[len+1];
    memset(dp, 0, sizeof(dp));
    dp[0] = 1;
    for (int i = 1; i <= len; i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j] > 0 && (i - j) % (j + 1) == 0) {
                dp[i]++;
            }
        }
    }
    return dp[len];
}