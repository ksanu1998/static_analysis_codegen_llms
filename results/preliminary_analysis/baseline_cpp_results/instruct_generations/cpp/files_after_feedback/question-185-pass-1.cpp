#include <bits/stdc++.h>
using namespace std;
void solve(int a[], int n) {
    // Sort the array in non-decreasing order
    sort(a, a + n);
    // Initialize the prefix sum array
    int prefixSum[n + 1];
    prefixSum[0] = 0;
    for (int i = 1; i <= n; i++) {
        prefixSum[i] = prefixSum[i - 1] + a[i - 1];
    }
    // Find the maximum number of primes in the prefix sum
    int maxPrimes = 0;
    for (int i = 1; i <= n; i++) {
        int j = i;
        while (j <= n && prefixSum[j] - prefixSum[i - 1] <= 1000000) {
            j++;
        }
        maxPrimes = max(maxPrimes, j - i);
    }
    // Print the result
    cout << maxPrimes << endl;
}
int main() {
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    solve(a, n);
    return 0;
}