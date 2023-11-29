#include <iostream>
using namespace std;
bool isSumEqual(const int ar[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += ar[i];
    }
    return sum == n;
}
int main() {
    int ar[] = {1, 2, 3, 4, 5};
    int n = sizeof(ar) / sizeof(ar[0]);
    bool result = isSumEqual(ar, n);
    cout << "The sum of the first " << n << " elements is " << (result? "equal" : "not equal") << " to " << n << "." << endl;
    return 0;
}