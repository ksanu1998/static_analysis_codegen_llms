// Minimum possible value of ( i * j ) % 2019. 
 #include <bits/stdc++.h> 
 using namespace std ;
 const int MOD = 2019 ;
 int min_modulo ( int l , int r ) {
 
    int min = 0 ;
    for ( int i = l ; i <= r ; i++ ) {
        for ( int j = l ; j <= r ; j++ ) {
            int x = ( i * j ) % MOD ;
            if ( x < min ) {
                min = x ;
            }
        }
    }
    return min ;
 }
 
 int main ( ) {
    int l = 1, r = 1000000 ;
    cout << min_modulo ( l, r ) << endl ;
    return 0 ;
 }
