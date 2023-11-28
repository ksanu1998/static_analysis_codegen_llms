#include <bits/stdc++.h>
using namespace std;
int minOperations(const int A[], int n) {
    int min_operations = 0;
    for (int i = 0; i < n; i++) {
        if (A[i] == 0) {
            min_operations++;
        }
    }
    return min_operations;
}