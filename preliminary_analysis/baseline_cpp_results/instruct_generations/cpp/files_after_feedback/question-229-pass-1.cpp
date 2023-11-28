#include <bits/stdc++.h>
using namespace std;
int maxResult(int n, int a, int b, int c) {
    int x, y, z;
    x = (n - a) / b;
    y = (n - a) / c;
    z = n / (a + b + c);
    return x + y + z;
}
int main() {
    int n, a, b, c;
    cin >> n >> a >> b >> c;
    cout << maxResult(n, a, b, c) << endl;
    return 0;
}