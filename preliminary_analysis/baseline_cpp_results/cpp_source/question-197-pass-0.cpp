// Length of the smallest number which is divisible by K and formed by using 1 's only. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int numLen ( int K ) {
 
     int len = 0 ;
     while ( K % 2 == 0 ) {
         K /= 2 ;
         len++ ;
     }
     return len ;
 }
 int main ( ) {
     int T ;
     cin >> T ;
     while ( T-- ) {
         int K ;
         cin >> K ;
         int len = numLen ( K ) ;
         if ( len == 0 ) {
             cout << 1 << endl ;
         }
         