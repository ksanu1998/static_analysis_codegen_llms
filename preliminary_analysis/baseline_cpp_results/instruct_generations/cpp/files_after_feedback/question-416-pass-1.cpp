#include <iostream>
using namespace std;
int getTotalNumberOfSequences(int m, int n) {
    int total = 1;
    for (int i = m; i <= n; i++) {
        total *= i;
    }
    return total;
}
int main() {
    int m, n;
    cout << "Enter the lower and upper bound of the sequence: ";
    cin >> m >> n;
    int total = getTotalNumberOfSequences(m, n);
    cout << "The total number of sequences is: " << total << endl;
    return 0;
}