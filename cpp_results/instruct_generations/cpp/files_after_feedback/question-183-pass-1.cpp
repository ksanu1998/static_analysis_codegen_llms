#include <bits/stdc++.h>
using namespace std;
int closetAND(const int arr[], int n, int k) {
    int i = 0, j = n - 1;
    while (i < j) {
        if (arr[i] & arr[j]) {
            i++;
            j--;
        } else {
            j--;
        }
    }
    return arr[i] & k;
}