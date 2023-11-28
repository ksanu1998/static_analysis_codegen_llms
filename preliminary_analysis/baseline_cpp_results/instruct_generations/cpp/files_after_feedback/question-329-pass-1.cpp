#include <iostream>
#include <algorithm>
const int MAX_N = 100000;
int a[MAX_N];
void findMax(int a[], int n) {
    int max = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > max) {
            max = a[i];
        }
    }
    std::cout << "Maximum value in the array is: " << max << std::endl;
}