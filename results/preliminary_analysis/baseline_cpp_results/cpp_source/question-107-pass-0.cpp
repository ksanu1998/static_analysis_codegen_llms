// Count of Subsets containing only the given value K. 
 #include <iostream> 
 using namespace std ;
 int count ( int arr [ ] , int N , int K ) {
 
 int count = 0 ;
 for ( int i = 0 ; i < N ; i++ ) {
 
 if ( arr [ i ] == K )
 count++ ;
 }
 return count ;
 }
 
 int main ( ) {
 
 int arr [ ] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 } 