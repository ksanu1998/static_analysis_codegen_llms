#include <iostream>
using namespace std;
int getMinNum(int a, int b, int c) {
    int minNum = 0;
    for (int i = a; i <= b; i++) {
        if (i % c == 0 && i > 0) {
            minNum = i;
            break;
        }
    }
    return minNum;
}
int main() {
    int a, b, c;
    cout << "Enter the values of a, b and c: ";
    cin >> a >> b >> c;
    int minNum = getMinNum(a, b, c);
    if (minNum == 0) {
        cout << "No positive integer divisible by " << c << " is in the range [" << a << ", " << b << "]";
    } else {
        cout << "The minimum positive integer divisible by " << c << " is " << minNum;
    }
    return 0;
}