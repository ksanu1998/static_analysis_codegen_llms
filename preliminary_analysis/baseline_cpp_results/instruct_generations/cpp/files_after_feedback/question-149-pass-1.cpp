#include <bits/stdc++.h>
using namespace std;
string minInt(const string& str) {
    int n = stoi(str);
    string res = to_string(n);
    while (n > 0) {
        res = to_string(n % 10) + res;
        n /= 10;
    }
    return res;
}