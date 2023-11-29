#include <bits/stdc++.h> 
 using namespace std ;
long max_gcd(long n, long p) {
    long gcd = 0;
    for (long i = 1; i <= n; i++) {
        for (long j = 1; j <= p; j++) {
            long temp_gcd = __gcd(i, j);
            if (temp_gcd > gcd) {
                gcd = temp_gcd;
            }
        }
    }
    return gcd;
}