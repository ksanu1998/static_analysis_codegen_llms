// Count the pairs in an array such that the difference between them and their indices is equal. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int countPairs ( int arr [ ] , int n ) {
 
    // Sort the array in increasing order
    sort ( arr, arr + n ) ;
 
    // Initialize result
    int res = 0 ;
 
    // Traverse the array
    for ( int i = 0 ; i < n - 1 ; i++ ) {
 
        // Find the difference between the current element and the next element
        int diff = arr [ i + 1 ] - arr [ i ] ;
 
        // If the difference is 1, then increment the result
        if ( diff == 1 )
            res++ ;
    }
 
    return res ;
 }
 
 // Driver code
 int main ( ) {
    int arr [ ] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 } 