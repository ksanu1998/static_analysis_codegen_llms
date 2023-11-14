#include <bits/stdc++.h>
using namespace std;
int countSol(const int coeff[], int start, int end, int rhs) {
    int count = 0;
    for (int i = start; i <= end; i++) {
        if (coeff[i] == 0) continue;
        int curr = rhs;
        for (int j = start; j < i; j++) {
            curr -= coeff[j] * coeff[i];
        }
        if (curr == 0) count++;
    }
    return count;
}