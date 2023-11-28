// Check if the number is even or odd whose digits and base ( radix ) is given. 
 #include <iostream> 
 using namespace std ;
 bool isEven ( int arr [ ] , int n , int r ) {
 
    int sum = 0 ;
    for ( int i = 0 ; i < n ; i++ ) {
        sum += arr [ i ] ;
    }
    if ( sum % r == 0 )
        return true ;
    else
        return false ;
 }
 int main ( ) {
    int arr [ ] = { 1, 2, 3, 4, 5 } 