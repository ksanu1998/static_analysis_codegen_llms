#include <bits/stdc++.h>
using namespace std;
int maximumOccurrence(const string& s) {
    int n = s.length();
    vector<int> count(n);
    for (int i = 0; i < n; i++) {
        count[i] = 1;
        for (int j = 0; j < i; j++) {
            if (s[i] == s[j]) {
                count[i] = max(count[i], count[j] + 1);
            }
        }
    }
    return *max_element(count.begin(), count.end());
}