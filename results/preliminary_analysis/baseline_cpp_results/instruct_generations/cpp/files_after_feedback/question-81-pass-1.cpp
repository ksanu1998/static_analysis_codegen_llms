#include <iostream>
using namespace std;
int countWays(int n) {
    int dp[n+1];
    memset(dp, 0, sizeof(dp));
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i-1; j++) {
            if (j + dp[i-j] <= i) {
                dp[i]++;
            }
        }
    }
    return dp[n];
}
int main() {
    int n;
    cout << "Enter a positive integer: ";
    cin >> n;
    cout << "The count of ways to write " << n << " as a sum of three numbers is: " << countWays(n) << endl;
    return 0;
}