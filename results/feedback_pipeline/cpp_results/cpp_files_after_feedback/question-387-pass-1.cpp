#include <iostream>
void fib(int n) {
    int a = 0, b = 1, c;
    for (int i = 0; i < n; i++) {
        c = a + b;
        a = b;
        b = c;
        std::cout << c << " ";
    }
}
int main() {
    int n;
    std::cout << "Enter the number of terms: ";
    std::cin >> n;
    fib(n);
    return 0;
}