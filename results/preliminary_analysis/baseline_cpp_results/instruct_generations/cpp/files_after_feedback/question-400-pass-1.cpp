#include <bits/stdc++.h>
using namespace std;
int nswp(int n) {
    if (n <= 1) return 0;
    int s = 0;
    while (n > 1) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
        s++;
    }
    return s;
}
int main() {
    int n;
    cin >> n;
    cout << nswp(n) << endl;
    return 0;
}