#include <iostream>
void FindAllElements(int n, int k) {
    // Initialize an array to store the powers of two
    int powersOfTwo[k];
    // Initialize the first element of the array
    powersOfTwo[0] = 1;
    // Loop through the remaining elements of the array
    for (int i = 1; i < k; i++) {
        // Multiply the current element by 2 to get the next power of two
        powersOfTwo[i] = powersOfTwo[i - 1] * 2;
    }
    // Print out the powers of two
    for (int i = 0; i < k; i++) {
        std::cout << powersOfTwo[i] << " ";
    }
    std::cout << std::endl;
}
int main() {
    int n, k;
    std::cout << "Enter a positive integer: ";
    std::cin >> n;
    std::cout << "Enter the number of powers of two to find: ";
    std::cin >> k;
    FindAllElements(n, k);
    return 0;
}