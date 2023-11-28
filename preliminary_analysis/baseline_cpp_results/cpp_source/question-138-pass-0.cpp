// Find the Nth digit in the proper fraction of two numbers. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int findNthDigit ( int p , int q , int N ) {
 
    int n = 1 ;
    int d = 9 ;
    int m = 1 ;
    int count = 0 ;
    int num = 0 ;
    while ( n <= p ) {
        n *= d ;
        m *= d ;
        d *= 10 ;
    }
    while ( count < N ) {
        num = ( q * m + n / d ) ;
        count += num ;
        n %= d ;
        n *= 10 ;
        m /= 10 ;
    }
    return num ;
}

int main() {
    int p = 1000 ;
    int q = 1000 ;
    int N = 1000 ;
    cout << findNthDigit ( p, q, N ) << endl ;
    return 0 ;
}





























































































































































































































































