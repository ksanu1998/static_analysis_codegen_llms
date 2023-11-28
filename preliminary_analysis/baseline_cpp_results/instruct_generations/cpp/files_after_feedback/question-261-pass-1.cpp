#include <bits/stdc++.h>
using namespace std;
int findTwoThreePrime(int l, int r) {
    int count = 0;
    for (int i = l; i <= r; i++) {
        bool isPrime = true;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            count++;
        }
    }
    return count;
}