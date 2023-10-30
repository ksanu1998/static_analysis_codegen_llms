// Minimum steps to convert X to Y by repeated division and multiplication. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int solve ( int X , int Y ) {
 
 	int steps = 0 ;
 	while ( X!= Y ) {
 		if ( X > Y ) {
 			X = X - Y ;
 			steps += 1 ;
 		}
 		else {
 			Y = Y - X ;
 			steps += 1 ;
 		}
 	}
 	return steps ;
 }
 
 int main ( ) {
 	int X, Y ;
 	cin >> X >> Y ;
 	cout << solve ( X, Y ) << endl ;
 	return 0 ;
 }
