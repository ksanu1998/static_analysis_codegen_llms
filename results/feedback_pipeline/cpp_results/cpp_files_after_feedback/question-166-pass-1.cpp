#include <bits/stdc++.h>
using namespace std;
void findMin(int arr[], int n) {
    // Sort the array in ascending order
    sort(arr, arr + n);
    // Initialize the sum to 0
    int sum = 0;
    // Initialize the minimum sum to the first element of the array
    int min_sum = arr[0];
    // Iterate over the array
    for (int i = 1; i < n; i++) {
        // Add the current element to the sum
        sum += arr[i];
        // If the sum is less than the minimum sum, update the minimum sum
        if (sum < min_sum) {
            min_sum = sum;
        }
    }
    // Return the minimum sum
    return min_sum;
}
int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << findMin(arr, n) << endl;
    return 0;
}