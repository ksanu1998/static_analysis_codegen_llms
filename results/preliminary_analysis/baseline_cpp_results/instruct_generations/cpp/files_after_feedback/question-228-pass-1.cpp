#include <bits/stdc++.h>
using namespace std;
bool isPossible(int n, int k, const array<int, n>& arr) {
    unordered_map<int, int> count;
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }
    for (auto it = count.begin(); it!= count.end(); it++) {
        int key = it->first;
        int value = it->second;
        if (value % k!= 0) {
            return false;
        }
    }
    return true;
}