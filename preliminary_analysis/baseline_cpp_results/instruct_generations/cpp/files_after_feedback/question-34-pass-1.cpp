#include <bits/stdc++.h>
using namespace std;
const int print_h_index(const int arr[], int N) {
    // Initialize result
    int result = 0;
    // Loop through the array
    for (int i = 0; i < N; i++) {
        // Check if the current element is greater than or equal to the result
        if (arr[i] >= result) {
            // Increment the result
            result++;
        }
    }
    // Return the result
    return result;
}