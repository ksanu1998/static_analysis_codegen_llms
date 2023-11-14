#include <bits/stdc++.h>
using namespace std;
void updateMatrix(int n, int q[3][4]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (q[i][j] == 1) {
                q[i][j] = 0;
            } else {
                q[i][j] = 1;
            }
        }
    }
}
int main() {
    int n;
    cin >> n;
    int q[3][4];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> q[i][j];
        }
    }
    updateMatrix(n, q);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << q[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}