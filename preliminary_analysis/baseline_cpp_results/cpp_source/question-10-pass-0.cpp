// Minimum row or column swaps required to make every pair of adjacent cell of a Binary Matrix distinct. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int minSwaps ( vector < vector < int > > & b ) {
 
 	int n = b.size() ;
 	int m = b[0].size() ;
 	int ans = 0 ;
 	int row[n] ;
 	int col[m] ;
 	for ( int i = 0 ; i < n ; i++ ) {
 		row[i] = 0 ;
 		col[i] = 0 ;
 	}
 	for ( int i = 0 ; i < n ; i++ ) {
 		for ( int j = 0 ; j < m ; j++ ) {
 			if ( b[i][j] == 1 ) {
 				row[i]++ ;
 				col[j]++ ;
 			}
 		}
 	}
 	for ( int i = 0 ; i < n ; i++ ) {
 		for ( int j = 0 ; j < m ; j++ ) {
 			if ( b[i][j] == 1 ) {
 				ans += max ( row[i] - 1, col[j] - 1 ) ;
 			}
 		}
 	}
 	return ans ;
 }
 
 int main ( ) {
 	int t ;
 	cin >> t ;
 	while ( t-- ) {
 		int n, m ;
 		cin >> n >> m ;
 		vector < vector < int > > b ( n, vector < int > ( m, 0 ) ) ;
 		for ( int i = 0 ; i < n ; i++ ) {
 			for ( int j = 0 ; j < m ; j++ ) {
 				cin >> b[i][j] ;
 			}
 		