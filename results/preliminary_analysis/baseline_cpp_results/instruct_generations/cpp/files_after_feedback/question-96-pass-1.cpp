#include <bits/stdc++.h>
using namespace std;
int findUniqueElements(int arr[], int N, int K) {
    unordered_map<int, int> freq;
    for (int i = 0; i < N; i++) {
        freq[arr[i]]++;
    }
    for (int i = 0; i < N; i++) {
        if (freq[arr[i]] == 1) {
            return arr[i];
        }
    }
    return -1;
}
int main() {
    int arr[] = {1, 2, 2, 3, 1};
    int N = sizeof(arr) / sizeof(arr[0]);
    int K = 2;
    int result = findUniqueElements(arr, N, K);
    cout << "The unique element is: " << result << endl;
    return 0;
}