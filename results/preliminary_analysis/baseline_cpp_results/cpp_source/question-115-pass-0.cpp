// Product of all Subarrays of an Array. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void product_subarrays ( int arr [ ] , int n ) {
 
    int i, j, prod ;
    for ( i = 0 ; i < n ; i++ ) {
        prod = 1 ;
        for ( j = i ; j < n ; j++ ) {
            prod *= arr [ j ] ;
            cout << prod << " " ;
        }
        cout << endl ;
    }
 }
 int main ( ) {
    int arr [ ] = { 1, 2, 3, 4, 5 } 