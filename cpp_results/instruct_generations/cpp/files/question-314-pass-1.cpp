#include <bits/stdc++.h> 
 using namespace std ;
 #define ll  long long int 
int max_value(int array[M][2], int M, int K, int N) {
    // Initialize the maximum value to 0
    int max_val = 0;

    // Loop through each row of the array
    for (int i = 0; i < M; i++) {
        // Loop through each column of the array
        for (int j = 0; j < N; j++) {
            // Check if the current element is greater than the maximum value
            if (array[i][j] > max_val) {
                // If it is, update the maximum value
                max_val = array[i][j];
            }
        }
    }

    // Return the maximum value
    return max_val;
}