// Mode in a stream of integers ( running integers ). 
 #include <bits/stdc++.h> 
 using namespace std ;
 void findMode ( int a [ ] , int n ) {
 
    int max_count = 1, max_element = a [ 0 ] ;
    int count = 1 ;
    for ( int i = 1 ; i < n ; i++ ) {
        if ( a [ i ] == a [ i - 1 ] ) {
            count++ ;
        }
        else {
            if ( count > max_count ) {
                max_count = count ;
                max_element = a [ i - 1 ] ;
            }
            count = 1 ;
        }
    }
    if ( count > max_count ) {
        max_count = count ;
        max_element = a [ n - 1 ] ;
    }
    cout << "Mode is " << max_element << " and it occurs " << max_count << " times " << endl ;
 }
 int main ( ) {
    int a [ ] = { 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5