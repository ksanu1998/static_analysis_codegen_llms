#include <bits/stdc++.h> 
 using namespace std ;
 const int MOD = 2019 ;
int min_modulo(int l, int r) {
    int min_val = l % MOD;
    for (int i = l + 1; i <= r; i++) {
        int val = i % MOD;
        if (val < min_val) {
            min_val = val;
        }
    }
    return min_val;
}