// Number of triplets such that each value is less than N and each pair sum is a multiple of K. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int NoofTriplets ( int N , int K ) {
 
    int count = 0 ;
    for ( int i = 1 ; i <= N ; i++ ) {
        for ( int j = i + 1 ; j <= N ; j++ ) {
            if ( i + j <= N ) {
                if ( ( i + j ) % K == 0 ) {
                    count++ ;
                }
            }
        }
    }
    return count ;
}
int main ( ) {
    int T ;
    cin >> T ;
    while ( T-- ) {
        int N, K ;
        cin >> N >> K ;
        cout << NoofTriplets ( N, K ) << endl ;
    }
    