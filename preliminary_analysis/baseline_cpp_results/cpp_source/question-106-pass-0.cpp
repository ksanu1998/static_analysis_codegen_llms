// Number of subsets with same AND , OR and XOR values in an Array. 
 #include <bits/stdc++.h> 
 using namespace std ;
 const int mod = 1000000007 ;
 int countSubsets ( int a [ ] , int n ) {
 
    int dp [ n + 1 ] [ 3 ] ;
    memset ( dp, 0, sizeof ( dp ) ) ;
    dp [ 0 ][ 0 ] = 1 ;
    dp [ 0 ][ 1 ] = 1 ;
    dp [ 0 ][ 2 ] = 1 ;
    for ( int i = 1 ; i <= n ; i++ ) {
        dp [ i ][ 0 ] = ( dp [ i - 1 ][ 0 ] + dp [ i - 1 ][ 1 ] ) % mod ;
        dp [ i ][ 1 ] = ( dp [ i - 1 ][ 0 ] + dp [ i - 1 ][ 2 ] ) % mod ;
        dp [ i ][ 2 ] = ( dp [ i - 1 ][ 1 ] + dp [ i - 1 ][ 2 ] ) % mod ;
    }
    return ( dp [ n ][ 0 ] + dp [ n ][ 1 ] + dp [ n ][ 2 ] ) % mod ;
 }
 int main ( ) {
    int t ;
    cin >> t ;
    while ( t-- ) {
        int n ;
        cin >> n ;
        int a [ n ] ;
        for ( int i = 0 ; i < n ; i++ ) {
            cin >> a [ i ] ;
        }
        