#include <iostream>
void getResult(int n) {
    // Initialize variables to store the product of digits at even and odd places
    int productEven = 1, productOdd = 1;
    // Extract the digits of the number
    while (n > 0) {
        // If the digit is even, multiply it with the product of digits at even places
        if (n % 2 == 0) {
            productEven *= n % 10;
        }
        // If the digit is odd, multiply it with the product of digits at odd places
        else {
            productOdd *= n % 10;
        }
        n /= 10;
    }
    // Check if the product of digits at even and odd places is equal
    if (productEven == productOdd) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
}
int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    getResult(n);
    return 0;
}