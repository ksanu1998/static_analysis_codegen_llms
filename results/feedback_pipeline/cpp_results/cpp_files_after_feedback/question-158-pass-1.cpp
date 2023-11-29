#include <bits/stdc++.h>
using namespace std;
int minCost(const array<int, n> &arr) {
    int min_cost = 0;
    for (int i = 0; i < n - 1; i++) {
        min_cost += abs(arr[i] - arr[i + 1]);
    }
    return min_cost;
}