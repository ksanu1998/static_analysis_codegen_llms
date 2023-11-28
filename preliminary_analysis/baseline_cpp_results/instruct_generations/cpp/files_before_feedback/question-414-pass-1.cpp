#include <bits/stdc++.h> 
 using namespace std ;
 int maxSumWithK ( int a [ ] , int n , int k ) {
// Initialize variables
    int maxSum = 0;
    int sum = 0;
    int i = 0;
    int j = 0;

    // Loop through the array
    for (i = 0; i < n; i++)
    {
        sum = sum + a[i];
        if (sum > maxSum)
            maxSum = sum;
        else if (sum < 0)
        {
            sum = 0;
            j = i + 1;
        }
    }

    // Return the maximum sum
    return maxSum;
}

// Test the function
int main()
{
    int a[] = {1, 2, 3, 4, 5};
    int n = sizeof(a) / sizeof(a[0]);
    int k = 2;
    int result = maxSumWithK(a, n, k);
    cout << "Maximum sum of subarray with at most " << k << " elements is " << result << endl;
    return 0;
}