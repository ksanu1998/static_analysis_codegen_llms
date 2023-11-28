#include <bits/stdc++.h>
using namespace std;
int countWays(int n, int l, int r) {
    int count = 0;
    for (int i = l; i <= r; i++) {
        if (i % 2 == 0) {
            count++;
        }
    }
    return count;
}
int main() {
    int n, l, r;
    cin >> n >> l >> r;
    cout << countWays(n, l, r);
    return 0;
}