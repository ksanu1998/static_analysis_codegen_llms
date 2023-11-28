#include <bits/stdc++.h>
using namespace std;
void findSetBits(int n) {
    for (int i = 0; i <= n; i++) {
        int count = 0;
        while (i > 0) {
            count += i % 2;
            i /= 2;
        }
        cout << count << " ";
    }
    cout << endl;
}