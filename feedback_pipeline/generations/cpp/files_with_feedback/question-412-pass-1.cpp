#include <bits/stdc++.h>
using namespace std;
long countWays(int n, int k) {
    if (n == 0) return 1;
    if (n < 0 || k < 0) return 0;
    return countWays(n - 1, k) + countWays(n - 1, k - 1);
}