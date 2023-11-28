#include <bits/stdc++.h> 
 using namespace std ;
 void possibleEqualArray ( int A [ ] , int N ) {
for ( int i = 0 ; i < N - 1 ; i++ ) {
        A [ i ] = A [ i ] ^ A [ i + 1 ] ;
    }
    A [ N - 1 ] = A [ N - 1 ] ^ A [ 0 ] ;
}

int main ( ) {
    int A [ ] = { 1, 2, 3, 4, 5 } ;
    possibleEqualArray ( A, 5 ) ;
    for ( int i = 0 ; i < 5 ; i++ ) {
        cout << A [ i ] << " " ;
    }
    return 0 ;
}