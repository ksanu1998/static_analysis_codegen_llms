#include <bits/stdc++.h>
using namespace std;
void alternateFib(int n) {
    int a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            cout << a << " ";
            a = a + b;
        } else {
            cout << b << " ";
            b = a + b;
        }
    }
    cout << endl;
}
int main() {
    int n;
    cin >> n;
    alternateFib(n);
    return 0;
}