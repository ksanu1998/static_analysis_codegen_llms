#include <bits/stdc++.h>
using namespace std;
bool isPossible(int a, int b, int c) {
    return a + b + c == 10;
}
int main() {
    int a, b, c;
    cin >> a >> b >> c;
    if (isPossible(a, b, c)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}