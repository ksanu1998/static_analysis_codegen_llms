// Count of distinct index pair ( i , j ) such that element sum of First Array is greater. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int count_pairs ( int a [ ] , int b [ ] , int N ) {
 
    int count = 0 ;
    for ( int i = 0 ; i < N ; i++ ) {
        for ( int j = 0 ; j < N ; j++ ) {
            if ( a [ i ] + b [ j ] > 0 ) {
                count++ ;
            }
        }
    }
    return count ;
}
int main ( ) {
    int N ;
    cin >> N ;
    int a [ N ], b [ N ] ;
    for ( int i = 0 ; i < N ; i++ ) {
        cin >> a [ i ] ;
    }
    