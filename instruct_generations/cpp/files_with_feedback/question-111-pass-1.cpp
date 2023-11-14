#include <iostream>
void countOfGreaterElements(const int arr[], int n) {
    int count[n];
    for (int i = 0; i < n; i++) {
        count[i] = 0;
        for (int j = i + 1; j < n; j++) {
            if (arr[i] < arr[j]) {
                count[i]++;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        std::cout << count[i] << " ";
    }
    std::cout << std::endl;
}
int main() {
    int arr[] = {1, 3, 5, 7, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    countOfGreaterElements(arr, n);
    return 0;
}