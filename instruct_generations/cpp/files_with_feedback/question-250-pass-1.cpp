#include <iostream>
void sumArray(const int arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    std::cout << "Sum of the array is: " << sum << std::endl;
}
int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    sumArray(arr, n);
    return 0;
}