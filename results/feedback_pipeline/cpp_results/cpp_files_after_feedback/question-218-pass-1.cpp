#include <bits/stdc++.h>
using namespace std;
int maxAND(int L, int R) {
    int max = 0;
    for (int i = L; i <= R; i++) {
        for (int j = L; j <= R; j++) {
            if ((i & j) > max) {
                max = i & j;
            }
        }
    }
    return max;
}