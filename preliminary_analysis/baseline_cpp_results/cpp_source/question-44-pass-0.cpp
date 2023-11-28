// Digitally balanced numbers. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int checkSame ( int n , int b ) {
 
 int temp = n ;
 int count = 0 ;
 while ( temp > 0 ) {
 int rem = temp % b ;
 if ( rem == 0 )
 count++ ;
 temp /= b ;
 }
 return count ;
 }
 int main ( ) {
 int n ;
 cin >> n ;
 int b ;
 cin >> b ;
 int count = 0 ;
 for ( int i = 1 ; i <= n ; i++ ) {
 if ( checkSame ( i, b ) == checkSame ( n - i, b ) )
 count++ ;
 }
 