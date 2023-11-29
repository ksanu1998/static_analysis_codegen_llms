#include <bits/stdc++.h>
using namespace std;
int nthTerm(int N) {
    return pow(N, 2) * 5;
}
int main() {
    int N;
    cin >> N;
    cout << nthTerm(N) << endl;
    return 0;
}