#include <bits/stdc++.h>
using namespace std;
int nth_group(int n) {
    return n * (n + 1) / 2;
}
int main() {
    int n;
    cin >> n;
    cout << nth_group(n) << endl;
    return 0;
}