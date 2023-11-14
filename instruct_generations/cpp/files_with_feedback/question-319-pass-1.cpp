#include <bits/stdc++.h>
using namespace std;
int CountOfTriplets(const int a[], int n) {
    int count = 0;
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if ((a[i] ^ a[j]) == (a[j] ^ a[k])) {
                    count++;
                }
            }
        }
    }
    return count;
}