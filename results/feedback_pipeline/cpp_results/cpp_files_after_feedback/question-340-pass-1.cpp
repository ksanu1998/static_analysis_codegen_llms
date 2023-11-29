#include <bits/stdc++.h>
using namespace std;
void NumberOfShortestPaths(int n, int m) {
    // Create a 2D array to store the number of shortest paths
    // to reach each cell from the bottom
    int dp[n][m];
    // Initialize the first row and column with 1
    for (int i = 0; i < n; i++) {
        dp[i][0] = 1;
    }
    for (int j = 0; j < m; j++) {
        dp[0][j] = 1;
    }
    // Calculate the number of shortest paths for each cell
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    // Print the number of shortest paths for each cell
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
}