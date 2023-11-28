// Minimize the sum of the array according the given condition. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void findMin ( int arr [ ] , int n ) {
 
    int min = arr [ 0 ] ;
    for ( int i = 1 ; i < n ; i++ ) {
        if ( arr [ i ] < min ) {
            min = arr [ i ] ;
        }
    }
    cout << "Minimum element is " << min << endl ;
 }
 int main ( ) {
    int arr [ ] = { 10, 20, 30, 40, 50 } 