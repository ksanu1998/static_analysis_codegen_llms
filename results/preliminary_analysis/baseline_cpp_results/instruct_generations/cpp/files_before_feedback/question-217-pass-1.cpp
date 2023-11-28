#include <bits/stdc++.h> 
 using namespace std ;
 #define ll  long long int 
 ll minSum ( int arr [ ] , int n , int x ) {
// Find the minimum element in the array
int minElement = arr[0];
for (int i = 1; i < n; i++)
    minElement = min(minElement, arr[i]);

// Find the maximum element in the array
int maxElement = arr[0];
for (int i = 1; i < n; i++)
    maxElement = max(maxElement, arr[i]);

// Calculate the minimum sum
ll minSum = 0;
for (int i = 0; i < n; i++)
    minSum += max(0, arr[i] - x);

// Return the minimum sum
return minSum;
}

// Driver code
int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 2;
    cout << minSum(arr, n, x) << endl;
    return 0;
}

// Time Complexity: O(n)
// Space Complexity: O(1)

// Explanation:

// The function first finds the minimum and maximum elements in the array.
// Then it calculates the minimum sum by adding the maximum of (0, arr[i] - x) for each element in the array.
// The time complexity is O(n) because we are iterating through the array once.
// The space complexity is O(1) because we are using constant extra space to store the minimum and maximum elements.