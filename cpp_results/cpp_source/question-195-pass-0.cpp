// Predict the winner of the game on the basis of absolute difference of sum by selecting numbers. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int decideWinner ( int a [ ] , int n ) {
 
 int sum1 = 0, sum2 = 0 ;
 for ( int i = 0 ; i < n ; i++ ) {
 sum1 += a [ i ] ;
 }
 
 for ( int i = 0 ; i < n ; i++ ) {
 sum2 += a [ n - i - 1 ] ;
 }
 
 if ( sum1 > sum2 )
 return 1 ;
 else if ( sum1 < sum2 )
 return 2 ;
 else
 return 0 ;
 }
 
 int main ( ) {
 int t ;
 cin >> t ;
 while ( t-- ) {
 int n ;
 cin >> n ;
 int a [ n ] ;
 for ( int i = 0 ; i < n ; i++ )
 cin >> a [ i ] ;
 
 int winner = decideWinner ( a, n ) ;
 if ( winner == 1 )
 cout << "A" << endl ;
 else if ( winner == 2 )
 cout << "B" << endl ;
 else
 cout << "Tie" << endl ;
 }
 