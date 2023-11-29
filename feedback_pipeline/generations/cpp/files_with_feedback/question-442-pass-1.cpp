#include <bits/stdc++.h>
using namespace std;
int partition(int arr[], int n) {
    int minDiff = INT_MAX, diff;
    for (int i = 0; i < n - 1; i++) {
        diff = arr[n - 1] - arr[i];
        if (diff < minDiff)
            minDiff = diff;
    }
    return minDiff;
}