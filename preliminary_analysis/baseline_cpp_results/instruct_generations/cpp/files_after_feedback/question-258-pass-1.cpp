#include <bits/stdc++.h>
using namespace std;
bool checkIsAP(const int arr[], int n) {
    // Initialize variables
    int diff = arr[1] - arr[0];
    int i = 1;
    // Loop through the array
    while (i < n) {
        // Check if the difference between the current element and the previous element is equal to the difference between the first two elements
        if (arr[i] - arr[i - 1]!= diff) {
            return false;
        }
        i++;
    }
    // If the loop completes successfully, return true
    return true;
}
int main() {
    int arr[] = {1, 3, 5, 7, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    if (checkIsAP(arr, n)) {
        cout << "Yes";
    } else {
        cout << "No";
    }
    return 0;
}