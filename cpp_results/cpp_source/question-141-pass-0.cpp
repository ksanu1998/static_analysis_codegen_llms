// Cake Distribution Problem. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int cntCakes ( int n , int m ) {
 
 	int dp[n+1][m+1];
 	for ( int i = 0 ; i <= n ; i++ ) {
 		for ( int j = 0 ; j <= m ; j++ ) {
 			if ( i == 0 || j == 0 ) {
 				dp[i][j] = 0;
 			}
 			else if ( i == 1 ) {
 				dp[i][j] = j;
 			}
 			else if ( j == 1 ) {
 				dp[i][j] = i;
 			}
 			else {
 				dp[i][j] = max ( dp[i-1][j], dp[i][j-1] );
 			}
 		}
 	}
 	return dp[n][m];
 }
 
 int main ( ) {
 	int n, m ;
 	cin >> n >> m ;
 	cout << cntCakes ( n, m ) << endl;
 	return 0;
 }
