#include <bits/stdc++.h>
using namespace std;
int sumOfSubstrings(const string& num) {
    int sum = 0;
    for (int i = 0; i < num.length(); i++) {
        for (int j = i; j < num.length(); j++) {
            string substring = num.substr(i, j - i + 1);
            sum += stoi(substring);
        }
    }
    return sum;
}