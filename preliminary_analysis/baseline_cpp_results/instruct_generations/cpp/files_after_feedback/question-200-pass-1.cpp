#include <bits/stdc++.h>
using namespace std;
void printBalancedExpression(int a, int b, int c, int d) {
    // Check if the given brackets are balanced
    if (a!= b || c!= d) {
        cout << "Not a balanced expression" << endl;
        return;
    }
    // Print the balanced expression
    cout << "(" << a << " + " << b << ") - (" << c << " - " << d << ")" << endl;
}
int main() {
    // Test case 1: Balanced expression
    printBalancedExpression(3, 4, 5, 6);
    // Test case 2: Unbalanced expression
    printBalancedExpression(3, 4, 5, 7);
    return 0;
}