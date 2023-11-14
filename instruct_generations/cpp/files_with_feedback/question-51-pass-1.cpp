#include <bits/stdc++.h>
using namespace std;
bool isDroll(int n) {
    return n % 2 == 0 && n > 2;
}
int main() {
    int n;
    cin >> n;
    if (isDroll(n)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}