// Find the largest number that can be formed by changing at most K digits. 
 #include <iostream> 
 using namespace std ;
 string findMaximumNum ( string str , int n , int k ) {
 
    int len = str.length() ;
    int dp[len+1][k+1] ;
    for ( int i = 0 ; i <= len ; i++ ) {
        for ( int j = 0 ; j <= k ; j++ ) {
            if ( i == 0 ) {
                dp[i][j] = 0 ;
            }
            else if ( j == 0 ) {
                dp[i][j] = 1 ;
            }
            else if ( j == 1 ) {
                dp[i][j] = 1 ;
            }
            else if ( i == 1 ) {
                dp[i][j] = 1 ;
            }
            else {
                dp[i][j] = max ( dp[i-1][j], dp[i-1][j-1] ) ;
            }
        }
    }
    int max_val = 0 ;
    int max_len = 0 ;
    for ( int i = 0 ; i <= len ; i++ ) {
        for ( int j = 0 ; j <= k ; j++ ) {
            if ( dp[i][j] > max_val ) {
                max_val = dp[i][j] ;
                max_len = i ;
            }
        }
    }
    return str.substr(0,max_len) ;
 }
 int main() {
    string str ;
    cin >> str ;
    int n, k ;
    cin >> n >> k ;
    cout << findMaximumNum ( str, n, k ) ;
    return 0 ;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
