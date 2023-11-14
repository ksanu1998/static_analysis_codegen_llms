#include <bits/stdc++.h>
using namespace std;
int sum(int N, int X, int Y) {
    int sum = 0;
    for (int i = 1; i <= N; i++) {
        if (i % X == 0 || i % Y == 0) {
            sum += i;
        }
    }
    return sum;
}