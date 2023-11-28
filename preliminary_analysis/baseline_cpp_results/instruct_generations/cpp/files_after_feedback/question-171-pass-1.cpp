#include <iostream>
int sum(int A, int B, int R) {
    int sum = 0;
    for (int i = 0; i < R; i++) {
        sum += A[i] + B[i];
    }
    return sum;
}
int main() {
    int A[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    int B[3][3] = {
        {10, 11, 12},
        {13, 14, 15},
        {16, 17, 18}
    };
    int R = 3;
    int sum = sum(A, B, R);
    std::cout << "Sum of elements: " << sum << std::endl;
    return 0;
}