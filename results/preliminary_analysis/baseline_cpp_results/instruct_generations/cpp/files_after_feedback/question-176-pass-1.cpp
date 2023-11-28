#include <bits/stdc++.h>
using namespace std;
#define ll long long int
ll findNumber(int n) {
    ll num = 1;
    for (int i = 2; i <= n; i++) {
        num = num * 10 + i;
    }
    return num;
}
int main() {
    int n;
    cin >> n;
    ll result = findNumber(n);
    cout << result << endl;
    return 0;
}