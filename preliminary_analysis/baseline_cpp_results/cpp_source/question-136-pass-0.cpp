// Find the value of N XOR 'ed to itself K times. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int xorK ( int n , int k ) {
 
    int x = n ;
    for ( int i = 0 ; i < k ; i++ ) {
        x = x ^ n ;
    }
    return x ;
 }
 
 int main () {
    int n, k ;
    cin >> n >> k ;
    cout << xorK ( n, k ) << endl ;
    return 0 ;
 }
