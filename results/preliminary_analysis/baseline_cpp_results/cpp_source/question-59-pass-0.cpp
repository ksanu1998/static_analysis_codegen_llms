// Find two numbers whose difference of fourth power is equal to N. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void solve ( int n ) {
 
     int a, b ;
     for ( int i = 1 ; i <= n ; i++ ) {
         for ( int j = i + 1 ; j <= n ; j++ ) {
             int diff = pow ( i, 4 ) - pow ( j, 4 ) ;
             if ( diff == n ) {
                 a = i ;
                 b = j ;
                 break ;
             }
         }
     }
     cout << a << " " << b << endl ;
 }
 int main ( ) {
     int t ;
     cin >> t ;
     while ( t-- ) {
         int n ;
         cin >> n ;
         solve ( n ) ;
     }
     