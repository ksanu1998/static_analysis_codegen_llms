#include <bits/stdc++.h> 
 using namespace std ;
 void sameProductQuadruples ( int nums [ ] , int N ) {
// Initialize the count to 0
    int count = 0;

    // Loop through all possible pairs of numbers
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            // Calculate the product of the two numbers
            int product1 = nums[i] * nums[j];

            // Loop through all possible pairs of numbers
            for (int k = j + 1; k < N; k++) {
                for (int l = k + 1; l < N; l++) {
                    // Calculate the product of the two numbers
                    int product2 = nums[k] * nums[l];

                    // Check if the product of the two pairs is equal
                    if (product1 == product2) {
                        // Increment the count
                        count++;
                    }
                }
            }
        }
    }

    // Print the count
    cout << count << endl;
}