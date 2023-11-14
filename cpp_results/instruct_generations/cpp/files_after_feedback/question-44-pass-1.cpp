#include <bits/stdc++.h>
using namespace std;
bool isBalanced(int n) {
    int count = 0;
    while (n > 0) {
        if (n % 10 == 0) {
            count++;
        }
        n /= 10;
    }
    return count % 2 == 0;
}
int main() {
    int n;
    cin >> n;
    if (isBalanced(n)) {
        cout << "Balanced" << endl;
    } else {
        cout << "Not Balanced" << endl;
    }
    return 0;
}