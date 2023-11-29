#include <bits/stdc++.h> 
 using namespace std ;
int maxSumBitonicSubArr(int arr[], int n) {
    // Initialize variables
    int max_sum = 0, sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
        if (sum > max_sum) {
            max_sum = sum;
        }
        if (sum < 0) {
            sum = 0;
        }
    }
    return max_sum;
}