#include <bits/stdc++.h>
using namespace std;
int count_setbit(int N) {
    int count = 0;
    while (N > 0) {
        N = N & (N - 1);
        count++;
    }
    return count;
}