#include <bits/stdc++.h> 
 using namespace std ;
int findMin(int arr[], int n) {
    int minDiff = INT_MAX, diff;
    sort(arr, arr + n);
    for (int i = 0; i < n - 1; i++) {
        diff = arr[n - 1] - arr[i];
        if (diff < minDiff)
            minDiff = diff;
    }
    return minDiff;
}