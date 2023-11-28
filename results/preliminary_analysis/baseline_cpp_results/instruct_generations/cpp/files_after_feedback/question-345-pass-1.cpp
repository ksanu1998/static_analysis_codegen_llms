#include <bits/stdc++.h>
using namespace std;
#define maxLen 10
int dp[maxLen];
bool visit[maxLen];
int maxSum(int arr[], int i, int n, int k) {
    if (i == n || k == 0) {
        return 0;
    }
    if (visit[i]) {
        return dp[i];
    }
    visit[i] = true;
    int include = arr[i] + maxSum(arr, i + 1, n, k - 1);
    int exclude = maxSum(arr, i + 1, n, k);
    dp[i] = max(include, exclude);
    return dp[i];
}