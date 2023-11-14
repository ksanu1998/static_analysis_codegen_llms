#include <bits/stdc++.h>
using namespace std;
bool isConcentrichexagonal(int N) {
    // Check if N is a perfect square
    int sqrtN = (int)sqrt(N);
    if (sqrtN * sqrtN!= N) return false;
    // Check if N is a hexagonal number
    int x = N * (2 * N - 1);
    int y = N * (3 * N - 1);
    if (x % 2 == 0 && y % 2 == 0) return true;
    return false;
}
int main() {
    int N;
    cin >> N;
    if (isConcentrichexagonal(N)) {
        cout << "Yes, " << N << " is a Concentric Hexagonal Number." << endl;
    } else {
        cout << "No, " << N << " is not a Concentric Hexagonal Number." << endl;
    }
    return 0;
}