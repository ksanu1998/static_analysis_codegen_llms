#include <bits/stdc++.h>
using namespace std;
#define ll long long int
ll sum(int n) {
    if (n == 1) {
        return 1;
    } else {
        return (n * n) + sum(n - 1);
    }
}
int main() {
    int n;
    cin >> n;
    cout << sum(n) << endl;
    return 0;
}