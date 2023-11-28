#include <bits/stdc++.h> 
 using namespace std ;
 void checkArray ( int a [ ] , int b [ ] , int n ) {
// Initialize variables
    int minOps = INT_MAX;
    int currOps = 0;

    // Loop through each subarray of A
    for (int i = 0; i < n; i++) {
        // Calculate the difference between the current subarray and the corresponding subarray of B
        int diff = abs(a[i] - b[i]);

        // Add the difference to the current number of operations
        currOps += diff;

        // Update the minimum number of operations if necessary
        if (currOps < minOps) {
            minOps = currOps;
        }
    }

    // Return the minimum number of operations
    return minOps;
}

// Test case 1:
int a1[] = {1, 2, 3, 4, 5};
int b1[] = {1, 2,