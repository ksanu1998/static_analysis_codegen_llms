#include <bits/stdc++.h>
using namespace std;
int min_moves(int n) {
    if (n == 1) return 0;
    if (n == 2) return 1;
    if (n == 3) return 2;
    if (n == 4) return 3;
    if (n == 5) return 4;
    if (n == 6) return 5;
    if (n == 7) return 6;
    if (n == 8) return 7;
    if (n == 9) return 8;
    if (n == 10) return 9;
    return min_moves(n - 1) + 1;
}