#include <bits/stdc++.h>
using namespace std;
int maxSumWO3Consec(int n) {
    // Initialize variables
    int maxSum = 0;
    int sum = 0;
    // Calculate the sum of the array
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    // Calculate the maximum sum that can be obtained by selecting no more than two consecutive elements
    for (int i = 0; i < n - 1; i++) {
        maxSum = max(maxSum, sum - arr[i] - arr[i + 1] + arr[i + 2]);
    }
    return maxSum;
}