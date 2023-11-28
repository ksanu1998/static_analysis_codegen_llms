#include <bits/stdc++.h>
using namespace std;
void PrintReverseOrder(int N) {
    for (int i = N; i >= 1; i--) {
        cout << i << " ";
    }
}
int main() {
    int N;
    cin >> N;
    PrintReverseOrder(N);
    return 0;
}