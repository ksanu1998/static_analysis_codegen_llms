// Compute the maximum power with a given condition. 
 #include <bits/stdc++.h> 
 using namespace std ;
 #define ll  long long 
 int calculate ( ll int n , ll int k , ll int m , ll int power ) {
 
 ll int ans = 0 ;
 ll int temp = 1 ;
 
 while ( temp <= n ) {
 
 if ( temp % k == 0 && temp % m == 0 ) {
 
 ans += power ;
 
 }
 
 temp *= 2 ;
 
 }
 
 return ans ;
 
 }
 
 int main ( ) {
 
 ll int n, k, m, power ;
 cin >> n >> k >> m >> power ;
 
 ll int ans = 0 ;
 
 for ( ll int i = 1 ; i <= n ; i++ ) {
 
 ans += calculate ( n, k, m, power ) ;
 
 }
 
 