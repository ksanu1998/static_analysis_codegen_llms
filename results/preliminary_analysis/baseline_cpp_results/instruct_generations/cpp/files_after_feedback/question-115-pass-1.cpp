#include <bits/stdc++.h>
using namespace std;
void product_subarrays(const int arr[], int n) {
    int result[n];
    for (int i = 0; i < n; i++) {
        result[i] = 1;
        for (int j = i; j < n; j++) {
            result[j] *= arr[i];
        }
    }
    for (int i = 0; i < n; i++) {
        cout << result[i] << " ";
    }
    cout << endl;
}
int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    product_subarrays(arr, n);
    return 0;
}