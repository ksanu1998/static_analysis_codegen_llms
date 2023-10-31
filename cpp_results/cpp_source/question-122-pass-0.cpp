// Find N from the value of N !. 
 #include " bits / stdc + + . h " 
 #define ll  long long int 
 using namespace std ;
 map < ll , ll > m ;
 int precompute ( ) {
 
 	ll n = 1000000000000000000LL ;
 	ll i = 2 ;
 	while ( i <= n ) {
 		m [ i ] = i ;
 		i = i + 1 ;
 	}
 	ll j = 2 ;
 	while ( j * j <= n ) {
 		if ( m [ j ] == j ) {
 			ll k = j + 1 ;
 			while ( k <= n / j ) {
 				m [ k ] = m [ k - j ] * j ;
 				k = k + 1 ;
 			}
 		}
 		j = j + 1 ;
 	}
 	return 0 ;
 }
 ll nth ( ll n ) {
 	if ( m [ n ] == n ) {
 		return n ;
 	}
 	return nth ( m [ n ] ) ;
 }
 int main ( ) {
 	precompute ( ) ;
 	ll n ;
 	cin >> n ;
 	cout << nth ( n ) << endl ;
 	return 0 ;
 }
