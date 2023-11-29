#include <bits/stdc++.h> 
 using namespace std ;
 void sumArray ( int arr [ ] , int n ) {
int sum = 0 ;
    for ( int i = 0 ; i < n ; i++ ) {
        sum += arr [ i ] ;
    }
    cout << "Sum of the array is : " << sum << endl ;
}

int main ( ) {
    int arr [ ] = { 1, 2, 3, 4, 5 } ;
    int n = sizeof ( arr ) / sizeof ( arr [ 0 ] ) ;
    sumArray ( arr, n ) ;
    return 0 ;
}