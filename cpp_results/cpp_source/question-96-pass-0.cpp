// Unique element in an array where all elements occur K times except one. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int findUniqueElements ( int arr [ ] , int N , int K ) {
 
    // Create a frequency array of size 100000
    int freq [ 100000 ] ;
    for ( int i = 0 ; i < 100000 ; i++ )
        freq [ i ] = 0 ;
 
    // Fill the frequency array
    for ( int i = 0 ; i < N ; i++ )
        freq [ arr [ i ] ]++ ;
 
    // Find the element that occurs K times
    for ( int i = 0 ; i < 100000 ; i++ )
        if ( freq [ i ] == K )
            return i ;
 
    return -1 ;
 }
 
 int main ( ) {
    int arr [ ] = { 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 