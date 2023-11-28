// Droll Numbers. 
 #include <bits/stdc++.h> 
 using namespace std ;
 bool isDroll ( int n ) {
 
     if ( n < 1 || n > 100 ) return false ;
     int sum = 0 ;
     while ( n > 0 ) {
         int d = n % 10 ;
         if ( d < 1 || d > 6 ) return false ;
         sum += d ;
         n /= 10 ;
     }
     return sum % 10 == 0 ;
 }
 int main ( ) {
     int n ;
     cin >> n ;
     while ( n-- ) {
         int x ;
         cin >> x ;
         if ( isDroll ( x ) ) cout << "YES" << endl ;
         else cout << "NO" << endl ;
     }
     