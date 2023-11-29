#include <bits/stdc++.h>
using namespace std;
int numLen(int K) {
    int len = 1;
    while (K > 1) {
        K >>= 1;
        len++;
    }
    return len;
}
int main() {
    int K;
    cin >> K;
    cout << numLen(K) << endl;
    return 0;
}