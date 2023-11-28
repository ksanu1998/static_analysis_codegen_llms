#include <bits/stdc++.h> 
 using namespace std ;
 int arr [ ] = {
 100 , 1000 , 100 , 1000 , 1 } ;
 int sum [ 10000 ] ;
int maxSumWO3Consec(int n) {
    int maxSum = 0;
    for (int i = 0; i < n; i++) {
        maxSum = max(maxSum, sum[i] + sum[i+2] - sum[i+1]);
    }
    return maxSum;
}