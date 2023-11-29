#include <iostream>
int cnt_squares(int n) {
    return n * n;
}
int main() {
    int n;
    std::cin >> n;
    std::cout << cnt_squares(n) << std::endl;
    return 0;
}