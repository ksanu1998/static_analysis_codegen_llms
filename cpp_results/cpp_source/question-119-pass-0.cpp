// Minimum number of operations to convert array A to array B by adding an integer into a subarray. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void checkArray ( int a [ ] , int b [ ] , int n ) {
 
 	for ( int i = 0 ; i < n ; i++ ) {
 		if ( a [ i ]!= b [ i ] ) {
 			cout << "Not Equal" << endl ;
 			return ;
 		}
 	}
 	cout << "Equal" << endl ;
 }
 int main ( ) {
 	int a [ ] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 } 