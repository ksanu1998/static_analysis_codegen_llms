#include <bits/stdc++.h>
using namespace std;
int numberOfSolutions(int n) {
    int count = 0;
    for (int x = 1; x <= n; x++) {
        if (n % x == 0) {
            count++;
        }
    }
    return count;
}