#include <bits/stdc++.h>
using namespace std;
int findNumberOfEvenCells(int n, const int q[][2], int size) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (q[i][j] % 2 == 0) {
                count++;
            }
        }
    }
    return count;
}