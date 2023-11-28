#include <bits/stdc++.h>
using namespace std;
int decideWinner(const int a[], int n) {
    int sum1 = 0, sum2 = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            sum1 += a[i];
        } else {
            sum2 += a[i];
        }
    }
    if (abs(sum1 - sum2) > 1) {
        return 1;
    } else {
        return 2;
    }
}