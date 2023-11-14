#include <bits/stdc++.h>
using namespace std;
int findMinSum(int arr[], int n) {
    int minSum = 0;
    for (int i = 0; i < n; i++) {
        int minElement = arr[i];
        for (int j = i; j < n; j++) {
            if (arr[j] < minElement) {
                minElement = arr[j];
            }
        }
        minSum += minElement;
    }
    return minSum;
}