// Maximize first array element by performing given operations at most K times. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int getMax ( int arr [ ] , int N , int K ) {
 
 	int max = arr [ 0 ] ;
 	int i = 0 ;
 	int j = 1 ;
 	int count = 0 ;
 	while ( count < K ) {
 		if ( arr [ i ] < arr [ j ] ) {
 			max = max + arr [ j ] ;
 			count++ ;
 			j++ ;
 			if ( j == N ) {
 				j = 0 ;
 			}
 		}
 		else {
 			i++ ;
 			if ( i == N ) {
 				i = 0 ;
 			}
 		}
 	}
 	return max ;
 }
 
 int main ( ) {
 	int T ;
 	cin >> T ;
 	while ( T-- ) {
 		int N ;
 		cin >> N ;
 		int arr [ N ] ;
 		for ( int i = 0 ; i < N ; i++ ) {
 			cin >> arr [ i ] ;
 		}
 		