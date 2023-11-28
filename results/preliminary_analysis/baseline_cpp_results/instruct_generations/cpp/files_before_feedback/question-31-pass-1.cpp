#include <bits/stdc++.h> 
 using namespace std ;
 typedef long long int ll ;
ll countQuadruples(ll N) {
    ll count = 0;
    for (ll i = 1; i <= N; i++) {
        for (ll j = i; j <= N; j++) {
            ll sum1 = i * i + j * j;
            for (ll k = j; k <= N; k++) {
                ll sum2 = sum1 + k * k;
                for (ll l = k; l <= N; l++) {
                    ll sum3 = sum2 + l * l;
                    if (sum3 == N * N) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}