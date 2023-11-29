#include <bits/stdc++.h>
using namespace std;
int cntCakes(int n, int m) {
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (i * j <= n) {
                cnt++;
            }
        }
    }
    return cnt;
}
int main() {
    int n, m;
    cin >> n >> m;
    cout << cntCakes(n, m) << endl;
    return 0;
}