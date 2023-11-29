#include <bits/stdc++.h>
using namespace std;
void printPair(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j++) {
            if (__gcd(i, j) == n && __lcm(i, j) == n) {
                cout << i << " " << j << endl;
                return;
            }
        }
    }
}
int main() {
    int n;
    cin >> n;
    printPair(n);
    return 0;
}