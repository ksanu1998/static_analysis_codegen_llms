#include <bits/stdc++.h>
#define ll long long int
using namespace std;
int count(const int a[], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        bool divisible = false;
        for (int j = 0; j < n; j++) {
            if (i!= j && a[i] % a[j] == 0) {
                divisible = true;
                break;
            }
        }
        if (!divisible) {
            count++;
        }
    }
    return count;
}