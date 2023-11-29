#include <bits/stdc++.h>
using namespace std;
int addNDigits(int a, int b, int n) {
    int result = 0;
    for (int i = 0; i < n; i++) {
        result = (result + a) % b;
    }
    return result;
}