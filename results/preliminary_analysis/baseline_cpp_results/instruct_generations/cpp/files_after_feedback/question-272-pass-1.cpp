#include <iostream>
int getResult(int n) {
    if (n <= 1) {
        return n;
    }
    return getResult(n-1) + getResult(n-2);
}
int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    std::cout << "Fibonacci(" << n << ") = " << getResult(n) << std::endl;
    return 0;
}