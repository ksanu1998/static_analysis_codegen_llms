#include <bits/stdc++.h> 
 using namespace std ;
long long calculate(long long p, long long q) {
    long long mod = 998244353;
    long long inv = 1;
    while (q) {
        if (q & 1) {
            inv = (inv * p) % mod;
        }
        q >>= 1;
        p = (p * p) % mod;
    }
    return inv;
}