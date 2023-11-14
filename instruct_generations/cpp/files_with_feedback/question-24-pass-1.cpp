#include <bits/stdc++.h>
using namespace std;
int countRepeatingDigits(int N) {
    int count = 0;
    int digit = N % 10;
    while (N > 0) {
        int next_digit = N % 10;
        if (next_digit == digit)
            count++;
        N /= 10;
    }
    return count;
}
int main() {
    int N;
    cin >> N;
    cout << countRepeatingDigits(N) << endl;
    return 0;
}