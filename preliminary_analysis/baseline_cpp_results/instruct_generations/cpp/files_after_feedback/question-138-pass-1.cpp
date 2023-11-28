#include <bits/stdc++.h>
using namespace std;
int findNthDigit(int p, int q, int N) {
    int n = p / q;
    int digit = 0;
    int count = 1;
    while (n!= 0) {
        n /= 10;
        count *= 10;
    }
    digit = (p - (count - 1) * (q - 1)) / count;
    if (N <= count) {
        return digit;
    } else {
        return findNthDigit(digit, q, N - count);
    }
}