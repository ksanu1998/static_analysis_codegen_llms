#include <bits/stdc++.h>
using namespace std;
int countOddZeros(int n) {
    int count = 0;
    while (n > 0) {
        if (n % 10 == 0) {
            count++;
        }
        n /= 10;
    }
    return count;
}
int countNumbers(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        if (countOddZeros(i) == n - 1) {
            count++;
        }
    }
    return count;
}