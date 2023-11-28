// Compare sum of first N. 
 #include <iostream> 
 using namespace std ;
 bool isSumEqual ( int ar [ ] , int n ) {
 
 int sum = 0 ;
 for ( int i = 0 ; i < n ; i++ )
 sum += ar [ i ] ;
 
 int sum1 = 0 ;
 for ( int i = n ; i < 2 * n ; i++ )
 sum1 += ar [ i ] ;
 
 if ( sum == sum1 )
 return true ;
 else
 return false ;
 }
 
 int main ( ) {
 int ar [ ] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 } 