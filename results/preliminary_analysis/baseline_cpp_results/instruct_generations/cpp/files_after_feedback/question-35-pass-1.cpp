#include <bits/stdc++.h>
using namespace std;
const int MAX_N = 1e5 + 5;
int prefixProduct[MAX_N];
void prefixProduct(const int a[], int n) {
    prefixProduct[0] = 1;
    for (int i = 1; i <= n; i++) {
        prefixProduct[i] = prefixProduct[i - 1] * a[i - 1];
    }
}