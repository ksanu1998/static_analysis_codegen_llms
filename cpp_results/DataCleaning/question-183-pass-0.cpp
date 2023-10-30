// Bitwise AND of sub. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int closetAND ( int arr [ ] , int n , int k ) {
 
 int res = 0 ;
 for ( int i = 0 ; i < n ; i++ ) {
 
 res = res | arr [ i ] ;
 
 if ( __builtin_popcount ( res ) > k ) {
 
 res = res & ( ~ arr [ i ] ) ;
 
 }
 
 }
 
 return res ;
 
 }
 
 int main ( ) {
 
 int arr [ ] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 } 