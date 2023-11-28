// Length of Smallest subarray in range 1 to N with sum greater than a given value. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int countNumber ( int N , int S ) {
 
    int dp[N+1];
    dp[0] = 0;
    dp[1] = 1;
    for ( int i = 2 ; i <= N ; i++ ) {
        dp[i] = dp[i-1] + 1;
        for ( int j = 1 ; j < i ; j++ ) {
            if ( dp[i] > dp[j-1] + 1 && ( S - j ) >= j ) {
                dp[i] = dp[j-1] + 1;
            }
        }
    }
    return dp[N];
}
int main() {
    int N, S;
    cin >> N >> S;
    cout << countNumber(N, S);
    return 0;
}





































































































































































































































































