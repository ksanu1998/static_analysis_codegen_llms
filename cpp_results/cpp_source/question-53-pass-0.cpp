// Check if A can be converted to B by reducing with a Prime number. 
 #include <bits/stdc++.h> 
 using namespace std ;
 bool isPossible ( int A , int B ) {
 
     if ( A == B ) return true ;
     if ( A < B ) return false ;
 
     int prime = 2 ;
     while ( prime * prime <= A ) {
         if ( A % prime == 0 ) return false ;
         prime++ ;
     }
     return true ;
 }
 
 int main ( ) {
     int A, B ;
     cin >> A >> B ;
     if ( isPossible ( A, B ) ) cout << "YES" << endl ;
     else cout << "NO" << endl ;
     return 0 ;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
