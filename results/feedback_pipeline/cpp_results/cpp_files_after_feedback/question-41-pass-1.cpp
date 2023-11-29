#include <iostream>
#include <cmath>
long sumOfSumSeries(int n) {
    long sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i * (i + 1) / 2;
    }
    return sum;
}
int main() {
    int n;
    std::cout << "Enter a positive integer: ";
    std::cin >> n;
    if (n <= 0) {
        std::cout << "Invalid input." << std::endl;
        return 1;
    }
    long sum = sumOfSumSeries(n);
    std::cout << "The sum of the first " << n << " positive integers is: " << sum << std::endl;
    return 0;
}