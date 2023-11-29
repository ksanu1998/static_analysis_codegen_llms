#include <bits/stdc++.h>
using namespace std;
bool isPossible(int A, int B) {
    int prime = 2;
    while (prime <= A) {
        if (A % prime == 0 && B % prime == 0) {
            return true;
        }
        prime++;
    }
    return false;
}
int main() {
    int A, B;
    cin >> A >> B;
    if (isPossible(A, B)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}