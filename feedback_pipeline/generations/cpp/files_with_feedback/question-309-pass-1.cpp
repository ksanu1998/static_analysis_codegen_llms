#include <bits/stdc++.h>
#define ll long long int
using namespace std;
double findSum(ll n) {
    double sum = 0;
    for (ll i = 1; i <= n; i++) {
        sum += i * i;
    }
    return sum;
}
int main() {
    ll n;
    cin >> n;
    cout << findSum(n) << endl;
    return 0;
}