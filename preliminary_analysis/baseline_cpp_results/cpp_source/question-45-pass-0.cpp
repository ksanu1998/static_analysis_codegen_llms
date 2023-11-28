// Sum of series formed by difference between product and sum of N natural numbers. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int seriesSum ( int n ) {
 
    int sum = 0 ;
    for ( int i = 1 ; i <= n ; i++ ) {
        sum += ( i * ( i + 1 ) ) ;
    }
    return sum ;
 }
 
 int productSum ( int n ) {
 
    int sum = 0 ;
    for ( int i = 1 ; i <= n ; i++ ) {
        sum += ( i * ( n + 1 - i ) ) ;
    }
    return sum ;
 }
 
 int main ( ) {
 
    int n ;
    cin >> n ;
    cout << seriesSum ( n ) - productSum ( n ) << endl ;
    return 0 ;
 }
