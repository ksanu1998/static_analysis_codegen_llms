// Program to check if N is a Tetradecagonal Number. 
 #include <bits/stdc++.h> 
 using namespace std ;
 bool istetradecagonal ( int N ) {
 
    int sum = 0 ;
    int i = 1 ;
    while ( i * i <= N ) {
        if ( N % i == 0 ) {
            sum += i ;
            if ( i * i!= N ) {
                sum += N / i ;
            }
        }
        i++ ;
    }
    if ( sum == N ) {
        return true ;
    }
    return false ;
 }
 int main ( ) {
    int N ;
    cin >> N ;
    if ( istetradecagonal ( N ) ) {
        cout << "Yes" ;
    }
    