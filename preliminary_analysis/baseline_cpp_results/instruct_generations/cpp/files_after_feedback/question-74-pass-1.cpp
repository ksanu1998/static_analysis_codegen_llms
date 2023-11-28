#include <bits/stdc++.h>
using namespace std;
bool isPentadecagon(int N) {
    // Formula to check if a number is a Pentadecagonal Number:
    // (N * (3N - 1)) / 2
    int pentadecagonalNumber = (N * (3 * N - 1)) / 2;
    return pentadecagonalNumber == N;
}
int main() {
    int N;
    cin >> N;
    if (isPentadecagon(N)) {
        cout << "Yes";
    } else {
        cout << "No";
    }
    return 0;
}