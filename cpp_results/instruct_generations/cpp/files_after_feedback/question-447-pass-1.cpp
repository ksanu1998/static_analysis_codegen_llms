#include <bits/stdc++.h>
using namespace std;
int steps(int source, int step, int dest) {
    if (source == dest) {
        return 0;
    }
    if (source < dest) {
        return steps(source + step, step, dest) + 1;
    } else {
        return steps(source - step, step, dest) + 1;
    }
}