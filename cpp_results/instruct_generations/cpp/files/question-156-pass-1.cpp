#include <bits/stdc++.h> 
 using namespace std ;
 #define ll  long long 
int calculate(ll n, ll k, ll m, ll power) {
    int result = 0;
    for (ll i = 0; i < n; i++) {
        if (i % k == 0) {
            result += m;
        } else {
            result += power;
        }
    }
    return result;
}