#include <bits/stdc++.h>
using namespace std;
int countPairs(const array<int, n> &arr) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] - i == arr[j] - j) {
                count++;
            }
        }
    }
    return count;
}