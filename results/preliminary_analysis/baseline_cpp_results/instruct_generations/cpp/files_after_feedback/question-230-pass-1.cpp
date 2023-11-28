#include <bits/stdc++.h>
using namespace std;
bool EqualNumbers(const int a[], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (a[i]!= a[0]) {
            count++;
        }
    }
    return count <= 1;
}