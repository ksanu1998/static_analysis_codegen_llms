#include <bits/stdc++.h>
using namespace std;
int minAbsDiff(int n) {
    int diff = INT_MAX;
    for (int i = 1; i <= n; i *= 2) {
        diff = min(diff, abs(n - i));
    }
    return diff;
}