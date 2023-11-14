#include <bits/stdc++.h>
using namespace std;
const int MAX = 10;
int F[MAX][MAX];
int C[MAX];
int noOfAssignments(string& S, int& n, int i, int c_x) {
    if (i == n) {
        return 1;
    }
    int count = 0;
    for (int j = i; j < n; j++) {
        if (S[j] == '0') {
            count += noOfAssignments(S, n, j + 1, c_x);
        } else if (c_x > 0) {
            count += noOfAssignments(S, n, j + 1, c_x - 1);
        }
    }
    return count;
}