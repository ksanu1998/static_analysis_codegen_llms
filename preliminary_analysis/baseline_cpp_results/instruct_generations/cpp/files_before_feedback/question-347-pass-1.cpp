#include <bits/stdc++.h> 
 using namespace std ;
 #define SIZE  3 
 const int N = 3 ;
 int minSum ( int A [ ] , int B [ ] , int C [ ] , int i , int n , int curr , int dp [ SIZE ] [ N ] ) {
if (i == n) {
        return 0;
    }
    if (dp[i][n]!= -1) {
        return dp[i][n];
    }
    int minVal = INT_MAX;
    for (int j = 0; j < N; j++) {
        int sum = A[i] + B[j] + C[n - 1];
        if (sum < minVal) {
            minVal = sum;
        }
    }
    return minVal;
}

int main() {
    int A[] = {1, 2, 3};
    int B[] = {4, 5, 6};
    int C[] = {7, 8, 9};
    int n = sizeof(A) / sizeof(A[0]);
    int dp[SIZE][N] = {{-1}};
    cout << minSum(A, B, C, 0, n, 0, dp) << endl;
    return 0;
}