#include <iostream>
int countWays(int n) {
    int ways = 1;
    for (int i = 1; i <= n; i++) {
        ways *= i;
    }
    return ways;
}
int main() {
    int n;
    std::cout << "Enter a positive integer: ";
    std::cin >> n;
    if (n < 0) {
        std::cout << "Invalid input.";
        return 0;
    }
    int ways = countWays(n);
    std::cout << "The number of ways to arrange the first " << n << " positive integers is " << ways << ".";
    return 0;
}