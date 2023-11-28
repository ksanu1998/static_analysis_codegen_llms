#include <bits/stdc++.h>
using namespace std;
void maxLCMWithGivenSum(int X) {
    int n = sqrt(X);
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j++) {
            if (i * j == X) {
                cout << "The two numbers are " << i << " and " << j << "." << endl;
                cout << "Their LCM is " << lcm(i, j) << "." << endl;
                return;
            }
        }
    }
    cout << "No such pair of numbers exists." << endl;
}
int lcm(int a, int b) {
    return a * b / gcd(a, b);
}
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}