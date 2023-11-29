#include <bits/stdc++.h>
using namespace std;
bool isOctagonal(int N) {
    int n = (int)sqrt(24*N+1);
    return (n*(n-1)) == 8*N;
}
int main() {
    int N;
    cin >> N;
    if (isOctagonal(N)) {
        cout << "Yes, " << N << " is an octagonal number." << endl;
    } else {
        cout << "No, " << N << " is not an octagonal number." << endl;
    }
    return 0;
}