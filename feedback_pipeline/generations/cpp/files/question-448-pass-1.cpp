#include <bits/stdc++.h> 
 using namespace std ;
 int LCSubStr ( string s , string t , int n , int m ) {
int dp[n+1][m+1];
    int result = 0;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            if(s[i-1] == t[j-1]){
                dp[i][j] = dp[i-1][j-1] + 1;
                result = max(result, dp[i][j]);
            }
            else{
                dp[i][j] = 0;
            }
        }
    }
    return result;
}