#include <bits/stdc++.h>
using namespace std;
bool isSubSeqDivisible(const string& str) {
    int n = str.length();
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (str[i] % 8 == 0) {
            count++;
        }
    }
    return count > 0;
}