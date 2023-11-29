#include <bits/stdc++.h> 
 using namespace std ;
 void countWays ( int n ) {
// Initialize the dp array
    int dp[n+1];
    memset(dp, 0, sizeof(dp));
    dp[0] = 1;

    // Loop through the numbers from 1 to n
    for (int i = 1; i <= n; i++) {
        // Loop through the numbers from 1 to i-1
        for (int j = 1; j <= i-1; j++) {
            // If the sum of the current number and the previous number is less than or equal to i,
            // then there is one more way to write i as a sum of three numbers
            if (j + dp[i-j] <= i) {
                dp[i]++;
            }
        }
    }

    // Print the count of ways to write n as a sum of three numbers
    cout << "The count of ways to write " << n << " as a sum of three numbers is: " << dp[n] << endl;
}

int main() {
    int n;
    cout << "Enter a positive integer: ";
    cin >> n;
    countWays(n);
    return 0;
}