#include <bits/stdc++.h> 
 using namespace std ;
 bool modularSum ( int arr [ ] , int n , int m ) {
// Initialize result
    bool result = false;

    // Iterate through the array
    for (int i = 0; i < n; i++)
    {
        // Initialize sum
        int sum = 0;

        // Iterate through the remaining elements of the array
        for (int j = i; j < n; j++)
        {
            // Add the element to the sum
            sum += arr[j];

            // Check if the sum is divisible by m
            if (sum % m == 0)
            {
                // If it is, return true
                result = true;
                break;
            }
        }

        // If the sum is divisible by m, break out of the loop
        if (result)
            break;
    }

    // Return the result
    return result;
}

# Subset with sum divisible by m.
#include <bits/stdc++.h> 
using namespace std ;
bool modularSum ( int arr [ ], int n, int m ) {