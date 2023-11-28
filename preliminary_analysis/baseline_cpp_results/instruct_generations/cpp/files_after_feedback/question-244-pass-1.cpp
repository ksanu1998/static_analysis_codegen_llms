#include <bits/stdc++.h>
using namespace std;
void divide(int a, int b) {
    int gcd = findGCD(a, b);
    int divA = a / gcd;
    int divB = b / gcd;
    cout << divA << " " << divB << endl;
}
int findGCD(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return findGCD(b, a % b);
    }
}
int main() {
    int a = 12;
    int b = 18;
    divide(a, b);
    return 0;
}