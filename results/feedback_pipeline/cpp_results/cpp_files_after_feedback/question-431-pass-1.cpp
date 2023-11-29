#include <bits/stdc++.h>
using namespace std;
int maxSumPair(const int arr[], int N, int k) {
    int max_sum = 0;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (arr[j] - arr[i] == k) {
                max_sum = max(max_sum, arr[j] + arr[i]);
            }
        }
    }
    return max_sum;
}