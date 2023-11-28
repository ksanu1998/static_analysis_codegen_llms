// Count of elements not divisible by any other elements of Array. 
 #include <bits/stdc++.h> 
 #define ll  long long int 
 using namespace std ;
 int count ( int a [ ] , int n ) {
 
 	int count = 0 ;
 	for ( int i = 0 ; i < n ; i++ ) {
 		for ( int j = i + 1 ; j < n ; j++ ) {
 			if ( a [ i ] % a [ j ] == 0 ) {
 				count++ ;
 				break ;
 			}
 		}
 	}
 	return count ;
 }
 int main ( ) {
 	int n ;
 	cin >> n ;
 	int a [ n ] ;
 	for ( int i = 0 ; i < n ; i++ ) {
 		cin >> a [ i ] ;
 	}
 	