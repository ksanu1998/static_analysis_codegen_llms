// Chocolate Distribution Problem. 
 #include <iostream> 
 using namespace std ;
 void minChocolates ( int A [ ] , int N ) {
 
    int i, j, k, l, m, n, sum, count, max;
    int dp[N+1][N+1];
    for ( i = 0 ; i <= N ; i++ ) {
        for ( j = 0 ; j <= N ; j++ ) {
            dp[i][j] = 0;
        }
    }
    for ( i = 1 ; i <= N ; i++ ) {
        dp[i][0] = 1;
    }
    for ( i = 1 ; i <= N ; i++ ) {
        for ( j = 1 ; j <= N ; j++ ) {
            if ( A[i-1] <= j ) {
                dp[i][j] = dp[i-1][j] + dp[i-1][j-A[i-1]];
            }
            else {
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    cout << dp[N][N] << endl;
 }
 int main () {
    int N;
    cin >> N;
    int A[N];
    for ( int i = 0 ; i < N ; i++ ) {
        cin >> A[i];
    }
    