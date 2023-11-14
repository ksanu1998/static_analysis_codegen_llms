#include <bits/stdc++.h>
using namespace std;
const int N = 101;
const int mod = 1e9 + 7;
int exactsum[N][N][N];
int exactnum[N][N][N];
int getSum(int x, int y, int z) {
    return exactsum[x][y][z] % mod;
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        int x, y, z;
        cin >> x >> y >> z;
        exactsum[x][y][z]++;
        exactnum[x][y][z]++;
    }
    int ans = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                if (exactnum[i][j][k] > 0) {
                    ans += getSum(i, j, k);
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}