// Find count of numbers from 0 to n which satisfies the given equation for a value K. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int findAns ( int a , int b , int n ) {
 
 	int count = 0 ;
 	for ( int i = 0 ; i <= n ; i++ ) {
 		if ( a * i + b * i * i == n ) {
 			count++ ;
 		}
 	}
 	return count ;
 }
 
 int main () {
 	int a, b, n ;
 	cin >> a >> b >> n ;
 	cout << findAns ( a, b, n ) ;
 	return 0 ;
 }
