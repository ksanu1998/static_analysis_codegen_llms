#include <bits/stdc++.h>
using namespace std;
long long int minOperations(long long int n) {
    long long int count = 0;
    while (n > 1) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
        count++;
    }
    return count;
}