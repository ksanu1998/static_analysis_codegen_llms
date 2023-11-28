#include <bits/stdc++.h>
using namespace std;
int proizvolov(const int a[], const int b[], int n) {
    int result = 0;
    for (int i = 0; i < n; i++) {
        result += a[i] * b[i];
    }
    return result;
}