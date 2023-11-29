#include <bits/stdc++.h>
using namespace std;
int getMax(const int arr[], int N, int K) {
    int max_val = arr[0], max_idx = 0;
    for (int i = 1; i < N; i++) {
        if (arr[i] > max_val) {
            max_val = arr[i];
            max_idx = i;
        }
    }
    return max_val;
}