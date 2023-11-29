#include <iostream>
void pairwiseDifference(const int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        std::cout << std::abs(arr[i] - arr[i + 1]) << " ";
    }
    std::cout << std::abs(arr[n - 1] - arr[0]) << std::endl;
}
int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    pairwiseDifference(arr, n);
    return 0;
}