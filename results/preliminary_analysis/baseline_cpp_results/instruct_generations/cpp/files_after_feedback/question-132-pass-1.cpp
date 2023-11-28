#include <bits/stdc++.h>
using namespace std;
void findNums(const int arr[], int n) {
    // Write your code here
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            count++;
        }
    }
    if (count % 2 == 0) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}