#include <bits/stdc++.h>
using namespace std;
void solve(int arr[], int n) {
    unordered_map<int, int> count;
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                count[arr[i]]--;
                if (count[arr[i]] == 0) {
                    count.erase(arr[i]);
                }
                break;
            }
        }
    }
    for (auto it = count.begin(); it!= count.end(); it++) {
        cout << it->first << " " << it->second << endl;
    }
}
int main() {
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    solve(arr, n);
    return 0;
}