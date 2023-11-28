#include <bits/stdc++.h>
using namespace std;
int maxSumWithK(const int a[], int n, int k) {
    int maxSum = 0;
    int sum = 0;
    int i = 0;
    int j = 0;
    for (i = 0; i < n; i++) {
        sum += a[i];
        if (sum > maxSum) {
            maxSum = sum;
            j = i + 1;
        } else if (sum < 0) {
            sum = 0;
            j = i + 1;
        }
    }
    return maxSum;
}
int main() {
    int a[] = {1, 2, 3, 4, 5};
    int n = sizeof(a) / sizeof(a[0]);
    int k = 2;
    int result = maxSumWithK(a, n, k);
    cout << "Maximum sum of subarray with at most " << k << " elements is " << result << endl;
    return 0;
}