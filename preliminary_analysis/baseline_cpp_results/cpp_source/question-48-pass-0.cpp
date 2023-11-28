// Count pairs in an array containing at least one even value. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int CountPairs ( int arr [ ] , int n ) {
 
 int count = 0 ;
 for ( int i = 0 ; i < n ; i++ ) {
 
 for ( int j = i + 1 ; j < n ; j++ ) {
 
 if ( arr [ i ] % 2 == 0 && arr [ j ] % 2 == 0 ) {
 
 count++ ;
 }
 }
 }
 return count ;
 }
 int main ( ) {
 int arr [ ] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 } 