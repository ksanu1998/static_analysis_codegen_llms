// Proizvolov 's Identity. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int proizvolov ( int a [ ] , int b [ ] , int n ) {
 
 int i, j, k, prod = 1 ;
 
 for ( i = 0 ; i < n ; i++ ) {
 
 for ( j = 0 ; j < n ; j++ ) {
 
 for ( k = 0 ; k < n ; k++ ) {
 
 prod *= a [ i ] * b [ j ] * c [ k ] ;
 
 }
 
 }
 
 }
 
 return prod ;
 
 }
 
 int main ( ) {
 
 int a [ ] = { 1, 2, 3 }