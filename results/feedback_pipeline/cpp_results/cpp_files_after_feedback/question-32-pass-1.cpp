#include <bits/stdc++.h>
using namespace std;
int count_pairs(const int a[], const int b[], int N) {
    int count = 0;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (a[i] + a[j] > b[i] + b[j]) {
                count++;
            }
        }
    }
    return count;
}