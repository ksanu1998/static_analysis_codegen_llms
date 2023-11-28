// Check if there exists a number with X factors out of which exactly K are prime. 
 #include <bits/stdc++.h> 
 using namespace std ;
 bool check ( int X , int K ) {
 
 int count = 0 ;
 for ( int i = 1 ; i <= X ; i++ ) {
 
 if ( X % i == 0 ) {
 
 if ( isPrime ( i ) ) {
 
 count++ ;
 }
 }
 }
 
 if ( count == K ) {
 
 return true ;
 }
 
 return false ;
 }
 
 bool isPrime ( int n ) {
 
 if ( n == 1 ) {
 
 return false ;
 }
 
 for ( int i = 2 ; i * i <= n ; i++ ) {
 
 if ( n % i == 0 ) {
 
 return false ;
 }
 }
 
 return true ;
 }
 v
 int main ( ) {
 
 int T ;
 cin >> T ;
 
 while ( T-- ) {
 
 int X, K ;
 cin >> X >> K ;
 
 if ( check ( X, K ) ) {
 
 cout << "YES" << endl ;
 }
 