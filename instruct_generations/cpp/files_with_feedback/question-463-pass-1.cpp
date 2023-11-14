#include <iostream>
int nthTerm(int N) {
    if (N == 1) {
        return 2;
    } else if (N == 2) {
        return 3;
    } else {
        return nthTerm(N - 1) + nthTerm(N - 2);
    }
}
int main() {
    int N;
    std::cout << "Enter the value of N: ";
    std::cin >> N;
    std::cout << "The " << N << "th term is: " << nthTerm(N) << std::endl;
    return 0;
}