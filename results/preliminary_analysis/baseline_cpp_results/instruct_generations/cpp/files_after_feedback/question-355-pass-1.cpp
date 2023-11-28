#include <algorithm>
#include <iostream>
using namespace std;
int maxSum(int a[], int n) {
    // Sort the array in ascending order
    sort(a, a + n);
    // Initialize the maximum sum
    int max_sum = 0;
    // Initialize the sum of the first two elements
    int sum = a[0] + a[1];
    // Initialize the maximum sum of the first two elements
    int max_sum_of_first_two = a[0] + a[1];
    // Iterate over the remaining elements
    for (int i = 2; i < n; i++) {
        // Update the sum
        sum = max(sum, a[i] + a[n - i]);
        // Update the maximum sum
        max_sum = max(max_sum, sum);
    }
    // Return the maximum sum
    return max_sum;
}
int main() {
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cout << maxSum(a, n) << endl;
    return 0;
}