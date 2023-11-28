// Number of ways to color boundary of each block of M * N table. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int CountWays ( int N , int M ) {
 
    int dp[N+1][M+1];
    memset(dp,0,sizeof(dp));
    dp[0][0] = 1;
    for(int i=1;i<=N;i++){
        for(int j=1;j<=M;j++){
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    }
    return dp[N][M];
 }
 int main() {
    int N, M;
    cin >> N >> M;
    cout << CountWays(N, M);
    return 0;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
