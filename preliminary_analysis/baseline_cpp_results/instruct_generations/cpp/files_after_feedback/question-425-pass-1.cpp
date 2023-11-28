#include <bits/stdc++.h>
using namespace std;
int maximumDifferenceSum(const array<int, N> &arr) {
    int maxDiff = 0;
    for (int i = 0; i < N - 1; i++) {
        maxDiff = max(maxDiff, arr[i + 1] - arr[i]);
    }
    return maxDiff;
}