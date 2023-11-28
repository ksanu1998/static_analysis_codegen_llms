#include <bits/stdc++.h>
using namespace std;
int lcs(const string& X, const string& Y) {
    int m = X.size();
    int n = Y.size();
    int dp[m + 1][n + 1];
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            } else if (X[i - 1] == Y[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[m][n];
}
int main() {
    string X = "abcdefg";
    string Y = "abcde";
    int lcs_len = lcs(X, Y);
    cout << "The length of the LCS is: " << lcs_len << endl;
    return 0;
}