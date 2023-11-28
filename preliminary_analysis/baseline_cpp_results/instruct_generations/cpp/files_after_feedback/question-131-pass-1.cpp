#include <bits/stdc++.h>
using namespace std;
void FermatFactors(int n) {
    int a = (int)sqrt(n) + 1;
    while (a % 2 == 0) a++;
    for (int i = 1; i <= a; i++) {
        if (n % i == 0) {
            cout << i << " ";
            n /= i;
            i--;
        }
    }
    if (n > 1) cout << n << endl;
}
int main() {
    int n;
    cin >> n;
    FermatFactors(n);
    return 0;
}