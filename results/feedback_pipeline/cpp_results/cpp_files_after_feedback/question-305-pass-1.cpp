#include <iostream>
int calculateSum(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i * i;
    }
    return sum;
}
int main() {
    int n;
    std::cout << "Enter the value of n: ";
    std::cin >> n;
    std::cout << "The sum of the first " << n << " terms of the series is: " << calculateSum(n) << std::endl;
    return 0;
}