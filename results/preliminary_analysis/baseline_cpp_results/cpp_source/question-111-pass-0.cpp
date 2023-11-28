// Count of greater elements for each element in the Array. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void countOfGreaterElements ( int arr [ ] , int n ) {
 
    // Create an array to store count of greater elements for each element in the Array. 
    int count [ n ] ;
    memset ( count, 0, sizeof ( count ) ) ;
 
    // Traverse the Array and update count of greater elements for each element in the Array. 
    for ( int i = 0 ; i < n ; i++ ) {
        for ( int j = i + 1 ; j < n ; j++ ) {
            if ( arr [ i ] < arr [ j ] )
                count [ i ]++ ;
        }
    }
 
    // Print the count of greater elements for each element in the Array. 
    for ( int i = 0 ; i < n ; i++ )
        cout << count [ i ] << " " ;
}
 
// Driver Code 
int main ( ) {
    int arr [ ] = { 1, 3, 4, 2, 5 } 