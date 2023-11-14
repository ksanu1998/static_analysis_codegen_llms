#include <bits/stdc++.h>
using namespace std;
#define maxLen 10
#define maskLen 130
int dp[maxLen][maskLen];
bool v[maxLen][maskLen];
int minSteps(int arr[], int i, int mask, int n) {
    if (i == n) {
        return 0;
    }
    if (v[i][mask]) {
        return dp[i][mask];
    }
    int minVal = INT_MAX;
    for (int j = 0; j < n; j++) {
        if ((mask & (1 << j)) == 0 && arr[j] <= arr[i]) {
            int val = minSteps(arr, j, mask | (1 << j), n);
            if (val!= -1 && val + 1 < minVal) {
                minVal = val + 1;
            }
        }
    }
    v[i][mask] = true;
    dp[i][mask] = minVal;
    return minVal;
}