// Maximum Prefix Sum possible by merging two given arrays. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int maxPresum ( vector < int > a , vector < int > b ) {
 
 	int n = a.size() ;
 	int m = b.size() ;
 	vector < int > c ( n + m ) ;
 	int i, j ;
 	for ( i = 0 ; i < n ; i++ ) {
 		c[i] = a[i] ;
 	}
 	for ( j = 0 ; j < m ; j++ ) {
 		c[i++] = b[j] ;
 	}
 	
 	int max_sum = INT_MIN ;
 	for ( i = 0 ; i < n + m ; i++ ) {
 		if ( max_sum < c[i] ) {
 			max_sum = c[i] ;
 		}
 	}
 	return max_sum ;
 }
 
 int main () {
 	vector < int > a = { 1, 2, 3, 4, 5 } 