#include <bits/stdc++.h>
using namespace std;
int numberOfPairs(const int* a, const int* b, int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] + a[j] > b[i] + b[j]) {
                count++;
            }
        }
    }
    return count;
}