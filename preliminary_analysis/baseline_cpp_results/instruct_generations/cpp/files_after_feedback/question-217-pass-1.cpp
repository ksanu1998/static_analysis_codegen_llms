#include <bits/stdc++.h>
using namespace std;
#define ll long long int
ll minSum(const int arr[], int n, int x) {
    // Find the minimum element in the array
    int minElement = arr[0];
    for (int i = 1; i < n; i++) {
        minElement = min(minElement, arr[i]);
    }
    // Find the maximum element in the array
    int maxElement = arr[0];
    for (int i = 1; i < n; i++) {
        maxElement = max(maxElement, arr[i]);
    }
    // Calculate the minimum sum
    ll minSum = 0;
    for (int i = 0; i < n; i++) {
        minSum += max(0, arr[i] - x);
    }
    // Return the minimum sum
    return minSum;
}
// Driver code
int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 2;
    cout << minSum(arr, n, x) << endl;
    return 0;
}