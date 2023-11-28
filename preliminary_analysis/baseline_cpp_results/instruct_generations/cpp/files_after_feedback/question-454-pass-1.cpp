#include <bits/stdc++.h>
using namespace std;
vector<int> restore(int arr[], int N) {
    vector<int> result;
    map<int, int> mp;
    for (int i = 0; i < N; i++) {
        if (mp[arr[i]] == 0) {
            result.push_back(arr[i]);
            mp[arr[i]]++;
        }
    }
    return result;
}
void print_result(vector<int> result) {
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
}
int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int N = sizeof(arr) / sizeof(arr[0]);
    vector<int> result = restore(arr, N);
    print_result(result);
    return 0;
}