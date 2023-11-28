#include <iostream>
using namespace std;
int countSetBits(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        count += __builtin_popcount(i);
    }
    return count;
}
int main() {
    int n;
    cout << "Enter a positive integer: ";
    cin >> n;
    cout << "The total number of set bits in all numbers from 1 to " << n << " is: " << countSetBits(n) << endl;
    return 0;
}