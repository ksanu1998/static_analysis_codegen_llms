#include <bits/stdc++.h>
using namespace std;
int Check_is_possible(int l, int r, int k) {
    for (int i = l; i <= r; i++) {
        for (int j = i + 1; j <= r; j++) {
            if (__gcd(i, j) % k == 0) {
                return 1;
            }
        }
    }
    return 0;
}