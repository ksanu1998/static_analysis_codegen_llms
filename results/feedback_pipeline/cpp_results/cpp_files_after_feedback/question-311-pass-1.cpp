#include <iostream>
using namespace std;
void printPair(int g, int l) {
    cout << "(" << g << ", " << l << ")" << endl;
}
int main() {
    int gcd, lcm;
    cout << "Enter the first number: ";
    cin >> gcd;
    cout << "Enter the second number: ";
    cin >> lcm;
    if (gcd > lcm) {
        cout << "No pair found." << endl;
    } else {
        printPair(gcd, lcm);
    }
    return 0;
}