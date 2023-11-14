#include <bits/stdc++.h>
using namespace std;
int check(int A, int B) {
    return (B * 10 + B % 10) % 10 == (A % 10);
}
int main() {
    int A, B;
    cin >> A >> B;
    if (check(A, B)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}