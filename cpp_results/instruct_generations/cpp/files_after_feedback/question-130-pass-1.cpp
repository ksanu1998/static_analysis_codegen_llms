#include <bits/stdc++.h>
using namespace std;
int maxHeight(int h1, int h2) {
    return max(h1, h2);
}
int main() {
    int h1, h2;
    cin >> h1 >> h2;
    cout << maxHeight(h1, h2) << endl;
    return 0;
}