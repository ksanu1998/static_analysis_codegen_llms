#include <bits/stdc++.h> 
 #define ll  long long int 
 using namespace std ;
 ll pre_compute ( ll a [ ] , ll n , ll index , ll k ) {
ll dp[n+1];
dp[0] = 0;
for(int i=1; i<=n; i++){
    dp[i] = max(dp[i-1] + a[i], a[i]);
}
return dp[n];