// Form the Cubic equation from the given roots. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void findEquation ( int a , int b , int c ) {
 
     int d = ( b * b ) - ( 4 * a * c ) ;
     if ( d == 0 ) {
         cout << "The equation has only one root" << endl ;
         cout << "The root is " << -b / ( 2 * a ) << endl ;
     }
     else if ( d > 0 ) {
         cout << "The equation has two roots" << endl ;
         cout << "The roots are " << ( -b + sqrt ( d ) ) / ( 2 * a ) << " and " << ( -b - sqrt ( d ) ) / ( 2 * a ) << endl ;
     }
     else {
         cout << "The equation has no real roots" << endl ;
     }
 }
 int main ( ) {
     int a, b, c ;
     cout << "Enter the value of a : " ;
     cin >> a ;
     cout << "Enter the value of b : " ;
     cin >> b ;
     cout << "Enter the value of c : " ;
     cin >> c ;
     findEquation ( a, b, c ) ;
     return 0 ;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
