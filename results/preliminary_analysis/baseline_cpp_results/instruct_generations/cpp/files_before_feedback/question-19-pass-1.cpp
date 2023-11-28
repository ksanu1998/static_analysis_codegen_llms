#include <bits/stdc++.h> 
 using namespace std ;
 void findMode ( int a [ ] , int n ) {
// Create a map to store the count of each element
    map < int, int > count ;
    
    // Initialize the mode to -1
    int mode = -1 ;
    
    // Iterate through the array
    for ( int i = 0 ; i < n ; i++ ) {
        // If the current element is not present in the map, insert it with count 1
        if ( count.find ( a [ i ] ) == count.end () ) {
            count [ a [ i ] ] = 1 ;
        }
        // If the current element is already present in the map, increment its count
        else {
            count [ a [ i ] ]++ ;
        }
    }
    
    // Find the element with maximum count
    for ( auto it = count.begin () ; it!= count.end () ; it++ ) {
        if ( it->second > count [ mode ] ) {
            mode = it->first ;
        }
    }
    
    // Print the mode
    cout << "Mode: " << mode << endl ;
}

int main ( ) {
    int n ;
    cout << "Enter the number of elements: " ;
    cin >> n ;
    int a [ n ] ;
    cout << "Enter the elements: " ;
    for ( int i = 0 ; i < n ; i++ ) {
        cin >> a [ i ] ;
    }
    findMode ( a, n ) ;
    return 0 ;
}