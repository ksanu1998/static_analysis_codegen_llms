#include <iostream>
int getMaxNum(int a, int b, int c) {
    int maxNum = 0;
    for (int i = a; i <= b; i++) {
        if (i % c == 0 && i > maxNum) {
            maxNum = i;
        }
    }
    return maxNum;
}
int main() {
    int a, b, c;
    std::cout << "Enter the value of a, b and c: ";
    std::cin >> a >> b >> c;
    std::cout << "The maximum positive integer divisible by " << c << " and is in the range [" << a << ", " << b << "] is: " << getMaxNum(a, b, c) << std::endl;
    return 0;
}