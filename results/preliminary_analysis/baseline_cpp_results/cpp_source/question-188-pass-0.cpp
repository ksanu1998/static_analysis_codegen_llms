// Choose X such that ( A xor X ) + ( B xor X ) is minimized. 
 #include <iostream> 
 using namespace std ;
 int findX ( int A , int B ) {
 
 int x = 0 ;
 int min = A + B ;
 
 while ( x < min ) {
 
 if ( ( A ^ x ) + ( B ^ x ) < min ) {
 
 min = ( A ^ x ) + ( B ^ x ) ;
 
 }
 
 x++ ;
 
 }
 
 return x ;
 
 }
 
 int main ( ) {
 
 int A, B ;
 
 cin >> A >> B ;
 
 cout << findX ( A, B ) << endl ;
 
 return 0 ;
 
 }
