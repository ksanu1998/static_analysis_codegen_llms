#include <bits/stdc++.h> 
 using namespace std ;
 int CntDivbyX ( int arr [ ] , int n , int x ) {
int count = 0 ;
    for ( int i = 0 ; i < n ; i++ ) {
        if ( arr [ i ] % x == 0 )
            count++ ;
    }
    return count ;
}