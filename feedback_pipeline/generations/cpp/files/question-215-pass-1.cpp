#include <bits/stdc++.h> 
 using namespace std ;
 int findMinSum ( int arr [ ] , int n ) {
int minSum = 0;
for (int i = 0; i < n; i++) {
    int minElement = arr[i];
    for (int j = i; j < n; j++) {
        if (arr[j] < minElement) {
            minElement = arr[j];
        }
    }
    minSum += minElement;
}
return minSum;
}

# Sum of maximum element of all subarrays of a sorted array.
#include <bits/stdc++.h> 
using namespace std;
int findMaxSum(int arr[], int n) {
    int maxSum = 0;
    for (int i = 0; i < n; i++) {
        int maxElement = arr[i];
        for (int j = i; j < n; j++) {
            if (arr[j] > maxElement) {
                maxElement = arr[j];
            }
        }
        maxSum += maxElement;
    }
    return maxSum;
}

# Sum of all elements of all subarrays of a sorted array.
#include <bits/stdc++.h> 
using namespace std;
int findAllSum(int arr[], int n) {
    int allSum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            allSum += arr[j];
        }
    }
    return allSum;
}

# Sum of all elements of all subarrays of a sorted array.
#include <bits/stdc++.h> 
using namespace std;
int findAllSum(int arr[], int n) {
    int all