#include <bits/stdc++.h>
using namespace std;
int getHeight(int X) {
    return X >= 0? X : -X;
}
int main() {
    int X;
    cin >> X;
    cout << getHeight(X) << endl;
    return 0;
}