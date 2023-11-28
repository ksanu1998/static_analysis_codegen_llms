#include <bits/stdc++.h> 
 using namespace std ;
 int countSubarray ( int arr [ ] , int n , int k ) {
int count = 0 ;
    for ( int i = 0 ; i < n ; i++ ) {
        int max_val = arr [ i ] ;
        for ( int j = i ; j < n ; j++ ) {
            if ( arr [ j ] > max_val )
                max_val = arr [ j ] ;
            if ( max_val > k )
                count++ ;
        }
    }
    return count ;
}