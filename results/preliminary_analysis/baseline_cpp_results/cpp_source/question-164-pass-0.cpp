// Probability that a N digit number is palindrome. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void solve ( int n ) {
 
    int dp[n+1][n+1];
    for ( int i = 0 ; i <= n ; i++ ) {
        for ( int j = 0 ; j <= n ; j++ ) {
            if ( i == 0 || j == 0 ) {
                dp[i][j] = 1;
            }
            else if ( i == j ) {
                dp[i][j] = 1;
            }
            else {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
    }
    cout << dp[n][n] << endl;
 }
 int main ( ) {
    int n;
    cin >> n;
    solve ( n );
    return 0;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
