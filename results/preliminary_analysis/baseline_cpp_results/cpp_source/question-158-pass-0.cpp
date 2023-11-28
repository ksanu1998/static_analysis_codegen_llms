// Minimum cost to make all array elements equal. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int minCost ( int arr [ ] , int n ) {
 
 int dp [ n ] [ 2 ] ;
 dp [ 0 ] [ 0 ] = 0 ;
 dp [ 0 ] [ 1 ] = arr [ 0 ] ;
 
 for ( int i = 1 ; i < n ; i++ ) {
 
 dp [ i ] [ 0 ] = min ( dp [ i - 1 ] [ 0 ], dp [ i - 1 ] [ 1 ] ) + abs ( arr [ i ] - arr [ i - 1 ] ) ;
 dp [ i ] [ 1 ] = dp [ i - 1 ] [ 0 ] + arr [ i ] ;
 }
 
 return min ( dp [ n - 1 ] [ 0 ], dp [ n - 1 ] [ 1 ] ) ;
 }
 
 int main ( ) {
 int arr [ ] = { 1, 6, 10, 13, 11, 12 } 