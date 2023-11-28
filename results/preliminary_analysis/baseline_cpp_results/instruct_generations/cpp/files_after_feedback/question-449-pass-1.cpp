#include <iostream>
using namespace std;
string X, Y;
int lcs(int i, int j, int count) {
    if (i == 0 || j == 0) {
        return count;
    }
    if (X[i - 1] == Y[j - 1]) {
        return lcs(i - 1, j - 1, count + 1);
    } else {
        int a = lcs(i - 1, j, count);
        int b = lcs(i, j - 1, count);
        return a > b? a : b;
    }
}
int main() {
    cin >> X >> Y;
    int n = X.length();
    int m = Y.length();
    int dp[n + 1][m + 1];
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            } else if (X[i - 1] == Y[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    cout << lcs(n, m, 0) << endl;
    return 0;
}