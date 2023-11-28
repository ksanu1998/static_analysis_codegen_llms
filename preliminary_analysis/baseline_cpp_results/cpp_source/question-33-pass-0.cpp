// Count of distinct index pair ( i , j ) such that element sum of First Array is greater. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int numberOfPairs ( int * a , int * b , int n ) {
 
    int count = 0 ;
    for ( int i = 0 ; i < n ; i++ ) {
        for ( int j = i + 1 ; j < n ; j++ ) {
            if ( a[i] + b[j] > a[j] + b[i] ) {
                count++ ;
            }
        }
    }
    return count ;
 }
 int main ( ) {
    int n ;
    cin >> n ;
    int a[n], b[n] ;
    for ( int i = 0 ; i < n ; i++ ) {
        cin >> a[i] ;
    }
    