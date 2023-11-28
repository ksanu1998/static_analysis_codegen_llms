#include <bits/stdc++.h> 
 using namespace std ;
 void func ( int n , int m , int A [ ] ) {
// Initialize result as false
    bool result = false;

    // Iterate through the array
    for (int i = 0; i < n; i++)
    {
        // Initialize sum as 0
        int sum = 0;

        // Iterate through the remaining elements in the array
        for (int j = i; j < n; j++)
        {
            // Add the current element to sum
            sum += A[j];

            // Check if sum is divisible by M
            if (sum % m == 0)
            {
                // If sum is divisible by M, return true
                result = true;
                break;
            }
        }

        // If result is true, break the loop
        if (result)
            break;
    }

    // Return the result
    return result;
}

// Driver code
int main()
{
    // Test case 1:
    int n = 5, m = 3;
    int A[] = {1, 2, 3, 4, 5};
    if (func(n, m, A))
        cout << "There is a valid sequence";
    else
        cout << "There is no valid sequence";

    // Test case 2:
    int n = 5, m = 2;
    int A[] = {1, 2, 3, 4, 5};
    if (func(n, m, A))
        cout << "There is a valid sequence";
    else
        cout << "There is no valid sequence";

    return 0;
}