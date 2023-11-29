#include <bits/stdc++.h>
using namespace std;
int largestNumber(int n) {
    int largest = 0;
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 1) {
            largest = i;
        }
    }
    return largest;
}
int main() {
    int n;
    cin >> n;
    cout << largestNumber(n) << endl;
    return 0;
}