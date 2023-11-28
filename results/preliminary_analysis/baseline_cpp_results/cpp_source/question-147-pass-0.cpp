// Represent ( 2 / N ) as the sum of three distinct positive integers of the form ( 1 / m ). 
 #include <bits/stdc++.h> 
 using namespace std ;
 void find_numbers ( int N ) {
 
    int m = 1 ;
    int sum = 0 ;
    while ( sum < N ) {
        sum += 1 / m ;
        m++ ;
    }
    int a = 1 / m ;
    int b = 1 / ( m - 1 ) ;
    int c = 1 / ( m - 2 ) ;
    cout << a << " " << b << " " << c << endl ;
 }
 
 int main ( ) {
    int N ;
    cin >> N ;
    find_numbers ( N ) ;
    return 0 ;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 