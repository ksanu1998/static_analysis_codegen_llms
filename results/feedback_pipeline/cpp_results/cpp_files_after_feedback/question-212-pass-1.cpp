#include <bits/stdc++.h>
using namespace std;
int findMinimum(int x, int y) {
    return x > y? y : x;
}
int main() {
    int x, y;
    cin >> x >> y;
    cout << findMinimum(x, y) << endl;
    return 0;
}