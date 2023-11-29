#include <bits/stdc++.h>
using namespace std;
bool isCenteredCube(int N) {
    int x = sqrt(N);
    return (x * x * x == N);
}
int main() {
    int N;
    cin >> N;
    if (isCenteredCube(N)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}