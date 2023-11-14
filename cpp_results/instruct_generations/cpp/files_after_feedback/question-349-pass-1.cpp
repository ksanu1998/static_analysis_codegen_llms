#include <bits/stdc++.h>
using namespace std;
int MaximumMarks(int marksarr[], int timearr[], int h, int n, int p) {
    // Sort the arrays in descending order based on the time
    sort(timearr, timearr + n, greater<int>());
    // Initialize the dp array with 0
    int dp[n + 1];
    memset(dp, 0, sizeof(dp));
    // Initialize the maximum marks variable
    int maxMarks = 0;
    // Loop through the time array
    for (int i = 0; i < n; i++) {
        // Loop through the dp array
        for (int j = h; j >= timearr[i]; j--) {
            // Update the dp array with the maximum of the current value and the previous value plus the current mark
            dp[j] = max(dp[j], dp[j - timearr[i]] + marksarr[i]);
            // Update the maximum marks variable with the maximum value in the dp array
            maxMarks = max(maxMarks, dp[j]);
        }
    }
    return maxMarks;
}