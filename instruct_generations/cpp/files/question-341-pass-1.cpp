#include <bits/stdc++.h> 
 using namespace std ;
 int Max_Sum ( int arr1 [ ] , int arr2 [ ] , int n ) {
int max_sum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int sum = arr1[i] + arr2[j];
            if (sum > max_sum) {
                max_sum = sum;
            }
        }
    }
    return max_sum;
}