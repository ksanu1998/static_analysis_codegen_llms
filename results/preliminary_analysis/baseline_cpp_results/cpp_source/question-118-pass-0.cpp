// Find K distinct positive odd integers with sum N. 
 #include <bits/stdc++.h> 
 using namespace std ;
 #define ll  long long int 
 void findDistinctOddSum ( ll n , ll k ) {
 
 	ll sum = 0 ;
 	ll count = 0 ;
 	ll i = 1 ;
 	while ( sum < n && count < k ) {
 		sum += i ;
 		count++ ;
 		i += 2 ;
 	}
 	if ( sum == n && count == k ) {
 		cout << "Yes" << endl ;
 	}
 	else {
 		cout << "No" << endl ;
 	}
 }
 
 int main ( ) {
 	ll n, k ;
 	cin >> n >> k ;
 	findDistinctOddSum ( n, k ) ;
 	return 0 ;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 