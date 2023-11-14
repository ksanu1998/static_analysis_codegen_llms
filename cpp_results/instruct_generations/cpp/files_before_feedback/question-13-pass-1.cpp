#include <iostream> 
 using namespace std ;
 void minChocolates ( int A [ ] , int N ) {
// Sort the array in non-decreasing order
    sort ( A, A + N ) ;

    // Initialize variables
    int i = 0, j = N - 1, count = 0 ;

    // Loop through the array and find the minimum number of chocolates
    // that can be distributed such that no two children get the same number of chocolates
    while ( i < j ) {
        count += ( j - i ) ;
        i++, j-- ;
    }

    // Print the minimum number of chocolates that can be distributed
    cout << count << endl ;
}

int main ( ) {
    int N ;
    cin >> N ;
    int A [ N ] ;
    for ( int i = 0 ; i < N ; i++ ) {
        cin >> A [ i ] ;
    }
    minChocolates ( A, N ) ;
    return 0 ;
}