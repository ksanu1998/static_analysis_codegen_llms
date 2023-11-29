#include <bits/stdc++.h> 
 using namespace std ;
 int maxPresum ( vector < int > a , vector < int > b ) {
int n = a.size();
    int m = b.size();
    vector < int > c ( n + m );
    for ( int i = 0 ; i < n ; i++ ) {
        c[i] = a[i];
    }
    for ( int i = 0 ; i < m ; i++ ) {
        c[i + n] = b[i];
    }
    int max_sum = 0;
    for ( int i = 0 ; i < n + m ; i++ ) {
        if ( i == 0 ) {
            max_sum = c[i];
        } else {
            max_sum = max ( max_sum, c[i] + c[i - 1] );
        }
    }
    return max_sum;
}